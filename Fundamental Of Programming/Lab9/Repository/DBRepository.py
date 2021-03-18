from Domain.assignment import Assignment
from Domain.grade import Grade
from Domain.student import Student
from Repository.Repository import Repository, RepositoryException
import psycopg2
from psycopg2 import Error
from Settings.setparams import SetParameters


class DataBaseRepo(Repository):
    def __init__(self,repo_type):
        super().__init__()
        # we set the attributes here for knowing how to load
        params = SetParameters(repo_type)
        self._entity, self._atr1, self._atr2, self._atr3 = params.setup_parameters()

        self._load()

    @property
    def get_selectquery(self):
        if self._entity == "Student":
            return "select * from student"

        if self._entity == "Assignment":
            return "select * from assignment"

        if self._entity == "Grade":
            return "select * from grade"

    @property
    def get_addquery(self):
        if self._entity == "Student":
            return "insert into student values (%s, %s, %s)"

        if self._entity == "Assignment":
            return "insert into assignment values (%s, %s, %s)"

        if self._entity == "Grade":
            return "insert into grade values (%s, %s, %s)"

    @property
    def get_removequery(self):
        if self._entity == "Student":
            return "delete from student where student_id = %s and student_name =%s and student_group = %s"

        if self._entity == "Assignment":
            return "delete from assignment where assignment_id = %s and description =%s and deadline = %s"

        if self._entity == "Grade":
            return "delete from grade where student_id = %s and assignment_name =%s and grade_value = %s"

    @property
    def get_updatequery(self):
        if self._entity == "Student":
            return "update student set student_group = %s where student_id = %s and student_name = %s"

        if self._entity == "Assignment":
            return "update assignment set deadline = %s where assignment_id = %s and description = %s"

        if self._entity == "Grade":
            return "update grade set grade_value = %s where student_id = %s and assignment_id = %s"

    """
    The following functions are "copies" from their inheriter
    but the change is that we also do separately saving for each method because
    each method implies a different sql query
    """
    def add_object(self, object):
        super().add_object(object)
        self._save_add(object)

    def remove_object(self, object):
        super().remove_object(object)
        self._save_remove(object)

    def update_object(self, index, value):
        super().update_object(index, value)
        object = self.objects[index]
        self._save_update(object, value)


    def _save_add(self, object):
        """
        this is the function for saving data in database after adding a new object
        :param object: the new object we add
        """
        # firstly we will reastablish the connection, the reason we do that is because after every save we want to close the connection
        connection_string = psycopg2.connect("host=localhost dbname=postgres user=postgres password=polopolo")
        current_connector = connection_string.cursor()
        current_connector.execute(self.get_addquery, (getattr(object, self._atr1),getattr(object, self._atr2),getattr(object, self._atr3)))
        # we execute the command and then we commit in order to save the data even after restarting the app


        connection_string.commit()
        # we close the connection to make sure everything is fine
        current_connector.close()
        connection_string.close()

    def _save_remove(self,object):
        """
        this is the function for saving data in database after remove a new object
        :param object: the object we remove
        """

        # firstly we will reastablish the connection, the reason we do that is because after every save we want to close the connection
        connection_string = psycopg2.connect("host=localhost dbname=postgres user=postgres password=polopolo")
        current_connector = connection_string.cursor()
        # we execute the remove command
        current_connector.execute(self.get_removequery, (getattr(object, self._atr1),getattr(object, self._atr2),getattr(object, self._atr3)))
        # we execute the command and then we commit in order to save the data even after restarting the app


        connection_string.commit()
        # we close the connection to make sure everything is fine
        current_connector.close()
        connection_string.close()

    def _save_update(self, object, value):
        """
        this is the function for saving data in database after updating a new object
        :param object: the object updated
        """
        # firstly we will reastablish the connection, the reason we do that is because after every save we want to close the connection
        connection_string = psycopg2.connect("host=localhost dbname=postgres user=postgres password=polopolo")
        current_connector = connection_string.cursor()
        current_connector.execute(self.get_updatequery, (value,getattr(object, self._atr1),getattr(object, self._atr2)))


        # we execute the command and then we commit in order to save the data even after restarting the app
        connection_string.commit()
        # we close the connection to make sure everything is fine
        current_connector.close()
        connection_string.close()


    def _load(self):
        """
        We load the data from Data base
        """
        try:
            # we try here to make the connection to the data base
            connection_string = psycopg2.connect("host=localhost dbname=postgres user=postgres password=polopolo")
            current_connector = connection_string.cursor()
            # if we get to this line it means that the connection was succesfully done!
            # now according to the value stored in self._entity we will select all data from the corresponding table
            current_connector.execute(self.get_selectquery)

            # after that we will store it in the list
            for row in current_connector:
                if self._entity == 'Student':
                    super().add_object(Student(str(row[0]), str(row[1]), str(row[2])))
                if self._entity == 'Assignment':
                    super().add_object(Assignment(str(row[0]), str(row[1]), str(row[2])))
                if self._entity == 'Grade':
                    super().add_object(Grade(str(row[0]), str(row[1]), str(row[2])))
            current_connector.close()
            connection_string.close()

        except Exception as ve:
            raise RepositoryException(ve)