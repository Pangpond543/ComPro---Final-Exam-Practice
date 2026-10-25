def analyze_skills(job_skills, candidate_skills):
    
    job_set = set(job_skills)
    candidate = set(candidate_skills)
    
    matchde_ = candidate.intersection(job_set)
    missing_ = job_set.difference(candidate)
    extra_ = candidate.difference(job_set)
    bool_ = candidate >= job_set
    
    return {
        "matchde" : matchde_,
        "missing" : missing_,
        "extra" : extra_,
        "is_qualified" : bool_
    }

job = ["Python", "SQL", "Git", "Docker"] 
candidate = ["Python", "SQL", "HTML", "CSS"] 
print(analyze_skills(job, candidate)) 
# output = { 
        # 'matched': {'Python', 'SQL'},
        # 'missing': {'Git', 'Docker'}, 
        # 'extra': {'HTML', 'CSS'}, 
        # 'is_qualified': False # 
# }