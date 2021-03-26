# -*- coding: utf-8 -*-
from datetime import date, datetime, time ,  timedelta
import time as tm

aula={}
profesor={}
profesor_rest={}
materia={}
curso={}
curso_grupo={}
horario={}
horario_receso={}

curso={1:{"id":1,"nombre":"7mo. A"}, 
       2:{"id":2,"nombre":"7mo. B"}, 
       3:{"id":3,"nombre":"8vo. A"}, 
       3:{"id":4,"nombre":"8vo. B"}
       }

curso_grupo={1:{"id":1,"id_curso":1,"nombre":"1er. Grupo" }, 
                    2:{"id":2,"id_curso":1,"nombre":"2do. Grupo" }, 
                    3:{"id":3,"id_curso":1,"nombre":"Varones" }, 
                    4:{"id":4,"id_curso":1,"nombre":"Hembras" }, 
                    5:{"id":5,"id_curso":2,"nombre":"1er. Grupo" }, 
                    6:{"id":6,"id_curso":2,"nombre":"2do. Grupo" }, 
                    7:{"id":7,"id_curso":2,"nombre":"Varones" }, 
                    8:{"id":8,"id_curso":2,"nombre":"Hembras" }, 
           }

horario_general={1:{"id":1,"nombre":"Horario General","hr_ini":"07:00","hr_fin":"18:00", 
                                "lunes_1":1, "hr_valor":40, "days":[1, 2, 3, 4, 5]}}

horario_receso={1:{"id":1,"minutos":10, "dia":1,"slot":2}, 
                            2:{"id":2,"minutos":10, "dia":1,"slot":4},   
                            3:{"id":3,"minutos":15, "dia":2,"slot":2}, 
                            4:{"id":4,"minutos":15, "dia":2,"slot":5}, 
                            5:{"id":5,"minutos":10, "dia":3,"slot":2}, 
                            6:{"id":6,"minutos":10, "dia":3,"slot":4}, 
                            7:{"id":7,"minutos":15, "dia":4,"slot":2}, 
                            8:{"id":8,"minutos":15, "dia":4,"slot":5}, 
                            9:{"id":9,"minutos":10, "dia":5,"slot":2}, 
                            10:{"id":10,"minutos":10, "dia":5,"slot":4},                             
                }

aula={1:{"id":1,"nombre":"Salon de 7mo"}, 
      2:{"id":2,"nombre":"Salon de 8vo"}, 
      3:{"id":3,"nombre":"Salon de 9no"}, 
      3:{"id":3,"nombre":"Lab. Biologia", "compartido":1}, 
      3:{"id":3,"nombre":"Lab. Dibujo", "compartido":1}, 
      3:{"id":3,"nombre":"Cancha", "compartido":1}, 
      
      }

materia={1:{"id":1,"nombre":"Castellano"}, 
                    2:{"id":2,"nombre":"Matematica"}, 
                    3:{"id":3,"nombre":"Ingles"}, 
                    4:{"id":4,"nombre":"Hist. de Venezuela"}, 
                    5:{"id":5,"nombre":"Geografia"}, 
                    6:{"id":6,"nombre":"Ciencias Biologicas"}, 
                    7:{"id":7,"nombre":"Dibujo Tecnico", "compartido":1}, 
                    8:{"id":8,"nombre":"Contabilidad", "compartido":1}, 
                    9:{"id":9,"nombre":"Educacion Fisica", "compartido":1}, 
                    10:{"id":10,"nombre":"Computacion", "compartido":1}, 
                    11:{"id":11,"nombre":"Ciencias de la Tierra"}, 
                    12:{"id":12,"nombre":"Catedra Bolivariana"}, 
                    13:{"id":13,"nombre":"Historia Universal"}, 
                    14:{"id":14,"nombre":"Educacion para la Salud"}, 
                    15:{"id":15,"nombre":"Geografia Economica"}, 
                    16:{"id":16,"nombre":"Educacion Artistica"}, 
                    17:{"id":17,"nombre":"Fisica"}, 
                    18:{"id":18,"nombre":"Quimica"}, 
                }

