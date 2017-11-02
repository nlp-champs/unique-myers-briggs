# imports
import nltk
import pprint
from nltk.corpus import stopwords

# pretty print settings
pp = pprint.PrettyPrinter(indent=4)

# declare dicts otherwise Python will rage at us
dMyersBriggs = {}
dCleanedMyersBriggs = {}
dUniqueMyersBriggs = {}
dDescriptiveMyersBriggs = {}
dSharedMyersBriggs = {}


# the dict values - text directly from http://www.myersbriggs.org/my-mbti-personality-type/mbti-basics/the-16-mbti-types.htm?bhcp=1
dMyersBriggs['ISTJ'] = 'Quiet, serious, earn success by thoroughness and dependability. Practical, matter-of-fact, realistic, and responsible. Decide logically what should be done and work toward it steadily, regardless of distractions. Take pleasure in making everything orderly and organized - their work, their home, their life. Value traditions and loyalty.'
dMyersBriggs['ISFJ'] = 'Quiet, friendly, responsible, and conscientious. Committed and steady in meeting their obligations. Thorough, painstaking, and accurate. Loyal, considerate, notice and remember specifics about people who are important to them, concerned with how others feel. Strive to create an orderly and harmonious environment at work and at home.'
dMyersBriggs['INFJ'] = 'Seek meaning and connection in ideas, relationships, and material possessions. Want to understand what motivates people and are insightful about others. Conscientious and committed to their firm values. Develop a clear vision about how best to serve the common good. Organized and decisive in implementing their vision.'
dMyersBriggs['INTJ'] = 'Have original minds and great drive for implementing their ideas and achieving their goals. Quickly see patterns in external events and develop long-range explanatory perspectives. When committed, organize a job and carry it through. Skeptical and independent, have high standards of competence and performance - for themselves and others.'
dMyersBriggs['ISTP'] = 'Tolerant and flexible, quiet observers until a problem appears, then act quickly to find workable solutions. Analyze what makes things work and readily get through large amounts of data to isolate the core of practical problems. Interested in cause and effect, organize facts using logical principles, value efficiency.'
dMyersBriggs['ISFP'] = 'Quiet, friendly, sensitive, and kind. Enjoy the present moment, whats going on around them. Like to have their own space and to work within their own time frame. Loyal and committed to their values and to people who are important to them. Dislike disagreements and conflicts, do not force their opinions or values on others.'
dMyersBriggs['INFP'] = 'Idealistic, loyal to their values and to people who are important to them. Want an external life that is congruent with their values. Curious, quick to see possibilities, can be catalysts for implementing ideas. Seek to understand people and to help them fulfill their potential. Adaptable, flexible, and accepting unless a value is threatened.'
dMyersBriggs['INTP'] = 'Seek to develop logical explanations for everything that interests them. Theoretical and abstract, interested more in ideas than in social interaction. Quiet, contained, flexible, and adaptable. Have unusual ability to focus in depth to solve problems in their area of interest. Skeptical, sometimes critical, always analytical.'
dMyersBriggs['ESTP'] = 'Flexible and tolerant, they take a pragmatic approach focused on immediate results. Theories and conceptual explanations bore them - they want to act energetically to solve the problem. Focus on the here-and-now, spontaneous, enjoy each moment that they can be active with others. Enjoy material comforts and style. Learn best through doing.'
dMyersBriggs['ESFP'] = 'Outgoing, friendly, and accepting. Exuberant lovers of life, people, and material comforts. Enjoy working with others to make things happen. Bring common sense and a realistic approach to their work, and make work fun. Flexible and spontaneous, adapt readily to new people and environments. Learn best by trying a new skill with other people.'
dMyersBriggs['ENFP'] = 'Warmly enthusiastic and imaginative. See life as full of possibilities. Make connections between events and information very quickly, and confidently proceed based on the patterns they see. Want a lot of affirmation from others, and readily give appreciation and support. Spontaneous and flexible, often rely on their ability to improvise and their verbal fluency.'
dMyersBriggs['ENTP'] = 'Quick, ingenious, stimulating, alert, and outspoken. Resourceful in solving new and challenging problems. Adept at generating conceptual possibilities and then analyzing them strategically. Good at reading other people. Bored by routine, will seldom do the same thing the same way, apt to turn to one new interest after another.'
dMyersBriggs['ESTJ'] = 'Practical, realistic, matter-of-fact. Decisive, quickly move to implement decisions. Organize projects and people to get things done, focus on getting results in the most efficient way possible. Take care of routine details. Have a clear set of logical standards, systematically follow them and want others to also. Forceful in implementing their plans.'
dMyersBriggs['ESFJ'] = 'Warmhearted, conscientious, and cooperative. Want harmony in their environment, work with determination to establish it. Like to work with others to complete tasks accurately and on time. Loyal, follow through even in small matters. Notice what others need in their day-by-day lives and try to provide it. Want to be appreciated for who they are and for what they contribute.'
dMyersBriggs['ENFJ'] = 'Warm, empathetic, responsive, and responsible. Highly attuned to the emotions, needs, and motivations of others. Find potential in everyone, want to help others fulfill their potential. May act as catalysts for individual and group growth. Loyal, responsive to praise and criticism. Sociable, facilitate others in a group, and provide inspiring leadership.'
dMyersBriggs['ENTJ'] = 'Frank, decisive, assume leadership readily. Quickly see illogical and inefficient procedures and policies, develop and implement comprehensive systems to solve organizational problems. Enjoy long-term planning and goal setting. Usually well informed, well read, enjoy expanding their knowledge and passing it on to others. Forceful in presenting their ideas.'

