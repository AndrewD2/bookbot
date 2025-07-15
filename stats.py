def get_num_words(text):
    words = text.split()
    return len(words)
  
def get_chars_dict(text):
    chars = {}
    
    for c in text:
        lowered = c.lower()

        if lowered in chars:
            chars[lowered] += 1
        else:
            chars[lowered] = 1
    return chars

def sort_on(items):
    return items["num"]

def make_report(dict):
    report_list = []
    for e in dict:
        count = dict[e]
        #print(e)
        new_entry = {"char":e, "num": count}
        #print(f"new entry: {new_entry}")
        report_list.append(new_entry)

        report_list.sort(reverse=True, key=sort_on)

    for e in report_list:
       if e["char"].isalpha():
           print(f"{e['char']}: {e['num']}")
