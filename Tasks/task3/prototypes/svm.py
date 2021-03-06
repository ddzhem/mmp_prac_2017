class SVMSolver:
    """
    Класс с реализацией SVM через метод внутренней точки.
    """
    def __init__(self, C, method, kernel='linear'):
        """
        C - float, коэффициент регуляризации
        
        method - строка, задающая решаемую задачу, может принимать значения:
            'primal' - соответствует прямой задаче
            'dual' - соответствует двойственной задаче
        kernel - строка, задающая ядро при решении двойственной задачи
            'linear' - линейное
            'polynomial' - полиномиальное
            'rbf' - rbf-ядро
        Обратите внимание, что часть функций класса используется при одном методе решения,
        а часть при другом
        """
        pass
    
    def compute_primal_objective(self, X, y):
        """
        Метод для подсчета целевой функции SVM для прямой задачи
        
        X - переменная типа numpy.array, признаковые описания объектов из обучающей выборки
        y - переменная типа numpy.array, правильные ответы на обучающей выборке,
        """
        pass
        
    def compute_dual_objective(self, X, y):
        """
        Метод для подсчёта целевой функции SVM для двойственной задачи
        
        X - переменная типа numpy.array, признаковые описания объектов из обучающей выборки
        y - переменная типа numpy.array, правильные ответы на обучающей выборке,
        """ 
        pass
        
    def fit(self, X, y, tolerance, max_iter):
        """
        Метод для обучения svm согласно выбранной в method задаче
        
        X - переменная типа numpy.array, признаковые описания объектов из обучающей выборки
        y - переменная типа numpy.array, правильные ответы на обучающей выборке,
        tolerance - требуемая точность для метода обучения
        max_iter - максимальное число итераций в методе
        
        """
            
    def predict(self, X):
        """
        Метод для получения предсказаний на данных
        
        X - переменная типа numpy.array, признаковые описания объектов из обучающей выборки
        """
        pass
        
    def get_w(self, X=None, y=None):
        """
        Получить прямые переменные (без учёта w_0)
        
        Если method = 'dual', а ядро линейное, переменные должны быть получены
        с помощью выборки (X, y) 
        
        return: одномерный numpy array
        """
        pass
        
    def get_w0(self, X=None, y=None):
        """
        Получить вектор сдвига
        
        Если method = 'dual', а ядро линейное, переменные должны быть получены
        с помощью выборки (X, y) 
        
        return: float
        """
        pass
        
    def get_dual(self):
        """
        Получить двойственные переменные
        
        return: одномерный numpy array
        """    