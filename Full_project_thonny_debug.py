from datetime import datetime
import time

task_list1 = ["Wake up", "Study", "Input New Tasks", "POD Break", "I am working and counting the time{now}"]
def scheduling():
    global task_list1
    while True:
        now = datetime.now()
        
        if now.hour == 7 and now.minute == 30:
            task_list1 = []
            
            while True:
                 tasks = input("Input new school tasks, or \"Q\" to quit.")
                 if tasks == "Q":
                     break
                    
                 task_list1.append(tasks)
            yield task_list1
            
            
        if now.hour in range(8,17):
            if task_list1:
                yield task_list1[1]
            if now.minute == 25:
                yield task_list1[3]
            elif now.minute == 35:
                yield task_list[1]
            elif now.minute % 2:
                yield task_list1[4]
        
        time.sleep(60)
        
 
                

if __name__ == "__main__":
    
    for tasks in scheduling():
        print(tasks)
    
    
        
            
            
        
        
