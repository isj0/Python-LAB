import pandas as pd

print(pd.__version__)

dataset = {
    'car': ["BMW", "Volvo", "Ford"],
    'passings': [3, 7, 2]
}

myvar = pd.DataFrame(dataset)

print(myvar)