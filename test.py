import pandas as pd
from misogny_classifier import get_misogny_classification
from toxic_classifier import get_toxic_classification

df = pd.read_csv('final_labels.csv')

def find_comment_parents(df, row_index):
    parents = []
    current_row = df.iloc[row_index]
    while pd.notna(current_row.iloc[2]):
        parent_id = current_row.iloc[2].split('_')[1] if '_' in current_row.iloc[2] else current_row.iloc[2]

        parent_row = df[df['entry_id'] == parent_id]
        
        if parent_row.empty:
            break
            
        parent_row = parent_row.iloc[0]
        comment = parent_row.iloc[6]
        parents.append(comment)
        
        current_row = parent_row

    parents.reverse()
    
    return parents


def find_parents(idx):
    parents = find_comment_parents(df, 6565)
    str1 = ""

    for parent in parents:
        str1 += parent + "\n\n--------\n\n"
    
    return str1

for i in range(len(df)):
    comment = df.iloc[i].iloc[6]
    parents = find_parents(i)
    classification = get_toxic_classification(parents, comment)
    
    print(comment)
    print(classification)
    
for i in range(len(df)):
    comment = df.iloc[i].iloc[6]
    parents = find_parents(i)
    classification = get_misogny_classification(parents, comment)
    
    print(comment)
    print(classification)