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

### *author*
Clara Gaubil

### *date*  
31/10/2023

### *Data set:*  
https://www.kaggle.com/code/abdrakhmanmurat/fraudulent-job-posting-detection-nlp/input

