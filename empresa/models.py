# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models


class Departamento(models.Model):
    numero = models.AutoField(db_column='NUMERO', primary_key=True)  # Field name made lowercase.
    nome = models.CharField(db_column='NOME', max_length=50, blank=True, null=True)  # Field name made lowercase.
    rg_gerente = models.ForeignKey('Empregado', models.DO_NOTHING, db_column='RG_GERENTE', blank=True, null=True)  # Field name made lowercase.

    def __str__(self):
        return self.nome

    class Meta:
        managed = False
        db_table = 'departamento'


class DepartamentoProjeto(models.Model):
    codigo = models.AutoField(db_column='CODIGO', primary_key=True)  # Field name made lowercase.
    numero_depto = models.ForeignKey(Departamento, models.DO_NOTHING, db_column='NUMERO_DEPTO')  # Field name made lowercase.
    numero_projeto = models.ForeignKey('Projeto', models.DO_NOTHING, db_column='NUMERO_PROJETO')  # Field name made lowercase.
    def __str__(self):
        return self.numero_projeto.nome+" - "+self.numero_depto.nome
    class Meta:
        managed = False
        db_table = 'departamento_projeto'


class Dependente(models.Model):
    codigo = models.AutoField(db_column='CODIGO', primary_key=True)  # Field name made lowercase.
    rg_responsavel = models.ForeignKey('Empregado', models.DO_NOTHING, db_column='RG_RESPONSAVEL')  # Field name made lowercase.
    nome_dependente = models.CharField(db_column='NOME_DEPENDENTE', max_length=50, blank=True, null=True)  # Field name made lowercase.
    nascimento = models.DateField(db_column='NASCIMENTO', blank=True, null=True)  # Field name made lowercase.
    relacao = models.CharField(db_column='RELACAO', max_length=10, blank=True, null=True)  # Field name made lowercase.
    sexo = models.CharField(db_column='SEXO', max_length=1, blank=True, null=True)  # Field name made lowercase.
    def __str__(self):
        return self.nome_dependente

    class Meta:
        managed = False
        db_table = 'dependente'


class Empregado(models.Model):
    rg = models.IntegerField(db_column='RG', primary_key=True)  # Field name made lowercase.
    nome = models.CharField(db_column='NOME', max_length=50, blank=True, null=True)  # Field name made lowercase.
    cpf = models.CharField(db_column='CPF', max_length=10, blank=True, null=True)  # Field name made lowercase.
    depto = models.ForeignKey(Departamento, models.DO_NOTHING, db_column='DEPTO', blank=True, null=True)  # Field name made lowercase.
    rg_supervisor = models.ForeignKey('self', models.DO_NOTHING, db_column='RG_SUPERVISOR', blank=True, null=True)  # Field name made lowercase.
    salario = models.DecimalField(db_column='SALARIO', max_digits=12, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    dat_ini_sal = models.DateField(db_column='DAT_INI_SAL', blank=True, null=True)  # Field name made lowercase.
    
    def __str__(self):
        return self.nome

    class Meta:
        managed = False
        db_table = 'empregado'


class EmpregadoProjeto(models.Model):
    codigo = models.AutoField(db_column='CODIGO', primary_key=True)  # Field name made lowercase.
    rg_empregado = models.ForeignKey(Empregado, models.DO_NOTHING, db_column='RG_EMPREGADO')  # Field name made lowercase.
    numero_projeto = models.ForeignKey('Projeto', models.DO_NOTHING, db_column='NUMERO_PROJETO')  # Field name made lowercase.
    horas = models.IntegerField(db_column='HORAS', blank=True, null=True)  # Field name made lowercase.

    def __str__(self):
        return self.numero_projeto.nome+" - "+self.rg_empregado.nome
		
    class Meta:
        managed = False
        db_table = 'empregado_projeto'


class HistoricoSalario(models.Model):
    codigo = models.AutoField(db_column='CODIGO', primary_key=True)  # Field name made lowercase.
    rg = models.ForeignKey(Empregado, models.DO_NOTHING, db_column='RG')  # Field name made lowercase.
    dat_ini_sal = models.DateField(db_column='DAT_INI_SAL')  # Field name made lowercase.
    dat_fim_sal = models.DateField(db_column='DAT_FIM_SAL')  # Field name made lowercase.
    salario = models.DecimalField(db_column='SALARIO', max_digits=10, decimal_places=2)  # Field name made lowercase.
    def __str__(self):
        return self.rg.nome+" \t\t teve salario de : "+str(self.salario)+" até "+str(self.dat_fim_sal)
    class Meta:
        managed = False
        db_table = 'historico_salario'
        unique_together = (('rg', 'dat_ini_sal'),)


class Projeto(models.Model):
    numero = models.AutoField(db_column='NUMERO', primary_key=True)  # Field name made lowercase.
    nome = models.CharField(db_column='NOME', max_length=50, blank=True, null=True)  # Field name made lowercase.
    localizacao = models.CharField(db_column='LOCALIZACAO', max_length=50, blank=True, null=True)  # Field name made lowercase.
    def __str__(self):
        return self.nome
    class Meta:
        managed = False
        db_table = 'projeto'

