import Document, SkillsPage, EducationPage, ExperiencePage

class Resume(Document.Document):
    """description of class"""
    def __init__(self):
        super(Resume, self).__init__()

    def CreatePages(self):
        self._pages.append(SkillsPage.SkillsPage())
        self._pages.append(EducationPage.EducationPage())
        self._pages.append(ExperiencePage.ExperiencePage())


