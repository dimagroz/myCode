

#my imports
from readUser import fromUser
from allobjs import movable_points
from makeAllObj import allObjcts

class userObjs():

    mappedObjs = {"movable_points":movable_points} #what? oh it maps to the class itself

    def create_all():
        #creates everything
        pass

    #later I will change it to use the actaul classes part
    @classmethod
    def make_objs(cls,sectName, pos_dic = {}):#pos dic is which option to choose
        section =  fromUser.get_sect(sectName)
        #sect_dic = {} # this will be an ordered dict
        allObjcts.make_sect(sectName)
        for key,part in section.items():
            pos = pos_dic.get(key)
            if pos !=None: val = val[pos-1]
            #else: val = val[0] #check if double array
            #sect_dic[key] = cls.init_obj(sectName,part)
            allObjcts.addTo_sect(sectName,key,cls.init_obj(sectName,key,part))
        #allObjcts.all_sect[sectName] = sect_dic
        return allObjcts.get_sect(sectName)

    @classmethod 
    def init_obj(cls,sectName,sectClss,part):
        #print("I am here")
        return cls.mappedObjs[sectName](sectClss,part,True) #what? I see now(look for other what)


