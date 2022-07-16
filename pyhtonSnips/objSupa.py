#from functools import partial
from mathDuer import xy
from myPlot import graphClass


#superclass inherit from here
class make_all(object): #object or Object?
    #do I need self infront of vars in class open area
    def __init__(self,sectName,part,isFuser = False): #make this into array to take multiple parts?
        #also all_sect might be changed in the future
        #init function will take user or program created variable before part in futua

        self.sectName = sectName
        self.inP = {} #dic in python are offcourse on uorded
        self.isFuser = isFuser #stands for is_from_user      
        #in_part before called input_part
        self.check_params(part)
        #self.input_part = part

        #bellow could be its own method to init whats needed
        self.set_init()
        # first common with things only in part as needed
        if self.isCommon: self.init_common(part) # tookout sectName,part
        if self.isNum: self.init_num(part)
        elif self.isDrawble: self.init_drawn(part)
        self.init_unique(part)

        #then bellow will have running under init_ actaul, but for now keep this way

        #this here should only happend for drawn
        #-----------------------------
        if self.isDrawble:
            self.make_draw()

        #this should happen for all
        #------------------------------
        self.mapTo() #for now just runs method at the end
        
        #future I might split init and update but for now will be same
        #self.update_obj(["init"]) #leave this for now
        #this should only be done on update?

    def set_init(self):#tthis method could be made shorter
        self.isCommon = True
        self.isNum = False
        self.isDrawble = False
        self.initType()
        if self.isNum and self.isDrawble: print("can't have both drawble and num at same time")
        

    def check_params(self,in_part):
        pass
        #will make this later
        #bellow will throw excptions

    def init_common(self,in_part): # took out sectName,part
        #self.sectName = sectName
        #self.input_part = part
        self.inP["comment"] = self.in_part[-1]


    def init_uniqueFirst(self,in_part):
        #partSet = init_from_both(in_part)
        if self.isFuser: self.setFromUser(self,in_part)  #init_from_user(in_part,partSet)
        self.init_from_inPart(self,in_part)
        #else: init_from_clss(in_part,partSet)

        self.init_unique()

    #will worry about nums later
    def init_num(self,in_part): 
        self.inP["value"] = self.find_val()
        self.inP["units"] = self.find_units()

    def init_drawn(self,in_part):
         #--------------------------- set val bellow
        self.inP["color"] = self.in_part[0]
        self.inP["do_updDraw"] = True #this is ment so if you have an update that doesnt need draw to update do_updateDraw
        self.inP["drawPart"] = None # later will figure this out
        self.inP["xyLocs"] = [None]
        #self.xyLocs = self.find_xyLocs()
        #--------------------------- call methods bellow
        #self.make_draw()
        self.upTree = self.find_upTree() #find_xyLocs() replaced with find_upTree name
        
        #if self.input_part[-2] == "hide":
        #    self.show = False
        #else: self.show = True


    def get_pos(self,arrPos=None):
        #if type str go through and get int double loc
        #return loc at pos, if no pos, return full array
        return (1,2)

    
    #this method to be ovided since draw updates should happen at end
    #or maybe used since maybe just image update happen at end
    def update_obj(self,event = None): #returns true if obj updated else false
        #event is anything needed to update obj
        #if newPos != None:
        #    self.xyLocs = []
        #    for pos in event
        #        self.xyLocs.append(xy(pos))
        return self.update_params(event) #for now it returns
        if self.isDrawble: 
            self.update_draw(event)
            #here update marker in draw something like 
            #fig.canvas.draw_idle() or matplotlib.pyplot.draw()
            #figure graph updates everytime update

    #thise methods bellow if needed should be overwriten in child class's
    def initType(self):
        pass

    #3 methods bellow for making unique
    #-----------------------------------------------------
    #def init_from_both(self,in_part):
    #    return None   
    
    #def init_from_clss(self,in_part,partSet):
    #    pass

    #def init_from_user(self,in_part,partSet):
    #   pass

    def setFromUser(self,in_part):
        pass

    def init_from_inPart(self,in_part):
        pass
    def init_unique(self):
        pass    
    #----------------------------------------------------
    def mapTo(self):
        pass

    #for num-------------------------------
    def find_val(self):
        return self.input_part[0]

    def find_units(self):
        return self.input_part[1]

    #for drawn-----------------
    def make_draw(self):
        pass
    
    def find_mappedTo(self):
        #return xy(self.input_part[1])
        return None
    
    def update_params(self,event=None):
        None

    def update_draw(self,event=None):#this method draws is not currently used
        #the way I am doing things now is having marker itself do the update drawing
        if self.do_updDraw:
            print("inside draw")
            self.drawPart.set_data( self.toMarkType( self.xyLocs ) )
            self.drawPart.set_visible(True)
            graphClass.ax.figure.canvas.draw_idle()
            #self.drawPart.set_data( ToMarkType( get_pos() ) )

    #below methods will be used for aiding    
    @staticmethod
    def toMarkType(xyArr):
        #what its diff, actauly in make graph xy revirsed


            xs = []
            ys = []
            for point in xyArr:
                xs.append(point.x)
                ys.append(point.y)

            print(xs,ys)
            return (xs,ys)    

    #for now if update need to remake entire class
    #def update_val(self,value)
    #    self.val = value


