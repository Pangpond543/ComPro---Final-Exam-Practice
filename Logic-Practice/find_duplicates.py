def find_duplicates(items: list) -> list:
    dict_ = {}
    for i in items :
        dict_[i] = dict_.get(i, 0) + 1
        
    result = []
    for i, v in dict_.items() :
        if v >= 2 :
            result.append(i)
    return result

print(find_duplicates([1, 2, 3, 2, 4, 5, 1, 6]))
# -> [1, 2]   (เรียงตามลำดับที่เจอครั้งแรก, ไม่เอาตัวซ้ำของคำตอบเอง)