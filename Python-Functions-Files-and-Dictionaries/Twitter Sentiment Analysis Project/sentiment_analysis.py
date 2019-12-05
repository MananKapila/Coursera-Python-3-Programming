# Quoting from the Coursera project guidelines:

# "We have provided some synthetic (fake, semi-randomly generated) twitter data in a csv file named
# project_twitter_data.csv which has the text of a tweet, the number of retweets of that tweet, and the number of
# replies to that tweet. We have also words that express positive sentiment and negative sentiment, in the files
# positive_words.txt and negative_words.txt.
# Your task is to build a sentiment classifier, which will detect how positive or negative each tweet is. You will
# create a csv file, which contains columns for the Number of Retweets, Number of Replies, Positive Score
# (which is how many happy words are in the tweet), Negative Score (which is how many angry words are in the tweet)
# and the Net Score for each tweet. At the end, you upload the csv file to Excel or Google Sheets and produce a graph
# of the Net Score vs Number of Retweets."


punctuation_chars = ["'", '"', ",", ".", "!", ":", ";", '#', '@']


def strip_punctuation(s):
    for c in punctuation_chars:
        s = s.replace(c, '')
    return s


def get_pos(s):
    words = strip_punctuation(s).split()
    positivity = 0
    for pos_w in positive_words:
        if pos_w in words:
            positivity += 1
    return positivity


def get_neg(s):
    words = strip_punctuation(s).split()
    negativity = 0
    for neg_w in negative_words:
        if neg_w in words:
            negativity += 1
    return negativity


def evaluate_tweet(tweet_data_input_line):
    tweet, retweets_count, replies_count = tweet_data_input_line.strip().split(",")
    neg_score = get_neg(tweet)
    pos_score = get_pos(tweet)
    net_score = pos_score - neg_score
    return '{},{},{},{},{}\n'.format(retweets_count, replies_count, pos_score, neg_score, net_score)


positive_words = []
with open("data_files/positive_words.txt") as pos_f:
    for lin in pos_f:
        if lin[0] != ';' and lin[0] != '\n':
            positive_words.append(lin.strip())

negative_words = []
with open("data_files/negative_words.txt") as pos_f:
    for lin in pos_f:
        if lin[0] != ';' and lin[0] != '\n':
            negative_words.append(lin.strip())

with open("data_files/project_twitter_data.csv") as twitter_f:
    with open("data_files/resulting_data.csv", "w") as results_f:
        result_header = "Number of Retweets, Number of Replies, Positive Score, Negative Score, Net Score\n"
        results_f.write(result_header)
        reading_header = True
        for input_line in twitter_f:
            if reading_header:
                reading_header = False
                continue
            results_f.write(evaluate_tweet(input_line))
