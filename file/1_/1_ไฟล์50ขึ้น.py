def scores():
    with open("student_scores.txt", "r") as fel, \
        open("score_summary.txt", "w") as fel2:
        
        while fel:
            data = fel.readline().strip()
            if data == "":
                break
            
            spit = data.split(",")
            if int(spit[1]) >= 50:
                fel2.write(f"{data}\n")
            
scores()
    