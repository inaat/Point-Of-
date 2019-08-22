# # This is an auto-generated Django model module.
# # You'll have to do the following manually to clean this up:
# #   * Rearrange models' order
# #   * Make sure each model has one field with primary_key=True
# #   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
# #   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# # Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models



# class Attsejma(models.Model):
#     lur = models.CharField(db_column='LUR', max_length=100, blank=True, null=True)  # Field name made lowercase.
#     seruman = models.CharField(db_column='SeruMan', max_length=60, blank=True, null=True)  # Field name made lowercase.
#     wordpass = models.CharField(max_length=50, blank=True, null=True)
#     aut_one = models.CharField(db_column='Aut_One', max_length=25, blank=True, null=True)  # Field name made lowercase.
#     aut_two = models.CharField(db_column='Aut_Two', max_length=25, blank=True, null=True)  # Field name made lowercase.
#     aut_three = models.CharField(db_column='Aut_Three', max_length=25, blank=True, null=True)  # Field name made lowercase.

#     class Meta:
#         managed = False
#         db_table = 'attsejma'
#         app_label = 'genprocandfunctions'


# class Autologin(models.Model):
#     trade_code = models.DecimalField(db_column='Trade_Code', max_digits=4, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
#     project_code = models.DecimalField(db_column='Project_Code', max_digits=4, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
#     branch_code = models.DecimalField(db_column='Branch_Code', max_digits=4, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
#     terminal_code = models.DecimalField(db_column='Terminal_Code', max_digits=4, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
#     usercode = models.CharField(db_column='UserCode', max_length=7, blank=True, null=True)  # Field name made lowercase.
#     computer_name = models.CharField(db_column='Computer_Name', max_length=50, blank=True, null=True)  # Field name made lowercase.

#     class Meta:
#         managed = False
#         db_table = 'autologin'
#         app_label = 'genprocandfunctions'


# class Departments(models.Model):
#     dept_name = models.CharField(db_column='Dept_Name', max_length=30, blank=True, null=True)  # Field name made lowercase.
#     dept_code = models.DecimalField(db_column='Dept1_Code', primary_key=True, max_digits=4, decimal_places=0)  # Field name made lowercase.
#     active = models.TextField(db_column='Active', blank=True, null=True)  # Field name made lowercase. This field type is a guess.

#     class Meta:
#         managed = False
#         db_table = 'departments'
#         app_label = 'genprocandfunctions'


# class Deptsections(models.Model):
#     section_name = models.CharField(db_column='Section_Name', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     dept_code = models.DecimalField(db_column='Dept2_Code', primary_key=True, max_digits=4, decimal_places=0)  # Field name made lowercase.
#     sec_code = models.DecimalField(db_column='Sec_Code', max_digits=4, decimal_places=0)  # Field name made lowercase.
#     active = models.TextField(db_column='Active', blank=True, null=True)  # Field name made lowercase. This field type is a guess.

#     class Meta:
#         managed = False
#         db_table = 'deptsections'
#         unique_together = (('dept_code', 'sec_code'),)
#         app_label = 'genprocandfunctions'


# class Formtasks(models.Model):
#     formname = models.CharField(db_column='FormName', primary_key=True, max_length=50)  # Field name made lowercase.
#     dept_code = models.ForeignKey('Sectiontasks', models.DO_NOTHING, db_column='Dept3_Code')  # Field name made lowercase.
#     sec_code = models.ForeignKey('Sectiontasks', models.DO_NOTHING, db_column='Sec_Code')  # Field name made lowercase.
#     task_code = models.ForeignKey('Sectiontasks', models.DO_NOTHING, db_column='Task_Code')  # Field name made lowercase.
#     tasktab = models.DecimalField(db_column='TaskTab', max_digits=4, decimal_places=0)  # Field name made lowercase.
#     active = models.TextField(db_column='Active', blank=True, null=True)  # Field name made lowercase. This field type is a guess.

#     class Meta:
#         managed = False
#         db_table = 'formtasks'
#         unique_together = (('formname', 'tasktab'),)
#         app_label = 'genprocandfunctions'


# class Freesejma(models.Model):
#     lur = models.CharField(db_column='LUR', max_length=100, blank=True, null=True)  # Field name made lowercase.
#     seruman = models.CharField(db_column='SeruMan', max_length=60, blank=True, null=True)  # Field name made lowercase.
#     wordpass = models.CharField(max_length=50, blank=True, null=True)
#     aut_one = models.CharField(db_column='Aut_One', max_length=25, blank=True, null=True)  # Field name made lowercase.
#     aut_two = models.CharField(db_column='Aut_Two', max_length=25, blank=True, null=True)  # Field name made lowercase.
#     aut_three = models.CharField(db_column='Aut_Three', max_length=25, blank=True, null=True)  # Field name made lowercase.

#     class Meta:
#         managed = False
#         db_table = 'freesejma'
#         app_label = 'genprocandfunctions'