#---------------------------------------------------------------------------------------
#                                                                                     //
#                                                                                     //

#

#

#

#                                                                                     //
#                                                                                     //
#-----------------------------------------------------------------------------------------




class pointLine(make_all): # I will make it work for point then do both

    #Override
    def initType(self):
        self.isDrawble = True


    #@Override
    def make_draw(self):
        #here will make a marker type
        #invistage more into marker class why its an array
        typeM = graphClass.ax.plot([None],[None],marker='o',color = self.color)[0] #maybe way to make it not plot when made
        typeM.set_visible(False)
        self.drawPart = typeM

    
    # Override 
    def update_xyLocs():
        #will be an array of loc but for now only one 
        #(edit)still don't know what this array does
        #for now update xyLocs in update_params
        pass

    # ----------------------- I will start here
    #@override
    def init_unique(self): # starts of by making point type
        self.init_BothTypes()
        self.init_OneType()

    def init_OneType():
        pass # this will be to init point vs line part
        
        #mapTo()

    #@override
    def mapTo(self): #maps to connecting class
        allObjcts.addTo_Mapped(self.sectName,self.__class__.__name__,self.dimArrPlt[0][2]) #look at dimArrPlt layout
        #dimArrPlt layout here__________--- please
    
    def init_pointType(self):
        self.pointType = self.input_part[1] #[color,"plot_data", "av-x_data-range(ia)"] 
        if self.pointType == "plot_data":
            self.forPltType()
        elif self.pointType == "cordinates":
            self.forCor()
        elif self.pointType == on_line:
            self.forOnLine()

    def forPltType(self):
        #sentence = self.input_part[2] # will do none later, I will add in other later
        #sentArrX = self.input_part[2].split('-')
        #sentArrY = self.input_part[3].split('-')
        #self.forPlt = (sentArrX,sentArrY)
        self.dimArrPlt = self.make_coord(2,2,'-') #what(min)-xdata-range

    def make_coord(self,startPos,nD,splitOn): #if startingPos always same wont need then
        dimArr = []
        for d in range(nD):
             #2 lines reduce to one
            sentArr = self.input_part[startPos + d].split(splitOn) #hope-illy split works also shud be tuple
            dimArr.append(sentArr) #------ [["ia,av,time"],["ia,min,signal"]]
        return dimArr



    def forCor(self):
        pass

    def forOnLine(self):
        pass

    #Override
    def update_params(self,event): #also kwnon as update_point will put it in correct pos later
        #for now later I will find a way
        if self.pointType == "plot_data":
            xy_loc = self.updatePoint_nD(self.dimArrPlt)
        if self.pointType == "XyPos":
            xy_loc = None #self.xyLocs[0] # maybe in paratnses format
        elif self.pointType == "intercept":
            xy_loc = self.find_intercept()

        self.xyLocs[0] = xy(arr = xy_loc)  #(None,5) will handle none part later

        #for now update_draw will be activated from here
        self.update_draw(event)

    def updatePoint_nD(self,dimArr): #([min,xdata,ic],[avg,ydata,range(ia,b,z vateve)]) follow this format

        emptyPos = None #for now need only one empty pos, no need to get into planes now
        xyLoc = []
        count = 0 # might be a way to remove count
        print(dimArr)
        for d in dimArr:
            if d == None: #len(d) == 1 and d[0] == None: #"place" # place for place holder
                emptyPos = count
                count+=1
                pos = None
                print("in pos = place")
            else:
                #solve min,xdata, range)
                plt_sect = d[2]
                #print(d[2])
                #sys.exit()
                if plt_sect == "all":
                    plt_range = "all"
                #for now no inf and no specific num
                #movable points if _underscore_
                else: 
                    plt_range = allObjcts.get_sect("movable_points",plt_sect).get_MdataPos() # gets section will give [nBot,nTop]
                #better naming for data_sexton section
                pos = solveMath.solveOv(d[0],fromUser.get_data(d[1]), plt_range)
            xyLoc.append(pos) # cause I dont want to create second temp array?
        return xyLoc
        
        if emptyPos != None:
            AddinForEmpty()

        def AddinForEmpty(self):
            pass # will do later-  for func above



    def find_intercept(self):
        pass



    #Override  #for now update_draw not used will prob have own class for
    # drawing points,lines, areas, and all else  