phonebook_dict = {
    'Alice' : '703-493-1834',
    'Bob' : '857-384-1234',
    'Elizabeth' : '484-584-2923'
}

print phonebook_dict['Elizabeth']

phonebook_dict["Kareem"] = '404-332-2229'
print phonebook_dict["Kareem"]

#delete alice phone entry
del phonebook_dict['Alice']
print phonebook_dict

#changeBob'sphonenumber
phonebook_dict['Bob'] = '404-444-4444'
print phonebook_dict['Bob']

print phonebook_dict
