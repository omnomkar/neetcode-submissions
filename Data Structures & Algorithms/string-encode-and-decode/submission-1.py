class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_string = ''
        for s in strs:
            encoded_string += (f"{len(s)}#{s}")
        return encoded_string


    def decode(self, s: str) -> List[str]:
        result = []
        start = 0
        while start < len(s):
            end = start
            while s[end] != "#":
                end += 1
            length_number = int(s[start:end])
            result.append(s[end + 1:end + 1 + length_number])
            start = end + 1 + length_number
        return result
