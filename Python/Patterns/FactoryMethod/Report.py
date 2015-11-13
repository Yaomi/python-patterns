import Document, IntroductionPage, ResultsPage, ConclusionPage, SummaryPage, BibliographyPage

class Report(Document.Document):
    """description of class"""
    def __init__(self):
        super(Report, self).__init__()

    def CreatePages(self):
        self._pages.append(BibliographyPage.BibliographyPage())
        self._pages.append(ResultsPage.ResultsPage())
        self._pages.append(ConclusionPage.ConclusionPage())
        self._pages.append(SummaryPage.SummaryPage())
        self._pages.append(BibliographyPage.BibliographyPage())

