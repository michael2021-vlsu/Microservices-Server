from flask import Flask, request, jsonify
import threading
import time
import datetime

storage = [] 					#This is a storage variable. All incoming data will be stored here.
mutex = threading.Lock() 		#Mutex is needed in case 2 threads simultaneously want to change the "storage" variable

def storage_add(json): 			#Add to storage function
    mutex.acquire() 			#The beginning of a critical piece of code. Further, no more than one stream (request) can pass at the same time.
    storage.append(json) 		# Adding JSON to storage
    mutex.release() 			#The ending of a critical piece of code. Now another thread (request) can enter the critical part.

def storage_find(type, id):
    mutex.acquire()						#The beginning of a critical piece of code. Note that mutex is one by two functions. It turns out that the critical section is located in two functions at the same time. Thus, only one of the two functions can be executed at one time, moreover, only by one thread. Exclusive access.
    result = None 						#Declaring a variable and giving it a default value
    if type == 'null': 					#If the type is null, then it doesn't matter if the id is null. Any id will be considered meaningful.
        for item in storage: 			#Iterate through all the values in the store in search of one that satisfies the request.
            if item['visibleId'] and item['id'] == id:		 #If the id of the json element is designated as visible, check the requested id and the id of the json element.
                result = item 			#Assigning the result
                storage.remove(item) 	#Delete the found item from storage. It turns out a queue: from the end, elements arrive, from the beginning, they are removed.
                break; 					#We exit the cycle ahead of schedule. We have already found what we were looking for, there is no point in looking further.
    elif id == 'null': 					#Here the type can no longer be equal to null. But id can.
        for item in storage: 			#Iterate through all the values in the store in search of one that satisfies the request.
            if item['type'] == type: 	#Сheck the requested type and the type of the json element are same.
                result = item 			#Assigning the result
                storage.remove(item) 	#Delete the found item from storage. It turns out a queue: from the end, elements arrive, from the beginning, they are removed.
                break; 					#We exit the cycle ahead of schedule. We have already found what we were looking for, there is no point in looking further.
    else: 								#Here, both the type and id cannot be null. So, we are looking for both.
        for item in storage: 			#Iterate through all the values in the store in search of one that satisfies the request.
            if item['visibleId'] and item['type'] == type and item['id'] == id: 	#Based on the previous one, what do you think is going on here?
                result = item 			#Assigning the result
                storage.remove(item) 	#Delete the found item from storage. It turns out a queue: from the end, elements arrive, from the beginning, they are removed.
                break; 					#We exit the cycle ahead of schedule. We have already found what we were looking for, there is no point in looking further.
    mutex.release() 					#The ending of a critical piece of code. Now another thread (request) can enter the critical part.
    return result 						#Here we return the result. Well, or None. As you remember, the variable was originally assigned None.

app = Flask(__name__) 					#The Flask framework was used to run the server. He can do a lot of things, but now we are using the simplest.

@app.route('/5-semestr/compiler/get-job', methods=["GET"]) 	#The path to the get-job is specified here, as well as the request method (GET).
def jobGet():
    needType = request.values.get('type') 	#This is where you get the type parameter of the request
    if needType == None: 					#This condition checks if the type parameter is specified
        needType = 'null'					#And if NOT given, sets it to null. This is necessary so that the client can not insert the type or id parameters into the request, if one of them is not needed.
        
    needId = request.values.get('id') 		#This is where you get the id parameter of the request
    if needId == None:						#This condition checks if the type parameter is specified
        needId = 'null'						#And if NOT given, sets it to null. This is necessary so that the client can not insert the type or id parameters into the request, if one of them is not needed.
        
    result = None							#Set the default value for the result again. If during the search a suitable element is not found, the client will receive an error.
    end_time = start_time = datetime.datetime.now() #We get the current time to measure the waiting period for the result (25 seconds).
    while (end_time - start_time).seconds < 25: #And here we check if the 25 seconds allotted for the search have passed.
        result = storage_find(needType, needId) #Here is an attempt to find such an element that would satisfy the request
        if result != None: 					#Checking if the item was found.
            break; 							#If the item is found, we exit to give it to the client as soon as possible.
        time.sleep(1)						#We are waiting a bit to give time to other requests. This is necessary to reduce the load on the processor, since the processor is not busy with our business while waiting.
        end_time = datetime.datetime.now() 	#Get the current time to further verify if we have exceeded the 25 second wait limit.
        
    if result == None:						#Here we check if the desired element was found in the end.
        return '',408						#If not found, return error code 408.
    else:
        return jsonify(result)				#If found, translate it into a JSON text string and send it to the client.

@app.route('/5-semestr/compiler/post-job', methods=["POST"]) 	#The path to the post-job is specified here, as well as the request method (POST).
def jobPost():
    storage_add(request.get_json())				#Here the client has sent data to the server. The server needs to save them.
    return '',201								#The item was created successfully. Returning the success code.

if __name__ == '__main__':						#This is necessary to make sure that this script was launched independently, and not as part of another script.
    app.run(debug=False, host='0.0.0.0', port=8080) 	#Launching the Flask HTTP server
