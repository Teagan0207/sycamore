#Tiange Li Final Project
import random
import time
import tkinter
import tkinter.messagebox
from tkinter import filedialog
import threading

root = tkinter.Tk()
root.withdraw()
file=filedialog.askopenfilename(filetypes = (("Text File", "*.txt"),) )
print('You opened the score and movement record file')
##this sentence from Stack Overflow https://stackoverflow.com/questions/34619141/opening-text-files-and-saving-the-contents-of-the-selected-files-as-variables-in?noredirect=1&lq=1


class Deck:##define single card class
    color=['black','red']
    
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit
    
    def card_color(self):
        if self.suit=='Club' or self.suit=='Spade' or self.suit=='small':
            return self.color[0]
        if self.suit=='Diamond'or self.suit=='Heart' or self.suit=='big':
            return self.color[1]
    
    def card_value(self):
        if self.rank=='JOKER':
            if self.suit=='big':
                return 25
            if self.suit=='small':
                return 20
        elif self.rank in Decks.faces:
            return Decks.faces[self.rank]['value']
        else:
            return self.rank

class Decks(object):##define a suit of cards
    faces= {'J':{'fullname':'JACK','value': 11}
            ,'Q':{'fullname':'QUEEN','value':12}
            ,'K':{'fullname':'KING','value':13}
            ,'A':{'fullname':'ACE','value':14}}
    ranks=[str(n) for n in range(2,11)] + list(faces.keys())
    suits =['Club','Diamond','Heart','Spade']
            
    def __init__(self):
        self.all=[]
        for r in self.ranks:
            for s in self.suits:
                self.all.append(Deck(r,s))
        self.all.append(Deck('JOKER','big'))
        self.all.append(Deck('JOKER','small'))
                
    def print_all(self):
        for deck in self.all:
            print('rank: ' + deck.rank + ' suit: ' + deck.suit)
                       
    def deal(self,n):
        return random.sample(self.all,n)

class MyException(Exception):##define my exceptions that could possibly occur
    def __init__(self,*args):
        self.args=args

class IllegalMove(MyException):
    def __init__(self,args=('illegal move',),message='Please try another move',code=100):
        self.args=args
        self.message=message
        self.code=code
        
class NonExist(MyException):
    def __init__(self,args=('NonExist',),message='object does not exist',code=200):
        self.args=args
        self.message=message
        self.code=code

