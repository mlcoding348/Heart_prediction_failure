import matplotlib.gridspec as gridspec
import numpy as np
import matplotlib.pyplot as plt
def feature_plots(model, X_data_train, X_data_test,y_train ,indices):
    

    from sklearn.model_selection import cross_val_score

    feat_labels = X_data_train.columns
    test_accuracy = []
    cv_mean = []
    cv_plus = []
    cv_minus = []
    train_accuracy = []
    for i in range(1,len(feat_labels[indices])):
    
        model.fit(X_data_train[feat_labels[indices[0:i]]], y_train)
        #test = model.score(X_data_test[feat_labels[indices[0:i]]] , y_test)
        #test_accuracy.append(test)
    
        train = model.score(X_data_train[feat_labels[indices[0:i]]], y_train)
        train_accuracy.append(train)
    
        X = X_data_train[feat_labels[indices[0:i]]]
        scores =  cross_val_score(estimator=model,
                              X=X, y=y_train, cv=5,n_jobs=1)
        cv_mean.append(np.mean(scores))
        cv_plus.append(np.mean(scores) + np.std(scores))
        cv_minus.append(np.mean(scores) - np.std(scores))
        
    fig, ax1 = plt.subplots()
    ax1.grid()
    #ax1.plot(range(1,len(feat_labels[indices])) , test_accuracy, label = "Test accuracy")
    ax1.plot(range(1,len(feat_labels[indices])) , cv_mean, label = "CV Mean")
    ax1.plot(range(1,len(feat_labels[indices])), train_accuracy, '--', marker='o', color = 'black', label = "Train accuracy")
    ax1.fill_between(range(1,len(feat_labels[indices])),cv_plus , cv_minus, alpha=0.15, color='green' , label = "CV STD")
    plt.xticks(range(X_data_train.shape[1]),feat_labels[indices], rotation=90)
    
    
    ax2 = ax1.twinx()
    
    
    ax1.set_ylabel('Accuracy', color='g')
    ax2.set_ylabel('CV std', color='r')
    ax2.plot(range(1,len(feat_labels[indices])) , np.array(cv_plus) - np.array(cv_mean), '--', color = 'r', label = "CV Std")
    
    ax1.legend(loc='center left', bbox_to_anchor=(1.2, 0.5))
    ax2.legend(loc='center left', bbox_to_anchor=(1.2, 0.7))