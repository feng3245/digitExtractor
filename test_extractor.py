from digitpkg.digitextractor import extract_from_image
from digitpkg.digitUtil import getSortedDictionaryImages
import cv2
result = extract_from_image('amtsidebar.png', 28)
assert len(result) == 6
assert all([len(result[row]) == 3 for row in result])
assert all(all([(len(result[row][c]) == 28 and len(result[row][c][0])) == 28 for c in result[row]]) for row in result)

cv2.imwrite('Extract28.png', list(list(result.values())[0].values())[0])
sortedDict = getSortedDictionaryImages({2:{2:2, 1:1},1:{2:1, 1:2}}, 0)
assert len(sortedDict) == 2
issorted = [(sortedDict[i] >= sortedDict[i+1]) for i in range(len(sortedDict)-1)]
assert all(issorted)
result2 = extract_from_image('testChart2bar.png', 28)
assert len(result2) == 5
assert all([len(result2[row]) == 2 for row in result2])
