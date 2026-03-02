import db
import graph_generation
import metrics
import json
import brute

def main():
    db.create_tables()

    #num vertices
    """
    v = 8
    xy1 = 3
    xy2 = 4
    x = min(xy1, xy2)
    y = max(xy1, xy2)
    """
    vL = [8,8,9,9]
    xL = [3,4,4,6]
    yL = [5,4,5,5]


    for i in range(4):
        v = vL[i]
        x = xL[i]
        y = yL[i]
        
        graph_id = db.insert_graph(v=v, x=x, y=y)

        brute_metrics = brute.brute(v,x,y)
        db.insert_metrics_brute(graph_id, v, x, y, brute_metrics)
    
        if not db.metrics_exist(graph_id):
            computed_metrics = metrics.compute_metrics(v,x,y)
            db.insert_metrics(graph_id, v, x, y, computed_metrics)


if __name__ == "__main__":
    main()