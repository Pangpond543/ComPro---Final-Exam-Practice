def analyze_user_activity(log_file_path: str) -> dict:
    user = set()
    action_ = {}
    active_ = {}
    total = 0
    with open(log_file_path, "r") as data:
        for i in data:
            split_ = i.strip().split(" ")
            if len(split_) != 4:
                continue
            
            user.add(split_[1])
            
            action_[split_[2]] = action_.get(split_[2], 0) + 1
            active_[split_[1]] = active_.get(split_[1], 0) + int(split_[3])
            
            try:
                check_num = int(split_[3])
            except ValueError:
                continue
            
            if split_[2] == "login":
                total += check_num
        
        
        login_check = action_.get("login", 0)
        most = max(active_, key=active_.get) if active_ else None
        average = total/action_["login"] if login_check >= 0 else 0.0
        
        return {
            "total_users": len(user),
            "action_counts": action_,
            "most_active_user": most,
            "average_session_time": average
        }

result = analyze_user_activity("activity.log")
print(result)
    
# {
#   "total_users": 2,
#   "action_counts": {"login": 2, "view": 2, "submit": 1, "logout": 2},
#   "most_active_user": "u002",
#   "average_session_time": 160.0
# }