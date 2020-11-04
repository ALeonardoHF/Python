#https://stackoverflow.com/questions/16249736/how-to-import-data-from-mongodb-to-pandas


from sklearn.linear_model import SGDClassifier
from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer
from sklearn.metrics import recall_score, precision_score, confusion_matrix
from sklearn.model_selection import train_test_split
import pandas as pd
import pymongo

#client = pymongo.MongoClient("mongodb+srv://progra-int:f1r3w4ll@proyecto-final.az9ty.gcp.mongodb.net/prueba?retryWrites=true&w=majority")
client = pymongo.MongoClient("mongodb+srv://EAA:3312@proyectofinal.yytqy.gcp.mongodb.net/ProyectoFinal_v2?retryWrites=true&w=majority")
db = client.ProyectoFinal_v2

cl = db.test
q = cl.find({},{"_id":0})

cl = db.ExampleUTFCompleto
w = cl.find({},{"_id":0})

df = pd.DataFrame(list(w))
comtrain = df['Comment'].to_list()
strain = df['Sentiment'].to_list()

df = pd.DataFrame(list(q))
comtest = df['tweet'].to_list()
stest = df['sentimiento'].to_list()

#Proceso del algoritmo de clasificación

#train_comment, test_comment, train_sentiment, test_sentiment = train_test_split(comment, sentiment, test_size=0.2, random_state=42)

#Convierte el texto de los comentarios a números
vectorizer = CountVectorizer(max_df =1.0, binary = True, stop_words = 'english', max_features = 10000)
vectorizer.fit(comtrain)
train_features = vectorizer.transform(comtrain)


tfidf_transformer = TfidfTransformer(smooth_idf=True,
                                    use_idf=True).fit(train_features)
trainingTF = tfidf_transformer.transform(train_features)
train_features = trainingTF.toarray()



#Entrenamiento del modelo (Support Vector Machine)
classifier = SGDClassifier(loss='hinge',   #'hinge'  #'log'
                            penalty='l2',
                            alpha=0.00001,
                            random_state=42,
                            max_iter=5,
                            tol=None)
classifier.fit(train_features, strain)




print('Predicción sobre el conjunto TRAIN:')
p = classifier.predict(train_features)
print (p)
print( 'Train Recall: ' + str(recall_score(strain, p) ))
print( "Train Precision: " + str(precision_score(strain, p)))
print( 'Matriz de confusión: ' )
print(confusion_matrix(strain, p, labels=[0, 1]))
print('-----------------------------------------')



#Evaluación del conjunto TEST
test_features = vectorizer.transform(comtest)
p = classifier.predict(test_features)
print('Predicción sobre el conjunto TEST:')
print (p)
print( 'Test Recall: ' + str(recall_score(stest, p) ))
print( "Test Precision: " + str(precision_score(stest, p)))
print( 'Matriz de confusión: ' )
print(confusion_matrix(stest, p, labels=[0, 1]))
print('-----------------------------------------')




#En el siguiente fragmento de código se envia a clasificar un comentario nuevo, se clasifica y muestra si es positivo o negativo.
t = 'The was so good'
features = vectorizer.transform([t])
trainingTF = tfidf_transformer.transform(features)
features = trainingTF.toarray()
p = classifier.predict(features)[0]
print('Predicción valor introducido:')
print('Frase: ' + t)
print (p)
print('-----------------------------------------')

print ("Frase introducida:   " + t + '.    Sentimiento: ' + str(p))
