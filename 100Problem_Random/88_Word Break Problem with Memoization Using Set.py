def word_break(s: str, word_set: set) -> bool:
    memo = {}
    
    def word_2(after):
        if after in memo:
            return memo[after]
        # print("คำนวณ:", after)
        
        if after == "":                          # Base Case
            return True

        for i in range(1, len(after) + 1):
            if after[:i] in word_set and word_2(after[i:]):    # ชิ้นแรกเป็นคำ และส่วนที่เหลือตัดได้
                memo[after] = True
                return True
            
        memo[after] = False
        return False
    
    return word_2(s)
    
# s = "leetcode"
# word_set = {"leet", "code"}
# print(word_break(s, word_set))


s = "applepenapple"
word_set = {"apple", "pen"}
print(word_break(s, word_set))

s = "catsandog"
word_set = {"cats", "dog", "sand", "and", "cat"}
print(word_break(s, word_set))

