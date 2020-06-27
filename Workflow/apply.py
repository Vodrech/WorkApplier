from Applying.indeed import Indeed
from Database.ManagerSQLITE import SQL


class ApplyingInterface:

    print('ApplyingInterface Imported')

    # TODO: Change so it can have other object than Indeed
    def __init__(self):
        self.indeed = Indeed()
        self.sql = SQL()
        self.saved_jobs = self.sql.select_all()
        self.exists = True

    def apply_indeed(self):

        print('saving to database')

        for saveWorkPlace in self.indeed.applies:

            for job in self.saved_jobs:

                if job.__contains__(saveWorkPlace.get('workplace')) and job.__contains__(saveWorkPlace.get('worktitle')):
                    self.exists = False

            if self.exists is True:

                workplace = saveWorkPlace.get('workplace')
                worktitle = saveWorkPlace.get('worktitle')
                link = saveWorkPlace.get('link')
                print('Saving to DB: ', workplace, '-', worktitle)
                self.sql.save_workplace(workplace, worktitle, link)

            else:
                print('\nJob Already exist: ', saveWorkPlace.get('workplace'), '-', saveWorkPlace.get('worktitle'))




