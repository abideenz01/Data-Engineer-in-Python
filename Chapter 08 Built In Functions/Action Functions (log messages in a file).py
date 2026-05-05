#Task
#Stores application log messages in a a file whenever an event occurs
def write_log(message):
    with open(r"C:\Users\LENOVO\Desktop\Message log.txt","a") as file: #open the file and append message at the end of file
        file.write(message + "\n")
#write_log("App started")
#write_log("User Logged in")
write_log("App closed")