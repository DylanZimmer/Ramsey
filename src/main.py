import db
import graph_generation
import metrics
import json
import brute
import metrics_easy

def main():
    db.drop_tables()
    db.create_tables()

    #num vertices
    """
    v = 8
    xy1 = 3
    xy2 = 4
    x = min(xy1, xy2)
    y = max(xy1, xy2)
    """
    """
    vL = [9,10,11,12,13,14,15,16]
    xL = [3,4,5,6,3,4,5,6]
    yL = [4,5,6,7,4,5,6,7]
    """

    vL = [16,20,24]
    xL = [8,8,8]
    yL = [9,9,9]


    for i in range(len(vL)):
        v = vL[i]
        x = xL[i]
        y = yL[i]

        graph_id = db.insert_graph(v,x,y)

        brute_metrics = brute.brute(v,x,y)
        db.insert_metrics_brute(graph_id, v, x, y, brute_metrics)


"""
        a2oc = metrics_easy.compute_easy(v,x,y)
        db.insert_metrics(graph_id, v, x, y, a2oc)
"""

"""
        if not db.metrics_exist(graph_id):
            computed_metrics = metrics.compute_metrics(v,x,y)
            db.insert_metrics(graph_id, v, x, y, computed_metrics)
"""


if __name__ == "__main__":
    main()