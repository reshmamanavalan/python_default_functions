#list
li = [44,2,"aish",[2,3,4],'g']
print(li)
li.extend("sai")
print(li)
li.append("sai")
print(li)
li.insert(1,1)
print(li)
li.pop(2)
print(li)
li.count(1)
print(li)
print(li.copy())

#dict
dit1={"id":1,"name":"reshu","age":80,"city":"karur"}
print(dit1)
print(dit1.values())
print(dit1.get("id"))
print(dit1.keys())
print(dit1.pop("id"))
dit1.update({"lang":"tamil"})
print(dit1)

#tuple
tup1=(1,"aish","karur",34.8,"aish")
print(tup1)
print(tup1.count("aish"))
print(tup1.index("aish"))

#set
set1={"reshu","padma","arun",34,56,76.8}
print(set1)
set1.add("hh")
print(set1)
set2={"reshu","padma","arun",34,56,"fruit",7}
w=set1.isdisjoint(set2)
print(w)
h=set2.issubset(set1)
print(h)
h=set1.issuperset(set2)
print(h)
g=set1.symmetric_difference(set2)
print(g)

#string
string1="hello,good morning have a nice day!SPREAD positivity"
print(string1)
string2=string1.replace("hello","hii")
print(string2)
cd=string1.casefold()
print(cd)
print(string1.isalpha())
print(string1.partition("morning"))
my_dict = {97:103}
print(string1.translate(my_dict))
