def name_converter(name):
    return name.replace(" ", "%20")

def get_synopsis(option, recs):
    for rec in recs:
        if rec["option"] == option:
            return rec["synopsis"]
    return None
