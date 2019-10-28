import os
import re
import sys
#This gives filenames in current directory
directory_of_txt_files = 'Put Text file here'
filenames_list = os.listdir(directory_of_txt_files)
#print filenames_list
#print '\n'


filename_str=''.join(filenames_list)
Foldernames_without_directory=re.split('.txt',filename_str)[:-1]
#print Foldernames_without_directory
compacted_subject_name = [''.join(i.split()) for i in Foldernames_without_directory]
#print compacted_subject_name
qn_compacted_subject_name = [("qn_"+i)	for i in compacted_subject_name	]
#print qn_compacted_subject_name

filenames_with_directory = [(directory_of_txt_files+ '/'+filename) for filename in filenames_list]
#print filenames_with_directory
#print '\n'


def question_answer_py(file_name_with_directory,subject_compacted_name):

	# opening Building materials.txt
	with open(file_name_with_directory, 'r') as f:
	    # f.read extracts text as string and puts to line
	    lines = f.read()

	    #re.findall finds find ABCD in file and outputs A or B or C or D and puts to list answer since [ABCD] is put in ()
	answer = re.findall('Answer: Option ([ABCD])', lines)

	    # string is splitted when it finds Answer: Option [ABCD] and puts to Q_without_answer
	Q_without_answer = re.split('Answer: Option [ABCD]', lines)

	# converts list into string
	temp_string = ''.join(Q_without_answer)

	# string is splitted when it finds Question No. \d+ and puts to Q_without_que_ans
	#converted list constains first item at index 0 jpts so getting from item at index 1
	question =re.split('Question No. \d+', temp_string)[1:]

	fn = open('question_answer.py','a')
	sys.stdout = fn
	#prints question = question in list form
	print("question_"+subject_compacted_name+'=', question)
	#print "print (len("+"question_"+subject_compacted_line+")"+")"

	#prints answer = answer in list form
	print("answer_"+subject_compacted_name+'=', answer)
	#print "print (len("+"answer_"+subject_compacted_line+")"+")"

	fn.close()

open('question_answer.py','w').close()

for i,j in zip(filenames_with_directory,compacted_subject_name):
	question_answer_py(i,j)


#file to paste in main.py and Test.kv file

sys.stdout = open("2. copyPaste.py",'w')
print('#paste in #paste from 2.copyPaste.py import')
print('if os.path.exists("'+"qn_Favourite_questions"+'.py"'+'):')
print('    pass')
print('else:')
print('    with open("'+"qn_Favourite_questions"+'.py","w") as f:')
print('        f.write("'+"qn_Favourite_questions"+'=0")')
print('from', "qn_Favourite_questions", 'import',"qn_Favourite_questions")


for i in qn_compacted_subject_name:
	print('if os.path.exists("'+i+'.py"'+'):')
	print('    pass')
	print('else:')
	print('    with open("'+i+'.py","w") as f:')
	print('        f.write("'+i+'=0")')
	print('from', i, 'import',i)

print('\n\n\n\n')



print("#paste this in main file under def subject_click(self,*args): of main.py where copy is written in comment but make sure indendation is perfect")
print("if self.spnr_subject.text =="+'"'+"Favourite questions"+'"'+':')
print("    question=questions_fav")
print("    answer=answers_fav")
print("    self.btn_fav.text="+'"'+"Favourite"+'"')
print("    self.lbl_qn.text= str(qn_Favourite_questions)")
#print "    self.lbl_q.text=question[qn_Favourite_questions]"
for i,j,k in zip(Foldernames_without_directory,compacted_subject_name,qn_compacted_subject_name):
	print("if self.spnr_subject.text =="+'"'+str(i)+'":')
	print("    question=question_"+j)
	print("    answer=answer_"+j)
	print("    self.btn_fav.text="+'"'+"Favourite"+'"')
	print("    self.lbl_qn.text="+"str("+k+")")
	#print "    self.lbl_q.text=question["+k+"-1"+"]"

print("else:\n    pass")

#file to paste in kivy file
print("#file to paste in Test.ky file under")
print('# Spinner:')
print('#    id: spinner_subject ')
print('#    values: ')
print(["Favourite questions"]+Foldernames_without_directory)

print('\n\n\n\n')
print('#file to paste in main.py under function save_question_number_to_file')

print("if self.spnr_subject.text =="+'"'+"Favourite questions"+'"'+':')
print('    sys.stdout = open("'+"qn_Favourite_questions"+'.py","w")')
print('    print ("'+"qn_Favourite_questions",'=','",','self.lbl_qn.text',')')
print('    open("'+"qn_Favourite_questions"+'.py").close()')
for i,j in zip(Foldernames_without_directory, qn_compacted_subject_name):

	print("if self.spnr_subject.text =="+'"'+str(i)+'":')
	print('    sys.stdout = open("'+j+'.py","w")')
	print('    print('+'"'+j,'=','",','self.lbl_qn.text',')')
	print('    open("'+j+'.py").close()')

open("2. copyPaste.py").close

