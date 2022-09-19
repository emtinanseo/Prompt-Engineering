import pandas as pd

class EntityExtraction:
    def __init__(self):
        pass
    
    
    def listify(self, x: str):
        return x.split('\n')
    
    def metrics_str(self, y_true: str, y_extrac: str):
        #metrics_values = {'Accuracy': None, 'Recall': None, 'Precision':None}
        y_true = self.listify(y_true)
        y_extrac = self.listify(y_extrac)
        
        metrics_values = dict()
        n_true = len(y_true)
        n_extrac = len(y_extrac)
        
        temp = y_true
        count = 0
        for entity in y_extrac:
            if entity in temp:
                temp.remove(entity)
                count = count + 1
        
        n_pp = count
        n_pn = len(temp)
        n_np = len(y_extrac) - n_pp
        
        metrics_values['Accuracy'] = n_pp/n_true if n_true>0 else None
        metrics_values['Precision'] = n_pp/n_extrac if n_extrac>0 else None
        metrics_values['Missing'] = n_pn / n_true if n_true>0 else None
        metrics_values['OverShooting'] = n_np/n_extrac if n_extrac>0 else None
        
        return metrics_values
    
    def metrics_df(self, y_true: pd.Series, y_extrac: pd.Series):
        metrics_df = pd.DataFrame(columns= ['Accuracy', 'Precision', 'Missing','OverShooting'], index = range(len(y_true)))
        
        for i in range(len(y_true)):
            data = self.metrics_str(y_true.iloc[i], y_extrac.iloc[i])
            metrics_df.iloc[i]['Accuracy'] = data['Accuracy']
            metrics_df.iloc[i]['Precision'] = data['Precision']
            metrics_df.iloc[i]['Missing'] = data['Missing']
            metrics_df.iloc[i]['OverShooting'] = data['OverShooting']
            
        return metrics_df
        
        
        