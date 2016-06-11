from django.contrib import admin

# Register your models here.

from .models import Departamento
admin.site.register(Departamento)

from .models import DepartamentoProjeto
admin.site.register(DepartamentoProjeto)

from .models import Dependente
admin.site.register(Dependente)

from .models import Empregado
admin.site.register(Empregado)

from .models import EmpregadoProjeto
admin.site.register(EmpregadoProjeto)

from .models import HistoricoSalario
admin.site.register(HistoricoSalario)

from .models import Projeto
admin.site.register(Projeto)