###I made this tkinter object class with the help of this tutorial https://blog.csdn.net/metoo9527/article/details/78985632/
class drawer:
    def __init__(self):
        self.root=tkinter.Tk()
        self.root.title('Draw a prize! from Tiange-Li-prize-drawer' )
        self.root.minsize(400,470)
        self.root.wm_attributes('-topmost',1)
        self.show()
        self.isloop = False
        self.functions = False
        self.root.mainloop()
        
    def reply1(self):
        tkinter.messagebox.showinfo(title='WOW',message='SO LUCKY')
    def reply2(self):
        tkinter.messagebox.showinfo(title='WOW',message='Try again')
    def reply3(self):
        tkinter.messagebox.showinfo(title='WOW',message='Have a nice trip')
    def reply4(self):
        tkinter.messagebox.showinfo(title='WOW',message='Enjoy your meal')
    def reply5(self):
        tkinter.messagebox.showinfo(title='WOW',message='Unbelievable!\nSay hi for me')
    def reply6(self):
        tkinter.messagebox.showinfo(title='WOW',message='Study is your life')
    def reply7(self):
        tkinter.messagebox.showinfo(title='WOW',message='You are so blessed')
    def reply8(self):
        tkinter.messagebox.showinfo(title='WOW',message='Actually you can try again')
        
    def show(self):
        self.b1 = tkinter.Button(self.root, text = 'Grade A\nfor python', bg = 'red',command=self.reply1)
        self.b1.place(x = 20, y = 20, width = 100, height = 100)
        self.b2 = tkinter.Button(self.root, text = 'One more time', bg = 'white',command=self.reply2)
        self.b2.place(x = 150, y = 20, width = 100, height = 100)
        self.b3 = tkinter.Button(self.root, text = 'A trip to\n Antarctica', bg = 'white',command=self.reply3)
        self.b3.place(x = 280, y = 20, width = 100, height = 100)
        self.b4 = tkinter.Button(self.root, text = 'A meal with\nMr.Deamer', bg = 'white',command=self.reply4)
        self.b4.place(x = 20, y = 150, width = 100, height = 100)
        self.b5 = tkinter.Button(self.root, text = 'A meeting with\nMr.Trump', bg = 'white',command=self.reply5)
        self.b5.place(x =280, y = 150, width = 100, height = 100)
        self.b6 = tkinter.Button(self.root, text = 'A study package\n of Coursera', bg = 'white',command=self.reply6)
        self.b6.place(x = 20, y = 280, width = 100, height = 100)
        self.b7 = tkinter.Button(self.root, text = 'IphoneX', bg = 'white',command=self.reply7)
        self.b7.place(x = 150, y = 280, width = 100, height = 100)
        self.b8 = tkinter.Button(self.root, text = 'Thanks for\n participating', bg = 'white',command=self.reply8)
        self.b8.place(x = 280, y = 280, width = 100, height = 100)
        self.b_start = tkinter.Button(self.root, text = 'Start', command = self.newtask)
        self.b_start.place(x = 110, y = 400, width = 50, height = 50)
        self.b_stop = tkinter.Button(self.root, text = 'Stop', command = self.stop)
        self.b_stop.place(x = 240, y = 400, width = 50, height = 50)
    
    def around(self):
        if self.isloop == True:
            return
        i = 0
        while True:
            time.sleep(0.06)
            for j in self.prize:
                j['bg'] = 'white'
            self.prize[i]['bg'] = 'red'
            i += 1
            if i >= len(self.prize):
                i = 0
            if self.functions == True:
                continue
            else:
                break
        
    def newtask(self):
        self.prize = [self.b1,self.b2,self.b3,self.b5,self.b8,self.b7,self.b6,self.b4]
        t = threading.Thread(target = self.around)
        t.start()
        self.isloop = True
        self.functions = True
    
    def stop(self):
        self.functions = False
        self.isloop = False
        self.answer=tkinter.messagebox.askquestion(title='congratulations',message='Ready to back to game?')
        if self.answer=='yes':
            self.root.quit()
            self.root.destroy()
                
################functions will be used


def remove_card(cs,c):## let it includes my self-defined error
    if cs==[] or c not in cs:
        try: 
            raise IllegalMove()
        except IllegalMove as e:
            print('ErrorName:',e)
            print('ErrorMessage',e.message)
            print('ErrorCode',e.code)
    else:
        cs.remove(c)
        return(cs)

def all_same_color(cs):##using recursion 
    if cs==[]:
        return True
    elif len(cs)==1:
        return True
    elif cs[0].card_color()==cs[1].card_color():
        return(all_same_color(cs[1:]))
    else:
        return False
    
def sum_cards(cs):
    sum=0
    for item in cs:
        value=int(item.card_value())
        sum+=value
    return sum

def compare_suits(cs):##because final cards is prefered all same color, each time computer discards, it will choose to discard the color with fewer cards
    i=j=0
    for item in cs:
        if item.card_color()==Deck.color[0]:
            i+=1
        else:
            j+=1
    if i>j:
        return Deck.color[0]
    else:
        return Deck.color[1]
    
def score(cs,goal):##get 0 is best. if all same color, there is bonus. if sum > goal, there is huge penalty
    sum=sum_cards(cs)
    if sum>goal:
        pre_score=10*(sum-goal)
    else:
        pre_score= (goal-sum)
    if cs==[]:###if the evil player discards all his cards to achieve better score
        return pre_score+1000
    elif all_same_color(cs):##bonus
        return pre_score/3
    else:
        return pre_score

def find_card(cs, x):##let it includes error
    s=i=0
    while i<len(cs):
        if cs[i].rank==x or cs[i].rank==x.upper():
            s=1
            return cs[i]
            break
        else:
            i+=1
    if i==len(cs) and s==0:
         try:
             raise NonExist()
         except NonExist as e:
             print('ErrorName:',e)
             print('ErrorMessage',e.message)
             print('ErrorCode',e.code)
             
def print_cards1(cs):## to make reusing code easier
    print('The cards in your hand are:')
    for item in cs:
        print(item.rank, item.suit)
    print('The sum of your cards is',sum_cards(cs))

def print_cards2(cs):
    print('**The cards in computer\'s hand are:')
    for item in cs:
        print('**',item.rank, item.suit)
    print('**The sum of computer\'s cards is ',sum_cards(cs))

