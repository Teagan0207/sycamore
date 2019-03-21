
# coding: utf-8

# In[2]:
import xgboost as xgb
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split,cross_validate
from sklearn.svm import SVC, LinearSVC
from sklearn.ensemble import RandomForestClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.linear_model import Perceptron
from sklearn.linear_model import SGDClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import RandomizedSearchCV
from sklearn.model_selection import GridSearchCV
import numpy as np
from sklearn.metrics import accuracy_score,log_loss
import pandas as pd
import lightgbm as lgb
from sklearn.naive_bayes import GaussianNB
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.discriminant_analysis import QuadraticDiscriminantAnalysis
from sklearn.naive_bayes import MultinomialNB
from sklearn.neural_network import MLPClassifier
from sklearn.ensemble import AdaBoostClassifier
from sklearn.ensemble import BaggingClassifier
from sklearn.ensemble import ExtraTreesClassifier
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.ensemble import VotingClassifier
from sklearn.linear_model import LogisticRegression
import catboost as cb
from sklearn.decomposition import PCA 
from sklearn.linear_model import LinearRegression,BayesianRidge,ARDRegression,ElasticNetCV,LassoCV,RidgeCV
from sklearn.manifold import TSNE
from sklearn.feature_selection import SelectKBest,SelectFromModel
from sklearn.feature_selection import chi2,SelectPercentile, f_classif,RFECV
from tpot import TPOTClassifier
from vecstack import StackingTransformer
from sklearn.preprocessing import Normalizer,MinMaxScaler

def import_(path1=r"train_updated.csv",path2=r'processed-test.csv'):


    data = pd.read_csv(path1)
    data2=pd.read_csv(path2)
    
    test=data2.drop(['team1_coach_name', 'team2_coach_name'],axis=1)
  
    Y_train = data['result']
    X_train = data.drop(['result','Unnamed: 0'],axis=1)
    test=test.drop(['Unnamed: 0','region'],axis=1)
    
    score_train=X_train['score']
    
    X_train=X_train.drop(['score'],axis=1)
    X_train=X_train.drop(['num_ot'],axis=1)

    X_train=X_train.drop(['lat','long'],axis=1)
    X_test=test.drop(['lat','long'],axis=1)
    stdSc = StandardScaler()
    X_train.loc[:] = stdSc.fit_transform(X_train.loc[:])
  

    
#     print(len(X_train.columns))
#     print(len(X_test.columns))
#     print((X_train.columns))
#     print((X_test.columns))
 
    X_test.loc[:] = stdSc.transform(X_test.loc[:])
   

    


    # print(len(X_train.columns))
    #print(len(X_test.columns))
    
#     X_train=X_train.drop(['pt_overall_ncaa','pt_overall_ff','pt_overall_s16','pt_school_ncaa','pt_school_ff','pt_school_s16','pt_team_season_losses','pt_coach_season_losses', 'pt_team_season_wins','pt_coach_season_wins'],axis=1)
#     X_test=X_test.drop(['pt_overall_ncaa','pt_overall_ff','pt_overall_s16','pt_school_ncaa','pt_school_ff','pt_school_s16','pt_team_season_losses','pt_coach_season_losses', 'pt_team_season_wins','pt_coach_season_wins'],axis=1)
    return [X_train,Y_train,X_test]
    # print(len(X_train.columns))
    #print(len(X_test.columns))
data=import_()
X_train=data[0]
Y_train=data[1]
X_test=data[2]

from sklearn.model_selection import cross_val_score
import warnings
def training(model,X_train=X_train,Y_train=Y_train):
    def warn(*args, **kwargs):
        pass
    warnings.warn=warn
    x_train, x_test, y_train, y_test = train_test_split(X_train, Y_train, test_size=0.16)
    model.fit(x_train,y_train)
    cross_score=np.mean(cross_val_score(model,x_train,y_train,cv=10,scoring='accuracy'))
    pre=model.predict(x_test)
    pre_train=model.predict(x_train)
    print("val_log_loss: ",format(log_loss(y_test,pre),'f'))
    print("train_log_loss",format(log_loss(y_train,pre_train),'f'))
    print( "Score: ", model.score(x_train,y_train))
    print('Val_score: ',cross_score)
    print('')
    
    try:
        print('test_score: ',model.score(x_test,y_test))
        prob=model.predict_proba(x_test)
        print("log_loss: ",format(log_loss(y_test,prob),'f'))
    except:
        pass
    try:
        important_features_dict = {}
        col=list(X_train.columns.values)
        for idx,i in enumerate(model.feature_importances_):
            important_features_dict[col[idx]]=i
