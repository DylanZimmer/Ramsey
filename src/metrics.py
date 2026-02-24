from math import comb

def compute_noncolored_metrics(n, x, y):
    metrics = {}
    metrics['num_x_simplices'] = comb(n, x)
    metrics['num_y_simplices'] = comb(n, y)
    metrics['x_simplices_per_vertex'] = comb(n-1, x-1)
    metrics['y_simplices_per_vertex'] = comb(n-1, y-1)
    metrics['x_simplices_per_edge'] = comb(n-2, x-2)
    metrics['y_simplices_per_edge'] = comb(n-2, y-2)
    metrics['x_simplices_in_y_simplices'] = comb(y, x)
    return metrics