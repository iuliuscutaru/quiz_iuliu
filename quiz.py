class Question:
     def __init__(self, prompt, answer):
          self.prompt = prompt
          self.answer = answer

question_prompts = [
     "1. Funcţia de repartiţie conţine următoarea fază: \n"
     "(a) controlul administrării fondurilor financiare;\n"
     "(b) constituirea resurselor financiare la dispoziţia statului ;\n"
     "(c) repartizarea competenţelor aparatului administrativ\n"
     "(d) b+c ;\n"
     "(e) fluxuri financiare de intrare si ieşire;\n",

    "2. In cadrul funcţiei de repartiţie, instrumentele bancare includ: \n"
    "(a) impozitele pe profiturile băncilor ;\n"
    "(b) creditele şi dobânzile bancare ;\n"
    "(c) remuneraţiile funcţionarilor din sistemul bancar.\n"
    "(d) ratele scadente si comisioanele aferente ;\n"
    "(e) b+d\n",

    "3. Structura instrumentelor financiare include : \n"
    "(a) redevenţele şi chiriile pentru folosirea activelor statului ;\n"
    "(b) transferurile rambursabile de fonduri băne şti contra unor prestaţii certe;\n"
    "(c) contribuţiile la asigurările sociale de stat ;\n"
    "(d) c+e ;\n"
    "(e) indemnizaţiile de şomaj.\n",

    "4. Metodele de evaluare a veniturilor si cheltuielilor bugetare sunt : \n"
    "(a) metoda evaluării directe ;\n"
    "(b) metoda majorării /diminuării; \n"
    "(c) a+b ;\n"
    "(d) anexele la proiectul de lege;\n"
    "(e) b+d .\n",

    "5. Impozitul pe clădiri este un impozit:  \n"
    "(a) direct;\n"
    "(b) personal; \n"
    "(c) indirect ;\n"
    "(d) real ;\n"
    "(e) a+d .\n",

    "6. Fondul de consum social are ca destinaţie:  \n"
    "(a) finanţarea activităţilor culturale; \n"
    "(b) finanţarea activităţilor educative; \n"
    "(c) constituirea stocurilor de materii prime;\n"
    "(d) finanţarea investiţiilor; \n"
    "(e) a+b . \n",

    "7. Specializarea bugetară înseamnă : \n"
    "(a) debugetizarea unor venituri şi cheltuieli  \n"
    "(b) includerea veniturilor pe surse de provenienţă; \n"
    "(c) includerea cheltuielilor pe categorii de destinaţii;\n"
    "(d) împărţirea specifică bugetului in fond de acumulare şi de consum  \n"
    "(e) b+c. . \n",

    "8. Conform clasificării economice folosit de catre instituţiile O.N>U. ,cheltuielile publice sunt împărţite si anume : \n"
    "(a) dobanzi aferente datoriei publice;  \n"
    "(b) transferuri de capital ; \n"
    "(c) a+b+d \n"
    "(d) achiziţii de terenuri si active necorporale  \n"
    "(e) cheltuieli de apărare . \n",

    "9. Controlul jurisdicţional privitor se exercită de către : \n"
    "(a) Guvernul  \n"
    "(b) Consiliul Superior al Magistraturii ; \n"
    "(c) Consiliul Superior al Magistraturii ; \n"
    "(d) Înalta Curte de Casaţie şi Justiţie; \n"
    "(e) Trezoreria statului .  \n",


]
name = input("Please enter your name: ").title()
questions = [
     Question(question_prompts[0], "d"),
     Question(question_prompts[1], "e"),
     Question(question_prompts[2], "d"),
     Question(question_prompts[3], "c"),
     Question(question_prompts[4], "e"),
     Question(question_prompts[5], "e"),
     Question(question_prompts[6], "e"),
     Question(question_prompts[7], "c"),
     Question(question_prompts[8], "c"),
]

def run_quiz(questions):
     score = 0
     for question in questions:
          answer = input(question.prompt)
          if answer == question.answer:
               score += 1
    # print("Ati obtinut", score, " raspunsuri corecte din", len(questions))
     print("\n{0}, ai obtinut {1} raspunsuri corecte din {2}.".format(name, score, len(questions)))

run_quiz(questions)