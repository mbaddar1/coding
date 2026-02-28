"""
Here is a **realistic mock ML coding interview question** matching CodeSignal / Dropbox / Forgent AI style. It focuses on **clarity, reasoning, stopping criteria, evaluation, and ML intuition**, not fancy optimization.

---
# Mock Coding Interview Question: Implement Logistic Regression from Scratch
## Problem Statement
You are given a dataset for binary classification. Your task is to implement **Logistic Regression from scratch using NumPy**, without using any ML libraries such as scikit-learn.
You must implement training using **gradient descent**.
---

## Dataset

You are given:

```python
X = np.array([
    [0.5, 1.2],
    [1.0, 1.8],
    [1.5, 0.8],
    [2.0, 2.5],
    [2.5, 2.0],
    [3.0, 3.5]
])

y = np.array([0, 0, 0, 1, 1, 1])
```

Where:

* X shape = (n_samples, n_features)
* y shape = (n_samples,)
* Labels are binary: 0 or 1

---

## Requirements

Implement a class:

```python
class LogisticRegression:

    def __init__(self, learning_rate=0.01, max_iter=1000, tol=1e-6):
        pass

    def fit(self, X, y):

        # Train model using gradient descent

        pass

    def predict_proba(self, X):

        # Return probability estimates

        pass

    def predict(self, X):

        # Return binary predictions (0 or 1)

        pass
```

---

## Mathematical Definitions

### Sigmoid function

[
\sigma(z) = \frac{1}{1 + e^{-z}}
]

---

### Prediction

[
\hat{y} = \sigma(Xw + b)
]

---

### Binary Cross-Entropy Loss

[
L = -\frac{1}{n} \sum (y \log(\hat{y}) + (1-y)\log(1-\hat{y}))
]

---

### Gradient

[
dw = \frac{1}{n} X^T (\hat{y} - y)
]

[
db = \frac{1}{n} \sum (\hat{y} - y)
]

---

## Training Requirements

Use gradient descent:

```python
w = w - learning_rate * dw
b = b - learning_rate * db
```

Stop when either:

* max_iter reached, OR
* loss change < tol

---

## Expected Usage

```python
model = LogisticRegression(learning_rate=0.1, max_iter=1000)

model.fit(X, y)

preds = model.predict(X)

print(preds)
```

Expected output should roughly match:

```python
[0, 0, 0, 1, 1, 1]
```

---

# Follow-up Questions (VERY IMPORTANT — interviewers WILL ask)

Be ready to answer these:

---

## Follow-up 1: How do you know when to stop training?

Expected answer:

• max iterations
• loss convergence
• gradient magnitude small
• validation loss stops improving

---

## Follow-up 2: What is the time complexity per iteration?

Expected answer:

[
O(n \cdot d)
]

Where:

* n = samples
* d = features

---

## Follow-up 3: Why use sigmoid?

Expected answer:

• maps real numbers → probability (0,1)
• differentiable → gradient descent works

---

## Follow-up 4: How would you evaluate this model?

Expected answer:

For binary classification:

• Accuracy
• Precision
• Recall
• F1 score
• ROC-AUC

---

## Follow-up 5: How to improve convergence?

Expected answer:

• better learning rate
• feature normalization
• better initialization
• momentum / Adam
• regularization

---

## Follow-up 6: What causes overfitting?

Expected answer:

• too many parameters
• too little data
• training too long

Solution:

• regularization
• early stopping

---

# Harder Follow-up (common at Staff level)

Modify your code to include L2 regularization:

Loss becomes:

[
L = BCE + \lambda ||w||^2
]

---

# What interviewer evaluates with this question

This single question tests:

• Gradient descent understanding
• Loss function understanding
• Vectorized NumPy coding
• ML fundamentals
• Convergence logic
• Code clarity
• ML intuition

---

# If you want, I can now give you the full reference solution in clean interview-ready form.

"""

import numpy as np


