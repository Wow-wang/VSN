import random

if __name__ == '__main__':
    # max = pow(2, 10)-1
    max = 1000
    min = 0
    num_of_file = 1 # 1000个文件 10K

    # desktop_path = "/home/node2/yangxu/new/rangeStreaming/dataset_40K/"
    desktop_path = "/home/node2/yangxu/new/newfile/"

    for id in range(num_of_file):
        count = 32000 # 每个文件10条数据
        filename = desktop_path+str(id+1)
        f = open(filename, 'w')
        for i in range(count-1):
            num = random.randint(min,max)
            f.write(str(num) + ",")
        num = random.randint(min,max)
        f.write(str(num))
        f.close()