class NhzUsers(models.Model):
    trade_code = models.DecimalField(db_column='Trade_Code', max_digits=4, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    project_code = models.DecimalField(db_column='Project_Code', max_digits=4, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    branch_code = models.DecimalField(db_column='Branch_Code', max_digits=4, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    user_id = models.CharField(db_column='User_ID', primary_key=True, max_length=7)  # Field name made lowercase.
    user_name = models.CharField(db_column='User_Name', unique=True, max_length=50, blank=True, null=True)  # Field name made lowercase.
    pass_word = models.CharField(db_column='Pass_Word', max_length=24, blank=True, null=True)  # Field name made lowercase.
    usertype = models.CharField(db_column='UserType', max_length=30, blank=True, null=True)  # Field name made lowercase.
    active = models.TextField(db_column='Active', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    title = models.CharField(db_column='Title', max_length=50, blank=True, null=True)  # Field name made lowercase.
    cell = models.CharField(db_column='Cell', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tele = models.CharField(db_column='Tele', max_length=40, blank=True, null=True)  # Field name made lowercase.
    photo = models.CharField(db_column='Photo', max_length=8000, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'nhz_users'
        app_label = 'genprocandfunctions'


# class Regions(models.Model):
#     branch_code = models.DecimalField(db_column='Branch_Code', max_digits=5, decimal_places=0)  # Field name made lowercase.
#     region_code = models.DecimalField(db_column='Region_Code', primary_key=True, max_digits=5, decimal_places=0)  # Field name made lowercase.
#     region_name = models.CharField(db_column='Region_Name', max_length=100, blank=True, null=True)  # Field name made lowercase.
#     active = models.TextField(db_column='Active', blank=True, null=True)  # Field name made lowercase. This field type is a guess.

#     class Meta:
#         managed = False
#         db_table = 'regions'
#         app_label = 'genprocandfunctions'


# class RptHd(models.Model):
#     rpt_lg_name = models.CharField(db_column='rpt_LG_Name', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     rpt_lg = models.CharField(db_column='rpt_LG', max_length=6000, blank=True, null=True)  # Field name made lowercase.

#     class Meta:
#         managed = False
#         db_table = 'rpt_hd'
#         app_label = 'genprocandfunctions'


# class RptTitles(models.Model):
#     rpt_name = models.CharField(db_column='rpt_Name', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     rpttag = models.CharField(db_column='rptTag', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     rpt_lg = models.CharField(db_column='rpt_LG', max_length=50, blank=True, null=True)  # Field name made lowercase.

#     class Meta:
#         managed = False
#         db_table = 'rpt_titles'
#         app_label = 'genprocandfunctions'


# class Sectiontasks(models.Model):
#     task_name = models.CharField(db_column='Task_Name', unique=True, max_length=50, blank=True, null=True)  # Field name made lowercase.
#     dept_code = models.ForeignKey(Deptsections, models.DO_NOTHING, db_column='Dept4_Code', primary_key=True)  # Field name made lowercase.
#     sec_code = models.ForeignKey(Deptsections, models.DO_NOTHING, db_column='Sec_Code')  # Field name made lowercase.
#     task_code = models.DecimalField(db_column='Task_Code', max_digits=4, decimal_places=0)  # Field name made lowercase.
#     active = models.TextField(db_column='Active', blank=True, null=True)  # Field name made lowercase. This field type is a guess.

#     class Meta:
#         managed = False
#         db_table = 'sectiontasks'
#         unique_together = (('dept_code', 'sec_code', 'task_code'),)
#         app_label = 'genprocandfunctions'


# class UserLocations(models.Model):
#     location_name = models.CharField(db_column='Location_Name', unique=True, max_length=50)  # Field name made lowercase.
#     location_id = models.DecimalField(db_column='Location_ID', primary_key=True, max_digits=4, decimal_places=0)  # Field name made lowercase.
#     active = models.TextField(db_column='Active', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
#     status = models.TextField(db_column='Status', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
#     user_id = models.CharField(db_column='User_ID', max_length=7, blank=True, null=True)  # Field name made lowercase.
#     computer_name = models.CharField(db_column='Computer_Name', max_length=50, blank=True, null=True)  # Field name made lowercase.

#     class Meta:
#         managed = False
#         db_table = 'user_locations'
#         app_label = 'genprocandfunctions'


# class Usersrights(models.Model):
#     user = models.ForeignKey(NhzUsers, models.DO_NOTHING, db_column='User_ID', blank=True, null=True)  # Field name made lowercase.
#     trade_code = models.DecimalField(db_column='Trade_Code', max_digits=2, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
#     project_code = models.DecimalField(db_column='Project_Code', max_digits=4, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
#     branch_code = models.DecimalField(db_column='Branch_Code', max_digits=4, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
#     dept_code = models.ForeignKey(Sectiontasks, models.DO_NOTHING, db_column='Dept5_Code')  # Field name made lowercase.
#     sec_code = models.ForeignKey(Sectiontasks, models.DO_NOTHING, db_column='Sec_Code')  # Field name made lowercase.
#     task_code = models.ForeignKey(Sectiontasks, models.DO_NOTHING, db_column='Task_Code')  # Field name made lowercase.
#     reader = models.TextField(db_column='Reader', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
#     writer = models.TextField(db_column='Writer', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
#     updater = models.TextField(db_column='Updater', blank=True, null=True)  # Field name made lowercase. This field type is a guess.

#     class Meta:
#         managed = False
#         db_table = 'usersrights'
#         app_label = 'genprocandfunctions'
