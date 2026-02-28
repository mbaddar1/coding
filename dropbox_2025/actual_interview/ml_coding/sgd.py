import numpy as np


def L2_loss(y_true, y_pred):
    return 0.5 * np.mean(np.square(y_true - y_pred))

def predict(w,X):
    y_pred = np.matmul(X,w)
    return y_pred

def SGD(X,y,batch,epochs,alpha):
    n,d = X.shape[0],X.shape[1]
    w = np.random.randn(d,1)
    for epoch in range(epochs):
        epochs_loss = 0
        for batch_start in range(0,n,batch):
            batch_end = min(batch_start + batch,n)
            Xb = X[batch_start:batch_end,:]
            yb = y[batch_start:batch_end]
            yb_pred = predict(w,Xb)
            l2loss = L2_loss(yb,yb_pred)
            epochs_loss += l2loss
            dldw = 1.0/batch*np.average(np.multiply((yb_pred - yb),Xb),axis=0).reshape(-1,1)
            w = w-alpha*dldw
        print(f"epoch = {epoch}, avg loss = {epochs_loss/n}")


if __name__=="__main__":
    n = 10_000
    d = 2
    X = np.random.rand(n, d)
    w = np.random.rand(d).reshape(-1, 1)
    y = np.matmul(X, w) + np.random.rand(n, 1)
    epochs = 1000
    batch = 64

    SGD(X,y,batch,epochs,0.001)
