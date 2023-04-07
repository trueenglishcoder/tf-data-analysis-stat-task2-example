import pandas as pd
import numpy as np

from scipy.stats import gamma


chat_id = 346373029 # Ваш chat ID, не меняйте название переменной

def solution(p: float, x: np.array) -> tuple:
    # Измените код этой функции
    # Это будет вашим решением
    # Не меняйте название функции и её аргументы
    alpha = 1 - p
    loc = x.mean() - 1
    scale = 2/20**2
    n = len(x)
    
    return loc - scale * gamma.ppf(1 - alpha / 2, n), \
           loc - scale * gamma.ppf(alpha / 2, n)
