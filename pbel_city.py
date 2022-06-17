 import pickle

 names=["alex","busted","ping pong"]
 #k="rupesh.pkl"
 f=open("filename","wb")
 pickle.dump("names")
 f.close()

f1=open("file name","rb")
k=pickle.load("file name")
f1.close()
print(k)
