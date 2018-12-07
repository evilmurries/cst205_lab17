# Lab 17 - Christopher Piwarski
# 5 December 2018
# Python version 3.7.1
# Developed with Sublime Text 3.1.1 Build 3176 and Mac OS X Terminal


def problem1():
    # declare variables
    wordCount = {}
    filename = 'eggs.txt'
    htmlFile = 'eggs.html'
    header = ''

    print('Problem 1:')
    # process file
    try:
      # open file
        with open(filename, 'r') as eggFile:
            print('opened ' + filename)

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

  # print out results to HTML File
    try:
        with open(htmlFile, 'w') as eggHtml:
            eggHtml.close()
    except IOError:
        print('\nIO Error Detected. HTML File Writing Failed.')
        raise SystemExit
    finally:
        print('\nFile Writing Sequence Finished: HTML File Created')


# Main function to run the script
if __name__ == '__main__':
  problem1()

