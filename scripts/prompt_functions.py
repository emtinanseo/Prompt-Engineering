import pandas as pd


def streamline_tokens(token:list) -> str:
    extracted = ''
    if len(token) != 0:
        for i,x in enumerate(token):
            text = x['text']
            entityLabel = x['entityLabel']
            extracted = extracted + entityLabel +': ' + text
            if i < len(token)-1:
                extracted = extracted + '\n'
    return extracted

def example_prompt(df: pd.DataFrame, num = None, task_description = '', sep = '\n--\n') -> str:
    if str(num) == 'None':
        n = len(df)
    else:
        n = num
    
    prompt = task_description
    for i in range(n):
        doc = df.iloc[i]['document']
        extracted = streamline_tokens(df.iloc[i]['tokens'])
        prompt = prompt + 'DOCUMENT: ' + doc + '\nEXTRACTED TEXT:\n'+ extracted + sep
    
    return prompt

def test_prompt(df: pd.DataFrame, index: int) -> str:
    doc = df.iloc[index]['document']
    prompt = 'DOCUMENT: ' + doc + '\nEXTRACTED TEXT:' 
    return prompt

def test_labels(df: pd.DataFrame, index:int) -> str:
    extracted = streamline_tokens(df.iloc[index]['tokens'])
    return extracted


def make_prompt(dfTest:pd.DataFrame, indexTest:int, dfEx=None ,numEx=None, task_description='', sep ='\n--\n', same_file=False) -> str:
    if same_file:
        dfEx = dfTest
        numEx = indexTest if str(numEx) == 'None' else numEx
    
    promptEx = example_prompt(dfEx, num=numEx, task_description=task_description, sep=sep)
    promptTest = test_prompt(dfTest, indexTest)
    prompt = promptEx + promptTest
    
    return prompt

    
    
    