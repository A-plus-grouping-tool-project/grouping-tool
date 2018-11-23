import csv

FIELD_NAMES = ['group_id', 'id', 'username', 'student_id', 'email']

def create_csv(filename = 'groups'):
    try:
        #group, id, name, student_id, email
        with open(f'{filename}.csv', 'w') as groupsfile:
            group_writer = csv.DictWriter(groupsfile,fieldnames=FIELD_NAMES)
            group_writer.writeheader()
    except IOError:
        print('CSV-writer IO-error')

def export_to_csv(student_object, filename = 'groups'):
    try:
        #group, id, name, student_id, email
        with open(f'{filename}.csv', 'a') as groupsfile:
            group_writer = csv.DictWriter(groupsfile,fieldnames=FIELD_NAMES)
            student_object = format_student_data(student_object)
            group_writer.writerow(student_object)
    except IOError:
        print('CSV-writer IO-error')


def format_student_data(student_object):
    formatted_student = {}
    formatted_student['group_id'] = student_object['group_id']
    formatted_student['id'] = student_object['id']
    formatted_student['username'] = student_object['username']
    formatted_student['student_id'] = student_object['student_id']
    formatted_student['email'] = student_object['email']
    return formatted_student
