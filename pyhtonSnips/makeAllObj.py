class allObjcts(): # later change name to somethin like mAllObjcts
    #this holdes all sections, it holds everything
    all_sect = {}
    sectMapped = {}


    @classmethod
    def addTo_Mapped(cls,clssname,clsstype,mapToName): #for now all three typeclss clss name and towhat
        if mapToName not in cls.sectMapped:
            cls.sectMapped[mapToName] = []
        cls.sectMapped[mapToName].append((clsstype,clssname))

    @classmethod
    def callUpdate(cls,what): # what is name of class
        #this method I am finding the class in all_sect and running the @ovrided update method on all that are there
        #then those classes call the method and thus all are done
        #this should better be breath first in the future
        for clss in cls.sectMapped[what]: #clss is (clsstype,clssname)
            cls.all_sect[clss[0]][clss[1]].update_obj()

    
    @classmethod    
    def unmap():
        pass

    #I will later have a class/method realocaton and decide this problem then
    #@classmethod
    #def init_obj(cls,sectName,sectClss,part,fromUser = False):
    #    return cls.mappedObjs[sectName](sectClss,part,fromUser)   

    @classmethod
    def get_sect(cls,section,name = None):
        sect_dic = cls.all_sect.get(section)
        if sect_dic == None: 
            print(section + " has not been made yet or does not exist")
            return
        if name == None: #later will update to have check
            return sect_dic
        else: 
            return sect_dic[name]


    def get_Allsect(cls):
        return cls.all_sect


    @classmethod
    def make_sect(cls,section, override = False):
        if override or section not in cls.all_sect: # again way to make it look though only once
            cls.all_sect[section] = {}

    @classmethod
    def addTo_sect(cls,section,secPart,objct):
        if section in cls.all_sect: # might be tid bit faster if not go through dic twice
            cls.all_sect[section][secPart] = objct
        else: print(section + " section does not exist")


