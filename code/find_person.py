# -*- coding: utf-8 -*-


def find_person(dict_users, strU):
     if strU in dict_users.keys():
        return dict_users[strU]
     else:
        return 'Not Found'
if __name__ == "__main__":
     dict_users = {"xiaoyun":"88888", "xiaohong":"5555555", "xiaoteng":"11111","xiaoyi":"12341234","xiaoyang":"121212"}
     strU =  input()
     print(find_person(dict_users, strU))