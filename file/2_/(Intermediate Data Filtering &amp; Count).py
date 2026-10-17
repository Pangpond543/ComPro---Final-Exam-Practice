def process_system_log(input_file):
    
    result =  {"[INFO]" : 0, "[WARNING]" : 0, "[ERROR]" : 0}
    with open(input_file, "r") as f1, open("error_only.txt", "w") as f2:
        
        for data in f1:
            f_data = data.strip()
            
            if "[ERROR]" in f_data:
                f2.write(data)
                result["[ERROR]"] += 1
                
            if "[INFO]" in f_data:
                result["[INFO]"] += 1
                
            if "[WARNING]" in f_data:
                result["[WARNING]"] += 1
    print(result)
        
process_system_log("system_log.txt")