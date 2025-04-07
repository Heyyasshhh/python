products ={"milk":50, "coffee":80, "bread":28}

# 1) Convert al items price INR to USD and show updated items with price
print({k:v*0.012 for k,v in products.items()})

# 2) Show only those itmes whose price greater than 30
print({k:v*0.012 for k,v in products.items() if v>30})

# 3) Show only coffee details
print({k:v*0.012 for k,v in products.items() if k=="coffee"})