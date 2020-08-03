import sqlite3


class VaxTraxDb:

    def __init__(self, dbname="vaxtrax.db"):
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
        sql = """
            DROP TABLE IF EXISTS vaccines;
            CREATE TABLE vaccines (
                name text,
                type text,
                stage text,
                info text);"""

        self.conn.executescript(sql)
        self.conn.commit()

    def insert_sample_data(self):
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


if __name__ == '__main__':
    db = VaxTraxDb()
    db.create_tables()
    db.insert_sample_data()
