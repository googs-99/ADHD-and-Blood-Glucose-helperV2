from datetime import datetime
import time
now = datetime.now()
tasks = [
    ["Study","POD Break"]
    []
    []
    ["Wake up","Input New Tasks"]
    ["f'I am working and counting the time{now}'"]
    ]
school_tasks = tasks[0]
chore_tasks = tasks[1]
hobby_tasks = tasks[2]
routine_tasks = tasks[3]
extras_for_debugging = tasks[4]

def scheduling():
    global task_list1
    while True:
        now = datetime.now()
        
        if now.hour == 7 and now.minute == 30:
            print(routine_tasks[1])
            while True:
                 school_tasks.append(input("Input new school tasks, or \"Q\" to quit."))
                 if tasks == "Q":
                     break
            yield school_tasks
            
            
                    
              
            
            
        if now.hour in range(8,17):
            if school_tasks:
                
                yield school_tasks
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
    
    
        
            
            
        
        
