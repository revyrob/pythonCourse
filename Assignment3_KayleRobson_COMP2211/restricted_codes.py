# Function for restricted company codes in list
# Restricted products in security level R in countries with a country code
# 2000 or higher
# This products are under heading 'Invalid Restricted Code(s)'
# I made the 'security' in in upper so it was easier to catch

def get_restricted(valid):
    restricted = []
    for d in valid:
        security = d[9:10]
        security = security.upper()
        country_restricted = d[3:4]
        if (security == 'R') and (int(country_restricted) >= 2):
            restricted.append(d)
            
    for c in restricted:
        if c in valid:
            valid.remove(c)
    return restricted
