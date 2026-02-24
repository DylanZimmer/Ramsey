import sqlite3
from pathlib import Path

DB_PATH = Path(__file__).parent.parent / "data" / "ramsey.db"

def get_connection():
    """Return a SQLite connection."""
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn

def create_tables():
    """Create graphs and graph_metrics tables if they don't exist."""
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS graphs (
            graph_id INTEGER PRIMARY KEY,
            n_vertices INTEGER NOT NULL,
            x_in_Rxy INTEGER NOT NULL,
            y_in_Rxy INTEGER NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        );
        """)
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS graph_metrics (
            graph_id INTEGER,
            num_x_simplices INTEGER,
            num_y_simplices INTEGER,
            x_simplices_per_vertex INTEGER,
            y_simplices_per_vertex INTEGER,
            x_simplices_per_edge INTEGER,
            y_simplices_per_edge INTEGER,
            x_simplices_in_y_simplices INTEGER,
            FOREIGN KEY(graph_id) REFERENCES graphs(graph_id)
        );
        """)
        conn.commit()

def insert_graph(n_vertices, x_in_Rxy, y_in_Rxy):
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute("""
        INSERT INTO graphs (n_vertices, x_in_Rxy, y_in_Rxy)
        VALUES (?, ?, ?)
        """, (n_vertices, x_in_Rxy, y_in_Rxy))
        conn.commit()
        return cursor.lastrowid

def insert_graph_metrics(graph_id, metrics):
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute("""
        INSERT INTO graph_metrics (
            graph_id,
            num_x_simplices,
            num_y_simplices,
            x_simplices_per_vertex,
            y_simplices_per_vertex,
            x_simplices_per_edge,
            y_simplices_per_edge,
            x_simplices_in_y_simplices
        ) VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        """, (
            graph_id,
            metrics['num_x_simplices'],
            metrics['num_y_simplices'],
            metrics['x_simplices_per_vertex'],
            metrics['y_simplices_per_vertex'],
            metrics['x_simplices_per_edge'],
            metrics['y_simplices_per_edge'],
            metrics['x_simplices_in_y_simplices']
        ))
        conn.commit()