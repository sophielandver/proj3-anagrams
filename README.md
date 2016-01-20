Author: Sophie Landver. (initial version by M Young)

Path to project3 on ix: slandver@ix-trusty: ~/public_html/cis399/htbin/proj3-anagrams

# proj3-anagrams
Vocabularly anagrams game for primary school English language learners (ELL)


## Overview

A simple anagram game designed for English-language learning students in 
elementary and middle school.  
Students are presented with a list of vocabulary words (taken from a text file) 
and an anagram.  The anagram is a jumble of some number of vocabulary words, randomly chosen.  Students attempt to type vocabulary words that can be created from the  
jumble.  When a matching word is typed, it is added to a list of solved words. 
If a character is typed in that is not in the anagram, it is deleted and a message is displayed to the user. 
If a word from the vocabulary list is typed in, that has already been typed in, then a message is displayed to the user. In addition, the words from the vocabulary list that contain all the characters that have been typed in so far by the user, are highlighted. 

The vocabulary word list is fixed for one invocation of the server, so multiple
students connected to the same server will see the same vocabulary list but may 
have different anagrams. 


## To run automated tests 
* `nosetests`

There are currently nose tests for vocab.py, letterbag.py, and jumble.py. 



