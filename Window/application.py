
"""
    TODO: Fix so that when the save button is pressed all the settings are saved, currently no values are being
    generated because its value is taken when the object is created.
"""

import selenium
import tkinter as tk
import Workflow.apply as aply

from selenium import webdriver
from Settings import save
from tkinter import ttk
from Settings import settings
from Database import ManagerSQLITE


class Application(tk.Frame):

    print('Application Imported')

    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()

    def create_widgets(self):

        self.master.minsize(width=700, height=500)
        self.master.maxsize(width=700, height=500)
        self.title = self.master.title('WorkApplier')

        # Notebook
        tabControl = ttk.Notebook(self.master)

        def create_main_tab():

            sql = ManagerSQLITE.SQL()

            main_tab = ttk.Frame(tabControl)
            tabControl.add(main_tab, text='Main')
            tabControl.pack(expand=1, fill="both")

            # Top Container
            top_container = tk.Frame(main_tab, borderwidth=1)
            top_container.pack(side='top', fill='x')

            # ScrollBarY Container
            containerScrollbarY = tk.Frame(main_tab, borderwidth=1)
            containerScrollbarY.pack(side='left', fill='y')

            # TreeView Container
            container = tk.Frame(main_tab, borderwidth=1, background='grey')
            container.pack(side='left', fill='both', pady=5, padx=5)

            # Table of Content
            Tree = ttk.Treeview(container)
            Tree.pack(side='left', fill='y')

            def display_jobs():

                jobs = sql.fetch_all_data_two()
                index = iid = 1

                if Tree.exists(str(index)):

                    pos = 1
                    boolValue = True

                    while boolValue:

                        boolValue = Tree.next(str(pos)) is not ""
                        Tree.delete(str(pos))
                        pos += 1

                for row in jobs:

                    values = [index]
                    for y in list(row):

                        values.append(y)

                    Tree.insert("", index, iid, values=values)
                    index = iid = index + 1

            display_jobs()  # So the content is displayed when starting the application

            def delete_job():
                selected_row = Tree.focus()
                data = Tree.item(selected_row).get('values')
                job_id = data[1]

                sql.delete_data_two_job_id(job_id)

            def delete_all_jobs():

                sql.delete_data_two_all_jobs()

            def apply():

                selected_row = Tree.focus()
                data = Tree.item(selected_row).get('values')
                url = data[7]
                driver = webdriver.Chrome('C:\\Users\\Vidar\\PycharmProjects\\WorkApplier\\Settings\\chromedriver.exe') # TODO: FIX Better solution
                driver.get(url)

            def seek_jobs():
                arbetsformedlningen = aply.ApplyingInterface()
                arbetsformedlningen.apply_arbetsformedlningen()
                display_jobs()

            # ScrollBarX Container
            containerScrollbarX = tk.Frame(main_tab, borderwidth=1)
            containerScrollbarX.pack(side='bottom', fill='x')
            button = ttk.Button(top_container, text='Seek Jobs', width=50, command=seek_jobs)
            button.pack(pady=15)

            button_delete_all = ttk.Button(top_container, text='DELETE ALL', width=10, command=delete_all_jobs)
            button_delete_all.pack(side='right')

            button_delete = ttk.Button(top_container, text='DELETE', width=10, command=delete_job)
            button_delete.pack(side='right')

            button_update = ttk.Button(top_container, text='UPDATE TABLE', width=20, command=display_jobs)
            button_update.pack(side='right')

            button_apply = ttk.Button(top_container, text='APPLY', width=10, command=apply)
            button_apply.pack(side='right')

            # Scrollbar
            scrollBarY = ttk.Scrollbar(containerScrollbarY, orient='vertical', command=Tree.yview)
            scrollBarY.pack(fill='y', side='left')

            scrollBarX = ttk.Scrollbar(containerScrollbarX, orient='horizontal', command=Tree.xview)
            scrollBarX.pack(fill='x', side='bottom')

            Tree.configure(yscrollcommand=scrollBarY.set, xscrollcommand=scrollBarX.set)
            Tree["columns"] = ["row", "job_id", "occupation", "company_name", "keywords", "publication_date", "last_publication_date", "url"]
            Tree.column('row', width=30)
            Tree.column('job_id', width=60)
            Tree.column('occupation', width=110)
            Tree.column('company_name', width=110)
            Tree.column('keywords', width=110)
            Tree.column('publication_date', width=110)
            Tree.column('last_publication_date', width=140)

            Tree["show"] = "headings"
            Tree.heading("row", text="row")
            Tree.heading("job_id", text="job_id")
            Tree.heading("occupation", text="occupation")
            Tree.heading("company_name", text="company_name")
            Tree.heading("keywords", text="keywords")
            Tree.heading("publication_date", text="publication_date")
            Tree.heading("last_publication_date", text="last_publication_date")
            Tree.heading("url", text="url")

        def create_settings_tab():

            # ------------------------------------- Create Settings One --------------------------------------------------

            settings_tab = ttk.Frame(tabControl)
            tabControl.add(settings_tab, text='Settings')
            tabControl.pack(expand=1, fill="both")

            # Container
            container = tk.Frame(settings_tab, borderwidth=1)
            container.pack(side='left', fill='y')
            ttk.Label(container, text='Program Settings', width=40, font=0.1).grid(row=0, column=0)    # Headline

            # Directory Base Option
            ttk.Label(container, text='Base Directory Path', width=20).grid(row=1, column=0, sticky='W')
            base_dir_entry = ttk.Entry(container)
            base_dir_entry.grid(row=1, column=0, pady=2)
            base_dir_entry.insert(0, settings.settings_dictionary.get('main_folder'))


            # API-KEY Option
            ttk.Label(container, text='API-key', width=20).grid(row=2, column=0, sticky='W')
            api_key_entry = ttk.Entry(container)
            api_key_entry.grid(row=2, column=0)
            api_key_entry.insert(0, settings.settings_dictionary.get('api_key'))

            def program_settings():

                # Save Objects
                objects = {
                    'main_folder': str(base_dir_entry.get()),
                    'api_key': str(api_key_entry.get()),
                }

                return objects

            # -------------------------------------------------------------------------------------------------------------

            # ------------------------------------- Create Settings Two ---------------------------------------------------

            # Container and Headline
            container_two = tk.Frame(settings_tab, borderwidth=1)
            container_two.pack(side='left', fill='y')
            tk.Label(container_two, text='Special Search Settings', width=40, font=1).grid(row=0, column=1)

            # Occupation Checkbox
            occupation_check = ttk.Checkbutton(container_two, text='Occupation list', variable='occupation_checkbox')
            occupation_check.grid(row=1, column=1, sticky='W')

            # Occupation Entry
            occupation_entry = ttk.Entry(container_two)
            occupation_entry.grid(row=1, column=1, pady=2)

            # Occupation Enabled/Disabled
            occupation_check.setvar('occupation_checkbox', settings.settings_search_dictionary.get('ssyk_active'))
            occupation_entry.insert(0, settings.settings_search_dictionary.get('ssyk_value'))

            def occupation_setting():

                val = check_button_checked(occupation_check.state())

                # Save Objects
                dict_occupation = {
                    'ssyk_active': val,
                    'ssyk_value': occupation_entry.get().split(' ')
                }

                return dict_occupation

            # Driving license Checkbox
            driving_license_check = ttk.Checkbutton(container_two, text='Driving License', variable='d_checkbox')
            driving_license_check.grid(row=2, column=1, pady=5, sticky='W')

            # License Type Entry
            ttk.Label(container_two, text='License Type').grid(row=3, column=1, ipadx=100)
            license_type_entry = ttk.Entry(container_two)
            license_type_entry.grid(row=3, column=1, pady=2)

            # Has own car Checkbox
            has_car_check = ttk.Checkbutton(container_two, text='Has own car', variable='car_checkbox')
            has_car_check.grid(row=4, column=1, ipadx=90)

            # Driving License Enabled/Disabled
            driving_license_check.setvar('d_checkbox',settings.settings_search_dictionary.get('driving_license_active'))
            license_type_entry.insert(0, settings.settings_search_dictionary.get('driving_license_value'))

            # Has own car Enabled/Disabled
            has_car_check.setvar('car_checkbox', settings.settings_search_dictionary.get('driving_license_own_car'))

            def driving_license_setting():

                val = check_button_checked(driving_license_check.state())
                val_two = check_button_checked(has_car_check.state())

                # Save Objects
                dict_driving_license = {
                    'driving_license_active': val,
                    'driving_license_value': str(license_type_entry.get()),
                    'driving_license_own_car': val_two
                }

                return dict_driving_license

            # Reduce Working Hours
            reduce_entry = ttk.Entry(container_two)
            reduce_entry.grid(row=5, column=1) # TODO: fix row

            # Reduce Checkbox
            reduce_check = ttk.Checkbutton(container_two, text='Reduce hours', variable='reduce_checkbox')
            reduce_check.grid(row=5, column=1, sticky='W', pady=5)

            # Reduce Enabled/Disabled
            reduce_check.setvar('reduce_checkbox', settings.settings_search_dictionary.get('reduce_working_hours_active'))
            reduce_entry.insert(0, settings.settings_search_dictionary.get('reduce_working_hours_value'))

            def reduce_hours_setting():

                val = check_button_checked(reduce_check.state())

                dict_reduce_hours = {
                    'reduce_working_hours_active': val,
                    'reduce_working_hours_value': reduce_entry.get()
                }

                return dict_reduce_hours

            # Language Entry
            language_entry = ttk.Entry(container_two)
            language_entry.grid(row=6, column=1)

            # Language Checkbox
            language_check = ttk.Checkbutton(container_two, text='Specific Language', variable='language_checkbox')
            language_check.grid(row=6, column=1, sticky='W', pady=10)

            # Language Enabled/Disabled
            language_check.setvar('language_checkbox', settings.settings_search_dictionary.get('language_active'))
            language_entry.insert(0, settings.settings_search_dictionary.get('language_value'))

            def language_setting():

                val = check_button_checked(language_check.state())

                # Save Objects
                dict_language = {

                    'language_active': val,
                    'language_required': True,  # TODO: FIX MAYBE
                    'language_value': str(language_entry.get())

                }

                return dict_language

            # Location Checkbox
            location_check = ttk.Checkbutton(container_two, text='Location Radius', variable='location_checkbox')
            location_check.grid(row=7, column=1, sticky='W', pady=2, ipadx=100)

            # Location Longitude Entry
            ttk.Label(container_two, text='Latitude').grid(row=8, column=1, ipadx=100)
            latitude_entry = ttk.Entry(container_two)
            latitude_entry.grid(row=8, column=1, pady=2)

            # Location Latitude Entry
            ttk.Label(container_two, text='Longitude').grid(row=9, column=1, ipadx=100)
            longitude_entry = ttk.Entry(container_two)
            longitude_entry.grid(row=9, column=1, pady=2)

            # Location Radius Entry
            ttk.Label(container_two, text='Radius (km)').grid(row=10, column=1, ipadx=100)
            radius_entry = ttk.Entry(container_two)
            radius_entry.grid(row=10, column=1, pady=2)

            # Location Enabled/Disabled
            location_check.setvar('location_checkbox', settings.settings_search_dictionary.get('radius_active'))

            if settings.settings_search_dictionary.get('radius_active'):
                homePos = settings.settings_search_dictionary.get('radius_home').split(',')

                if len(homePos) <= 2:
                    homeLat = homePos[0]
                    homeLong = homePos[1]
                    latitude_entry.insert(0, homeLat)
                    longitude_entry.insert(0, homeLong)

                radius_entry.insert(0, settings.settings_search_dictionary.get('radius_acceptable'))

            def location_setting():

                val = check_button_checked(location_check.state())

                # Save Objects
                dict_location = {

                    'radius_active': val,
                    'radius_home': (str(latitude_entry.get()) + ',' + str(longitude_entry.get())),
                    'radius_acceptable': radius_entry.get()

                }

                return dict_location

            # Keywords Checkbox
            keywords_check = ttk.Checkbutton(container_two, text='Keywords', variable='keywords_checkbox')
            keywords_check.grid(row=11, column=1, sticky='W', pady=10)

            # Keywords Entry
            keywords_entry = ttk.Entry(container_two)
            keywords_entry.grid(row=11, column=1)

            # Keywords Enabled/Disabled
            keywords_check.setvar('keywords_checkbox', settings.settings_search_dictionary.get('keywords_active'))
            keywords_entry.insert(0, settings.settings_search_dictionary.get('keywords_value'))

            def keywords_setting():

                val = check_button_checked(keywords_check.state())

                # Save Objects
                dict_keywords = {

                    'keywords_active': val, # bool(keywords_check.getvar('keywords_checkbox'))
                    'keywords_value':  keywords_entry.get().split(' ')

                }

                return dict_keywords

            # Limit Checkbox
            limit_check = ttk.Checkbutton(container_two, text='Return Amount', variable='limit_checkbox')
            limit_check.grid(row=12, column=1, sticky='W', pady=2)

            # Limit Entry
            limit_entry = ttk.Entry(container_two)
            limit_entry.grid(row=12, column=1)

            # Limit Enabled/Disabled
            limit_check.setvar('limit_checkbox', settings.settings_search_dictionary.get('limit_active'))
            limit_entry.insert(0, settings.settings_search_dictionary.get('limit_value'))

            def amount_returned_setting():

                val = check_button_checked(limit_check.state())

                # Save Objects
                dict_limit = {

                    'limit_active': val,
                    'limit_value': limit_entry.get()

                }

                return dict_limit

            def save_settings():

                dict_list = [program_settings(), occupation_setting(), reduce_hours_setting(), driving_license_setting(),
                             language_setting(), location_setting(), keywords_setting(), amount_returned_setting()]

                # Loop trough each object
                for d in dict_list:

                    for k in list(d.keys()):
                        key = k
                        value = d.get(k)

                        save.SaveSettings(key, value).save_settings_file()
                        print('Saved: ' + str(key) + ' with value of: ' + str(value))

            def check_button_checked(an_dictionary):

                if len(an_dictionary) > 0:

                    if an_dictionary[0] == 'selected':
                        val = True

                else:
                    val = False

                return val

            # Save Button
            save_button = ttk.Button(container, text='Save Settings', width=20, command=save_settings)
            save_button.grid(row=13, column=0, ipady=3, pady=235, ipadx=50, padx='50', sticky='W')

        create_main_tab()
        create_settings_tab()
