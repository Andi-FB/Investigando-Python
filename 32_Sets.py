"""
The aim of this exercise is to use a Set.
Create two sets of students, one for those who took an exam and one for those
that submitted a project. You can use simple strings to represent the students, for
example:

# Set up sets
exam = {'Andrew', 'Kirsty', 'Beth', 'Emily', 'Sue'}
project = {'Kirsty', 'Emily', 'Ian', 'Stuart'}
# Output the basic sets
print('exam:', exam)
print('project:', project)


Using these sets answer the following questions:
• Which students took both the exam and submitted a project?
• Which students only took the exam?
• Which students only submitted the project?
• List all students who took either (or both) of the exam and the project.
• List all students who took either (but not both) of the exam and the project.
"""

# Set up sets
exam = {'Andrew', 'Kirsty', 'Beth', 'Emily', 'Sue'}
project = {'Kirsty', 'Emily', 'Ian', 'Stuart'}
# Output the basic sets
print('exam:', exam)
print('project:', project)
print('Took both: {}'.format(exam.intersection(project)))
print('Only took exam: {}'.format(exam.difference(project)))
print('Only submitted project: {}'.format(project.difference(exam)))
print('All students who took exam or project or both: {}'.format(exam | project))
print('All students who took either but nor both: {}'.format(exam.symmetric_difference(project)))
