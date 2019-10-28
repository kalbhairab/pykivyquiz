# question loaded from another file
from question_answer import *
import os



#paste in #paste from 2.copyPaste.py import
if os.path.exists("qn_Favourite_questions.py"):
    pass
else:
    with open("qn_Favourite_questions.py","w") as f:
        f.write("qn_Favourite_questions=0")
from qn_Favourite_questions import qn_Favourite_questions
if os.path.exists("qn_BuildingConstruction.py"):
    pass
else:
    with open("qn_BuildingConstruction.py","w") as f:
        f.write("qn_BuildingConstruction=0")
from qn_BuildingConstruction import qn_BuildingConstruction
if os.path.exists("qn_BuildingMaterials.py"):
    pass
else:
    with open("qn_BuildingMaterials.py","w") as f:
        f.write("qn_BuildingMaterials=0")
from qn_BuildingMaterials import qn_BuildingMaterials
if os.path.exists("qn_ConcreteTechnologyandDesign.py"):
    pass
else:
    with open("qn_ConcreteTechnologyandDesign.py","w") as f:
        f.write("qn_ConcreteTechnologyandDesign=0")
from qn_ConcreteTechnologyandDesign import qn_ConcreteTechnologyandDesign
if os.path.exists("qn_Cpm.py"):
    pass
else:
    with open("qn_Cpm.py","w") as f:
        f.write("qn_Cpm=0")
from qn_Cpm import qn_Cpm
if os.path.exists("qn_DesignofMasonryStructures.py"):
    pass
else:
    with open("qn_DesignofMasonryStructures.py","w") as f:
        f.write("qn_DesignofMasonryStructures=0")
from qn_DesignofMasonryStructures import qn_DesignofMasonryStructures
if os.path.exists("qn_DesignofSteelStructures.py"):
    pass
else:
    with open("qn_DesignofSteelStructures.py","w") as f:
        f.write("qn_DesignofSteelStructures=0")
from qn_DesignofSteelStructures import qn_DesignofSteelStructures
if os.path.exists("qn_EstimatingandCosting.py"):
    pass
else:
    with open("qn_EstimatingandCosting.py","w") as f:
        f.write("qn_EstimatingandCosting=0")
from qn_EstimatingandCosting import qn_EstimatingandCosting
if os.path.exists("qn_HighwayEngineering.py"):
    pass
else:
    with open("qn_HighwayEngineering.py","w") as f:
        f.write("qn_HighwayEngineering=0")
from qn_HighwayEngineering import qn_HighwayEngineering
if os.path.exists("qn_IrrigationEngineering.py"):
    pass
else:
    with open("qn_IrrigationEngineering.py","w") as f:
        f.write("qn_IrrigationEngineering=0")
from qn_IrrigationEngineering import qn_IrrigationEngineering
if os.path.exists("qn_SoilMechanicsandFoundationEngineering.py"):
    pass
else:
    with open("qn_SoilMechanicsandFoundationEngineering.py","w") as f:
        f.write("qn_SoilMechanicsandFoundationEngineering=0")
from qn_SoilMechanicsandFoundationEngineering import qn_SoilMechanicsandFoundationEngineering
if os.path.exists("qn_StrengthofMaterials.py"):
    pass
else:
    with open("qn_StrengthofMaterials.py","w") as f:
        f.write("qn_StrengthofMaterials=0")
from qn_StrengthofMaterials import qn_StrengthofMaterials
if os.path.exists("qn_StructuralAnalysis.py"):
    pass
else:
    with open("qn_StructuralAnalysis.py","w") as f:
        f.write("qn_StructuralAnalysis=0")
from qn_StructuralAnalysis import qn_StructuralAnalysis
if os.path.exists("qn_TheoryofStructures.py"):
    pass
else:
    with open("qn_TheoryofStructures.py","w") as f:
        f.write("qn_TheoryofStructures=0")
from qn_TheoryofStructures import qn_TheoryofStructures





writepath = "favourite_questions_answers.py"
if os.path.exists(writepath):
    pass
else:
    with open(writepath, "w") as f:
        f.write("questions_fav=[]\nanswers_fav=[]")

# this is done so as to make a file so that import works
from favourite_questions_answers import answers_fav, questions_fav
from kivy.app import App
# box layout is imported
from kivy.uix.boxlayout import BoxLayout
from kivy.core.window import Window
import sys

# size of window as my mobile. Comment this to disable this
Window.size = (340, 550)
set_size = 0
question = []
answer = []
favourite_subject = []
# question and answer are in list format
# question = ["what is the color of apple \n A. red \n B. orange \n C.sky \n D. dark",
#           "what is the color of milk \n A. red \n B. white \n C. orange \n D. green"]
# answer = ["A", "B"]


