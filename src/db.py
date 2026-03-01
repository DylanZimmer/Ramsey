import sqlite3
import json
from pathlib import Path

DB_PATH = Path(__file__).parent.parent / "data" / "ramsey.db"


def get_connection():
    """Return a SQLite connection with row factory for dict-like access."""
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn


def create_tables():
    """Create graphs and graph_metrics tables if they don't exist."""
    with get_connection() as conn:
        cursor = conn.cursor()

        # Graph table
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS graphs (
            graph_id INTEGER PRIMARY KEY,
            n_vertices INTEGER NOT NULL,
            x_in_Rxy INTEGER NOT NULL,
            y_in_Rxy INTEGER NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        );
        """)

        # Metrics table
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS graph_metrics (
            graph_id INTEGER PRIMARY KEY,
            
            -- First-order coloring metrics
            num_first_order_lines INTEGER,
            first_order_lines TEXT,  -- JSON array
            num_Ky_with_one_blue_line_a1oc INTEGER,
            num_Ky_still_fully_red_a1oc INTEGER,
            num_Kx_with_one_blue_line_a1oc INTEGER,
            num_Kx_still_fully_red_a1oc INTEGER,
            untouched_vertex_a1oc TEXT,  -- JSON array

            -- Second-order coloring metrics
            num_second_order_lines INTEGER,
            second_order_lines TEXT,  -- JSON array
            num_Ky_with_u_blue_lines_a2oc TEXT,  -- JSON dict
            num_Ky_still_fully_red_a2oc INTEGER,
            num_Kx_with_u_blue_lines_a2oc TEXT,  -- JSON dict
            num_Kx_still_fully_red_a2oc INTEGER,

            FOREIGN KEY(graph_id) REFERENCES graphs(graph_id)
        );
        """)

        conn.commit()


def insert_graph(n_vertices, x_in_Rxy, y_in_Rxy):
    """Insert a graph and return its graph_id."""
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute("""
        INSERT INTO graphs (n_vertices, x_in_Rxy, y_in_Rxy)
        VALUES (?, ?, ?)
        """, (n_vertices, x_in_Rxy, y_in_Rxy))
        conn.commit()
        return cursor.lastrowid


def insert_graph_metrics(graph_id, metrics):
    """
    Insert computed metrics for a graph.
    Lists and dictionaries are serialized to JSON strings.
    """
    with get_connection() as conn:
        cursor = conn.cursor()

        cursor.execute("""
        INSERT INTO graph_metrics (
            graph_id,

            num_first_order_lines,
            first_order_lines,
            num_Ky_with_one_blue_line_a1oc,
            num_Ky_still_fully_red_a1oc,
            num_Kx_with_one_blue_line_a1oc,
            num_Kx_still_fully_red_a1oc,
            untouched_vertex_a1oc,

            num_second_order_lines,
            second_order_lines,
            num_Ky_with_u_blue_lines_a2oc,
            num_Ky_still_fully_red_a2oc,
            num_Kx_with_u_blue_lines_a2oc,
            num_Kx_still_fully_red_a2oc
        ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, (
            graph_id,

            metrics.get('num_first_order_lines'),
            json.dumps(metrics.get('first_order_lines', [])),
            metrics.get('num_Ky_with_one_blue_line_a1oc'),
            metrics.get('num_Ky_still_fully_red_a1oc'),
            metrics.get('num_Kx_with_one_blue_line_a1oc'),
            metrics.get('num_Kx_still_fully_red_a1oc'),
            json.dumps(metrics.get('untouched_vertex_a1oc', [])),

            metrics.get('num_second_order_lines'),
            json.dumps(metrics.get('second_order_lines', [])),
            json.dumps(metrics.get('num_Ky_with_u_blue_lines_a2oc', {})),
            metrics.get('num_Ky_still_fully_red_a2oc'),
            json.dumps(metrics.get('num_Kx_with_u_blue_lines_a2oc', {})),
            metrics.get('num_Kx_still_fully_red_a2oc')
        ))

        conn.commit()


def drop_all_tables():
    """Drop all user tables."""
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute("DROP TABLE IF EXISTS graph_metrics;")
        cursor.execute("DROP TABLE IF EXISTS graphs;")
        conn.commit()