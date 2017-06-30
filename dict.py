
student_1 = {
  'name': 'priyanka',
  'salutation': 'Ms.',
  'age': 20,
  'rating': 4.0,
  'is_online': True
}

student_2 = {
  'name': 'priya',
  'salutation': 'Ms.',
  'age': 18,
  'rating': 3.0,
  'is_online': False
}
student_3 = {
  'name': 'pri',
  'salutation': 'Ms.',
  'age': 15,
  'rating': 3.0,
  'is_online': True
}

students = [student_1, student_2, student_3]
for student in students:
  print ( "Name- %s. %s of age %d having rating %.1f." % (student['salutation'], student['name'],student['age'],student['rating']))

