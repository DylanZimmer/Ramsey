import sqlite3
import json
from pathlib import Path

DB_PATH = Path(__file__).parent.parent / "data" / "ramsey.db"


def get_connection():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn

def create_tables():
    with get_connection() as conn:
        cursor = conn.cursor()

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS graphs (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            v INTEGER NOT NULL,
            x INTEGER NOT NULL,
            y INTEGER NOT NULL,
            UNIQUE(v, x, y)
        )
        """)

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS graph_metrics (
            graph_id INTEGER PRIMARY KEY,
            v INTEGER NOT NULL,
            x INTEGER NOT NULL,
            y INTEGER NOT NULL,
            Kx_with_u_blue_lines_a1oc TEXT,
            Ky_with_u_blue_lines_a1oc TEXT,
            Kx_with_u_blue_lines_a2oc TEXT,
            Ky_with_u_blue_lines_a2oc TEXT,
            FOREIGN KEY (graph_id) REFERENCES graphs(id)
        )
        """)

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS graph_metrics_brute (
            graph_id INTEGER PRIMARY KEY,
            v INTEGER NOT NULL,
            x INTEGER NOT NULL,
            y INTEGER NOT NULL,
            Kx_with_u_blue_lines_a1oc TEXT,
            Ky_with_u_blue_lines_a1oc TEXT,
            Kx_with_u_blue_lines_a2oc TEXT,
            Ky_with_u_blue_lines_a2oc TEXT,
            FOREIGN KEY (graph_id) REFERENCES graphs(id)
        )
        """)
        conn.commit()

def insert_graph(v, x, y):
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(
            "INSERT OR IGNORE INTO graphs (v, x, y) VALUES (?, ?, ?)",
            (v, x, y)
        )
        conn.commit()

        if cursor.lastrowid:
            return cursor.lastrowid

        #If it already existed
        cursor.execute(
            "SELECT id FROM graphs WHERE v = ? AND x = ? AND y = ?",
            (v, x, y)
        )
        row = cursor.fetchone()
        return row["id"]

def metrics_exist(graph_id):
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(
            "SELECT 1 FROM graph_metrics WHERE graph_id = ?",
            (graph_id,)
        )
        return cursor.fetchone() is not None

def insert_metrics(graph_id, v, x, y, metrics):
    with get_connection() as conn:
        cursor = conn.cursor()

        cursor.execute(
            """
            INSERT INTO graph_metrics (
                graph_id,
                v,
                x,
                y,
                Kx_with_u_blue_lines_a1oc,
                Ky_with_u_blue_lines_a1oc,
                Kx_with_u_blue_lines_a2oc,
                Ky_with_u_blue_lines_a2oc
            )
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)
            """,
            (
                graph_id,
                v,
                x,
                y,
                json.dumps(metrics["Kx_with_u_blue_lines_a1oc"]),
                json.dumps(metrics["Ky_with_u_blue_lines_a1oc"]),
                json.dumps(metrics["Kx_with_u_blue_lines_a2oc"]),
                json.dumps(metrics["Ky_with_u_blue_lines_a2oc"]),
            )
        )

        conn.commit()

def insert_metrics_brute(graph_id, v, x, y, metrics):
    with get_connection() as conn:
        cursor = conn.cursor()

        cursor.execute(
            """
            INSERT INTO graph_metrics_brute (
                graph_id,
                v,
                x,
                y,
                Kx_with_u_blue_lines_a1oc,
                Ky_with_u_blue_lines_a1oc,
                Kx_with_u_blue_lines_a2oc,
                Ky_with_u_blue_lines_a2oc
            )
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)
            """,
            (
                graph_id,
                v,
                x,
                y,
                json.dumps(metrics["Kx_with_u_blue_lines_a1oc"]),
                json.dumps(metrics["Ky_with_u_blue_lines_a1oc"]),
                json.dumps(metrics["Kx_with_u_blue_lines_a2oc"]),
                json.dumps(metrics["Ky_with_u_blue_lines_a2oc"]),
            )
        )

        conn.commit()