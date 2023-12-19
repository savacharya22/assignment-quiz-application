import json
import pandas as pd

def high_scores():
    
    try: 
        with open("scores.json", "r") as f:
            scores = json.load(f)
            if not scores:
                print("No scores yet")
            else:
                
                df = pd.DataFrame(scores)
                df = df.sort_values(by='score', ascending=False)
                print("Leaderboard:")
                print(df.to_string(index=False))

            
    except FileNotFoundError:
        scores = []
        with open("scores.json", "w") as f:
            json.dump(scores, f)
  
  
            
def save_score(name, score):
    try: 
        with open("scores.json", 'r') as f:
            scores = json.load(f)
    except FileNotFoundError:
        scores =[]
        
    scores.append({'name': name, 'score': score})
    
    with open('scores.json', 'w') as f:
        json.dump(scores, f)
   




