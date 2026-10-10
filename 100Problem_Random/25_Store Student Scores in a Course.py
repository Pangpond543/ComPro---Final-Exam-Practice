def store_student_scores(student_data: list[tuple[str, str, float]]) -> dict[str, dict[str, float]]: 
    result = {}
    for i in range(len(student_data)):
        result[student_data[i][0]] = {}
        result[student_data[i][0]]["name"] = student_data[i][1]
        result[student_data[i][0]]["score"] = student_data[i][2]
    return result

input_ = [ ("123456", "Alice", 85.5), ("654321", "Bob", 92.0), ("112233", "Charlie", 78.0) ]

print(store_student_scores(input_))

# { 
    # "123456": {"name": "Alice", "score": 85.5}, 
    # "654321": {"name": "Bob", "score": 92.0}, 
    # "112233": {"name": "Charlie", "score": 78.0}
# }