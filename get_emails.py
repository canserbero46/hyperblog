import re, json

re_obj = re.compile(r"<(\S+@\S+?)>")
emails_dict = dict()

with open("mails.txt", "rt", encoding="utf-8") as file:
    for mail in re_obj.findall(file.read()):
        if mail not in emails_dict.keys():
            emails_dict[mail] = 1
        else:
             emails_dict[mail] += 1

emails_dict = dict(sorted(emails_dict.items(), key=lambda x:x[1], reverse=True))
with open("result.txt", "wt", encoding="utf-8") as file:
    file.write(json.dumps(emails_dict, indent=4))
        