#         important_features_list = sorted(important_features_dict,key=important_features_dict.get,reverse=True)
#         for i in range(len(important_features_list)):
#             print(important_features_list[i],important_features_dict[important_features_list[i]])
        return sorted(important_features_dict.items(), key=lambda kv: kv[1],reverse=True)
 
    except:
        pass
    


def coef(model,X_train):
    col=list(X_train.columns.values)
    assert len(col)==len(model.coef_)
    prior=np.abs(model.coef_)
    coef_dict={}
    try:
        for idx,i in enumerate(prior[0]):
            coef_dict[col[idx]]=i
    except:
        for idx,i in enumerate(prior):
            coef_dict[col[idx]]=i
    return sorted(coef_dict.items(), key=lambda kv: kv[1],reverse=True)
#     coef_list = sorted(coef_dict,key=coef_dict.get,reverse=True)
#     for i in range(len(coef_list)):
#         print(coef_list[i],coef_dict[coef_list[i]],i+1)

def linear(model,X_train=X_train):
    x_train, x_test, y_train, y_test = train_test_split(X_train, score_train, test_size=0.16)
    clssfy=[]
    clf=model
    clf.fit(x_train,y_train)
    prediction=clf.predict(x_train)
    predict_test=clf.predict(x_test)
#     for i in predict_test:
#         if i>0:
#             clssfy.append(1)
#         else:
#             clssfy.append(0)
#     assert len(clssfy)==len(y_test)
#     count=0
#     for i in range(len(clssfy)):
#         if clssfy[i]==y_test[i]:
#             count+=1
            
    print('MSE:',np.mean(np.power(y_train - prediction, 2)))
    print('train score:',clf.score(x_train,y_train))
    print('test MSE:',np.mean(np.power(y_test - predict_test, 2)))
    print('test score:',clf.score(x_test,y_test))
    
#    print('classify score',float(count)/len(clssfy))
#     print(clf.coef_)
    print('\n')
    return coef(model)
    


# linear(LassoCV(cv=10))
# linear(RidgeCV(cv=10))
# linear(ARDRegression())
# linear(BayesianRidge())
# linear(ElasticNetCV(cv=10))

#feature selection
def features(model):

    model.fit(X_train, Y_train)
    mask=model.get_support()
    print(X_train.columns[~mask])
#     N_train=model.transform(X_train)
#     N_test=model.transform(X_test)

    

#features(SelectKBest(f_classif, k=50))
#features(RFECV(estimator=LogisticRegression(), step=1, scoring='accuracy'))



# class LR(LogisticRegression):
#     def __init__(self, threshold=0.01, dual=False, tol=1e-4, C=1.0,
#                  fit_intercept=True, intercept_scaling=1, class_weight=None,
#                  random_state=None, solver='liblinear', max_iter=100,
#                  multi_class='ovr', verbose=0, warm_start=False, n_jobs=1):

#         #权值相近的阈值
#         self.threshold = threshold
#         LogisticRegression.__init__(self, penalty='l1', dual=dual, tol=tol, C=C,
#                  fit_intercept=fit_intercept, intercept_scaling=intercept_scaling, class_weight=class_weight,
#                  random_state=random_state, solver=solver, max_iter=max_iter,
#                  multi_class=multi_class, verbose=verbose, warm_start=warm_start, n_jobs=n_jobs)
#         #使用同样的参数创建L2逻辑回归
#         self.l2 = LogisticRegression(penalty='l2', dual=dual, tol=tol, C=C, fit_intercept=fit_intercept, intercept_scaling=intercept_scaling, class_weight = class_weight, random_state=random_state, solver=solver, max_iter=max_iter, multi_class=multi_class, verbose=verbose, warm_start=warm_start, n_jobs=n_jobs)

#     def fit(self, X, y, sample_weight=None):
#         #训练L1逻辑回归
#         super(LR, self).fit(X, y, sample_weight=sample_weight)
#         self.coef_old_ = self.coef_.copy()
#         #训练L2逻辑回归
#         self.l2.fit(X, y, sample_weight=sample_weight)

#         cntOfRow, cntOfCol = self.coef_.shape
#         #权值系数矩阵的行数对应目标值的种类数目
#         for i in range(cntOfRow):
#             for j in range(cntOfCol):
#                 coef = self.coef_[i][j]
#                 #L1逻辑回归的权值系数不为0
#                 if coef != 0:
#                     idx = [j]
#                     #对应在L2逻辑回归中的权值系数
#                     coef1 = self.l2.coef_[i][j]
#                     for k in range(cntOfCol):
#                         coef2 = self.l2.coef_[i][k]
#                         #在L2逻辑回归中，权值系数之差小于设定的阈值，且在L1中对应的权值为0
#                         if abs(coef1-coef2) < self.threshold and j != k and self.coef_[i][k] == 0:
#                             idx.append(k)
#                     #计算这一类特征的权值系数均值
#                     mean = coef / len(idx)
#                     self.coef_[i][idx] = mean
#         return self

