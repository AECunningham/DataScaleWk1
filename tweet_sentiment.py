import sys
import json
import string

def hw():
    print 'Hello, world!'

def lines(fp):
    print str(len(fp.readlines()))

def main():
    sent_file = open(sys.argv[1])
    scores = {}
    for line in sent_file:
      term,score = line.split("\t")
      scores[term] = int(score)
    #print scores.items()

    with open(sys.argv[2]) as tweet_file:
      for line in tweet_file:
        python_tweet = json.loads(line)
        if 'text' in python_tweet:
          content = python_tweet['text'].split()
          tokens = [word.strip(string.punctuation) for word in content]
          #print tokens
          sentscore = 0
          for token in tokens:
            if token in scores: sentscore = sentscore + scores[token]
          print sentscore
        #else:
          #print ''
       
if __name__ == '__main__':
    main()
