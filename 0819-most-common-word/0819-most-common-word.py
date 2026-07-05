class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        banned_set = set(banned)
        normalized_str = re.sub(r"[!?',;.]", " ", paragraph).lower()
        words = normalized_str.split()
        valid_words = [word for word in words if word not in banned_set]
        counts = Counter(valid_words)
        return counts.most_common(1)[0][0]