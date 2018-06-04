# TwitterLive
Live stream and track tweets for any keywords

### Clone the repository

`git clone https://github.com/afzalsayed96/TwitterLive`

### Install requirements

```
cd TwitterLive
pip install -r requirements.txt
```

### Add your keys in streamtwy.py

```
#consumer key, consumer secret, access token, access secret.
ckey=""
csecret=""
atoken="-"
asecret=""
```

### Enter keywords to be tracked

```
keywords = ["github","microsoft"]

```

### Run streamtwy.py
```
python streamtwy.py
```

### See the generated output in CSV format

![alt text](https://github.com/afzalsayed96/TwitterLive/blob/master/screenshots/Screenshot%20from%202018-06-04%2000-17-41.png?raw=true)


### References:

https://pythonprogramming.net/twitter-api-streaming-tweets-python-tutorial/

http://t-redactyl.io/blog/2017/04/using-vader-to-handle-sentiment-analysis-with-social-media-text.html
