import db
import graph_generation
import metrics
import json

def main():
    db.create_tables()

    #num vertices
    v = 8
    xy1 = 3
    xy2 = 4
    x = min(xy1, xy2)
    y = max(xy1, xy2)

    G = graph_generation.complete_graph(v)

    edges_json = json.dumps(list(G.edges()))

    graph_id = db.insert_graph(
        n_vertices=v,
        x_in_Rxy = x,
        y_in_Rxy = y
    )

    db.create_tables()

    computed_metrics = metrics.compute_metrics(v,x,y)

    db.insert_graph_metrics(graph_id, computed_metrics)

if __name__ == "__main__":
    main()