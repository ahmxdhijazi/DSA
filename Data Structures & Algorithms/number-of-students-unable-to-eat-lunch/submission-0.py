class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        if not sandwiches:
            return False

        counter = 0
        while students and counter != len(students):
            #only need to check the top of the stack
            if students[0] == sandwiches[0]: 
                sandwiches.pop(0)
                students.pop(0)
                counter = 0
            else:
                students.append(students[0])
                students.pop(0)
                counter += 1

        return len(students)