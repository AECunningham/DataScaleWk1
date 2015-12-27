import sys
import json
import string

#def hw():
#    print 'Hello, world!'

#def lines(fp):
#    print str(len(fp.readlines()))

def main():
    sent_file = open(sys.argv[1])
    scores = {}
    assoc = {}
    posassoc = {}
    for line in sent_file:
      term,score = line.split("\t")
      scores[term] = int(score)
  
    with open(sys.argv[2]) as tweet_file:
      for line in tweet_file:
        python_tweet = json.loads(line)
        if 'text' in python_tweet:
          content = python_tweet['text'].split()
          tokens = [word.strip(string.punctuation) for word in content]
          sentscore = 0
          for token in tokens:
            if token in scores: sentscore = sentscore + scores[token]
          for token in tokens:
            if not (token in scores):
              assoc[token] = assoc.get(token,0) + 1
              if sentscore > 0: posassoc[token] = posassoc.get(token,0) + 1
              

#    with open(sys.argv[2]) as tweet_file:
#      for line in tweet_file:
#        python_tweet = json.loads(line)
#        if 'text' in python_tweet:
#          content = python_tweet['text'].split()
#          tokens = [word.strip(string.punctuation) for word in content]
#          for token in tokens:
#            if not (token in scores):
#              tokenscore = posassoc.get(token,0)/float(assoc.get(token,0))
#              print token, tokenscore

    for token in assoc.keys():
      tokenscore = posassoc.get(token,0)/float(assoc.get(token,0))
      print token, tokenscore

       
if __name__ == '__main__':
    main()
