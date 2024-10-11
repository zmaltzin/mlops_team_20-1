import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from sklearn.preprocessing import LabelEncoder

class ClassPlotter:
    def __init__(self, df, column):
        """Inicializa el objeto con el DataFrame y la columna a analizar"""
        self.df = df
        self.column = column
        self.class_counts = None

    def count_classes(self):
        """Cuenta las ocurrencias de cada clase en la columna dada"""
        self.class_counts = self.df[self.column].value_counts()

    def plot_classes(self):
        """Crea el gráfico de barras utilizando los conteos calculados"""
        if self.class_counts is None:
            raise ValueError("You must count the classes before plotting.")
        
        plt.bar(self.class_counts.index, self.class_counts.values)
        plt.title(f'Count of Each {self.column}')
        plt.xlabel(self.column)
        plt.ylabel('Count')
        plt.show()

class MissingValueAnalyzer:
    def __init__(self, data):
        """Inicializa el objeto con el DataFrame."""
        self.data = data
    
    def get_missing_columns(self):
        """Obtiene las columnas con valores faltantes y sus respectivos conteos."""
        missing_values = self.data.isnull().sum()
        columns_with_missing = missing_values[missing_values > 0]
        return columns_with_missing
    
    def display_missing_columns(self):
        """Muestra las columnas con valores faltantes si existen."""
        columns_with_missing = self.get_missing_columns()
        if columns_with_missing.empty:
            print("No hay columnas con valores faltantes.")
        else:
            print("Columnas con valores faltantes:")
            print(columns_with_missing)

class LabelEncoderWrapper:
    def __init__(self, data):
        """Inicializa el objeto con el DataFrame."""
        self.data = data
        self.label_encoders = {}

    def encode_column(self, column):
        """Aplica label encoding a una columna categórica específica."""
        if column not in self.data.columns:
            raise ValueError(f"La columna '{column}' no existe en el DataFrame.")
        
        label_encoder = LabelEncoder()
        self.data[column] = label_encoder.fit_transform(self.data[column])
        self.label_encoders[column] = label_encoder  
        
    def get_encoded_data(self):
        """Devuelve el DataFrame con las columnas codificadas."""
        return self.data
    
    def decode_column(self, column):
        """Decodifica los valores en una columna previamente codificada."""
        if column not in self.label_encoders:
            raise ValueError(f"La columna '{column}' no fue codificada o no se ha guardado el codificador.")
        
        label_encoder = self.label_encoders[column]
        self.data[column] = label_encoder.inverse_transform(self.data[column])

class CorrelationHeatmap:
    def __init__(self, data):
        """Inicializa el objeto con el DataFrame."""
        self.data = data
        self.correlation_matrix = None

    def calculate_correlation(self):
        """Calcula la matriz de correlación del DataFrame."""
        self.correlation_matrix = self.data.corr()
    
    def plot_heatmap(self, figsize=(16, 12), cmap='coolwarm', annot=False):
        """Grafica el heatmap de la matriz de correlación sin números en las celdas pero con nombres de columnas."""
        if self.correlation_matrix is None:
            raise ValueError("You must calculate the correlation matrix before plotting.")
        
        plt.figure(figsize=figsize)
        # Graficar el heatmap sin anotaciones y manteniendo las etiquetas
        sns.heatmap(self.correlation_matrix, cmap=cmap, annot=annot, cbar=False, xticklabels=True, yticklabels=True)
        plt.title('Correlation Heatmap')
        plt.show()