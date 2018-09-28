beginner = ["G", "D", "A"]
chroma_tones = ["Ab/G#","Bb/A#","Db/C#","Eb/D#","F#/Gb"]
bi_mode = ["major", "minor", "major arpeggio", "minor arpeggio"]
main_bowing = ["separate bows", "slurred, two notes to a bow"]

#dummy users
beginner = {
    "my_scale_set": beginner,
    "my_mode": bi_mode,
    "my_bow_pattern": main_bowing
}
advanced = {
    "my_scale_set": chroma_tones,
    "my_mode": bi_mode,
    "my_bow_pattern": main_bowing
}

db= [beginner, advanced]

def user_login(username):
    for item in db:
        if username == item:
            return item

#returns random scale:
from random import randint
def random_scale(scale_set, mode, bow_pattern):
    s = len(scale_set)
    s_i = randint(1,s) -1
    m = len(mode)
    m_i = randint(1,m) -1
    b = len(bow_pattern)
    b_i = randint(1,b) -1
    practice = '{} {}, {}'.format(scale_set[s_i],mode[m_i],bow_pattern[b_i])
    return practice

#****special to this version ****
scale_list=[]

def list_length(my_list):
    length=0
    for item in my_list:
        length+=1
    return length

def clear_list(my_lst):
    my_list=[]
    return my_list

#returns random scale from user's set:
def users_random_scale(username,my_list):
    a_scale = random_scale(username["my_scale_set"], username["my_mode"],username["my_bow_pattern"])
    my_list.append(a_scale)
    return a_scale

def is_first(my_list):
    if list_length(my_list)>1:
        return False
    else:
        return True




def test_scale_generator():
    username = beginner
    a_scale = random_scale(username["my_scale_set"], username["my_mode"],username["my_bow_pattern"])
    return a_scale

