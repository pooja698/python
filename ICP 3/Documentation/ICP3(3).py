import numpy as np
x = np.random.random(20)
print("x:",x)
y=x.reshape(4,5)
print("y:",y)
print("Maximum value replaced by 0:")
print(np.where(y==np.amax(y,axis=1,keepdims=True),0,y))