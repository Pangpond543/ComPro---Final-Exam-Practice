def analyze_event_participants(events):
    
    all_set = [set(con) for con in events]
        
    all_events_ = set.intersection(*all_set)
    
    counts = {}
    for i in events:
        for person in i:
            counts[person] = counts.get(person, 0)+1
            
    count_only = {k for k, v in counts.items() if v == 1}
    
    total = len(set.union(*all_set))
    
    return {
            'all_events': all_events_,
            'only_one_event': count_only,
            'total_unique': total
        }

events = [
    ["Alice", "Bob", "Charlie"],      # Event 1
    ["Alice", "Charlie", "David"],    # Event 2
    ["Alice", "Eve", "Charlie"]       # Event 3
]

print(analyze_event_participants(events))
# output = {
#     'all_events': {'Alice', 'Charlie'},
#     'only_one_event': {'Bob', 'David', 'Eve'},
#     'total_unique': 5
# }