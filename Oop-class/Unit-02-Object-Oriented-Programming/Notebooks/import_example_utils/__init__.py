# Style 1: Can be empty

# Style 2: Expose one/some items
# from .student_utils import Student          ### UNCOMMENT THIS FOR STYLE 1
## After this you can use: 
### from import_example_utils import Student 
### in your code, instead of
### from import_example_utils.student_utils import Student


# Style 3: Expose Multiple Items
from .student_utils import ( 
    Student,
    class_average,
    PASSING_SCORE,
) ### UNCOMMENT THIS CODE BLOCK FOR STYLE 2
### in your code, you can do, 
### from import_example_utils import Student, class_average


