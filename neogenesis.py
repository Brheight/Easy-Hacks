import dictnary

def find(end, start, names, email, li):
    if 'info' in email[:end]:
        if '.com' in email:
            last = email.index('.com')
            test_string = '{} {}'.format(email[end + 1:last], email)
            return test_string
    if 'enquiry' in email[:end]:
        if '.com' in email:
            last = email.index('.com')
            test_string = '{} {}'.format(email[end + 1:last], email)
            return test_string
    if 'sales' in email[:end]:
        if '.com' in email:
            last = email.index('.com')
            test_string = '{} {}'.format(email[end + 1:last], email)
            return test_string
    if 'admin' in email[:end]:
        if '.com' in email:
            last = email.index('.com')
            test_string = '{} {}'.format(email[end + 1:last], email)
            return test_string
    if '.' in email[:end]:
        test_string = email[:end]
        nval = -1
        while test_string[nval].isnumeric() == True:
            nval -= 1
        end = end + nval + 1
        point = email.index('.')
        name_string = '{} {} '.format(email[:point].capitalize(), email[point + 1:end].capitalize())    
        test_string = '{} {}'.format(name_string, email)
        return test_string
    for num in range(end):
        if end -start -1 < num:
            contact = '{} {}'.format(names, email)
            n = []
            for item in contact.split(' '):
                if item:
                    n.append(item)
            #print(n)
            contact = ' '.join(n)
            return contact
        for name in li:
            #print('email[{}:{}]'.format(start, end - num), email[start:end - num])
            if email[start:end - num] in name:
                #print(name)
                #print('names{}sd'.format(names))
                names = '{} {}'.format(names, name.capitalize())
                start = end-num +1
                if end -start > 2:
                    return find(end, start, names, email, li)
                contact = '{} {}'.format(names, email)
                #print('contact{}donwe'.format(contact))
                n = []
                for item in contact.split(' '):
                    if item:
                        n.append(item)
                #print(n)
                contact = ' '.join(n)
                return contact


#print(find(end, start, names, email))





def find_name(start, email):
	if '@' in email:
		email = email.lower()
		end = email.index('@')

		if email[:end].isalnum():
			test_string = email[:end]
			nval = -1
			if test_string[nval].isalpha():
				pass
			else:
				while test_string[nval].isnumeric() == True:
					nval -= 1
				end = end + nval + 1
				return find(end, start, names, email, li)
		else:
			return find(end, start, names, email, li)

final_list = []


def magnus(emails):
    final_list = []
    from sys import exit
    import sys
    sys.setrecursionlimit(20000)
    #names = []
    start = 0
    li = dictnary.names
    emails = emails.split()
    names = ''
    for email in emails:
        try:
            end = email.index('@')
            final_item = find(end, start, names, email, li)
            print(final_item)
            v = final_item.split(' ')
            #print(v)
            final_item=' '.join(v)
            final_list.append(final_item)
        except:
            pass
    #print('neo listP{}sdj'.format(final_list))
    return final_list