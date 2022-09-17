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

def example_prompt(df: pd.DataFrame, num = None, sep = '\n--\n') -> str:
    if not num:
        n = len(df)
    else:
        n = num
    
    prompt = ''
    for i in range(n):
        doc = df.iloc[n]['document']
        extracted = streamline_tokens(df.iloc[n]['tokens'])
        prompt = prompt + 'DOCUMENT: ' + doc + '\nEXTRACTED TEXT:\n'+ extracted + sep
    
    return prompt