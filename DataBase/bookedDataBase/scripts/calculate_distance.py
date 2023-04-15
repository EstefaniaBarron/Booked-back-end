import pgeocode


def run(*args):
    zip_code_1 = args[0]
    zip_code_2 = args[1]
    dist = pgeocode.GeoDistance('us')
    miles = to_miles(dist.query_postal_code(zip_code_1, zip_code_2))
    print(miles)


def to_miles(kms):
    return kms*0.621371
