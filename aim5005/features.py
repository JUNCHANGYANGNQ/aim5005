import numpy as np
from typing import List, Tuple
### YOU MANY NOT ADD ANY MORE IMPORTS (you may add more typing imports)

class MinMaxScaler:
    def __init__(self):
        self.minimum = None
        self.maximum = None
        
    def _check_is_array(self, x:np.ndarray) -> np.ndarray:
        """
        Try to convert x to a np.ndarray if it'a not a np.ndarray and return. If it can't be cast raise an error
        """
        if not isinstance(x, np.ndarray):
            x = np.array(x)
            
        assert isinstance(x, np.ndarray), "Expected the input to be a list"
        return x
        
    
    def fit(self, x:np.ndarray) -> None:   
        x = self._check_is_array(x)
        self.minimum=x.min(axis=0)
        self.maximum=x.max(axis=0)
        
    def transform(self, x:np.ndarray) -> list:
        """
        MinMax Scale the given vector
        """
        x = self._check_is_array(x)
        diff_max_min = self.maximum - self.minimum
        
        # TODO: There is a bug here... Look carefully! 
         return (x - self.minimum) / diff_max_min
    
    def fit_transform(self, x:list) -> np.ndarray:
        x = self._check_is_array(x)
        self.fit(x)
        return self.transform(x)
    
    
class StandardScaler:
    def __init__(self):
        self.mean = None
        self.std = None  
    
    def fit(self, data: np.ndarray) -> None:
        data = np.array(data)
        self.mean = data.mean(axis=0)
        self.std = data.std(axis=0) + 1e-9  

    def transform(self, data: np.ndarray) -> np.ndarray:
        data = np.array(data)
        return (data - self.mean) / self.std


class LabelEncoder:
    def __init__(self):
        self.classes_ = None

    def fit(self, y):
        y = np.array(y)
        self.classes_ = np.unique(y)

    def transform(self, y):
        if self.classes_ is None:
            raise ValueError("LabelEncoder has not been fitted yet.")
        y = np.array(y)
        return np.array([np.where(self.classes_ == label)[0][0] for label in y])

    def fit_transform(self, y):
        self.fit(y)
        return self.transform(y)
