import sys
import json
import string

hashlog = {}

def main():
        
    with open(sys.argv[1]) as tweet_file:
      for line in tweet_file:
        python_tweet = json.loads(line)
        if 'text' in python_tweet:
          if 'entities' in python_tweet:
            if 'hashtags' in python_tweet['entities']: 
              for tag in python_tweet['entities']['hashtags']:
                tagtext = tag['text']
                hashlog[tagtext] = hashlog.get(tagtext,0) + 1
  
      topten = sorted(hashlog,key=hashlog.get,reverse=True)[:10]
      for key in topten:
        print key,hashlog[key]
    
                    
                                 
       
if __name__ == '__main__':
    main()
