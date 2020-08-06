import sqlite3


class VaxTraxDb:

    def __init__(self, dbname="vaxtrax.db"):
        """init db connection"""
        self.dbname = dbname
        self.conn = sqlite3.connect(self.dbname)
        self.conn.text_factory = str

    def cursor(self):
        """Return a cursor on the database"""
        return self.conn.cursor()

    def commit(self):
        """Commit pending changes"""

        self.conn.commit()

    def create_tables(self):
        """Create database tables"""
        sql = """
            DROP TABLE IF EXISTS vaccines;
            CREATE TABLE vaccines (
                name text,
                type text,
                stage text,
                info text);
                
            DROP TABLE IF EXISTS quiz;
            CREATE TABLE quiz (
                question_id INTEGER PRIMARY KEY AUTOINCREMENT,
                question text,
                optionOne text,
                optionTwo text,
                optionThree text,
                optionFour text);
                
            DROP TABLE IF EXISTS quizAnswers;
            CREATE TABLE quizAnswers ( 
                question_id integer UNIQUE NOT NULL,
                optionOne integer,
                optionTwo integer,
                optionThree integer,
                optionFour integer,
                FOREIGN KEY(question_id) REFERENCES quiz(question_id));
                
            DROP TABLE IF EXISTS quizTwo;
            CREATE TABLE quizTwo (
                question_id INTEGER PRIMARY KEY AUTOINCREMENT,
                question text,
                optionOne text,
                optionTwo text);
                    
            DROP TABLE IF EXISTS quizTwoAnswers;
            CREATE TABLE quizTwoAnswers (
                question_id integer UNIQUE NOT NULL,
                optionOne integer,
                optionTwo integer,
                FOREIGN KEY(question_id) REFERENCES quizTwo(question_id));
        """

        self.conn.executescript(sql)
        self.conn.commit()

    def insert_vaccine_data(self):
        """insert sample data to vaccine table"""
        cursor = self.cursor()
        vaccines = [
            ("Amgen and Adaptive Biotechnologies", "Anti-body treatment", "Preclinical",
             "Amgen Inc. and Adaptive Biotechnologies Corp. are looking at how to use antibodies to prevent or treat COVID-19."),
            ("Altimmune", "Vaccine", "Preclinical",
             "Altimmune Inc. partnered with University of Alabama to develop a single-dose, intranasal COVID-19 vaccine."),
            ("BioNTech and Pfizer", "mRNA vaccine", "Phase 1",
             "The development of a 4 experimental vaccines, each with unique RNA messaging combinations."),
            ("CytoDyn", "Treatment", "Phase 2",
             "Currently testing its drug \"leronlimab\" in two kinds of patients; mild-to-moderate and critically ill patients."),
            ("Gilead Sciences", "Treatment", "Emergency Use Authorisation",
             "Gilead Sciences is currently testing the use of the antiviral drug remdesvir against COVID-19. It was previously tested as a drug for Ebola."),
            ("GlaxoSmithKline", "Vaccine/Treatment", "Phase 2",
             "GSK is currently working with University of Queensland which has access to their vaccine adjuvant platform technology, which is believed to strengthen the response of the vaccine and reduce the amount of vaccine needed per dose."),
            ("Heat Biologics", "Vaccine", "Preclinical",
             "Currently developing a vaccine with the University of Miami Miller School of Medicine. Their gp96 technology is focused on clearing virus-infected cells and promoting long-term cell immunity to prevent re-infection in susceptible individuals such as the elderly and those with undeelying conditions."),
            ("Inovio Pharmaceuticals", "DNA-based Vaccine", "Phase 1",
             "This DNA-based vaccine being developed by Inovio Pharmaceuticals focuses on preventing the infection by creating immunity against it."),
            ("Johnson&Johnson", "Vaccine", "Preclinical",
             "Johnson&Johnson started studying a library of antiviral molecules in January 2020 and is working with Beth Israel Deaconess Medical Centre in Boston to create a antiviral vaccine."),
            ("Moderna", "RNA-Vaccine", "Phase 1",
             "Moderna is currently working on Phase 1 trials that measure how high levels of neutralising anti-body works against a person with confirmed case of COVID-19."),
            ("Novavax", "Vaccine", "Phase 1",
             "Novavax is currently in Phase 1 human trials of their vaccine that utilises their proprietary Matrix-M technology to enhance immune response to fight COVID-19."),
            ("Regeneron Pharmaceuticals", "Prevention and Treatment", "Preclinical",
             "Regeneron Pharmaceuticals started working on developing identical immune cell antibodies to treat COVID-19 infection."),
            ("Regeneron Pharmaceuticals and Sanofi", "Treatment", "Phase 2",
             "This collaboration between Renegeron Pharmaceuticals and Sanofi is focused on lessening patient fevers and need for supplemental oxygen."),
            ("Roche", "Treatment", "Phase 3",
             "Roche Holdings AG's drug, Actemra, was approved in 2010 as a rheumatoid arthritis drug. It has since then been utilised to examine patient mortality and the need for mechanical ventiliation or an intensive care unit."),
            ("Sanofi", "Vaccine", "Preclinical",
             "Sanofi is working on developin g a vaccine for COVID-19 by using their recombinant DNA platform. This technology produces an exact genetic math of the proteins found on the surface of the virus. This will be used to create an antigen to stimulate the immune system."),
            ("Takeda Pharmaceutical", "Antibody Treatment", "Preclinical",
             "Takeda Pharmaceuticals is focusing their research on treating patients who have contracted COVID-19. This involves accessing the plasma of recovered patients and develop a plasma-derived vaccine."),
            ("Vaxart", "Vaccine", "Preclinical",
             "Vaxart aims to develop a stable, oral tablet form of treatment for COVID-19. Additionally, they hope to create the tablet so that it protects against the norovirus and seasonal flu too."),
            ("Vir Biotechnology", "Treatment", "Preclinical",
             "Vir Biotechnology have focused their efforts into creating a treatment that is designed to degrade the viral genome and reduce the live replication of the virus.")
        ]

        for v in vaccines:
            sqlite = "INSERT INTO vaccines (name, type, stage, info) VALUES (?,?,?,?)"
            cursor.execute(sqlite, v)
            self.commit()

    def insert_quiz_data(self):
        """insert sample data to quiz for question type 1"""
        cursor = self.cursor()
        quiz = [
            ("What country has the most number of active COVID-19 cases currently in the world?",
             "United States", "China", "Brazil", "Russia"),
            ("What is the most common symptom of COVID-19?",
             "Loss of smell and taste", "Fever", "Dry cough", "Depression"),
            ("What are the appropriate steps I should take if I develop COVID-19 like symptoms?",
             "Visit a medical professional", "Self isolate for 14 days", "Self isolate for 7 days", "Drink hot water"),
            ("Would you rather know about vaccine developments in private sectors, public sectors or both?",
             "Private sector", "Public sector", "Both", "None"),
        ]

        for q in quiz:
            sqlite = "INSERT INTO quiz (question, optionOne, optionTwo, optionThree, optionFour) VALUES (?,?,?,?,?)"
            cursor.execute(sqlite, q)
            self.commit()

    def insert_quiz_ans(self):
        """insert sample data to quiz solution for question type 1"""
        cursor = self.cursor()

        answer = [
            (1, 20, 6, 3, 1),
            (2, 6, 5, 19, 0),
            (3, 12, 11, 1, 6),
            (4, 6, 9, 15, 0),
        ]
        for a in answer:
            query = "INSERT INTO quizAnswers (question_id, optionOne, optionTwo, optionThree, optionFour) VALUES (?,?,?,?,?)"
            cursor.execute(query, a)
            self.commit()

    def insert_quiz_two_data(self):
        """insert sample data to quiz for question type 2"""
        cursor = self.cursor()
        quiz_two = [
            ("Are you interested to learn more about this pandemic that is taking the world by storm?", "Yes", "No"),
            ("Would you like to know about the vaccine development lifecycle?", "Yes", "No"),
            ("Do you feel overwhelmed by the current volume of data being presented to you in the media about coronavirus?", "Yes", "No"),
            ("Which area of Covid-19 are you more unfamiliar with?",
             "Prevention methods", "Current trends in your country and around the world")
        ]

        for q in quiz_two:
            sqlite = "INSERT INTO quizTwo (question, optionOne, optionTwo) VALUES (?,?,?)"
            cursor.execute(sqlite, q)
            self.commit()

    def insert_quiz_two_ans(self):
        """insert sample data to quiz solution for question type 2"""
        cursor = self.cursor()

        answer = [
            (1, 30, 0),
            (2, 27, 3),
            (3, 25, 5),
            (4, 14, 16),
        ]
        for a in answer:
            query = "INSERT INTO quizTwoAnswers (question_id, optionOne, optionTwo) VALUES (?,?,?)"
            cursor.execute(query, a)
            self.commit()


if __name__ == '__main__':
    db = VaxTraxDb()
    db.create_tables()
    db.insert_vaccine_data()
    db.insert_quiz_data()
    db.insert_quiz_ans()
    db.insert_quiz_two_data()
    db.insert_quiz_two_ans()
