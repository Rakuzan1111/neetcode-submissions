class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for s in strs:
            l = str(len(s))
            encoded += (l + "`" + s)
        print(encoded)
        return encoded

            

        
    def decode(self, s: str) -> List[str]:
        ls = []
        i = 0

        nums = "1234567890"
        
        while i < len(s) - 1:
            num_of_chars = ""
            while s[i] != '`':
                num_of_chars += s[i]
                i += 1
                print(i)

            num_of_chars = int(num_of_chars)
            print(s[i+1 : i+1+num_of_chars])
            ls.append(s[i+1 : i+1+num_of_chars])
            i = i + 1 + num_of_chars
        return ls

            

            
