__author__ = 'Michele Johnson'


# This program is about sets.
# The Computer Programming Department of a community college offers two certificate programs:
# Java Programming Certificate and C# Programming Certificate.
# Students need to finish CSC120, CSC121, CSC151 and CSC251 to get the Java certificate.
# They need to finish CSC120, CSC121, CSC153 and CSC253 to get the C# certificate.
# Write a Python program to do the following:

# (a)	Create a set to store courses in Java certificate.
# (b)	Create a set to store courses in C# certificate.
# (c)   A student wants to get both certificates.
# He wants to get a combined set of the courses he needs to take (with no duplicates).
# Perform a set operation with the two sets to obtain this combined set.  Display the set.
# (d)   The student wants to know what courses are common in both certificates.
# Perform a set operation with the two sets to obtain the set of common courses.  Display this set.
# (e)	The student wants to know what courses are in the Java certificate but not in the C# certificate.
# Perform a set operation with the two sets to obtain the answer to this question.  Display the answer.
# (f)	The student wants to know what courses are in the C# certificate but not in the Java certificate.
# Perform a set operation with the two sets to obtain the answer to this question.  Display the answer.


def main():
    # Introduce Program
    print("This program is about sets.\n")
    print("The Computer Programming Department of a community college offers two certificate programs:"
          "\nJava Programming Certificate and C# Programming Certificate."
          "\nStudents need to finish CSC120, CSC121, CSC151 and CSC251 to get the Java certificate."
          "\nThey need to finish CSC120, CSC121, CSC153 and CSC253 to get the C# certificate.\n")

    # (a)	Create a set to store courses in Java certificate.
    java = {'CSC120', 'CSC121', 'CSC151', 'CSC251'}
    print("Java set:", java)
    print("\nJava Certificate Courses:")
    for course in java:
        print(course)

    # (b)	Create a set to store courses in C# certificate.
    c_plus = {'CSC120', 'CSC121', 'CSC153', 'CSC253'}
    print("\nC# set:", c_plus)
    print("\nC# Certificate Courses:")
    for course in c_plus:
        print(course)

    # (c)   A combined set of the courses (with no duplicates).
    combined = java | c_plus
    print("\nCombined set:", combined)
    print("\nCourses required to earn both Java and C# certificates:")
    for course in combined:
        print(course)

    # (d)   A set of common courses.
    common = java & c_plus
    print("\nCommon set:", common)
    print("\nCourses in common between Java and C# certificates:")
    for course in common:
        print(course)

    # (e)	A set of courses in the Java certificate but not in the C# certificate.
    java_primary = java - c_plus
    print("\nJava difference set:", java_primary)
    print("\nCourses in Java certificate track, but not in C# track:")
    for course in java_primary:
        print(course)

    # (f)	A set of courses in the Java certificate but not in the C# certificate.
    c_plus_primary = c_plus - java
    print("\nC# difference set:", c_plus_primary)
    print("\nCourses in C# certificate track, but not in Java track:")
    for course in c_plus_primary:
        print(course)


main()
