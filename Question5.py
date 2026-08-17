def validate_pass(pass_code):
    if pass_code == "":
        return "no pass"
        
    if len(pass_code) < 5:
        return "too short"
        
    if pass_code[0] != "P":
        return "invalid prefix"
        
    if " " in pass_code:
        return "invalid format"
        
    return "valid"

print(validate_pass(""))  
print(validate_pass("P12"))  
print(validate_pass("w12345")) 
print(validate_pass("P123 456"))        
print(validate_pass("Precious"))        
