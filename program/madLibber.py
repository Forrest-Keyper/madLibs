from random import randrange

storyNumber = 0



def gameStart():


    print("Welcome to Mad Libs!")
    #if(storyNumber == 0):


class libClass:


    def __init__(self, storyNumber):
        self.name = self
        self.storyNumber = storyNumber
        self.userLibs = []
        self.lib1 = ["The ball went [adjective]",
                        " between bounces, from [noun]",
                        " palm to [adjective]",
                        " asphalt [verb]ly.",
                        "There are none whose [verb]",
                        " rivals that of a [adverb] toy"
                        ]

# "The ball went [0][0] between bounces, from [0][1] palm to [0][2]
# asphalt [0][3]. There are none whose [0][4] rivals that of a [0][5] toy"

    def lib(self, userLibs):
        user_libArr = self.userLibs
        if (user_lib.storyNumber == 0):
            print('userlib worked')
        for i in range(5):
                term = input(user_lib.lib1[i])
                user_libArr += [term]

                (user_libArr[0
            elif (i == 1):
                index1 = input(str(user_lib.term1))
                user_lib.userLibs = {'term1':index1}

            elif (i == 2):
                index2 = input(str(user_lib.term2))
                user_lib.userLibs = {'term2':index2}

            elif (i == 3):
                index3 = input(str(user_lib.term3))
                user_lib.userLibs = {'term3':index3}

            elif (i == 4):
                index4 = input(str(user_lib.term4))
                user_lib.userLibs = {'term4':index4}

            elif (i == 5):
                index5 = input(str(user_lib.term5))
                user_lib.userLibs = {'term5':index5}

'''
    #    lib_3_arr = [term0, term1, term2, term3, term4, term5]

    #termIndex = {0:verb, 1:adjective, 2:adverb, 3:verb, 4:verb, 5:adverb}




class processClass:



    def __init__(self, name, storyForm):
        self.name = name
        self.storyForm = storyForm
        self.libTracker = {}

user_lib = libClass(storyNumber)
user_lib.lib(0)
