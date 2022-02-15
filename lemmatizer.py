import nltk
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords

email = """Greetings,


This email is regarding your meeting.
We are planning to conduct your meeting on 15th February.
Kindly join the below link at 10:30 IST for your meeting call.
Google Meet joining info
Video call link: https://meet.google.com/xxx-xxxx-xxx
Kindly Acknowledge the same.

Please feel free to contact me if you have any queries.
All the best!!

Kind Regards,
XXXXXX,
HR team,
xxxxxxxx,
+1234567890(whatsapp only)"""
               
               
sentences = nltk.sent_tokenize(email)
lemmatizer = WordNetLemmatizer()

# Lemmatization
for i in range(len(sentences)):
    words = nltk.word_tokenize(sentences[i])
    words = [lemmatizer.lemmatize(word) for word in words if word not in set(stopwords.words('english'))]
    sentences[i] = ' '.join(words)      