import sys
import json
import string

def main():
    terms = {}
    termcount = 0
    with open(sys.argv[1]) as tweet_file:
      for line in tweet_file:
        python_tweet = json.loads(line)
        if 'text' in python_tweet:
          content = python_tweet['text'].split()
          tokens = [word.strip(string.punctuation) for word in content]
          for token in tokens:
            termcount = termcount + 1
            terms[token] = terms.get(token,0) + 1
 
    for token in terms.keys():
      relfreq = terms.get(token,0)/float(termcount)
      print token, relfreq

       
if __name__ == '__main__':
    main()
