# Generates a word cloud from a text file (depending on which function is used)
from wordcloud import WordCloud
import matplotlib.pyplot as plt

class WordCloudGenerator:
    # Generates a word cloud from a text file, however also has some logic to exclude retweets and remove the word https
    @staticmethod
    def generate_from_text_file(file_name, exclude_retweets):

        # Initialise the the whole text to be used by the word cloud as an empty string
        text = ""
        with open(file_name, 'r') as f:
            # for every line in the file
            for line in f:
                # if exclude tweets is true, then we check if the line is a retweet. If it is a retweet, we skip it
                # and don't add it to the text
                if exclude_retweets and "RT @" in line:
                    continue
                else:
                    # Removes the word https from the line
                    httpremoved = line.replace('https', '')
                    # Adds the line to the text
                    text = httpremoved + text
                    breakingremoved = httpremoved.replace('#BREAKING', '')
                    text = breakingremoved + text
                    tcoremoved = breakingremoved.replace('t.co', '')
                    text = tcoremoved + text
                    twitterremoved = tcoremoved.replace('twitter', ' ')
                    text = twitterremoved + text
                    tweetremoved = twitterremoved.replace('tweet',' ')
                    text = tweetremoved + text
                    coremoved = tweetremoved.replace('co', ' ')
                    text = coremoved + text


        # Generates the word cloud from the text
        print("Generate word cloud for: " + text)
        wordcloud = WordCloud().generate(text)
        plt.figure()
        plt.imshow(wordcloud, interpolation="bilinear")
        plt.axis("off")
        plt.show()


# an example of how to generate a word cloud from the generated text files below.
WordCloudGenerator.generate_from_text_file("tweets_20200121.txt", exclude_retweets= False)