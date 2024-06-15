a = input()
# a = 'IMG_20230430_092422111.jpg'
# IMG_20120427_1433383789.jpg

aa = ''.join([x for x in a if x in '0123456789']) + '.jpg'

# print(aa)

months = [None, 'Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']

print(f'{aa[:4]}_{months[int(aa[4:6])]}_{aa[6:8]}_PYTHON_CONFERENCE.jpg')




