import sys
import json
import string

states = {
        'AK': 'Alaska',
        'AL': 'Alabama',
        'AR': 'Arkansas',
        'AS': 'American Samoa',
        'AZ': 'Arizona',
        'CA': 'California',
        'CO': 'Colorado',
        'CT': 'Connecticut',
        'DC': 'District of Columbia',
        'DE': 'Delaware',
        'FL': 'Florida',
        'GA': 'Georgia',
        'GU': 'Guam',
        'HI': 'Hawaii',
        'IA': 'Iowa',
        'ID': 'Idaho',
        'IL': 'Illinois',
        'IN': 'Indiana',
        'KS': 'Kansas',
        'KY': 'Kentucky',
        'LA': 'Louisiana',
        'MA': 'Massachusetts',
        'MD': 'Maryland',
        'ME': 'Maine',
        'MI': 'Michigan',
        'MN': 'Minnesota',
        'MO': 'Missouri',
        'MP': 'Northern Mariana Islands',
        'MS': 'Mississippi',
        'MT': 'Montana',
        'NA': 'National',
        'NC': 'North Carolina',
        'ND': 'North Dakota',
        'NE': 'Nebraska',
        'NH': 'New Hampshire',
        'NJ': 'New Jersey',
        'NM': 'New Mexico',
        'NV': 'Nevada',
        'NY': 'New York',
        'OH': 'Ohio',
        'OK': 'Oklahoma',
        'OR': 'Oregon',
        'PA': 'Pennsylvania',
        'PR': 'Puerto Rico',
        'RI': 'Rhode Island',
        'SC': 'South Carolina',
        'SD': 'South Dakota',
        'TN': 'Tennessee',
        'TX': 'Texas',
        'UT': 'Utah',
        'VA': 'Virginia',
        'VI': 'Virgin Islands',
        'VT': 'Vermont',
        'WA': 'Washington',
        'WI': 'Wisconsin',
        'WV': 'West Virginia',
        'WY': 'Wyoming'
}
state_cum = {}
state_num = {}
avscore = {}

def main():
    sent_file = open(sys.argv[1])
    scores = {}
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
          
          if 'user' in python_tweet:
            #print python_tweet['user']
            if 'location' in python_tweet['user']: 
              userloc = python_tweet['user']['location']
              if userloc is not None:
                if userloc.find(',') != -1:
                  possState = userloc.rsplit(',',1)[-1]
                  upperState = possState.upper().strip(string.punctuation).strip()
                  #print upperState, states.get(upperState,'')
                  if upperState in states.keys():
                    state_num[upperState] = state_num.get(upperState,0) + 1
                    state_cum[upperState] = state_cum.get(upperState,0) + sentscore

    for state in state_num.keys():
      avscore[state] = state_cum[state]/float(state_num[state])
      
    print max(avscore,key=avscore.get)
                    
                                 
       
if __name__ == '__main__':
    main()
