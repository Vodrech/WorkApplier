from Applying.indeed import Indeed
from Database.ManagerSQLITE import SQL


class ApplyingInterface:

    indeed = Indeed()
    sql = SQL()
    saved_jobs = sql.select_all()
    exists = True

    saved_jobs = sql.select_all()

    for saveWorkPlace in indeed.applies:

        for job in saved_jobs:

            if job.__contains__(saveWorkPlace.get('workplace')) and job.__contains__(saveWorkPlace.get('worktitle')):
                exists = False

        if exists is True:

            workplace = saveWorkPlace.get('workplace')
            worktitle = saveWorkPlace.get('worktitle')
            link = saveWorkPlace.get('link')
            sql.save_workplace(workplace, worktitle, link)

        else:
            print('Job did already exist in the database')




