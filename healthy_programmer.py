#Importing modules

import time

import pygame



#Periods of notification


water_after_every_min=20


eye_after_every_min=30


exercise_after_every_min=45



#Pygame screen,etc..


pygame.init()


width=720

height=1370

screen=pygame.display.set_mode((width,height))


#Caption


pygame.display.set_caption("Healthy Programmer")



#Background

background=pygame.image.load("background.png")

background=pygame.transform.scale(background,(720,1370))


#Images

water_image=pygame.image.load("water.jpg")

water_image=pygame.transform.scale(water_image,(400,400))


eye_image=pygame.image.load("eye.jpg")

eye_image=pygame.transform.scale(eye_image,(400,400))


exercise_image=pygame.image.load("exercise.jpg")

exercise_image=pygame.transform.scale(exercise_image,(400,400))


done_image=pygame.image.load("done.jpg")

done_image=pygame.transform.scale(done_image,(400,400))



font=pygame.font.SysFont(None,100)
	
text=font.render("Done",True,(255,255,255))



def sound(path):
	"""This will play the sound"""
	
	pygame.mixer.init()
	
	pygame.mixer.music.load(path)
	
	pygame.mixer.music.play(-1)
	
	time.sleep(3.5) #Sleeping till the music will be played



#Getting the time to use it to make the water time ,etc..

first_time_hr=int(time.strftime("%H"))

first_time_min=int(time.strftime("%M"))



#Variables


water=False
	
eye=False
	
exercise=False
	
done=True


#Time


#Water Time


water_time_hr=first_time_hr

water_time_min=first_time_min+water_after_every_min


#Eye time


eye_time_hr=first_time_hr

eye_time_min=first_time_min+eye_after_every_min


#exercise time


exercise_time_hr=first_time_hr

exercise_time_min=first_time_min+exercise_after_every_min



while True: #Infinite loop

	
	
	#Time
	
	
	#Water time
	
	
	if water_time_min>=60:#Hour and Min management
			
		water_time_hr+=1
			
		water_time_min=water_time_min-60
			
		water_time= f"{water_time_hr}{water_time_min}"
			
	else:
		water_time= f"{water_time_hr}{water_time_min}"
		
		
	#Eye time
	
	
	if eye_time_min>=60:#Hour and Min management
			
		eye_time_hr+=1
			
		eye_time_min=eye_time_min-60
			
		eye_time= f"{eye_time_hr}{eye_time_min}"
			
	else:
		eye_time= f"{eye_time_hr}{eye_time_min}"
		
		
	#Exercise Time
	
	
	if exercise_time_min>=60:#Hour and Min management
			
		exercise_time_hr+=1
			
		exercise_time_min=exercise_time_min-60
			
		exercise_time= f"{exercise_time_hr}{exercise_time_min}"
			
	else:
		exercise_time= f"{exercise_time_hr}{exercise_time_min}"
		
	
		
	#Time managing
	
	
	real_time=time.strftime("%H%M")
	
		
	if real_time==water_time:
				
		done=False
				
		water=True
				
	elif real_time==eye_time:
				
		done=False
				
		eye=True
				
	elif real_time==exercise_time:
				
		done=False
				
		exercise=True
		
		
		
	#Pygame
	
	
	screen.blit(background,(0,0))
	
	
			
	#Mouse #Getting postition of mouse
	
	
	mouse=pygame.mouse.get_pos()
	
	
	
	
	#Done
	
	
	if done==True:
		
		water=False
		
		eye=False
		
		exercise=False
		
				
		
		screen.blit(done_image,(160,300))
		
		
		
	
	#Water
	
	
	elif water==True:
		
		
		
		done=False
		
		
		#Stop after clicking the button
		
		
		if 160<mouse[0]<560 and 720<mouse[1]<820:
			
			
			water_time_min+= water_after_every_min
			
			
			pygame.mixer.music.stop()
			
			done=True
			
			water=False
			
			
			#Logging the Data in file water.txt
				
			with open("water.txt","a") as water_log:
					
				water_time_log=time.strftime("%a %d/%b/%Y %H:%M:%S")
					
					
				water_log.write("[")
					
				water_log.write(water_time_log)
					
					
				water_log.write("]")
					
				water_log.write("Water\n")


			
		
		else:
			
			#Running the program Playimg sound and displayimg water image
							
			screen.blit(water_image,(160,300))
			
			
			sound("water.mp3")		
			
			
			rect=pygame.draw.rect(screen,(0,0,255),(160,720,400,100),5,5,5,5,5) #Round border for done button
			
			
			rect=pygame.draw.rect(screen,(0,0,255),(165,725,390,90)) # done button
			
			
			screen.blit(text,(280,735))
			
			
			
			
	#Eye
	
	
	elif eye==True:
		
		
		
		done=False
		
		
		#Stop after clicking the button
		
		
		if 160<mouse[0]<560 and 720<mouse[1]<820:
			
			
			eye_time_min+= eye_after_every_min
			
			
			pygame.mixer.music.stop()
			
			done=True
			
			eye=False
			
			
			#Logging the Data in file eye.txt
				
			with open("eye.txt","a") as eye_log:
					
				eye_time_log=time.strftime("%a %d/%b/%Y %H:%M:%S")
					
					
				eye_log.write("[")
					
				eye_log.write(eye_time_log)
					
					
				eye_log.write("]")
					
				eye_log.write("Eye Exercise\n")
				
				continue
			
		
		else:
			
			#Running the program Playimg sound and displayimg eye image
							
			screen.blit(eye_image,(160,300))
			
			
			sound("eye.mp3")		
			
			
			rect=pygame.draw.rect(screen,(0,0,255),(160,720,400,100),5,5,5,5,5) #Round border for done button
			
			
			rect=pygame.draw.rect(screen,(0,0,255),(165,725,390,90)) # done button
			
			
			screen.blit(text,(280,735))
			
			
			
	#Exercise
		
		
	elif exercise==True:
		
		
		
		done=False
			
			
		#Stop after clicking the button
			
			
		if 160<mouse[0]<560 and 720<mouse[1]<820:
				
				
			exercise_time_min+= exercise_after_every_min
				
				
			pygame.mixer.music.stop()
				
			done=True
				
			exercise=False
				
				
			#Logging the Data in file exercise.txt
				
			with open("exercise.txt","a") as exercise_log:
					
				exercise_time_log=time.strftime("%a %d/%b/%Y %H:%M:%S")
					
					
				exercise_log.write("[")
					
				exercise_log.write(exercise_time_log)
					
					
				exercise_log.write("]")
					
				exercise_log.write("Exercise\n")
				
				
				continue
						
						
			
		else:
				
			#Running the program Playimg sound and displayimg exercise image
								
			screen.blit(exercise_image,(160,300))
				
				
			sound("exercise.mp3")		
				
				
			rect=pygame.draw.rect(screen,(0,0,255),(160,720,400,100),5,5,5,5,5) #Round border for done button
				
				
			rect=pygame.draw.rect(screen,(0,0,255),(165,725,390,90)) # done button
				
				
			screen.blit(text,(280,735))		
		
		
		


	
	#End
	
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			
			pygame.quit()
			
			quit()
			
	pygame.display.update()
	
