import json
from pprint import pprint

def main():
    # obj.data.children[i].url

    file_arr = list()

    liked_1 = open('liked-page1.json')
    file_arr.append((liked_1, 1))
    liked_2 = open('liked-page2.json')
    file_arr.append((liked_2, 1))
    disliked_1 = open('disliked-page1.json')
    file_arr.append((disliked_1, 0))
    disliked_2 = open('disliked-page2.json')
    file_arr.append((disliked_2, 0))


    liked_output = open('liked.json', 'w+')
    disliked_output = open('disliked.json', 'w+')
    liked_list = list()
    disliked_list = list()

    for i in range(len(file_arr)):
        data = json.load(file_arr[i][0])


        for j in range(len(data["data"]["children"])):
            if file_arr[i][1]:
                # Write to the liked file
                pprint(data["data"]["children"][j])
                liked_list.append(data["data"]["children"][j]["data"]["url"])
            else:
                # Write to the disliked file
                disliked_list.append(data["data"]["children"][j]["data"]["url"])

    # writing to a file
    liked_output = open('liked.json', 'w+')
    disliked_output = open('disliked.json', 'w+')

    liked_output.write(json.dumps(liked_list))
    disliked_output.write(json.dumps(disliked_list))




if __name__ == '__main__':
    main()
