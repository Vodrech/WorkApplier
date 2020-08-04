import os

"""

    The save.py handles the save functionality for the gui to save settings for the settings.py file

    Usage:

    > Create Instance of class
    > Set the instance object to the current setting name that is going to be changed
    > Edit the value


"""


class SaveSettings:

    def __init__(self, object, value):
        self.object = object
        self.value = value
        self.settingsPath = os.path.dirname(os.path.realpath(__file__)) + '\\settings.py'

    def read_settings_file(self):

        numLine = 0

        try:
            with open(self.settingsPath, 'r') as file:
                content = file.readlines()
                for line in content:

                    if line.__contains__(self.object):
                        return [content, numLine]

                    numLine += 1

        except FileNotFoundError as e:
            raise e('File does not exist!')
        finally:
            file.close()

    def save_settings_file(self):

        variables = self.read_settings_file()

        position = variables[1]
        content = variables[0]

        try:
            with open(self.settingsPath, 'w') as file:

                if len(content) > position:

                    if content[position].__contains__(self.object):

                        if type(self.value) == bool:

                            if self.value == True:
                                newLine = ("    '" + self.object + "'" + ":" + " " + 'True' + ',\n')
                            else:
                                newLine = ("    '" + self.object + "'" + ":" + " " + 'False' + ',\n')

                            content[position] = newLine
                            file.writelines(content)

                        elif type(self.value) == str:
                            if self.value.isdecimal():
                                newLine = ("    '" + self.object + "'" + ":" + " " + self.value + ",\n")
                            else:
                                newLine = ("    '" + self.object + "'" + ":" + " " + "'" + self.value + "'" + ",\n")
                            content[position] = newLine
                            file.writelines(content)

                        elif type(self.value) == int:
                            newLine = ("    '" + self.object + "'" + ":" + " " + self.value + ',\n')
                            content[position] = newLine
                            file.writelines(content)

                        elif type(self.value) == list:

                            newLine = ("    '" + self.object + "'" + ":" + " [")
                            loopCount = 0

                            for x in self.value:

                                loopCount += 1

                                if type(x) == int:
                                    newLine += str(x)
                                elif type(x) == str:
                                    if x.isdecimal():
                                        newLine += str(x)
                                    else:
                                        newLine += "'" + x + "'"
                                else:
                                    Exception('Can not define the lists datatype, please check error log!')

                                if loopCount != len(self.value):
                                    newLine += ', '

                            newLine += "]" + ',\n'
                            content[position] = newLine
                            file.writelines(content)
                        else:
                            raise Exception('Could not define correct datatype')
                    else:
                        raise Exception(' The current active line in save.py does not match the creteria')

                else:
                    raise Exception('The line amount is overriding, please check error log')

        except FileNotFoundError as e:
            raise e('File does not exist')
        finally:
            file.close()



