class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        cell = ''
        div = columnNumber
        while div>26:
            rem = div%26
            cell = chr(64+rem)+cell
            div = div//26
        cell = chr(64+div)+cell
        return cell