def init_cards():##initially each player has 4 cards and player can set a goal
    global decks, player_hand, computer_hand,goal,quit,game_done,score_record
    print('***Showing all cards***')
    time.sleep(0.5)
    decks=Decks()
    decks.print_all()
    goal=input('The goal you want to set is __\n>>')
    if goal.upper()=='QUIT':
        quit=game_done=1
        return quit
    while not goal.isdigit() or int(goal)<=30:
        print('The goal should be a Nonnegative Number, and bigger than 30')
        goal=input('The goal you want to set is __\n>>')
        if goal.upper()=='QUIT':
            quit=game_done=1
            return quit
    score_record.write('Goal: '+goal+'\n')
    goal=int(goal)
    while True:
        player_hand=[]
        for cards in range(0,4):
            card=random.choice(decks.all)
            player_hand.append(card)
            decks.all.remove(card)
        computer_hand=[]
        for cards in range(0,4):
            card=random.choice(decks.all)
            computer_hand.append(card)
            decks.all.remove(card)
        if sum_cards(player_hand)<=goal and sum_cards(computer_hand)<=goal:##to prevent when a small goal is set and the sum of assigned cards immediately exceed the goal
            break
    print('***Arranging cards randomly with goal of',goal,'***')
    time.sleep(0.5)
    print_cards1(player_hand)
    print_cards2(computer_hand)
    return 0
                 
move=['DISCARD','DRAW','END']

def player_turn():##player has three options, for each of them, i include some error detecting part
    global decks, player_hand, computer_hand,end,over,blocked,goal,pblocked,quit,score_record
    print('<Your turn>')
    print_cards1(player_hand)
    time.sleep(0.2)
    movement=input('Now you choose to \'DISCARD\' , \'DRAW\' or \'END\'?\n>>')
    typo=['DI','DIS','DISC','DIC','DC','DISCA','DCR','DSR','DCD','DSCRD','DCRD']
    if movement.upper()=='QUIT':
        quit=1
        return quit
    while movement.replace(' ','').upper() not in move and movement.replace(' ','').upper() not in typo and movement.replace(' ','').upper() != 'DR':
         print('Invalid input. Please try again')
         movement=input('Now you choose to \'DISCARD\' or \'DRAW\' or \'END\'?\n>>')
         if movement.upper()=='QUIT':
             quit=1
             return quit
    if movement.replace(' ','').upper()==move[0] or movement.replace(' ','').upper() in typo:
        disdeck=input('The card you want to DISCARD is __(enter rank)\n>>')
        if disdeck.upper()=='QUIT':
            quit=1
            return quit
        if disdeck.upper()=='RESET':####check if player do not want to discard now
            return(player_turn())
        while True:
            try:
                found=find_card(player_hand,disdeck)
                new_list = [i for i in player_hand if i.rank.upper() == disdeck.upper()]
                ##iter_list=iter(new_list)
                if len(new_list)>1:###if there are more than one card with same rank in player_hand, ask them which one to discard
                    content='Which suit of \"'+disdeck+'\" card you want to discard?\n>>'
                    dissuit=input(content)
                    if dissuit.upper()=='QUIT':
                        quit=1
                        return quit
                    if dissuit.upper()=='RESET':####check if player do not want to discard now
                        return(player_turn())
                    while True:
                        s=i=0
                        while True:               
                            if new_list[i].suit.upper()==dissuit.replace(' ','').upper() or (new_list[i].suit)[0].upper()==dissuit.replace(' ','').upper():###user can input full name suit or the first letter of suit
                                s=1
                                remove_card(player_hand,new_list[i])
                                score_record.write('player turn: '+'DISCARD '+new_list[i].rank+' '+new_list[i].suit+'\n')
                                print('DISCARD',new_list[i].rank,new_list[i].suit)
                                break
                            elif i==len(new_list)-1 and s==0:##wrong input, continue inner looping
                                print('You do not have this suit of',disdeck)
                                dissuit=input(content)
                                i=0
                                if dissuit.upper()=='QUIT':
                                    quit=1
                                    return quit
                                if dissuit.upper()=='RESET':####
                                    return(player_turn())
                            else:
                                i+=1
                        break
                    break                                 
                else:
                    remove_card(player_hand,found)
                    score_record.write('player turn: '+'DISCARD '+found.rank+' '+found.suit+'\n')
                    print('DISCARD',found.rank,found.suit)
                    if player_hand==[]:
                        pblocked=1
                    break
            except:##wrong input, continue outer looping
                print('You do not have this rank')
                disdeck=input('The card you want to DISCARD is __(enter rank)\n>>')
                if disdeck.upper()=='QUIT':
                    quit=1
                    return quit
                if disdeck.upper()=='RESET':####check if player do not want to discard now
                    return(player_turn())
    elif movement.replace(' ','').upper()==move[1] or movement.replace(' ','').upper()=='DR':
        drawdeck=random.choice(decks.all)
        decks.all.remove(drawdeck)
        player_hand.append(drawdeck)
        score_record.write('player turn: '+'DRAW '+drawdeck.rank+' '+drawdeck.suit+'\n')
        if sum_cards(player_hand)>goal:
            over=1
        if decks.all==[]:
            blocked=1
    else:
        end=1
        score_record.write('player turn: '+'Player choose not to move.\n')
    if pblocked==1:
        return pblocked
    else:
        print_cards1(player_hand)

   
def computer_turn():##a simple algorithm of computer to determine the best movement. 
    global decks,player_hand,computer_hand,goal,end,over,blocked,score_record
    new_dict={11:'J',12:'Q',13:'K',14:'A'}
    print('<Computer turn>')
    print_cards2(computer_hand)
    time.sleep(0.2)
    if sum_cards(computer_hand)>goal:
        over=1
    elif computer_hand==[]:
        blocked=1
    elif goal-sum_cards(computer_hand)>=10:##a long distance from goal->keep drawing
        drawdeck=random.choice(decks.all)
        decks.all.remove(drawdeck)
        computer_hand.append(drawdeck)
        print('<Computer draws>')
        time.sleep(0.2)
        score_record.write('computer turn: '+'DRAW '+drawdeck.rank+' '+drawdeck.suit+'\n')
        if sum_cards(computer_hand)>goal:
            over=1
        if decks.all==[]:
            blocked=1
    elif goal-sum_cards(computer_hand)<=2 or goal-sum_cards(computer_hand)<=5 and goal-sum_cards(player_hand)<10:##close->stop
        time.sleep(0.5)
        print('<Computer choose not to move.>')
        score_record.write('computer turn: '+'Computer choose not to move.\n')
        end=1
    elif compare_suits(computer_hand)==Deck.color[0]:##when discards, computer choose the smallest one from minority color
        print('<Computer discards>')
        time.sleep(0.2)
        new_list=[]
        for item in computer_hand:
            if item.card_color()==Deck.color[1]:
                new_list.append(int(item.card_value()))
        if new_list==[]:
            for item in computer_hand:
                new_list.append(int(item.card_value()))
        disdeck=min(new_list)
        if disdeck <= 10:
            found=find_card(computer_hand,str(disdeck))
        else:
            found=find_card(computer_hand,str(new_dict[disdeck]))
        score_record.write('computer turn: '+'DISCARD '+found.rank+' '+found.suit+'\n')
        remove_card(computer_hand,found )
        
    else:
        print('<Computer discards>')
        time.sleep(0.2)
        new_list=[]
        for item in computer_hand:
            if item.card_color()==Deck.color[0]:
                new_list.append(int(item.card_value()))
        if new_list==[]:
            for item in computer_hand:
                new_list.append(int(item.card_value()))
        disdeck=min(new_list)
        if disdeck <= 10:
            found=find_card(computer_hand,str(disdeck))
        else:
            found=find_card(computer_hand,str(new_dict[disdeck]))
        score_record.write('computer turn: '+'DISCARD '+ found.rank +' '+found.suit+'\n')
        remove_card(computer_hand, found)
    print_cards2(computer_hand)


        
        
#########################main loop######################
def play():
    global decks, player_hand, computer_hand,end,over,blocked,goal,pblocked,quit,score_record
    done=False ##the entire game status
    player_total=computer_total=0###total score, the result of many game times
    game_time=1 ##which inning
    score_record=open(file,'a',encoding='utf-8')
    score_record.write('Game time: '+str(game_time)+'\n')

    while not done:
        game_done=False
        end=over=blocked=pblocked=quit=0 ##four ending status,quit means whenever player types 'quit',process will go to the end
        time_start=time.time()
        state=init_cards()
        if state==0:
            n=random.randint(0,2)##randomly choose who is the one to do the first movement
            naming=['st','nd','rd','th']
            if game_time%10==1:
                print('-------The',str(game_time)+naming[0],'game.Game Time-------')
            elif game_time%10==2:
                print('-------The',str(game_time)+naming[1],'game.Game Time-------')
            elif game_time%10==3:
                print('-------The',str(game_time)+naming[2],'game.Game Time-------')
            else:
                print('-------The',str(game_time)+naming[3],'game.Game Time-------')
            time.sleep(2)
            while not game_done:
                if n==0:##player first
                    player_turn()
                    if over==1 or end==1 or blocked==1 or pblocked==1 or quit==1:
                        game_done=True
                    if not game_done:
                        computer_turn()
                        if over==1 or end==1 or blocked==1 or pblocked==1 or quit==1:
                            game_done=True
                else:##computer first
                    computer_turn()
                    if over==1 or end==1 or blocked==1 or pblocked==1 or quit==1:
                        game_done=True
                    if not game_done:
                        player_turn()
                        if over==1 or end==1 or blocked==1 or pblocked==1 or quit==1:
                            game_done=True
                if game_done:
                    time_end=time.time()
                    game_time+=1
                    if quit==1:
                        pass
                    else:
                        if over==1:
                            time.sleep(0.2)
                            print('Sum exceeds goal.\nGame Over!')
                            score_record.write('Sum exceeds goal.Game Over!\n\n')
                        if end==1:
                            time.sleep(0.2)
                            print('Give up future movements.\nGame Over!')
                            score_record.write('Give up future movements.Game Over!\n\n')
                        if blocked==1:
                            time.sleep(0.2)
                            print('No more cards to draw.\nGame Over!')
                            score_record.write('No more cards to draw.Game Over!\n\n')
                        if pblocked==1:
                            time.sleep(0.2)
                            print('Player evily discard all cards. A penalty has been added to your score.\nGame Over!')
                            score_record.write('You have no cards in hand.Game Over!\n\n')
                        time.sleep(0.2)
                        print('Checking scores......')
                        time.sleep(0.2)
                        print('You','\t','Computer')
                        player_score=score(player_hand,goal)
                        computer_score=score(computer_hand,goal)
                        time.sleep(0.2)
                        print(player_score,'\t',computer_score)
                        score_record.write('*Game time-'+str(game_time-1)+' summary: player vs computer: '+str(player_score)+' vs '+ str(computer_score)+'\n')
                        if player_score < computer_score:
                            print('>>>>>YOU WINS!!!')
                            player_total+=1
                        elif player_score==computer_score:
                            print('>>>>>Interesting. But I will still take you as a winner.')
                            player_total+=1
                        else:
                            print('>>>>>You lose')
                            computer_total+=1
                        score_record.write('*Total score: player vs computer: '+str(player_total)+ ' vs '+ str(computer_total)+'\n')
                    print('This game lasts for', str(int(time_end-time_start))+'s')
                    score_record.write('*This game lasts for '+str(int(time_end-time_start))+'s\n\n')
        else:
            pass
        relax=input('Want to relax(Y/N)?\n>>')
        if relax.lower().startswith('y'):
            prize=drawer()
        again=input('Play again(Y/N)?\n>>')
        if again.lower().startswith('y'):
            done=False
            print('Up to now, the total score between you and computer is',player_total,'vs',computer_total)
            score_record.write('Game time: '+str(game_time)+'\n')
        else:
            done=True
    print('Final scores:')
    time.sleep(0.2)
    print('You','\t','Computer')
    print(player_total,'\t',computer_total)
    score_record.close()

tkinter.messagebox.showwarning('Unfortunately','The following game does not have a GUI version')
tkinter.messagebox.showinfo('However','There will be a prize drawer after you finish this game')
rules=tkinter.messagebox.askokcancel('Rules', 'The computer randomly arranged cards,initially four at hands\nPlayer and computer make movements in turn\nFor each movement, you can try discard/draw/end\ninput \'quit\' to quit at any time\ninput\'reset\' to redo your movement\nfor more information, see readme.pdf.')
if rules==True:
    begin=tkinter.messagebox.askyesno("introducing my game","Ready to start this game?")
    if begin==True:
        play()




