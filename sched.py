# -*- coding: utf-8 -*-
import config as db

MAX_HRS=2       #Maxima cantidad de horas consecutivas de una materia
#print db.horario_general


z=db.gen_slots()
for i in z:
   print i,z[i],'\n'

"""
For each Course
    For each available Teacher
        For each available Classroom
           Select the first Classroom available and book the resource.
           Update the course and teachers availability.
        end Classrooms
    end Teachers
end Courses
"""

#Hay que generar carga horaria por profesor, nro de horas par air restando
