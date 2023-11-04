# Natural Language Processing for Fraudulent Job Posting Detection

The aim of this project is to implement a fraudulent job posting prediction/detection model. To achieve this, a data exploratory analysis was first carried out, followed by the creation of a pre-processing pipeline.  Next, this project shows the implementation and comparison of different classification models (logistic regression, naive bayes, SVM) as well as model improvement processes (class rebalancing, hyperparameter variation). Finally, this project also includes the implementation and training of an RNN model for the detection of fraudulent job postings.

## Results: 

| Model | Accuracy | f1-score Fake class (%) | f1-score Fake class (%)
| --------- | --------- | --------- | ---------
|Logistic Regression|0.96|0.36|0.98| 
|Naive Bayes|0.93|0.52|0.96| 
|SVM (Baseline model)|0.97|0.64|0.99| 
|SVM (SMOTE + hyperparameters variation)|0.97|0.67|0.98| 
|RNN|0.68|0.10|0.81|


## Conclusion:

Dealing with class imbalance in fraud detection is a significant challenge. Traditional machine learning models like Logistic Regression, Naive Bayes, and even SVM struggle to identify fraudulent cases effectively due to the imbalanced distribution of the classes. The use of techniques like SMOTE and hyperparameter variation can  improve SVM performance especially for the prediciton of the "Fake" class, but there's still room for enhancement.

The RNN model, while showing promise in other natural language processing tasks, struggles with this particular job posting fraud detection problem, indicating the need for more sophisticated approaches.

### *author*
Clara Gaubil

### *date*  
31/10/2023

### *Dataset:*  
https://www.kaggle.com/code/abdrakhmanmurat/fraudulent-job-posting-detection-nlp/input

### *Sources:*  
https://www.kaggle.com/code/abdrakhmanmurat/fraudulent-job-posting-detection-nlp/input

https://scikit-learn.org/stable/modules/svm.html

https://medium.com/@dinghan1995/how-to-tackle-dataset-class-imbalance-for-nlp-4453af6f6b87#:~:text=Oversampling%20and%20undersampling%20techniques%20are,to%20achieve%20a%20balanced%20dataset.

https://www.forbes.com/sites/forbesbusinesscouncil/2023/05/10/getting-value-from-nlp-for-fraud-detection/?sh=7dcdf88f1ec8