# QuizApp class calls QuizApp from Test.kv and it inherints from boxlayout
class QuizApp(BoxLayout):


    def save_question_number_to_file(self):
        if self.spnr_subject.text =="Favourite questions":
            sys.stdout = open("qn_Favourite_questions.py","w")
            print ("qn_Favourite_questions = ", self.lbl_qn.text )
            open("qn_Favourite_questions.py").close()
        if self.spnr_subject.text =="Building Construction":
            sys.stdout = open("qn_BuildingConstruction.py","w")
            print("qn_BuildingConstruction = ", self.lbl_qn.text )
            open("qn_BuildingConstruction.py").close()
        if self.spnr_subject.text =="Building Materials":
            sys.stdout = open("qn_BuildingMaterials.py","w")
            print("qn_BuildingMaterials = ", self.lbl_qn.text )
            open("qn_BuildingMaterials.py").close()
        if self.spnr_subject.text =="Concrete Technology and Design":
            sys.stdout = open("qn_ConcreteTechnologyandDesign.py","w")
            print("qn_ConcreteTechnologyandDesign = ", self.lbl_qn.text )
            open("qn_ConcreteTechnologyandDesign.py").close()
        if self.spnr_subject.text =="Cpm":
            sys.stdout = open("qn_Cpm.py","w")
            print("qn_Cpm = ", self.lbl_qn.text )
            open("qn_Cpm.py").close()
        if self.spnr_subject.text =="Design of Masonry Structures":
            sys.stdout = open("qn_DesignofMasonryStructures.py","w")
            print("qn_DesignofMasonryStructures = ", self.lbl_qn.text )
            open("qn_DesignofMasonryStructures.py").close()
        if self.spnr_subject.text =="Design of Steel Structures":
            sys.stdout = open("qn_DesignofSteelStructures.py","w")
            print("qn_DesignofSteelStructures = ", self.lbl_qn.text )
            open("qn_DesignofSteelStructures.py").close()
        if self.spnr_subject.text =="Estimating and Costing":
            sys.stdout = open("qn_EstimatingandCosting.py","w")
            print("qn_EstimatingandCosting = ", self.lbl_qn.text )
            open("qn_EstimatingandCosting.py").close()
        if self.spnr_subject.text =="Highway Engineering":
            sys.stdout = open("qn_HighwayEngineering.py","w")
            print("qn_HighwayEngineering = ", self.lbl_qn.text )
            open("qn_HighwayEngineering.py").close()
        if self.spnr_subject.text =="Irrigation Engineering":
            sys.stdout = open("qn_IrrigationEngineering.py","w")
            print("qn_IrrigationEngineering = ", self.lbl_qn.text )
            open("qn_IrrigationEngineering.py").close()
        if self.spnr_subject.text =="Soil Mechanics and Foundation Engineering":
            sys.stdout = open("qn_SoilMechanicsandFoundationEngineering.py","w")
            print("qn_SoilMechanicsandFoundationEngineering = ", self.lbl_qn.text )
            open("qn_SoilMechanicsandFoundationEngineering.py").close()
        if self.spnr_subject.text =="Strength of Materials":
            sys.stdout = open("qn_StrengthofMaterials.py","w")
            print("qn_StrengthofMaterials = ", self.lbl_qn.text )
            open("qn_StrengthofMaterials.py").close()
        if self.spnr_subject.text =="Structural Analysis":
            sys.stdout = open("qn_StructuralAnalysis.py","w")
            print("qn_StructuralAnalysis = ", self.lbl_qn.text )
            open("qn_StructuralAnalysis.py").close()
        if self.spnr_subject.text =="Theory of Structures":
            sys.stdout = open("qn_TheoryofStructures.py","w")
            print("qn_TheoryofStructures = ", self.lbl_qn.text )
            open("qn_TheoryofStructures.py").close()



    def make_btnABCD_text_to_ABCD(self):
        self.btn_a.text = "A"
        self.btn_b.text = "B"
        self.btn_c.text = "C"
        self.btn_d.text = "D"

    def spnr_subjects(self, *args):
        self.spnr_subject.values = subjects

    def subject_click(self, *args):
        global question
        global answer
        self.make_btnABCD_text_to_ABCD()
        #self.lbl_qn.text = "0"
        #paste this in main file under def subject_click(self,*args): of main.py where copy is written in comment but make sure indendation is perfect
        if self.spnr_subject.text =="Favourite questions":
            question=questions_fav
            answer=answers_fav
            self.btn_fav.text="Favourite"
            self.lbl_qn.text= str(qn_Favourite_questions)
        if self.spnr_subject.text =="Building Construction":
            question=question_BuildingConstruction
            answer=answer_BuildingConstruction
            self.btn_fav.text="Favourite"
            self.lbl_qn.text=str(qn_BuildingConstruction)
        if self.spnr_subject.text =="Building Materials":
            question=question_BuildingMaterials
            answer=answer_BuildingMaterials
            self.btn_fav.text="Favourite"
            self.lbl_qn.text=str(qn_BuildingMaterials)
        if self.spnr_subject.text =="Concrete Technology and Design":
            question=question_ConcreteTechnologyandDesign
            answer=answer_ConcreteTechnologyandDesign
            self.btn_fav.text="Favourite"
            self.lbl_qn.text=str(qn_ConcreteTechnologyandDesign)
        if self.spnr_subject.text =="Cpm":
            question=question_Cpm
            answer=answer_Cpm
            self.btn_fav.text="Favourite"
            self.lbl_qn.text=str(qn_Cpm)
        if self.spnr_subject.text =="Design of Masonry Structures":
            question=question_DesignofMasonryStructures
            answer=answer_DesignofMasonryStructures
            self.btn_fav.text="Favourite"
            self.lbl_qn.text=str(qn_DesignofMasonryStructures)
        if self.spnr_subject.text =="Design of Steel Structures":
            question=question_DesignofSteelStructures
            answer=answer_DesignofSteelStructures
            self.btn_fav.text="Favourite"
            self.lbl_qn.text=str(qn_DesignofSteelStructures)
        if self.spnr_subject.text =="Estimating and Costing":
            question=question_EstimatingandCosting
            answer=answer_EstimatingandCosting
            self.btn_fav.text="Favourite"
            self.lbl_qn.text=str(qn_EstimatingandCosting)
        if self.spnr_subject.text =="Highway Engineering":
            question=question_HighwayEngineering
            answer=answer_HighwayEngineering
            self.btn_fav.text="Favourite"
            self.lbl_qn.text=str(qn_HighwayEngineering)
        if self.spnr_subject.text =="Irrigation Engineering":
            question=question_IrrigationEngineering
            answer=answer_IrrigationEngineering
            self.btn_fav.text="Favourite"
            self.lbl_qn.text=str(qn_IrrigationEngineering)
        if self.spnr_subject.text =="Soil Mechanics and Foundation Engineering":
            question=question_SoilMechanicsandFoundationEngineering
            answer=answer_SoilMechanicsandFoundationEngineering
            self.btn_fav.text="Favourite"
            self.lbl_qn.text=str(qn_SoilMechanicsandFoundationEngineering)
        if self.spnr_subject.text =="Strength of Materials":
            question=question_StrengthofMaterials
            answer=answer_StrengthofMaterials
            self.btn_fav.text="Favourite"
            self.lbl_qn.text=str(qn_StrengthofMaterials)
        if self.spnr_subject.text =="Structural Analysis":
            question=question_StructuralAnalysis
            answer=answer_StructuralAnalysis
            self.btn_fav.text="Favourite"
            self.lbl_qn.text=str(qn_StructuralAnalysis)
        if self.spnr_subject.text =="Theory of Structures":
            question=question_TheoryofStructures
            answer=answer_TheoryofStructures
            self.btn_fav.text="Favourite"
            self.lbl_qn.text=str(qn_TheoryofStructures)
        else:
            pass



        self.lbl_tqn.text = "/" + str(len(question))
        self.lbl_q.text = "Press Next to start quiz"
        self.spnr.text = "1"

    def save_favourite_quesions_to_file(*args):
        open("favourite_questions_answers.py", "w").close()
        fn = open("favourite_questions_answers.py", "w+")
        sys.stdout = fn
        print("questions_fav=", questions_fav)
        print("answers_fav=", answers_fav)
        fn.close()

    def on_spinner_select(self, *args):
        try:
            global answer
            global question
            global set_size
            set_size = int(self.spnr_set.text)
            self.lbl_qn.text = str(int(self.spnr.text) * set_size)
            self.lbl_q.text = question[int(self.spnr.text) * set_size - 1]
            self.make_btnABCD_text_to_ABCD()
        except IndexError:
            self.lbl_q.text = "No more questions in set"
            self.lbl_qn.text = '-'

    def total_question(self):
        self.lbl_tqn.text = str(len(question))
        return "/" + self.lbl_tqn.text

    def btn_favourite(self, *args):
        global questions_fav, answers_fav
        if self.spnr_subject.text != "Favourite questions":
            if self.lbl_qn.text == "0":
                self.lbl_q.text = "There is no question\n Select subject first. Then\n press next to start quiz if you have selected subject"
                pass
            else:
                if self.btn_fav.text == "Add to favourite":
                    self.btn_fav.text = "Remove from favourite"
                    questions_fav.append(self.lbl_q.text)
                    answers_fav.append(answer[int(self.lbl_qn.text) - 1])
                    self.save_favourite_quesions_to_file()

                elif self.btn_fav.text == "Remove from favourite":
                    self.btn_fav.text = "Add to favourite"
                    index_question = questions_fav.index((self.lbl_q.text))
                    questions_fav.pop(index_question)
                    answers_fav.pop(index_question)
                    self.save_favourite_quesions_to_file()
                else:
                    pass
        else:
            if self.lbl_qn.text == "0":
                pass
            elif self.lbl_q.text == "Question Removed":
                pass
            elif self.lbl_qn.text != "0":
                self.btn_fav.text = "Remove this question"
                # this means question is not removed
                if self.lbl_q.text != "Question Removed":
                    index_question = questions_fav.index(self.lbl_q.text)
                    # questions_fav.pop(index_question)
                    # favourite_subject.pop(index_question)
                    questions_fav.pop(index_question)
                    answers_fav.pop(index_question)
                    self.save_favourite_quesions_to_file()
                    if self.lbl_qn.text == "1":
                        self.lbl_qn.text = "0"
                        self.lbl_q.text = "Question Removed"
                        no_of_fav_question = len(questions_fav) + 1
                        self.lbl_tqn.text = "/" + str(no_of_fav_question - 1)
                        # self.make_btnABCD_text_to_ABCD()
                    else:
                        self.lbl_q.text = "Question Removed"
                        no_of_fav_question = len(questions_fav) + 1
                        self.lbl_tqn.text = "/" + str(no_of_fav_question - 1)

                else:
                    pass

    def btn_previous(self, *args):
        # this is done as btn_text is changed when btn is clicked
        self.make_btnABCD_text_to_ABCD()
        # question number initially is 0. So to leave it and do no disturbance
        if self.lbl_qn.text == '0':
            pass
        #>0 is not donw as it will make value -1 and last value of question is called
        if int(self.lbl_qn.text) > 1:
            self.lbl_qn.text = str(int(self.lbl_qn.text) - 1)
            self.lbl_q.text = str(question[int(self.lbl_qn.text) - 1])
        else:
            pass

        # if the spinner text is other than favourite questions then change add
        # to fav to remove from fav and vice-versa
        if self.spnr_subject.text != "Favourite questions":
            if self.lbl_q.text not in questions_fav:
                self.btn_fav.text = "Add to favourite"
            else:
                self.btn_fav.text = "Remove from favourite"
        # if the spinner text is fav then
        else:
            self.btn_fav.text = "Remove this question"
            if answers_fav == []:
                pass
            else:
                pass
        self.save_question_number_to_file()

        #*args as it takes more than 1 argument from question
    def btn_next(self, *args):
        # this is done as btn_text is changed when btn is clicked
        self.make_btnABCD_text_to_ABCD()

        # when number of question number is less than the questions than loops
        # continues otherwise error is obtained
        if int(self.lbl_qn.text) < len(question):
            self.lbl_qn.text = str(int(self.lbl_qn.text) + 1)
            self.lbl_q.text = question[int(self.lbl_qn.text) - 1]
        else:
            pass
        # if the spinner text is other than favourite questions then change add
        # to fav to remove from fav and vice-versa
        if self.spnr_subject.text != "Favourite questions":
            if self.lbl_q.text not in questions_fav:
                self.btn_fav.text = "Add to favourite"
            else:
                self.btn_fav.text = "Remove from favourite"

        # if the spinner text is fav then
        else:
            self.btn_fav.text = "Remove this question"
            if questions_fav == []:
                pass
            else:
                pass
        self.save_question_number_to_file()