# N_train,N_test=features(SelectFromModel(LR(threshold=0.7, C=0.1)))

# features(SelectFromModel(GradientBoostingClassifier(),threshold=1e-2))
# features(SelectFromModel(xgb.XGBClassifier(),threshold=1e-2))

from statsmodels.stats.outliers_influence import variance_inflation_factor    

def calculate_vif_(X=X_train, thresh=10.0):
    drop_col=[]
    variables = list(range(X.shape[1])) #0~70
    dropped = True
    while dropped:
        dropped = False
        vif = [variance_inflation_factor(X.iloc[:, variables].values, ix)
               for ix in range(len(variables))]
        
        maxloc = vif.index(max(vif))
        if max(vif) > thresh:
            print('dropping \'' + X.iloc[:, variables].columns[maxloc] +
                  '\' at index: ' + str(maxloc)+'\n')
            drop_col.append(X.iloc[:, variables].columns[maxloc])
            del variables[maxloc]
            dropped = True
    
#     print('Remaining variables:\n')
#     print(X.columns[variables])
    return drop_col
#N_train=calculate_vif_()

from gplearn.genetic import SymbolicTransformer
def gp(X_train=X_train,X_test=X_test,a=5):
    import pandas as pd
    function_set = ['add', 'sub', 'mul', 'div',
                    'sqrt', 'log', 'abs', 'neg', 'inv',
                    'max', 'min']
    gp = SymbolicTransformer(generations=50, population_size=2000,
                             hall_of_fame=100, n_components=a,
                             function_set=function_set,
                             parsimony_coefficient=0.0005,
                             max_samples=0.8, verbose=0,
                             n_jobs=3,warm_start=True)
    gp.fit(X_train, Y_train)
    gp_features = gp.transform(X_train)
    test=gp.transform(X_test)
    if a==5:
        gp_train=pd.concat([X_train, pd.DataFrame(columns=['gp_1','gp_2','gp_3','gp_4','gp_5'])])
        gp_train[['gp_1','gp_2','gp_3','gp_4','gp_5']]=gp_features
        stdSc = StandardScaler()
        gp_train.loc[:] = stdSc.fit_transform(gp_train.loc[:])
        
        gp_test=pd.concat([X_test, pd.DataFrame(columns=['gp_1','gp_2','gp_3','gp_4','gp_5'])])
        gp_test[['gp_1','gp_2','gp_3','gp_4','gp_5']]=test
        gp_test.loc[:] = stdSc.transform(gp_test.loc[:])
        return gp_train,gp_test
    else:
        return gp_features
    # gp_test=pd.concat([X_test, pd.DataFrame(columns=['gp_1','gp_2','gp_3','gp_4','gp_5'])])
    # gp_test[['gp_1','gp_2','gp_3','gp_4','gp_5']]=gp.transform(X_test)

def practice(x):
    print('extra trees')
    training(ExtraTreesClassifier(),x)
    print('random forest')
    training(RandomForestClassifier(),x)
    print('xgb')
    training(xgb.XGBClassifier(),x)
    print('gdb')
    training(GradientBoostingClassifier(),x)
    print('lgb')
    training(lgb.LGBMClassifier(),x)
    print('------original-------')
    print('extra trees')
    training(ExtraTreesClassifier(),)
    print('random forest')
    training(RandomForestClassifier())
    print('xgb')
    training(xgb.XGBClassifier())
    print('gdb')
    training(GradientBoostingClassifier())
    print('lgb')
    training(lgb.LGBMClassifier())
    
def lda(gp_train,gp_test,x=30):
    lda = LinearDiscriminantAnalysis(n_components=x)
    lda.fit(gp_train,Y_train)
    lda_feature = lda.transform(gp_train)  
    test=lda.transform(gp_test)
    lda_train=gp_train.copy()
    lda_train['lda']=lda_feature
    stdSc = StandardScaler()
    lda_train.loc[:]=stdSc.fit_transform(lda_train.loc[:])
    
    lda_test=gp_test.copy()
    lda_test['lda']=test
    lda_test.loc[:]=stdSc.transform(lda_test.loc[:])
#     lda_test=lda.transform(gp_test)
    return lda_train,lda_test
    


#print('X_train:',X_train.shape)
#print('gp_train:',gp_train.shape)


# In[ ]:




