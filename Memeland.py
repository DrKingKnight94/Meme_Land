# -*- coding: utf-8 -*-
#imports the exit function
from sys import exit 
import time
#Where your adventure starts off. Lets you choose which path to take. 
def start():
    print "\n---------------------------------------------------------------------------"
    print "You walk into a dimly lit room, a voice starts to speak from the darkness" 
    print "\n'Hello", name,"- I've been expecting you for a long time'\n"
    print "*A strange smiling skeleton walks out from the cover of darkness*\n"
    print "'You've spent a long time seeking an adventure that you deem worthy of your skills'"
    print "'I can promise that you've come to the right place.'"
    print "\"Here take this\", *Holds up sword*\"I am the SkElEtOn oF DoOm *cough* escuse me" 
    print "'Also, here's a set of T-51B Power Armor just cuz I got it like that"
    print "'Behind me are two doors...'"
    print "'On your left, you have the 'rich path''\n'Here you will have to fight many tough battles in order to reach the treasure at the end.'"
    print "'On your right, you have the 'poor path'',\n'Here you will be able to walk in peace and enjoy your scenery'\n"
    print "Your path can be tough or it can be cake"
    print "\n---------------------------------------------------------------------------"
    print "Rich or poor", name, "choose your fate!\n"
    direction= raw_input("Which way do you want to go? ").lower()
   
#Chooses which direction of the game you want to go in
    if direction == "left" or direction == "rich":
    	print "\n'You have chosen the rich path... very well'\n'To be honest, these paths lead to the same place anyway'" 
    	mentor()
    elif direction == "right" or direction == "poor":
    	print "\n---------------------------------------------------------------------------"
        print "\n'HAHAHAHAHA where's your sense of adventure!?!?'\n'very well... stay broke... pussy'\n'You know what?... nevermind...'"
        mentor()
    elif direction == "back" or direction == "turn around" :
        dead("\nYou turn around and leave\n'Ain't nobody got time for that!'")
    else:
        print dead("The Skeleton smiles and says 'you're taking too damn long'\nskeleton yells at you to get out... and you do")
    
    exit(0)
#Hi, my name is Adrian, and I identify as as an Apache attack helicopter...
def apache():
    print "\n---------------------------------------------------------------------------"
    print "*You walk into bright, humid room rife with lush trees. You find a ... rocket launcher?"
    print "You don't see an exit so, you just walk aimlessly around for a few hours until suddenly..."
    print "*Vroooooooooooooooooooooooooooooooooooooooooooooooooooom*"
    print "*A small helicopter rushes right past you, 30 MM cannons aimed right at you*"
    hit_points=100
    apache_points=100  
    apache_down=False
    turn=1
    
    while True:
    
        if hit_points <=0:
            dead("\nYou're body is now riddled with massive bullet holes. YOU DIED")
        
        
        elif turn == 12:
            dead("\nThe helicopter releases a vicious barrage of hellfire missles. You are obliterated")
            
        print "\n---------------------------------------------------------------------------"
        decision=raw_input("\nAWWWWW SNAP! Its an attack helicopter. What do you do? > ").lower()
		
	if decision == "attack" and turn%2!=0:
       		print "\nRight as you ready your rocket launcher, you get smacked by gun fire"
        	hit_points=hit_points-50
        	turn = turn+1
        elif decision == "attack" and turn%2==0:
            	print "\nIt appears the helicopter is reloading, you hit it with a missle"
            	apache_points=apache_points-25
            	turn=turn+1
         
            	if apache_points <=0:
            		print "\n---------------------------------------------------------------------------"
            		print "\nYou identify as an XM191 rocket launcher, you shoot down the Apache"
            		print "Your rocket launcher has ran out of missles, you simply throw it away"
            		print "You bumble about until you find an exit*"
            		time.sleep(5)
            		genji_room()
            
        elif decision == "defend" and turn%2!=0:
        	print "\nYou get hit with gun fire, but you are well prepared"
        	hit_points=hit_points-10
       		turn = turn+1
    
        elif decision == "defend" and turn==0:
        	print "\nYou try to defend yourself, but it appears the helicopter is reloading"
        	turn = turn+1
        	
      
        elif decision == "roll" and turn%2!=0:
        	print "\nYou successfully manage to roll out of the way of the Apache's gunfire."
        	turn = turn +1
        elif decision == "roll" and turn%2==0:
        	print "\nYou try to roll away but get hit indirectly, oh well"
        	hit_points=hit_points-25
        	turn=turn +1
        	
        elif "helicopter" in decision or "apache" in decision or "identify" in decision or "sexually" in decision:
        	print "\n---------------------------------------------------------------------------"
        	print "*The helicopter suddenly starts blaring out over loud speakers*"
        	print "I sexually Identify as an Attack Helicopter. Ever since I was a boy I dreamed of"
        	print "soaring over the oilfields dropping hot sticky loads on disgusting foreigners. People"
        	print "say to me that a person being a helicopter is Impossible and I’m fucking retarded"
        	print "but I don’t care, I’m beautiful. I’m having a plastic surgeon install rotary blades, 30"
        	print "mm cannons and AMG-114 Hellfire missiles on my body. From now on I want you"
        	print "guys to call me “Apache” and respect my right to kill from above and kill needlessly." 
        	print "If you can’t accept me you’re a heliphobe and need to check your vehicle privilege."
        	print "Thank you for being so understanding."
        	
        	turn =turn+1
        	
        else:
        	print "What is you doing, bruh?"
        	hit_points=hit_points-75
        	turn=turn+1    
#Where the code takes you when you die    
def dead(why):
    print "\n---------------------------------------------------------------------------"
    print why
    exit(0)
#First fight with navy seal. Involves the "Navy Seal" Copypasta. Theme is "tough guy" that is really a kid.    
def navy_seal():
    hit_points=100
    navy_points=100
    print "\n---------------------------------------------------------------------------"
    print "\nYou stroll past the dead body and enter the door behind him"
    print "\n---------------------------------------------------------------------------"
    print "The first thing you see in the room is a soldier armed to the teeth\nknives, grenades, bullet-proof vest, guns, and a helmet to boot"
    print "The soldier looks at you and disguistingly spits at the ground"
    print "\n'Huuuuuh', Looks like I caught my next victim"
    print "You can already see that you are gonna have to fight your way through this path\n"
    print "You look down, and pick up a HK Mark 23 handgun"
    #Causes the statement to loop
    seal_dead=False
    
    while True:
    
        if hit_points <=0:
            print "'Boom, Headshot... Kill Confirmed'"
            dead("LOL, you got taken out by him? Try again maggot")
    	print "\---------------------------------------------------------------------------"
        decision= raw_input("You calmly ready your firearm > ").lower()
        if decision == "attack":
            navy_points=navy_points-100
            print "'Ahhhhh.... You're dead maggot' *dies*"
            time.sleep(5)
            if navy_points<=0:
                apache()
                     
        
        elif decision == "roll" or decision == "defend":
            print "*Fires shots kinda in you're direction*\n'Hah, I bet you're scared maggot, you're dead'\n"
        
        elif "loser" in decision or "bitch" in decision or "punk" in decision  or "pussy" in decision or "taunt" in decision:
            print "\n---------------------------------------------------------------------------"
            print "What the fuck did you just fucking say to me,"
            print "you little bitch? I'll have you know I graduated"
            print "top of my class in the Navy Seals, and I've been"
            print "involved in numerous secret raids on Al-Quaeda, "
            print "and I have over 300 confirmed kills. I am trained"
            print "in gorilla warfare and I'm the top sniper in the "
            print "entire US armed forces You are nothing to me but"
            print "just another target. I will wipe you the fuck out"
            print "with precision the likes of which has never been"
            print "seen before on the Earth, mark my fucking words."
            print "You think you can get away with saying that shit"
            print "to me over the internet? Think again, fucker. As we"
            print "speak I am contacting my secret network of spies"
            print "accross the USA and your IP is being traced right now"
            print "so you better prepare for the storm, maggot. The"
            print "storm that wipes out the pathetic little thing you"
            print "call a life. You're fucking dead, kid. I can be"
            print "anywhere, anytime, and I can kill you in over seven"
            print "hundred ways, and that's just with my bare hands."
            print "Not only am I extensively trained in unarmed combat,"
            print "but I have access to the entire arsenal of the United"
            print "States Marine Corps and I will use it to its full"
            print "extent to wipe your miserable ass off the face of"
            print "the continent, you little shit. If only you could"
            print "have known what unholy retribution our little \"clever\""
            print "comment was about to bring down upon you, maybe you"
            print "would have held your fucking tongue. But you couldn't"
            print "you didn't, and now you're paying the price, you"
            print "goddamn idiot. I will shit fury all over you and"
            print "you will drown in it. You're fucking dead, kiddo.\n"
        else:
            print "You're about to be my next confirmed kill maggot *Shoot grazes you*\n"
            hit_points=hit_points-25
                
    exit(0)
#Douchebag Mentor    
def mentor():
	mentor_points=100
	hit_points=100
	print "\n---------------------------------------------------------------------------"
	print "Reminder, in case you skipped through the instructions, its 'attack, defend, or roll'"
	print "\n*You walk into a large room with a pretty sweet car in the center*"
	print "'Hello friend. Welcome to my garage'"
	print "'You know, I was in your shoes not too long ago'."
	print "'I was just like you... lost in this lonely world'"
	print "'But I can show you the path to success'\n'There's a computer right over there actually.'"
	print "'Why not sit down and go to my website and I can show you'\n'the keys to success. What do you say?'"  
	mentor_dead=False
	
	while True:
		print "\n---------------------------------------------------------------------------"
		decision= raw_input("\nWhat is this guy on... what do you want to do? > ").lower()
		if decision == "attack":
			mentor_points=mentor_points-100
			print "'\n'I *cough cough* only wanted to help you'"
			time.sleep(5)
			navy_seal()
		
		elif decision == "roll" or decision == "defend":
			print "\n'Friend, I only want to help you'"

		elif "sit" in decision or "seat" in decision or "computer" in decision or "garage" in decision or "tedx" in decision or "lamborghini" in decision:
			print "\n---------------------------------------------------------------------------"
			print "*You sit down at the computer*"
			print "\nHere in my garage, just bought this new Lamborghini here. It’s fun to drive up here in the Hollywood hills. But you know what I like more "
			print "than materialistic things? Knowledge. In fact, I’m a lot more proud of these seven new bookshelves that I had to get installed to hold two"
			print "thousand new books that I bought. It's like the billionaire Warren Buffett says, 'the more you learn, the more you earn.'"
			print "\nNow maybe you’ve seen my TEDx talk where I talk about how I read a book a day. You know, I read a book a day not to show off it’s again"
			print "about the knowledge. In fact, the real reason I keep this Lamborghini here is that it’s a reminder. A reminder that dreams are still possible,"
			print "because it wasn’t that long ago that I was in a little town across the country sleeping on a couch in a mobile home with only forty seven dollars"
			print "in my bank account. I didn’t have a college degree, I had no opportunities."
			print "\nBut you know what? Something happened that changed my life. I bumped into a mentor. And another mentor. And a few more mentors. I found five mentors."
			print "And they showed me what they did to become multimillionaires. Again, it’s not just about money, it’s about the good life; health, wealth, love and" 
			print "happiness. And so I record a little video, it’s actually on my website, you can click here on this video and it’ll take you to my website where"
			print "I share three things that they taught me. Three things that you can implement today no matter where you are."
			print "\nNow, this isn’t a “get rich quick” scheme. You know, like they say if things sound too good to be true they are too good to be true. I’m not"
			print "promising you that tomorrow you’re gonna be able to go out and buy a Lamborghini. But what I am telling you is that it can happen faster than" 
			print "you think if you know the proven steps. So, I record a little two minute video on my website. Like I said, now it’s not the most professional I just"
			print "shot it here with my iPhone, but it's real. Nobody can argue, this is my true story. And I'm going to give you the three most important things you can" 
			print "do today. So click the link, go there it’s completely free to watch it it’s just a couple minutes. Invest in yourself. Always be curious. Don’t be a" 
			print "cynic. Okay, people see videos like this and the say 'Ah that's not real that's for somebody else.'"
			print "\nDon’t listen, don’t listen. Be an optimist. Like, Conrad Hilton, the man who started Hilton Hotel, he said that he was only fifteen years old when he"
			print "read a book by Helen Keller, and that book changed his life. Books can change your life. And in that book, Helen Keller said 'optimism' so if you’re a"
			print "cynic, if you’re a pessimist you don’t need to click here. Don’t worry about it, I don’t need to talk to everybody. But if you’re somebody who knows that" 
			print "there’s something better, cause the dream is possible, you know, for some of you watching it’s not necessarily a Lamborghini, maybe it’s a new job,"
			print "a new opportunity, starting your own company."
			print "\nMaybe it’s a new lifestyle without so much stress, traveling the world, doing those things you know you’re destined to do. You can do those" 
			print "unless you understand finances. Money, I don’t call it money anymore, I call it fuel units. You must have enough fuel units to live out your dream and"
			print "to live out your destiny. So, Ill see you on my website, its a quick video and you'll see they're absolutely free."
			print "\nSo just click this video and you’ll be taken there in a second, and uh, I’m excited to share this amazing stuff. You’ll see, not because of anything"
			print "of me but because I’ve been fortunate enough to learn from mentors many years ahead of me. Not just in books like these, although I love books but"
			print "also real in-person mentors. So let me share with you these three tips that have made all the difference in my life. They’re practical, you can do them today,"
			print "you can start on them today. All right? See you there on my site."
			dead("You watch the TedX talk and literally die of boredom")
		else:
			print "I just want to help you, friend. Let me be you mentor"
	
     

#Broke ass...    
def poor_path():
    print "\n'You are now on the poor path... How the hell did you get here???'\nOl' I gotta hack everything I touch lookin ass...\nI just can't play the game lookin ass\nInvestigatin ass nigga"
    print "You know what? Fuck you. No seriously, fuck you."
    
    exit(0)
    
#For you overwatch players
def genji_room():
	print "\n---------------------------------------------------------------------------"
	print "You walk into a completely empty room*"
	print "A cyber ninja looking person silently motions you to pick up the pulse"
	print "rifle laying on the floor."
	
	turn=1
	hit_points=100
	ninja_points=100
	ninja_dead=False
	
	while True:
	
		print "\n---------------------------------------------------------------------------"
        	decision= raw_input("You start to aim down your pulse rifle, what do you do> ").lower()
        	
        	if turn == 11:
            		dead("\nThe ninja randomly yells 'Ryūjin no ken o kurae'\nHe pulls at his sword and hacks you to death.")
   
        	if decision == "attack" and turn==1:
       			print "\nThe ninja uses \"deflect\", you take damage"
        		hit_points=hit_points-50
        		turn = turn+1
        	elif decision == "attack" and turn==2:
            		print "\nYou try to attack but, the ninja quickly dashes forward and cuts you"
         	
           		hit_points=hit_points-50
           		turn=turn+1
         
        	elif decision == "attack" and turn==3: 
        		print "You catch the ninja off guard, and hit him with gun fire."
        		ninja_points=ninja_points-25
        		turn=turn+1
        	
        	elif decision == "attack" and turn==4:
        		print "You take advantage, and fire a few shots into the ninja"
        		ninja_points=ninja_points-25
        		turn=turn+1
        
        	elif decision == "attack" and turn ==5:
        		print "The ninja jumps and launches a few shuriken into you"
        		hit_points=hit_points-50
        		turn=turn+1
        
        	elif decision == "attack" and turn==6: 
        		print "You catch the ninja off guard, and hit him with gun fire."
        		ninja_points=ninja_points-25
        		turn=turn+1
        	
        	elif decision == "attack" and turn==7:
       			print "\nThe ninja uses \"deflect\", you take damage"
        		hit_points=hit_points-50
        		turn = turn+1
        
        	elif decision == "attack" and turn==8:
           		print "You take advantage, and fire a few shots into the ninja"
        		ninja_points=ninja_points-25
        		turn=turn+1
        		if ninja_points <=0 and hit_points==100:
            			print "\n---------------------------------------------------------------------------"
            			print "\nThe ninja sees that you are clearly superior to himself."
            			print "The ninja slowly falls to his knees and slits his stomach."
            			print "'Even if I sacrifice my body, but I will neveer sacrifice my honor'"
            			print "what he considers to be an honorable death"
            			print "You calmly exit through the door that suddenly appeared"
            			time.sleep(5)
            			comic_room()
            		if ninja_point <=0:
            			print "\n---------------------------------------------------------------------------"
            			print "The ninja keels over, succumbing to his wounds"
            			print "A door suddenly appears on the other side of the room"
            			print "You rush over to exit the room"
            			time.sleep(5)
            			comic_room()
        	
        	elif decision == "attack" and turn==9:
           		print "\nYou try to attack but, it the ninja quickly dashes forward and cuts you"
           		hit_points=hit_points-50
           		turn=turn+1
           	
        	elif decision == "attack" and turn==10:
        		print "You catch the ninja off guard, and hit him with gun fire."
        		ninja_points=ninja_points-25
        		turn= turn+1
        		
        		if ninja_points <=0:
            			print "\n---------------------------------------------------------------------------"
            			print "The ninja keels over, succumbing to his wounds"
            			print "A door suddenly appears on the other side of the room"
            			print "You rush over to exit the room"
            			time.sleep(5)
            			comic_room()
        		
        	elif decision == "defend" and turn ==1:
        		print "You watch the ninja wave his sword around"
        		turn= turn+1
        		
        	elif decision == "defend" and turn ==2:
        		print "The ninja tries to slash through you; moderate sucess"
        		hit_points= hit_points-12.5
        		turn=turn+1
        		
        	elif decision == "defend" and turn==3:
        		print "The ninja seems to be just hoping around"
        		turn= turn+1
        		
        	elif decision == "defend" and turn==4:
        		print "The ninja seems to be just hoping around"
        		turn= turn+1
        		
        	elif decision == "defend" and turn==5:
        		print "The ninja launches a few shuriken, but you're prepared."
        		hit_points=hit_points-12.5
        		turn= turn+1

        	elif decision == "defend" and turn==6:
        		print "The ninja seems to be jii loafing around"
        		turn= turn+1
        		
        	elif decision == "defend" and turn==7:
        		print "You watch the ninja wave his sword around"
        		turn= turn+1
        		
        	elif decision == "defend" and turn==8:
        		print "The ninja seems to be loafing around"
        		turn= turn+1
        		
        	elif decision == "defend" and turn ==9:
        		print "The ninja tries to slash through you; moderate sucess"
        		hit_points= hit_points-12.5
        		turn=turn+1
        		
        	elif decision == "defend" and turn ==10:
        		print "The ninja tries to slash through you; moderate sucess"
        		hit_points= hit_points-12.5
        		turn=turn+1
  
           		
        	elif decision == "roll" and turn ==1:
        		print "You somehow manage to roll into the the ninja who's just waving his sword around..."
        		print "You get smacked"
        		hit_points=hit_points-25
        		turn= turn+1
        		
        	elif decision == "roll" and turn ==2:
        		print "You manage to roll out of the way of the ninja's slash"
        		turn=turn+1
        		
        	elif decision == "roll" and turn==3:
        		print "The ninja seems to be just hoping around"
        		turn= turn+1
        		
        	elif decision == "roll" and turn==4:
        		print "The ninja seems to be just hoping around"
        		turn= turn+1
        		
        	elif decision == "roll" and turn==5:
        		print "The ninja launches a few shuriken, good thing you rolled out the way"
        		turn= turn+1

        	elif decision == "roll" and turn==6:
        		print "The ninja seems to be jii loafing around"
        		turn= turn+1
        		
        	elif decision == "roll" and turn==7:
        		print "You somehow manage to roll into the the ninja who's just waving his sword around..."
        		print "You get smacked"
        		hit_points=hit_points-25
        		turn= turn+1
        		
        	elif decision == "roll" and turn==8:
        		print "The ninja seems to be loafing around"
        		turn= turn+1
        		
        	elif decision == "roll" and turn ==9:
        		print "You manage to roll out of the way of the ninja's slash"
        		turn=turn+1
        		
        	elif decision == "roll" and turn ==10:
        		print "You manage to roll out of the way of the ninja's slash"
        		turn=turn+1
        	elif "harambe" in decision or "winston" in decision or "blizzard" in decision or "genji" in decision or "overwatch" in decision:
        		print "\nI'm fucking sick of it. I'm sick of all this shit. I"
        		print "throw my keyboard out of my window every other week."
        		print "I'm Genji and I suffer from crippling depression. I'm"
        		print "beginning to have suicidal thoughts, too. Everyone"
        		print "tells me to stop playing Overwatch if I get so angry"
        		print "at it, but they don't understand shit. Why the fuck"
        		print "does blizzard allow 3 fucking Winstons on the same team"
        		print "WHAT KIND OF FUCKING LOGIC IS IT, TO HAVE 3"
        		print "MOTHERFUCKING MONKEYS JUST SHOOTING MOTHERFUCKING"
        		print "LAZERS AT YOU AT ONCE?! I'M SICK OF ALL THIS SHIT AND"
        		print "I SWEAR TO GOD I WILL FUCKING BOMB BLIZZARD'S BUILDING"
        		print "SO THAT I CAN TAKE OVER AND FUCKING REMOVE WINSON FROM"
        		print "THE GAME. I AM TIRED OF THE SHIT BLIZZARD IS PULLING"
        		print "I HONESTLY ALMOST HUNG MYSELF WHEN MY FUCKING NERFS"
        		print "CAME IN, BUT THIS IS REALLY TRIGGERING ME NOW. IF"
        		print "ANYONE HAS CONTACT WITH A BLIZZARD CEO TWEET ME ON"
        		print "TWITTER @MinecraftKid12345"
        		
        		turn =turn+1
        	else: 
        		dead("The ninja stares deep into your eyes.\nHe slowly walks towards you with his sword pointed forward.\nA single tear rolls down his face as he plunges the sword\ninto your torso. You slowly lose consciousness.")
            		
#Sans is a dirty liar. I never even played this game lol.            
def comic_room():

	print "\n---------------------------------------------------------------------------"
	print "You walk into a completely empty room*"
	print "The strange smiling skeleton is staring at you"
	print "The pulse rifle you had suddenly disapperars and"
	print "your sword appears in your hand."
	print "\n---------------------------------------------------------------------------"
	print "'heya, you've been busy huh?'"
	time.sleep(1)
	print "'When you kill someone, your EXP increases. and you've got a lot.'"
	time.sleep(1)
	print "'you're a pretty bad person, dont you have any compassion?'"
	time.sleep(1)
	print "'you are REALLY not going to like what happens next.'"
	time.sleep(3)
	print "\n*The skeleton suddenly releases a viscious flurry of attacks, though"
	print "you manage to dodge them all.*"
	print "'huh. always wondered why people never use their strongest attack first'"
	turn=2
	hit_points=100
	sans_points=1
	sans_dead=False
	
	while True:
	
		print "\n---------------------------------------------------------------------------"
		if turn==31: 
			print "\n*The smiling skeleton falls asleep*"
    		decision= raw_input("You stare at that skeleton, looking for a chance to attack > ").lower()
        	
      		if decision == "attack" and turn==2:
       			print "*The smiling skeleton dodges your attack*"
       			print "\n'it's a beutiful day outside. birds are singing, flowers blooming...'"
       			print "'on days like these, kids like you...'"
       			print "'S h o u l d  b e  b u r n i n g  i n  h e l l.'"
       			print "\n*The skeleton suddenly releases a viscious flurry of attacks, though"
			print "you manage to dodge them all.*"
       			turn = turn + 1
       			
       		elif decision == "attack" and turn ==5:
       			print "*The smiling skeleton dodges your attack*"
       			print "\n'what you think i'm just gonna stand there and take it?'"
       			print "\n*The skeleton suddenly releases a viscious flurry of attacks, though"
			print "you manage to dodge them all.*"
       			turn = turn + 1
       			
       		elif decision == "attack" and turn == 6:
       			print "*The smiling skeleton dodges your attack*"
       			print "'\nour reports showed a massive anamoly in the timespace continuum'"
       			print "'timelines jumping left and right, stopping and starting..."
       			print "\n*The skeleton suddenly releases a viscious flurry of attacks, though"
			print "you manage to dodge them all.*"
       			turn = turn +1
       			
       		elif decision == "attack" and turn == 7:
       			print "*The smiling skeleton dodges your attack*"
       			print "\n'until suddenly, everything ends.'"
       			print "\n*The skeleton suddenly releases a viscious flurry of attacks, though"
			print "you manage to dodge them all.*"
       			turn = turn+1
       			
        	elif decision == "attack" and turn == 8:
       			print "*The smiling skeleton dodges your attack*"
       			print "\nheh heh heh... that's your fault isn't it?"
       			print "\n*The skeleton suddenly releases a viscious flurry of attacks, though"
			print "you manage to dodge them all.*"
       			turn = turn+1
       			
       		elif decision == "attack" and turn == 9:
       			print "*The smiling skeleton dodges your attack*"
       			print "\n'you can't understand how this feels'"
       			print "\n*The skeleton suddenly releases a viscious flurry of attacks, though"
			print "you manage to dodge them all.*"
       			turn = turn+1
       			
       		elif decision == "attack" and turn == 10:
       			print "*The smiling skeleton dodges your attack*"
       			print "\n'knowing that one day, without any warning...'"
       			print "'it's all going to be reset'"
       			print "\n*The skeleton suddenly releases a viscious flurry of attacks, though"
			print "you manage to dodge them all.*"
       			turn = turn+1
       	
       		elif decision == "attack" and turn == 11:
       			print "*The smiling skeleton dodges your attack*"
       			print "\nuntil suddenly, everything ends."
       			print "\n*The skeleton suddenly releases a viscious flurry of attacks, though"
			print "you manage to dodge them all.*"
       			turn = turn+1
       			
        	elif decision == "attack" and turn == 12:
       			print "*The smiling skeleton dodges your attack*"
       			print "\n'look. i gave up trying to go back a long time ago.'"
       			print "\n*The skeleton suddenly releases a viscious flurry of attacks, though"
			print "you manage to dodge them all.*"
       			turn = turn+1
       			
       		elif decision == "attack" and turn == 13:
       			print "*The smiling skeleton dodges your attack*"
       			print "\n'and leaving this place doesen't really appeal anymore, either.'"
       			print "\n*The skeleton suddenly releases a viscious flurry of attacks, though"
			print "you manage to dodge them all.*"
       			turn = turn+1
       			
       		elif decision == "attack" and turn == 14:
       			print "*The smiling skeleton dodges your attack*"
       			print "\n'cause even if we do... we'll just end up right back here.'"
       			print "'with no memory of it right?"
       			print "\n*The skeleton suddenly releases a viscious flurry of attacks, though"
			print "you manage to dodge them all.*"
       			turn = turn+1
       			
       		elif decision == "attack" and turn == 15:
       			print "*The smiling skeleton dodges your attack*"
       			print "\n'to be blunt... it makes it kind of hard to give it my all'"
       			print "\n*The skeleton suddenly releases a viscious flurry of attacks, though"
			print "you manage to dodge them all.*"
       			turn = turn+1
       			
       		elif decision == "attack" and turn == 16:
       			print "*The smiling skeleton dodges your attack*"
       			print "\n'... or is that just a poor excuse for being lazy...?'"
       			print "\n*The skeleton suddenly releases a viscious flurry of attacks, though"
			print "you manage to dodge them all.*"
       			print "'hell if i know.'"
       			turn = turn+1
       			
       		elif decision == "attack" and turn == 17:
       			print "*The smiling skeleton dodges your attack*"
       			print "\n'all i know is... seeing what comes next... i can't afford'"
       			print "\n*The skeleton suddenly releases a viscious flurry of attacks, though"
       			print "'not to care anymore.'"
			print "you manage to dodge them all.*"
       			
       			turn = turn+1
       			
       		elif decision == "attack" and turn == 18:
       			print "*The smiling skeleton dodges your attack*"
       			print "\n'ugh... that being said... you, uh, really like swinging that'"
       			print "'thing around, huh?... listen."
       			print "\n*The skeleton suddenly releases a viscious flurry of attacks, though"
			print "you manage to dodge them all.*"
       			turn = turn+1
       			
       		elif decision == "attack" and turn == 19:
       			print "*The smiling skeleton dodges your attack*"
       			print "\n'and leaving this place doesen't really appeal anymore, either.'"
       			print "\n*The skeleton suddenly releases a viscious flurry of attacks, though"
			print "you manage to dodge them all.*"
       			turn = turn+1
       			
       		elif decision == "attack" and turn == 20:
       			print "*The smiling skeleton dodges your attack*"
       			print "\n'i can feel it. there's a glimmer of a good person inside of you. the memory'"
       			print "'of someone who wanted to do the right thing. someone who, in'"
       			print "'another time, might have been... a friend? c'mon, if you're'"
       			print "' listening... let's forget all of this, ok? just lay down your'"
       			print "'weapon and... well, my job will be a lot easier.'"
       			print "\n*The skeleton suddenly releases a viscious flurry of attacks, though"
			print "you manage to dodge them all.*"
       			turn = turn+1
       			
       		elif decision == "attack" and turn == 21:
       			print "*The smiling skeleton dodges your attack*"
       			print "\n'welp, it was worth a shot. guess you like doing things the hard'"
       			print "'way, huh?'"
       			print "\n*The skeleton suddenly releases a viscious flurry of attacks, though"
			print "you manage to dodge them all.*"
       			turn = turn+1
       			
       		elif decision == "attack" and turn == 22:
       			print "*The smiling skeleton dodges your attack*"
       			print "\n'sounds strange, but before all this i was secretly hoping we could'"
       			print "'be friends. i always though the anamoly was doing this because you'"
       			print "'they were unhappy. and when they got what they wanted, they would'"
       			print "'stop all this.'"
       			print "\n*The skeleton suddenly releases a viscious flurry of attacks, though"
			print "you manage to dodge them all.*"
       			turn = turn+1
       		
       		elif decision == "attack" and turn == 23:
       			print "*The smiling skeleton dodges your attack*"
       			print "\n'and maybe all they needed was... i dunno some good food, some bad'"
       			print "'laughs, some nice friends.'"
       			print "\n*The skeleton suddenly releases a viscious flurry of attacks, though"
			print "you manage to dodge them all.*"
			turn=turn+1
			
		elif decision == "attack" and turn == 24:
       			print "*The smiling skeleton dodges your attack*"
       			print "\n'but that's ridculous, right? yeah, you're the type of person who won't'"
       			print "'EVER be happy.'"
       			print "\n*The skeleton suddenly releases a viscious flurry of attacks, though"
			print "you manage to dodge them all.*"
       			turn = turn+1
       			
       		elif decision == "attack" and turn == 25:
       			print "*The smiling skeleton dodges your attack*"
       			print "\n'you'll just keep consuming timelines over and over, untill... well.'"
       			print "'hey . take it from me, kid. someday... you gotta learn when to QUIT'."
       			print "\n*The skeleton suddenly releases a viscious flurry of attacks, though"
			print "you manage to dodge them all.*"
       			turn = turn+1
       		
       		elif decision == "attack" and turn == 24:
       			print "*The smiling skeleton dodges your attack*"
       			print "\n'but that's ridculous, right? yeah, you're the type of person who won't'"
       			print "'EVER be happy'."
       			print "\n*The skeleton suddenly releases a viscious flurry of attacks, though"
			print "you manage to dodge them all.*"
       			turn = turn+1
       			
       		elif decision == "attack" and turn == 25:
       			print "*The smiling skeleton dodges your attack*"
       			print "\n'and that day's TODAY.'"
       			print "\n*The skeleton suddenly releases a viscious flurry of attacks, though"
			print "you manage to dodge them all.*"
			
			
		elif decision == "attack" and turn == 26:
       			print "*The smiling skeleton dodges your attack*"
       			print "\n'cause... y'see... all this fighting is really tiring me out.'"
       			print "\n*The skeleton suddenly releases a viscious flurry of attacks, though"
			print "you manage to dodge them all.*"
       			turn = turn+1
       		elif decision == "attack" and turn == 27:
       			print "*The smiling skeleton dodges your attack*"
       			print "\n'and if you keep pushing me... then i'll be forced to use my special attack'"
       			print "\n*The skeleton suddenly releases a viscious flurry of attacks, though"
			print "you manage to dodge them all.*"
			turn = turn+1
			
		elif decision == "attack" and turn == 28:
       			print "*The smiling skeleton dodges your attack*"
       			print "\n'yeah, my special attack. sound familiar? well, get ready. cause'"
       			print "'after the next move, i'm going to use it. so, if you don't want to see it,'"
       			print "'now would be a good time to die.'"
       			print "\n*The skeleton suddenly releases a viscious flurry of attacks, though"
			print "you manage to dodge them all.*"
			turn=turn+1
			
		elif decision == "attack" and turn == 29:
       			print "*The smiling skeleton dodges your attack*"
       			print "\n'well, here goes nothing... are you ready? survive THIS and i'll show'"
       			print "'you my special attack!'"
       			print "\n*The skeleton suddenly releases a viscious flurry of attacks, though"
			print "you manage to dodge them all.*"
			turn=turn+1
			
		elif decision == "attack" and turn == 30:
       			print "*The smiling skeleton dodges your attack*"
       			print "\n'huff... puff... all right. that's it. it's time for my special attack'"
       			print "'are you ready? here goes nothing.'"
       			time.sleep(10)
       			print "\n'yep. that's right. it's literally nothing. and it's not going to be'"
       			print "'anything, either. heh heh heh... ya get it? i know i can't beat you.'"
       			print "'one of your turns... you're just gonna kill me. so, uh. i've decided...'"
       			print "'it's not gonna BE your turn. ever. i'm just gonna keep having MY turn'"
       			print "'until you give up. even if it means we have to stand here until the'"
       			print "'end of time. capiche?'"
       			time.sleep(30)
       			print "\n'you'll get bored here. if you  haven't gotten bored already, i mean.'"
       			print "'and then, you'll finally quit.'"
       			time.sleep(60)
       			print "\n'i know your type. you're, uh, very determined, aren't you? you'll never'"
       			print "'give up, even if there's uh... absolutely NO benefit to perservering'"
       			print "'whatsoever. if i can make that clear. no matter what, you'll keep going.'"
       			print "'not out of any desire for good or evil... but just because you think you'"
       			print "'can. and because you \"can\"... ... you \"have to\"."
       			time.sleep(120)
       			print "\n'but now, you've reached the end. there is nothing left for you now. so,'"
       			print "in my personal opinion... the most \"determined\" thing you can do here?'"
       			print "is to uh, completely give up. and... *yawn* do literally anything else.'"
       			time.sleep(180)
       			turn = turn +1
       			
       		elif decision == "attack" and turn == 31:
			print "*The smiling skeleton dodges your attack*"
			time.sleep(7)
			print "'\nheh, didja really think you would be able'"
			time.sleep(1)
			print "*you attack again*"
			sans_points=sans_points-999999999999999999
			print "\n999999999999999999 damage dealt"
			time.sleep(7)
			print "\n---------------------------------------------------------------------------"
       			print "'... ... so... guess that's it, huh?... just don't say i didn't warn you."
       			print "well. i'm going to grillby's. papyrus, do you want anything?'"
       			time.sleep(5)
       			end_game()
       			
       			
       		
       		elif decision == "attack":
       			print "*The smiling skeleton dodges your attack*"
       			print "\n*The skeleton suddenly releases a viscious flurry of attacks, though"
			print "you manage to dodge them all.*"
       			turn = turn+1
       			
       		elif decision == "defend":
       			dead("You couldn't defend against the skeleton's harsh flurry of attacks...\nYou die in agony")
       			
       		elif decision == "roll":
       			dead("you couldn't dodge the skeleton's harsh flurry of attacks...\nYou die in agony")
       			
       		elif decision == "spare":
       			print "\n'...you're sparing me? finally. buddy. pal. i know how hard it must be...'"
       			print "'to make that choice. to go back on everything you've worked up to. i want'"
       			print "'you to know... i won't let it go to waste. ... c'mere pal.'"
       			dead("geeetttttt dunked on!!! if you we're really friends... you won't come back'")
       			
       		elif "sans" in decision or "kira" in decision or "genocide" in decision or "undertale" in decision:
       			print "\n---------------------------------------------------------------------------"
       			print "'ok so i am ultimately PISSED OFF RIGHT NOW becaue my STUPID INSENSITIVE BIGOT"
       			print "OF A SCIENCE TEACHER WON'T COVER THE SKELETON IN OUR CLASSROOM!!!! ive told"
       			print "THOUSANDS of TIMES that i have sever anxiety from sans and ive actually"
       			print "developed ptsd from the sans fight and i have to carry around an inhaler"
       			print "everywhere i go now because when i see bones or the color blue i start"
       			print "hyperventilating becaue of panic then if i don't take my inhaler it turn into"
       			print "a ptsd episode and i already had to be sent home 3 TIMES BECAUSE THE SKELETON"
       			print "IN MY SCIENCE CLASS TRIGGERED ME!!!! AND HE WON'T COVER  IT!!!!!!!! like??????"
       			print "i don't know what to do ive tried talking about it to the councilors but they"
       			print "said my condition isnt real???? like um YEAH IT IS??? i would know???????????"
       			print "cause i wake up screaming and in tears each night because i have a reacurring"
       			print "nightmare where SANS TELLS ME I'M GOING TO HAVE A BAD TIME THEN HAS TH FUCKING"
       			print "DECENCY TO TELL ME I'VE DIED TEN TIMES, AND THAT I HAVE NO FRIENDS!!! YOU KNOW"
       			print "HOW MUCH THAT FUCKING TRIGGERS ME???????? and it just PISSES ME OFF how the"
       			print "school doesn't even CARE THAT I AM ON THE BRINK OF ODING BECAUSE OF THIS!!!!!"
       			
       			
       		else:
       			dead("geeetttttt dunked on!!!")
def end_game():
	print "\n---------------------------------------------------------------------------"
	print "This ya boy Adrian."
	print "I hope you dug through the game and discovered some dank memes"
	print "Visit r/copypasta for that linguini"
       	print "I really cant believe you actually beat this shit tho, lol"
       	print "Anyway, have a decent day."
	exit(0)

  
#Welcome message, game rules
print "Welcome! \n\nIf you're here you must want to play Adrian's first game."
print "Please note that Adrian created this game solely to help him learn to code\nso try not to trash it too hard."
print "\nHow to play:\n"
print "There are two paths you can take in this game.\nOn the 'rich' path your three optioins are to 'attack, defend, or roll'"
print "On the poor path you can choose to move 'left' or 'right', for movement."
print "Please note that you must type these in EXACTLY how its written here without the" 
print "quoatations or it won't work ;)"
print "And oh yeah, play in full screen"
print "Enjoy\n"   
name= raw_input("Choose your adventurer's name: ")
start()

#"Cheat Codes" for you guys that do way too much digging.
#Navy Seal copypasta: type loser, or bitch, or taunt, or pussy for pasta.
#Lamborghini copypasta: type sit down, sit, computer, garage, tedx, or lamborghini for that delicious pasta.
#Apache copypasta: type helicopter, apache, identify or sexually for that great tasting pasta.
#Genji copypasta: type harambe, winston, blizzard, genji, or overwatch for that Kraft.
#Sans copypasta: type sans, kira, genocide, or undertale for that rigatoni.
