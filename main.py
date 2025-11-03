# Calculating General Weighted Average.

from pyscript import display, document, window

def submit(e):
    document.getElementById('output').innerHTML = " "

    StudentFname = document.getElementById("fname").value
    StudentLname = document.getElementById("lname").value
    Grade1 = int(document.getElementById("Scigrade").value)
    Grade2 = int(document.getElementById("Enggrade").value)
    Grade3 = int(document.getElementById("ICTgrade").value)
    Grade4 = int(document.getElementById("Mathgrade").value)
    Grade5 = int(document.getElementById("Filgrade").value)
    Grade6 = int(document.getElementById("PEgrade").value)
    
    # Tuple for units
    units = (2, 5, 5, 5, 3, 1)
    # Subject unit assignment
    ICTu, Mathu, Engu, Sciu, Filu, PEu = units 

    # General Weighted Average Calculation : sum ( grade * unit )/ sum ( unit )
    GWA = ((Grade1*Sciu) + (Grade2*Engu) + (Grade3*ICTu) + (Grade4*Mathu) + (Grade5*Filu) + (Grade6*PEu))/(ICTu + Mathu + Engu + Sciu + Filu + PEu)
    GWAround = round(GWA, 2)

    # Multiline string
    Student_Summary = f"""
    Science : {Grade1}\n
    English : {Grade2}\n
    ICT : {Grade3}\n
    Math : {Grade4}\n
    Filipino : {Grade5}\n
    PE : {Grade6}
    """

    display(f'{StudentFname} {StudentLname}', target="studentnametitle")
    display(f'{Student_Summary}', target="studentsummary")
    display(f'Your general weighted average is . . . {GWAround}', target="output")