# for working of Button A,B,C,D or any number of button
# btn_name = name of btn eg self.btn_a which means btn_a of test.kv of quiz app func
# btn_text = Text of btn eg "A"
# use return self.btn_name_func(self.btn_a,"A")

    def btn_name_func(self, btn_name_of_kivy_file, btn_text):
        if self.lbl_qn.text == '0':
            pass
        elif answer == []:
            pass
        # if this line is omitted then when clicking button A again 'A no' is
        # obtained in button A
        elif btn_name_of_kivy_file.text == btn_text + "Yes":
            pass
        elif self.lbl_q.text == "Question Removed":
            pass
        elif btn_name_of_kivy_file.text != answer[int(self.lbl_qn.text) - 1]:
            btn_name_of_kivy_file.text = btn_text + "No"
        else:
            btn_name_of_kivy_file.text = btn_text + "Yes"

    def btn_A(self, *args):
        self.btn_name_func(self.btn_a, "A")

    def btn_B(self, *args):
        self.btn_name_func(self.btn_b, "B")

    def btn_C(self, *args):
        self.btn_name_func(self.btn_c, "C")

    def btn_D(self, *args):
        self.btn_name_func(self.btn_d, "D")

# TestApp calls Test.kv file automatically and it inherints from App


class TestApp(App):
    def build(self):
        return QuizApp()

# This is done to run app
if __name__ == '__main__':
    TestApp().run()
