class Solution:
    def mostCommonWord(self, paragraph: str, banned: list[str]) -> str:
        for i in "!?';.,":
            paragraph = paragraph.replace(i, ' ')
        banned = set(banned)
        words = [word.lower() for word in paragraph.split()]

        hashmap = {}

        for word in words:
            if word not in banned:
                if not hashmap.get(word):
                    hashmap[word] = 0
                hashmap[word] += 1
        
        answer = ('', 0)

        for word, freq in hashmap.items():
            if answer[1] < freq:
                answer = (word, freq)

        return answer[0]
