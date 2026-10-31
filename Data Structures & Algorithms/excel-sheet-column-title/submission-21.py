class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        cell = ''
        while columnNumber>26:
            cell = chr(64+(columnNumber%26))+cell
            columnNumber = columnNumber//26
        cell = chr(64+columnNumber)+cell
        return cell