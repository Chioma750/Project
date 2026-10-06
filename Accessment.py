import copy

#def passing_scores(scores):
    #passed = []
    #for score in scores:
     #   if score >= 50:
    #        passed.append(score)
   #     elif score == []:
  #          return []
 #   return passed
#print (passing_scores([49, 50, 80, 65]))
#assert passing_scores([50]) == [50]
#assert passing_scores([]) == []
#assert passing_scores([85]) == [85]


def add_tag(profile, tag):
    updated = profile.copy()
    updated["tags"] = profile["tags"] + [tag]
    return updated
original = {"name": "Ada", "tags": ["python"]}
changed = add_tag (original, "testing")
assert original["tags"] == ["python"]
assert changed["tags"] == ["python", "testing"]
changed["tags"].append("developer")
#assert original["tags"] == ["python"]
