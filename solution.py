import pandas as pd
import numpy as np

from scipy.stats import gamma


chat_id = 346373029 # Ваш chat ID, не меняйте название переменной

def solution(p: float, x: np.array) -> tuple:
    # Измените код этой функции
    # Это будет вашим решением
    # Не меняйте название функции и её аргументы
    alpha = 1 - p
    
    loc = x.mean() - 1/2
    n = len(x)
    scale = 2/20**2

    right_q = gamma.ppf(1 - alpha / 2, a = n) / n
    left_q = gamma.ppf(alpha / 2, a = n) / n
    
    return scale * (left_q + loc), \
           scale * (right_q + loc)