materia_curso={ 1:{"id":1,"id_curso":1, "id_materia":1, "nro_hrs_sem":4}, 
                2:{"id":2,"id_curso":1, "id_materia":2, "nro_hrs_sem":4}, 
                3:{"id":3,"id_curso":1, "id_materia":3, "nro_hrs_sem":3}, 
                4:{"id":4,"id_curso":1, "id_materia":4, "nro_hrs_sem":2}, 
                5:{"id":5,"id_curso":1, "id_materia":5, "nro_hrs_sem":2}, 
                6:{"id":6,"id_curso":1, "id_materia":6, "nro_hrs_sem":4}, 
                7:{"id":7,"id_curso":1, "id_materia":7, "nro_hrs_sem":2}, 
                8:{"id":8,"id_curso":1, "id_materia":8, "nro_hrs_sem":2}, 
                9:{"id":9,"id_curso":1, "id_materia":9, "nro_hrs_sem":2}, 
                10:{"id":10,"id_curso":1, "id_materia":10, "nro_hrs_sem":2}, 
                        
                    }

profesor={1:{"id":1,"nombre":"Pedro J.", "id_materia":1}, 
          2:{"id":2,"nombre":"Maria H.", "id_materia":2}, 
          3:{"id":3,"nombre":"Angela M.", "id_materia":3}, 
          4:{"id":4,"nombre":"Juan J.", "id_materia":[4, 13]},                   
          5:{"id":5,"nombre":"Josefa C.", "id_materia":6}, 
          6:{"id":6,"nombre":"Maria H.", "id_materia":7}, 
          7:{"id":7,"nombre":"Gerald S.", "id_materia":8}, 
          8:{"id":8,"nombre":"Frank P.", "id_materia":9},                   
          9:{"id":9,"nombre":"Karina S.", "id_materia":10},       
          10:{"id":10,"nombre":"Prof. Key", "id_materia":18},       
                }

profesor_rest={1:{"id":1,"id_profesor":1, "dia":1, "slot":[1, 2, 3]}, 
                  2:{"id":2,"id_profesor":1, "dia":3, "slot":[5, 6]}, 
                  3:{"id":3,"id_profesor":2, "dia":2, "slot":[  4, 5]}, 
                  4:{"id":4,"id_profesor":2, "dia":4, "slot":[7, 8]},
                  5:{"id":5,"id_profesor":3, "dia":1, "slot":[ 1, 2, 3, 4]}, 
                  6:{"id":6,"id_profesor":4, "dia":5, "slot":[4, 5]},
                }

def gen_slots():
    slots={}
    dias=len(horario_general[1]["days"])
    valor_gral=horario_general[1]["hr_valor"]    
    losdias={1:"Lunes",2:"Martes",3:"Miercoles",4:"Jueves",5:"Viernes", }    
    sched_d=[]
    sched_s={}
    for j in range(1, dias+1):        
        sched_d.append(str(j)+"\n"+losdias[j])            
        tmp=[]
        stritime=datetime.strptime(horario_general[1]["hr_ini"],"%I:%M")
        hrftime=stritime + timedelta(minutes=valor_gral)
        itime=stritime.strftime("%I:%M")
        ftime=hrftime.strftime("%I:%M")
        for i in range(1, 18):                        
            #print "valores: ", itime, ftime
        #print i
            tmp.append((itime+'-'+ftime, ''))
            for k in horario_receso.iteritems():
                if k[1]["slot"]==i and k[1]["dia"]==j:                    
                    valor=k[1]["minutos"]                     
                    #print "slot:%s dia: %s minutos: %s" % ( i, j, valor)
                    itime=datetime.strptime(ftime,  "%I:%M" )+timedelta(minutes=valor)                    
                    itime=itime.strftime("%I:%M")
                    break
                else:
                    itime=ftime
            ftime=datetime.strptime(itime,  "%I:%M" )+timedelta(minutes=valor_gral)
            ftime=ftime.strftime("%I:%M")
        sched_s[j]=tmp
    return sched_s

#time.strptime("07:00", "%H:%M")
"""
                      
                lunes       martes   miercoles  jueves  viernes
AULA 1 slot1   Castellano
AULA 1 slot2   Castellano
AULA 1 slot3   Matematica        
AULA 1 slot4   Matematica
AULA 1 slot5   receso

AULA 2 slot1   Castellano
AULA 2 slot2   Castellano
AULA 2 slot3   Matematica        
AULA 2 slot4   Matematica
AULA 2 slot5   receso

.
.
.

For each Course
    For each available Teacher
        For each available Classroom
           Select the first Classroom available and book the resource.
           Update the course and teachers availability.
        end Classrooms
    end Teachers
end Courses

"""