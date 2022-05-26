class Student:
    # [assignment] Skeleton class. Add your code here
    
    #initializing
    def __init__(self, name = 'muna', age = 13, score =99.9, tracks = ['frontend','backend'] ):
        self.name = name 
        self.age = age 
        self.tracks = tracks 
        self.score = score 
    # check initaliztion , just to be double sure
        print(name, age , tracks , score)

#methods
# change name
    def change_name(self,new_name):
        self.name = new_name
# change age
    def change_age(self,new_age):
        self.age = new_age
# add to list of tracks
    def add_track(self, added):
        list1 = self.tracks
        list2 = added
        # we use append so that its actually joined to the list1 as a whole
        # using extend seperates the list2 into letters.
        list1.append(list2)
        
# return score
    def get_score(self):
        return self.score
        



Bob = Student(name="Bob", age=26, tracks=["FE","BE"],score=20.90)
# to aid comparision during testing 
print(Bob.name , Bob.age , Bob.tracks , Bob.score )

# Expected methods
Bob.change_name("Peter")
Bob.change_age(34)
Bob.add_track("UI/UX")
Bob.get_score()

#testing the code's effect
print (Bob.name ,Bob.age, Bob.tracks, Bob.score)