for sPersonality, lDescription in dMyersBriggs.iteritems():
    print sPersonality + " " + str(len(lDescription.split())) # word counts raw description

for sPersonality, sDescription in dMyersBriggs.iteritems():
    # convert to lower
    sDescription = sDescription.lower()
    # remove '.', ' - ', and '.'
    sDescription = sDescription.replace(".", " ")
    sDescription = sDescription.replace(" - ", " ")
    sDescription = sDescription.replace(",", " ")
    # convert string to list of words
    lDescription = sDescription.split()
    # remove stop words
    lDescription = [sWord for sWord in lDescription if sWord not in stopwords.words('english')]
    # finally throw the tastiness into the 'cleaned' dict - converted to set for unique only, and back to a list for the list type which will prove useful later
    dCleanedMyersBriggs[sPersonality] = list(set(lDescription)) # unique only

print "Words unique to personality:"
for sPersonality, lDescription in dCleanedMyersBriggs.iteritems():
    # loop at each word in this personality's description:
    lWords = [] # build an array of unique words for each personality
    for sWord in lDescription:
        bFoundInOtherDescription = False # set match count of this word to 0
        # loop over all other personality descriptions
        for sInnerPersonality, lInnerDescription in dCleanedMyersBriggs.iteritems():
            if sPersonality == sInnerPersonality: #
                continue # don't search itself
            if sWord in lInnerDescription:
                bFoundInOtherDescription = True
        if bFoundInOtherDescription == False: # it is only unique if there were no other matches in any other of the descriptions
            lWords.append(sWord)
    #print sPersonality + " " + str(len(lWords)) # word counts unique for description
    print "<tr><td>" + sPersonality + "</td><td>" + str(lWords) + "</td></tr>"
    dUniqueMyersBriggs[sPersonality] = lWords

pp.pprint(dUniqueMyersBriggs) # pretty print the dict

print "'Descriptive' words for each personality:"
for sPersonality, lDescription in dUniqueMyersBriggs.iteritems():
    lWords = []
    lTokenText = nltk.word_tokenize(" ".join(lDescription)) # tokenize text
    lTaggedText = nltk.pos_tag(lTokenText) # tag tokens
    for tTaggedText in lTaggedText:
      if tTaggedText[1] == "RB" or tTaggedText[1] == "RBR" or tTaggedText[1] == "JJR" or tTaggedText[1] == "JJ" or tTaggedText[1] == "JJR" or tTaggedText[1] == "JJS":
          lWords.append(tTaggedText[0])
    dDescriptiveMyersBriggs[sPersonality] = lWords
    #print sPersonality + " " + str(len(lWords)) # word counts for 'descriptive' words for description
    print "<tr><td>" + sPersonality + "</td><td>" + str(lWords) + "</td></tr>"

pp.pprint(dDescriptiveMyersBriggs)

for iGroupShare in list(reversed(range(3,16))):
    print "Words shared by at least " + str(iGroupShare) + " personalities:"
    for sPersonality, lDescription in dCleanedMyersBriggs.iteritems():
        # loop at each word in this personality's description:
        lWords = [] # build an array of unique words for each personality
        for sWord in lDescription:
            iFoundCount = 0 # set the found count
            # loop over all other personality descriptions
            for sInnerPersonality, lInnerDescription in dCleanedMyersBriggs.iteritems():
                if sPersonality == sInnerPersonality: #
                    continue # don't search itself
                if sWord in lInnerDescription:
                    iFoundCount = iFoundCount + 1
            if iFoundCount >= iGroupShare: # it is  shared if it is in all
                lWords.append(sWord)
        # print sPersonality + " " + str(len(lWords)) # word counts unique for description
        dSharedMyersBriggs[sPersonality] = lWords
    pp.pprint(dSharedMyersBriggs) # pretty print the dict
