class univariate():
        def Qualquan (dataset):
            Qual = []
            Quan = []
            for col in dataset.columns:
                if dataset[col].dtype == 'O':
                    Qual.append(col)
                else:
                    Quan.append(col)
            return Qual, Quan      
        
        def freqtable(col,dataset):
            freqtable = pd.DataFrame(columns = ['Unique_Values', 'Frequency', 'Relative_Frequency', 'CumSum'])
            freqtable['Unique_Values'] = dataset[col].value_counts().index
            freqtable['Frequency'] = dataset[col].value_counts().values
            freqtable['Relative_Frequency'] = (freqtable['Frequency']/215)
            freqtable['CumSum'] = freqtable['Relative_Frequency'].cumsum()
            return freqtable
        
        def descriptivetable(dataset,Quan):
            descriptive = pd.DataFrame(index = ['Mean','Median','Mode','Q1-25%','Q2-50%','Q3-75%','99%','Q4-100%','IQR','1.5Range',
                                           'Lesser','Greater','min','max'], columns = Quan)
            for col in Quan:
                descriptive[col]['Mean'] = dataset[col].mean()
                descriptive[col]['Median'] = dataset[col].median()
                descriptive[col]['Mode'] = dataset[col].mode()[0]
                descriptive[col]['Q1-25%'] = dataset.describe()[col]['25%']
                descriptive[col]['Q2-50%'] = dataset.describe()[col]['50%']
                descriptive[col]['Q3-75%'] = dataset.describe()[col]['75%']
                descriptive[col]['99%'] = np.percentile(dataset[col],99)
                descriptive[col]['Q4-100%'] = dataset.describe()[col]['max']
                descriptive[col]['IQR'] = descriptive[col]['Q3-75%'] - descriptive[col]['Q1-25%']
                descriptive[col]['1.5Range'] = 1.5*descriptive[col]['IQR']
                descriptive[col]['Lesser'] = descriptive[col]['Q1-25%'] - descriptive[col]['1.5Range']
                descriptive[col]['Greater'] = descriptive[col]['Q3-75%'] + descriptive[col]['1.5Range']
                descriptive[col]['min'] = dataset[col].min()
                descriptive[col]['max'] = dataset[col].max()
            return descriptive
                
        def replace_outlier(dataset,descriptive):
            for col in Lesser:
                dataset[col][dataset[col] < descriptive[col]['Lesser']] = descriptive[col]['Lesser'] 
            for col in Greater:
                dataset[col][dataset[col] > descriptive[col]['Greater']] = descriptive[col]['Greater']
            return descriptive           
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                