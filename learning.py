import warnings
def warn(*arg,**kwargs):pass
warnings.warn= warn

from sklearn.ensemble import RandomForestClassifier

from statistics import mode
import numpy as np
import pandas as pd


def classifiers(X, Y, Z,  X_ind, Y_ind, Z_ind, Label1, Label2, Label3, label_ind, sequences, args):

    final_pred = np.array([])
    final_proba = np.array([])

    model1 = RandomForestClassifier(n_estimators=150)
    model2 = RandomForestClassifier(n_estimators=250)
    model3 = RandomForestClassifier(n_estimators=400)
    
    X_train = X
    LabelX_train = Label1

    model1.fit(X_train, LabelX_train)
    pred1 = model1.predict(X_ind)
    X_proba = model1.predict_proba(X_ind)[:, 1]

    Y_train = Y
    LabelY_train = Label2
        
    model2.fit(Y_train, LabelY_train)
    pred2 = model2.predict(Y_ind)
    Y_proba = model2.predict_proba(Y_ind)[:, 1]

    Z_train = Z
    LabelZ_train = Label3
        
    model3.fit(Z_train, LabelZ_train)
    pred3 = model3.predict(Z_ind)
    Z_proba = model3.predict_proba(Z_ind)[:, 1]

    for i in range(0, len(label_ind)):
        final_pred = np.append(final_pred, mode([pred1[i], pred2[i], pred3[i]]))

    final_proba = np.append(final_proba, (X_proba + Y_proba + Z_proba) / 3)
    
    pred_val = []
    true_val = []

    for i in range(len(sequences)):
        if label_ind[i] == 1:
            y_true =  "Positive"
        else:
            y_true = "Negative"

        if final_pred[i] == 1:
            y_pred =  "Positive"
        else:
            y_pred = "Negative"

        true_val.append(y_true)
        pred_val.append(y_pred)

    temp_dict = {'Sequences':sequences, 'True Value': true_val, 'Prediction': pred_val}
    df = pd.DataFrame.from_dict(temp_dict)

    df.to_csv('output.csv',index=False)

    print('Done!!!')