class LogisticRegression:
    def __init__(self,  max_iter=1000, tol=1e-6,y_threshold=0.5,debug=False,lambd=1e-3):
        self.max_iter = max_iter
        self.tol = tol
        self.y_threshold = y_threshold
        self.debug = debug
        self.lambd = lambd

    def fit(self, X, y,lr:float=1e-3,epochs:int=1000,batch_size:int=64,detla=1e-4,patience = 5):
        """
        Train model using gradient descent
        """
        assert len(X.shape) == 2
        assert len(y.shape) == 2
        n = X.shape[0]
        d = X.shape[1]
        assert y.shape[0] == n
        assert y.shape[1] == 1
        self.w = np.random.randn(d).reshape(-1,1)
        self.b = np.random.randn(1)
        loss_alpha = 0.9
        warmup_epochs = 10
        loss_ma = None
        num_batches = n // batch_size
        learning_curve = []
        for epoch in range(epochs):
            epoch_loss = 0.0
            for batch_start in range(0, n, batch_size):
                batch_end = min(batch_start + batch_size, n)
                Xb = X[batch_start:batch_end,:]
                yb = y[batch_start:batch_end].reshape(-1,1)
                yb_hat_proba = self.predict_proba(Xb)
                ce = Utils.calc_CE(y_true=yb, y_pred=yb_hat_proba)
                epoch_loss += ce
                dLdw = 1.0/n * np.matmul(Xb.T,(yb_hat_proba-yb))+self.lambd*self.w
                dLdb = 1.0/n * sum(yb_hat_proba-yb)
                self.w = self.w - lr * dLdw
                self.b = self.b - lr * dLdb
            avg_epoch_loss = 1.0*epoch_loss/num_batches
            loss_ma =  avg_epoch_loss if loss_ma is None else loss_alpha * avg_epoch_loss + (1 - loss_alpha) * loss_ma
            learning_curve.append(avg_epoch_loss)
            print(f"loss_ma at epoch {epoch} = {loss_ma}")
            # early stopping
            if epoch > warmup_epochs:
                loss_delta = learning_curve[epoch]-learning_curve[epoch-1]
                saturation_count = 0
                if  loss_delta < 0 and abs(loss_delta) < detla:
                    saturation_count+=1
                else:
                    saturation_count = 0
                if saturation_count>=patience:
                    print("Early stopping at epoch {}".format(epoch))
                    return learning_curve
        return learning_curve
    def predict_proba(self, X):
        """
        Return probability estimates
        """
        z = np.dot(X, self.w) + self.b
        y_proba = np.array([Utils.sigmoid(u) for u in z]).reshape(-1,1)
        return y_proba

    def predict(self, X):
        """
        Return binary predictions (0 or 1)
        """
        y_proba = self.predict_proba(X)
        y = [1 if u >= self.y_threshold else 0 for u in y_proba]
        return y


class Utils:
    @staticmethod
    def sigmoid(x):
        return 1 / (1 + np.exp(-x))
    @staticmethod
    def calc_CE(y_true, y_pred):
        n = y_true.shape[0]
        loss_sum = 0
        for j in range(n):
            loss_sum+= -(y_true[j]*np.log(y_pred[j])+(1-y_true[j])*np.log(1-y_pred[j]))
        return loss_sum[0]/n

class DataSetGenerator:
    @staticmethod
    def generate(n, d, t):
        X = np.random.randn(n, d)
        print("X.shape = ", X.shape)
        w = np.random.randn(d)
        b = np.random.randn(1)
        print("w.shape = ", w.shape)
        z = np.dot(X, w)+b
        y_proba = [Utils.sigmoid(z1) for z1 in z]
        y = np.array([1 if u >=t else 0 for u in y_proba])
        return X, y


"""
Points *
Reg. * 
Batch Training 
Early stop
handle imbalance
multidimensional output 
"""
if __name__ == '__main__':
    n = 10_000
    d = 2
    t = 0.5
    debug = False
    X,y = DataSetGenerator.generate(n, d, t)
    y = y.reshape(-1,1)
    # print(X)
    # print(y)
    log_reg = LogisticRegression()
    log_reg.fit(X,y,lr=1e-2,epochs=10_000)


