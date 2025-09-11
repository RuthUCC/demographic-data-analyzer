import numpy as np

def calculate(list):
    if len(list) != 9:
        raise ValueError("List must contain nine numbers.")
    
    b = np.array(list)
    d = b.reshape(3, 3)
    
    calculations = {
        'Mean': [np.mean(d, axis=0).tolist(), np.mean(d, axis=1).tolist(), np.mean(d).item()],
        'Variance': [np.var(d, axis=0).tolist(), np.var(d, axis=1).tolist(), np.var(d).item()],
        'Standard deviation': [np.std(d, axis=0).tolist(), np.std(d, axis=1).tolist(), np.std(d).item()],
        'Max': [np.max(d, axis=0).tolist(), np.max(d, axis=1).tolist(), np.max(d).item()],
        'Min': [np.min(d, axis=0).tolist(), np.min(d, axis=1).tolist(), np.min(d).item()],
        'Sum': [np.sum(d, axis=0).tolist(), np.sum(d, axis=1).tolist(), np.sum(d).item()]
    }
    
    return calculations


