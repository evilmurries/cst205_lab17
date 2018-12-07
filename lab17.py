# Lab 17 - Christopher Piwarski
# 5 December 2018
# Python version 3.7.1
# Developed with Sublime Text 3.1.1 Build 3176 and Mac OS X Terminal


import os

# This function creates an html document highlighting word frequency 
# in a dictionary
def makePage(eggWords):

    # declare variables
    filename = 'eggs.html'
    file = os.path.join(os.getcwd(), filename)
    header = '<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transition//EN"\
 "http://www.w3.org/TR/html4/loose.dtd">'
    title = '<html>\n<head><title> Green Eggs and Ham </title>\n</head>'
    bodyOpen = '<body>\n<h1>Word Frequency</h1>\n'
    bodyClose = '</body>\n</html>'
    htmlBody = '<p style="color:#%s; font-size:%spx; font-weight:bold">%s</p><br>\n'

    # try to write to a html file
    try:
        with open(file, 'w') as htmlPage:

            # write beginning of html file
            htmlPage.write(header)
            htmlPage.write(title)
            htmlPage.write(bodyOpen)
            htmlPage.write('Green Eggs and Ham Words:<br>')

            # for each word in the dictionary, use the word frequency to 
            #determine color and size. Then write to the html file
            for word in eggWords:
                color, size = determineSizeColor(eggWords[word])
                htmlPage.write(htmlBody % (color, size, word))

            # write end of html file and close
            htmlPage.write(bodyClose)
            htmlPage.close()
    except IOError:
        print('Error Creating HTML File. Aborting.')
        raise SystemExit
    finally:
        print('HTML File Process Completed.')

# This function determines the color and size for the word to be written into
# the html file.
def determineSizeColor(count):
    if count >= 0 and count <= 20:
        return ('CCFF00', '10')
    elif count > 20 and count <= 40:
        return ('99FF00', '20')
    elif count > 40 and count <= 60:
        return ('66FF00', '30')
    elif count > 60 and count <= 80:
        return ('00CC00', '40')
    elif count > 80 and count <= 100:
        return ('006600', '50')
    else: 
        return ('99FF00', '20')

# Main function for the script
def main():
    # declare variables
    wordCount = {}
    eggsText = 'eggs.txt'
    htmlFile = 'eggs.html'
    header = ''

    # process file
    try:
      # open file
        with open(eggsText, 'r') as eggFile:

            # read in a line and count the words
            for line in eggFile:
                # remove dashes and lower case sentence
                sentence = line.replace('-', ' ')
                sentenceLower = sentence.lower()
                sentenceList = sentenceLower.split()
                for word in sentenceList:
                    if word in wordCount.keys():
                        wordCount[word] += 1
                    else:
                        wordCount[word] = 1
        eggFile.close()
    except IOError:
        print('\nIO Error Detected. File Reading Failed')
        raise SystemExit
    finally:
        print('\nFile Reading Sequence Finished: eggs.txt processed')

    # determine word count and most common word
    mostCommon = 'eggs'
    totalWords = 0
    for word in wordCount.keys():
        totalWords += 1
        if wordCount[word] > wordCount[mostCommon]:
            mostCommon = word

    # generate HTML document
    makePage(wordCount)


# Main function to run the script
if __name__ == '__main__':
  main()

