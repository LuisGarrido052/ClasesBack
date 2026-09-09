from django.db import models
from django.utils import timezone # Esto para rescatar la fecha y hora del sistema
from NegocioModel.choices import sexos

# Create your models here.
class Cargo(models.Model):
    nombre = models.CharField(max_length=100,verbase_name='Nombre del cargo')
    creado = models.DateTimeField(default=timezone.now) #OBTENEMOS LA FECHA Y HORA DEL SISTEMA
    

    def __str__(self):
        return"{}".format(self.nombre)

    class Meta:
        db_table = 'cargo' #Nombre con el que se crea la tabla
        verbose_name = 'Cargo' #Nombre que se muestra en el panel de administración
        verbose_name_plural = 'Cargos' #Nombre que se muestra en  plural

class Departamento(models.Model):
    codigo= models.BigAutoField(primary_key=True)
    nombre= models.CharField(max_length=100,verbose_name='Nombre del departamento')
    creado= models.DateTimeField(default=timezone.now) #OBTENEMOS LA FECHA Y HORA DEL SISTEMA

    def __str__(self):
        return"{}".format(self.nombre)

    class Meta:
        db_table = 'departamento' #Nombre con el que se crea la tabla
        verbose_name = 'Departamento' #Nombre que se muestra en el panel de administración
        verbose_name_plural = 'Departamentos' #Nombre que se muestra en  plural

class Empleado(models.Model):
    run= models.CharField(max_length=10,verbose_name='RUN del empleado')
    nombre= models.CharField(max_length=100,verbose_name='Nombre del empleado')
    parterno= models.CharField(max_length=100,verbose_name='Apellido paterno del empleado')
    materno= models.CharField(max_length=100,verbose_name='Apellido materno del empleado')
    sexo= models.CharField(max_length=1,choices=sexos,default='m')
    codigoEmpleado= models.CharField(max_length=20,verbose_name='Código del empleado')
    sueldo= models.PositiveBigIntegerField(default=450000,verbose_name='Sueldo del empleado')
    fechaNac= models.DateField(blank=True,null=True,verbose_name='Fecha de nacimiento del empleado')
    cargo= models.ForeignKey(Cargo,null=False,on_delete=models.RESTRICT)
    departamento= models.ForeignKey(Departamento,null=True,on_delete=models.CASCADE)
    creado= models.DateTimeField(default=timezone.now) #OBTENEMOS LA FECHA Y HORA DEL SISTEMA

    def __str__(self):
        return"{} {} {}".format(self.nombre,self.parterno,self.materno)

    class Meta:
        db_table = 'empleado' #Nombre con el que se crea la tabla
        verbose_name = 'Empleado' #Nombre que se muestra en el panel de administración
        verbose_name_plural = 'Empleados' #Nombre que se muestra en  plural
        ordering = ['nombre','parterno','materno'] #Ordena por nombre apellido paterno y apellido materno
        