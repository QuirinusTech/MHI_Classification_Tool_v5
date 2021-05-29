def listedtier(item):
  for substance in listedSubstances:
    if int(item["chemid"]) == substance["chemid"] or substance['desc'] == item['category']:
      return float(item["qty"]) / int(substance["tier1"])