# # This is an auto-generated Django model module.
# # You'll have to do the following manually to clean this up:
# #   * Rearrange models' order
# #   * Make sure each model has one field with primary_key=True
# #   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
# #   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# # Feel free to rename the models, but don't rename db_table values or field names.
# from django.db import models


# class Accountbooks(models.Model):
#     book_name = models.CharField(db_column='Book_Name', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     branch_code = models.ForeignKey('Branches', models.DO_NOTHING, db_column='Branch_Code', primary_key=True)  # Field name made lowercase.
#     book_code = models.DecimalField(db_column='Book_Code', max_digits=2, decimal_places=0)  # Field name made lowercase.
#     active = models.TextField(db_column='Active', blank=True, null=True)  # Field name made lowercase. This field type is a guess.

#     class Meta:
#         managed = False
#         db_table = 'accountbooks'
#         unique_together = (('branch_code', 'book_code'),)


# class Accountperiods(models.Model):
#     trade_code = models.ForeignKey('Branchesprojects', models.DO_NOTHING, db_column='Trade_Code', blank=True, null=True)  # Field name made lowercase.
#     project_code = models.ForeignKey('Branchesprojects', models.DO_NOTHING, db_column='Project_Code', blank=True, null=True)  # Field name made lowercase.
#     branch_code = models.ForeignKey('Branchesprojects', models.DO_NOTHING, db_column='Branch_Code', blank=True, null=True)  # Field name made lowercase.
#     period_code = models.DecimalField(db_column='Period_Code', primary_key=True, max_digits=18, decimal_places=0)  # Field name made lowercase.
#     period_name = models.CharField(db_column='Period_Name', max_length=150, blank=True, null=True)  # Field name made lowercase.
#     startdate = models.DateField(db_column='StartDate', blank=True, null=True)  # Field name made lowercase.
#     enddate = models.DateField(db_column='EndDate', blank=True, null=True)  # Field name made lowercase.
#     active = models.TextField(db_column='Active', blank=True, null=True)  # Field name made lowercase. This field type is a guess.

#     class Meta:
#         managed = False
#         db_table = 'accountperiods'


# class Bankledger(models.Model):
#     period_code = models.DecimalField(db_column='Period_Code', max_digits=19, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
#     tran_no = models.DecimalField(db_column='Tran_No', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
#     check_slip_no = models.CharField(db_column='Check_Slip_No', max_length=25, blank=True, null=True)  # Field name made lowercase.

#     class Meta:
#         managed = False
#         db_table = 'bankledger'


# class Blockusingdocumentnos(models.Model):
#     trade_code = models.DecimalField(db_column='Trade_Code', max_digits=2, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
#     project_code = models.DecimalField(db_column='Project_Code', max_digits=4, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
#     branch_code = models.DecimalField(db_column='Branch_Code', max_digits=4, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
#     period_code = models.DecimalField(db_column='Period_Code', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
#     tran_no = models.DecimalField(db_column='Tran_No', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
#     tabletype = models.CharField(db_column='TableType', max_length=3, blank=True, null=True)  # Field name made lowercase.
#     network = models.CharField(db_column='Network', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     computername = models.CharField(db_column='ComputerName', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     branch = models.DecimalField(db_column='Branch', max_digits=4, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
#     terminalcode = models.DecimalField(db_column='TerminalCode', max_digits=3, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
#     usercode = models.CharField(db_column='UserCode', max_length=7, blank=True, null=True)  # Field name made lowercase.
#     formname = models.CharField(db_column='FormName', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     formno = models.IntegerField(db_column='FormNo', blank=True, null=True)  # Field name made lowercase.
#     tabno = models.IntegerField(db_column='TabNo', blank=True, null=True)  # Field name made lowercase.
#     active = models.TextField(db_column='Active', blank=True, null=True)  # Field name made lowercase. This field type is a guess.

#     class Meta:
#         managed = False
#         db_table = 'blockusingdocumentnos'


# class Blockusingids(models.Model):
#     trade_code = models.DecimalField(db_column='Trade_Code', max_digits=2, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
#     project_code = models.DecimalField(db_column='Project_Code', max_digits=4, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
#     branch_code = models.DecimalField(db_column='Branch_Code', max_digits=4, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
#     book_code = models.DecimalField(db_column='Book_Code', max_digits=2, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
#     tran_no = models.DecimalField(db_column='Tran_No', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
#     tabletype = models.CharField(db_column='TableType', max_length=3, blank=True, null=True)  # Field name made lowercase.
#     network = models.CharField(db_column='Network', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     computer_name = models.CharField(db_column='Computer_Name', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     branch = models.DecimalField(db_column='Branch', max_digits=4, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
#     terminal_code = models.DecimalField(db_column='Terminal_Code', max_digits=3, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
#     user_code = models.CharField(db_column='User_Code', max_length=7, blank=True, null=True)  # Field name made lowercase.
#     form_name = models.CharField(db_column='Form_Name', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     form_no = models.IntegerField(db_column='Form_No', blank=True, null=True)  # Field name made lowercase.
#     tab_no = models.IntegerField(db_column='Tab_No', blank=True, null=True)  # Field name made lowercase.
#     active = models.TextField(db_column='Active', blank=True, null=True)  # Field name made lowercase. This field type is a guess.

#     class Meta:
#         managed = False
#         db_table = 'blockusingids'


# class Branches(models.Model):
#     branch_name = models.CharField(db_column='Branch_Name', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     branch_code = models.DecimalField(db_column='Branch_Code', primary_key=True, max_digits=4, decimal_places=0)  # Field name made lowercase.
#     active = models.TextField(db_column='Active', blank=True, null=True)  # Field name made lowercase. This field type is a guess.

#     class Meta:
#         managed = False
#         db_table = 'branches'


# class Branchesprojects(models.Model):
#     trade_code = models.ForeignKey('Projects', models.DO_NOTHING, db_column='Trade_Code', primary_key=True)  # Field name made lowercase.
#     project_code = models.ForeignKey('Projects', models.DO_NOTHING, db_column='Project_Code')  # Field name made lowercase.
#     branch_code = models.ForeignKey(Branches, models.DO_NOTHING, db_column='Branch_Code')  # Field name made lowercase.
#     allowedbranch = models.TextField(db_column='AllowedBranch', blank=True, null=True)  # Field name made lowercase. This field type is a guess.

#     class Meta:
#         managed = False
#         db_table = 'branchesprojects'
#         unique_together = (('trade_code', 'project_code', 'branch_code'),)


# class ClosedPeriod(models.Model):
#     acc_no = models.DecimalField(db_column='Acc_No', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
#     trade_code = models.DecimalField(db_column='Trade_Code', max_digits=2, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
#     project_code = models.DecimalField(db_column='Project_Code', max_digits=4, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
#     branch_code = models.DecimalField(db_column='Branch_Code', max_digits=4, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
#     book_code = models.DecimalField(db_column='Book_Code', max_digits=2, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
#     debit = models.DecimalField(db_column='Debit', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
#     credit = models.DecimalField(db_column='Credit', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.

#     class Meta:
#         managed = False
#         db_table = 'closed_period'


# class Dayperiods(models.Model):
#     period_code = models.ForeignKey(Accountperiods, models.DO_NOTHING, db_column='Period_Code', primary_key=True)  # Field name made lowercase.
#     dayperiod_code = models.DecimalField(db_column='DayPeriod_Code', max_digits=3, decimal_places=0)  # Field name made lowercase.
#     dayperiod_name = models.CharField(db_column='DayPeriod_Name', max_length=150, blank=True, null=True)  # Field name made lowercase.
#     maxdays = models.DecimalField(db_column='MaxDays', max_digits=3, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
#     active = models.TextField(db_column='Active', blank=True, null=True)  # Field name made lowercase. This field type is a guess.

#     class Meta:
#         managed = False
#         db_table = 'dayperiods'
#         unique_together = (('period_code', 'dayperiod_code'),)


# class Documentnos(models.Model):
#     trade_code = models.DecimalField(db_column='Trade_Code', max_digits=2, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
#     project_code = models.DecimalField(db_column='Project_Code', max_digits=4, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
#     branch_code = models.DecimalField(db_column='Branch_Code', max_digits=4, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
#     period_code = models.DecimalField(db_column='Period_Code', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
#     docnos = models.DecimalField(db_column='DocNos', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
#     status = models.TextField(db_column='Status', blank=True, null=True)  # Field name made lowercase. This field type is a guess.

#     class Meta:
#         managed = False
#         db_table = 'documentnos'


# class Genledgers(models.Model):
#     period_code = models.ForeignKey('Journals', models.DO_NOTHING, db_column='Period_Code', blank=True, null=True)  # Field name made lowercase.
#     tran_no = models.ForeignKey('Journals', models.DO_NOTHING, db_column='Tran_No', blank=True, null=True)  # Field name made lowercase.
#     entryno = models.DecimalField(db_column='EntryNo', max_digits=4, decimal_places=0)  # Field name made lowercase.
#     acc_no = models.ForeignKey('Trialbalance', models.DO_NOTHING, db_column='Acc_No', blank=True, null=True)  # Field name made lowercase.
#     debit = models.DecimalField(db_column='Debit', max_digits=25, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
#     credit = models.DecimalField(db_column='Credit', max_digits=25, decimal_places=2, blank=True, null=True)  # Field name made lowercase.

#     class Meta:
#         managed = False
#         db_table = 'genledgers'


# class Genledgerstemp(models.Model):
#     period_code = models.DecimalField(db_column='Period_Code', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
#     tran_no = models.DecimalField(db_column='Tran_No', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
#     entryno = models.DecimalField(db_column='EntryNo', max_digits=4, decimal_places=0)  # Field name made lowercase.
#     acc_no = models.DecimalField(db_column='Acc_No', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
#     debit = models.DecimalField(db_column='Debit', max_digits=25, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
#     credit = models.DecimalField(db_column='Credit', max_digits=25, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
#     trantype = models.CharField(db_column='TranType', max_length=10, blank=True, null=True)  # Field name made lowercase.

#     class Meta:
#         managed = False
#         db_table = 'genledgerstemp'


# class Idcounter(models.Model):
#     trade_code = models.DecimalField(db_column='Trade_Code', max_digits=2, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
#     project_code = models.DecimalField(db_column='Project_Code', max_digits=4, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
#     branch_code = models.DecimalField(db_column='Branch_Code', max_digits=4, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
#     book_code = models.DecimalField(db_column='Book_Code', max_digits=2, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
#     tran_no = models.DecimalField(db_column='Tran_No', max_digits=9, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
#     tran_type = models.CharField(db_column='Tran_Type', max_length=3, blank=True, null=True)  # Field name made lowercase.
#     status = models.CharField(db_column='Status', max_length=3, blank=True, null=True)  # Field name made lowercase.

#     class Meta:
#         managed = False
#         db_table = 'idcounter'


# class Journals(models.Model):
#     period_code = models.ForeignKey(Dayperiods, models.DO_NOTHING, db_column='Period_Code', primary_key=True)  # Field name made lowercase.
#     dayperiod_code = models.ForeignKey(Dayperiods, models.DO_NOTHING, db_column='DayPeriod_Code', blank=True, null=True)  # Field name made lowercase.
#     tran_no = models.DecimalField(db_column='Tran_No', max_digits=18, decimal_places=0)  # Field name made lowercase.
#     trandate = models.DateTimeField(db_column='TranDate', blank=True, null=True)  # Field name made lowercase.
#     naration = models.CharField(db_column='Naration', max_length=300, blank=True, null=True)  # Field name made lowercase.
#     trantype = models.CharField(db_column='TranType', max_length=3, blank=True, null=True)  # Field name made lowercase.
#     user_id = models.CharField(db_column='User_ID', max_length=7, blank=True, null=True)  # Field name made lowercase.

#     class Meta:
#         managed = False
#         db_table = 'journals'
#         unique_together = (('period_code', 'tran_no'),)


# class Lengthofcodes(models.Model):
#     trade_code = models.IntegerField(db_column='Trade_Code', blank=True, null=True)  # Field name made lowercase.
#     project_code = models.IntegerField(db_column='Project_Code', blank=True, null=True)  # Field name made lowercase.
#     branch_code = models.IntegerField(db_column='Branch_Code', blank=True, null=True)  # Field name made lowercase.
#     book_code = models.IntegerField(db_column='Book_Code', blank=True, null=True)  # Field name made lowercase.
#     idlength = models.IntegerField(db_column='IDLength', blank=True, null=True)  # Field name made lowercase.
#     nolength = models.IntegerField(db_column='NoLength', blank=True, null=True)  # Field name made lowercase.
#     period_code = models.IntegerField(db_column='Period_Code', blank=True, null=True)  # Field name made lowercase.
#     dayperiod_code = models.IntegerField(db_column='DayPeriod_Code', blank=True, null=True)  # Field name made lowercase.
#     othercodes = models.IntegerField(db_column='OtherCodes', blank=True, null=True)  # Field name made lowercase.

#     class Meta:
#         managed = False
#         db_table = 'lengthofcodes'


# class Mainsubheadlinks(models.Model):
#     subacc = models.ForeignKey('Subaccounts', models.DO_NOTHING, db_column='SubAcc', primary_key=True)  # Field name made lowercase.
#     mainacc = models.ForeignKey('Trialbalance', models.DO_NOTHING, db_column='MainAcc')  # Field name made lowercase.

#     class Meta:
#         managed = False
#         db_table = 'mainsubheadlinks'
#         unique_together = (('subacc', 'mainacc'),)


# class Projects(models.Model):
#     project_name = models.CharField(db_column='Project_Name', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     trade_code = models.DecimalField(db_column='Trade_Code', primary_key=True, max_digits=2, decimal_places=0)  # Field name made lowercase.
#     project_code = models.DecimalField(db_column='Project_Code', max_digits=4, decimal_places=0)  # Field name made lowercase.
#     active = models.TextField(db_column='Active', blank=True, null=True)  # Field name made lowercase. This field type is a guess.

#     class Meta:
#         managed = False
#         db_table = 'projects'
#         unique_together = (('trade_code', 'project_code'),)


# class Subaccounts(models.Model):
#     acc_no = models.DecimalField(db_column='Acc_No', primary_key=True, max_digits=18, decimal_places=0)  # Field name made lowercase.
#     title = models.CharField(db_column='Title', max_length=200, blank=True, null=True)  # Field name made lowercase.
#     active = models.TextField(db_column='Active', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
#     opendr = models.DecimalField(db_column='OpenDr', max_digits=20, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
#     opencr = models.DecimalField(db_column='OpenCr', max_digits=20, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
#     debit = models.DecimalField(db_column='Debit', max_digits=20, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
#     credit = models.DecimalField(db_column='Credit', max_digits=20, decimal_places=2, blank=True, null=True)  # Field name made lowercase.

#     class Meta:
#         managed = False
#         db_table = 'subaccounts'


# class Subheadlinks(models.Model):
#     subofsub = models.ForeignKey(Subaccounts, models.DO_NOTHING, db_column='SubofSub', primary_key=True)  # Field name made lowercase.
#     mainofsubacc = models.ForeignKey(Subaccounts, models.DO_NOTHING, db_column='MainofsubAcc')  # Field name made lowercase.

#     class Meta:
#         managed = False
#         db_table = 'subheadlinks'
#         unique_together = (('subofsub', 'mainofsubacc'),)


# class Subledgers(models.Model):
#     period_code = models.ForeignKey(Journals, models.DO_NOTHING, db_column='Period_Code', blank=True, null=True)  # Field name made lowercase.
#     tran_no = models.ForeignKey(Journals, models.DO_NOTHING, db_column='Tran_No', blank=True, null=True)  # Field name made lowercase.
#     entryno = models.DecimalField(db_column='EntryNo', max_digits=4, decimal_places=0)  # Field name made lowercase.
#     acc_no = models.ForeignKey(Subaccounts, models.DO_NOTHING, db_column='Acc_No', blank=True, null=True)  # Field name made lowercase.
#     debit = models.DecimalField(db_column='Debit', max_digits=20, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
#     credit = models.DecimalField(db_column='Credit', max_digits=20, decimal_places=2, blank=True, null=True)  # Field name made lowercase.

#     class Meta:
#         managed = False
#         db_table = 'subledgers'


# class Templock(models.Model):
#     period_code = models.DecimalField(db_column='Period_Code', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
#     dayperiod_code = models.DecimalField(db_column='DayPeriod_Code', max_digits=3, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
#     tranno = models.DecimalField(db_column='TranNo', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
#     tran_type = models.CharField(db_column='Tran_Type', max_length=3, blank=True, null=True)  # Field name made lowercase.

#     class Meta:
#         managed = False
#         db_table = 'templock'


# class TemporaryBankledger(models.Model):
#     period_code = models.DecimalField(db_column='Period_Code', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
#     tran_no = models.DecimalField(db_column='Tran_No', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
#     check_slip_no = models.CharField(db_column='Check_Slip_No', max_length=25, blank=True, null=True)  # Field name made lowercase.

#     class Meta:
#         managed = False
#         db_table = 'temporary_bankledger'


# class TemporaryGenledgers(models.Model):
#     period_code = models.ForeignKey('TemporaryJournals', models.DO_NOTHING, db_column='Period_Code', blank=True, null=True)  # Field name made lowercase.
#     tran_no = models.ForeignKey('TemporaryJournals', models.DO_NOTHING, db_column='Tran_No', blank=True, null=True)  # Field name made lowercase.
#     entryno = models.DecimalField(db_column='EntryNo', max_digits=4, decimal_places=0)  # Field name made lowercase.
#     acc_no = models.ForeignKey('Trialbalance', models.DO_NOTHING, db_column='Acc_No', blank=True, null=True)  # Field name made lowercase.
#     debit = models.DecimalField(db_column='Debit', max_digits=25, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
#     credit = models.DecimalField(db_column='Credit', max_digits=25, decimal_places=2, blank=True, null=True)  # Field name made lowercase.

#     class Meta:
#         managed = False
#         db_table = 'temporary_genledgers'


# class TemporaryJournals(models.Model):
#     period_code = models.ForeignKey(Dayperiods, models.DO_NOTHING, db_column='Period_Code', primary_key=True)  # Field name made lowercase.
#     dayperiod_code = models.ForeignKey(Dayperiods, models.DO_NOTHING, db_column='DayPeriod_Code', blank=True, null=True)  # Field name made lowercase.
#     tran_no = models.DecimalField(db_column='Tran_No', max_digits=18, decimal_places=0)  # Field name made lowercase.
#     trandate = models.DateTimeField(db_column='TranDate', blank=True, null=True)  # Field name made lowercase.
#     naration = models.CharField(db_column='Naration', max_length=300, blank=True, null=True)  # Field name made lowercase.
#     trantype = models.CharField(db_column='TranType', max_length=3, blank=True, null=True)  # Field name made lowercase.
#     user_id = models.CharField(db_column='User_ID', max_length=7, blank=True, null=True)  # Field name made lowercase.

#     class Meta:
#         managed = False
#         db_table = 'temporary_journals'
#         unique_together = (('period_code', 'tran_no'),)


# class TemporaryJournalsEditing(models.Model):
#     period_code = models.DecimalField(db_column='Period_Code', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
#     dayperiod_code = models.DecimalField(db_column='DayPeriod_Code', max_digits=3, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
#     tran_no = models.DecimalField(db_column='Tran_No', max_digits=18, decimal_places=0)  # Field name made lowercase.
#     trandate = models.DateTimeField(db_column='TranDate', blank=True, null=True)  # Field name made lowercase.
#     naration = models.CharField(db_column='Naration', max_length=300, blank=True, null=True)  # Field name made lowercase.
#     trantype = models.CharField(db_column='TranType', max_length=3, blank=True, null=True)  # Field name made lowercase.
#     user_id = models.CharField(db_column='User_ID', max_length=7, blank=True, null=True)  # Field name made lowercase.

#     class Meta:
#         managed = False
#         db_table = 'temporary_journals_editing'


# class TemporarySubledgers(models.Model):
#     period_code = models.ForeignKey(TemporaryJournals, models.DO_NOTHING, db_column='Period_Code', blank=True, null=True)  # Field name made lowercase.
#     tran_no = models.ForeignKey(TemporaryJournals, models.DO_NOTHING, db_column='Tran_No', blank=True, null=True)  # Field name made lowercase.
#     entryno = models.DecimalField(db_column='EntryNo', max_digits=4, decimal_places=0)  # Field name made lowercase.
#     acc_no = models.ForeignKey(Subaccounts, models.DO_NOTHING, db_column='Acc_No', blank=True, null=True)  # Field name made lowercase.
#     debit = models.DecimalField(db_column='Debit', max_digits=20, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
#     credit = models.DecimalField(db_column='Credit', max_digits=20, decimal_places=2, blank=True, null=True)  # Field name made lowercase.

#     class Meta:
#         managed = False
#         db_table = 'temporary_subledgers'


# class Trades(models.Model):
#     trade_name = models.CharField(db_column='Trade_Name', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     trade_code = models.DecimalField(db_column='Trade_Code', primary_key=True, max_digits=2, decimal_places=0)  # Field name made lowercase.
#     active = models.TextField(db_column='Active', blank=True, null=True)  # Field name made lowercase. This field type is a guess.

#     class Meta:
#         managed = False
#         db_table = 'trades'


# class TransactionsTypes(models.Model):
#     tran_code = models.IntegerField(db_column='Tran_Code', blank=True, null=True)  # Field name made lowercase.
#     tran_type = models.CharField(db_column='Tran_Type', max_length=10, blank=True, null=True)  # Field name made lowercase.
#     tvrt = models.CharField(db_column='TVrT', max_length=10, blank=True, null=True)  # Field name made lowercase.

#     class Meta:
#         managed = False
#         db_table = 'transactions_types'


# class Trialbalance(models.Model):
#     acc_no = models.DecimalField(db_column='Acc_No', primary_key=True, max_digits=18, decimal_places=0)  # Field name made lowercase.
#     trade_code = models.ForeignKey(Projects, models.DO_NOTHING, db_column='Trade_Code', blank=True, null=True)  # Field name made lowercase.
#     project_code = models.ForeignKey(Projects, models.DO_NOTHING, db_column='Project_Code', blank=True, null=True)  # Field name made lowercase.
#     branch_code = models.ForeignKey(Accountbooks, models.DO_NOTHING, db_column='Branch_Code', blank=True, null=True)  # Field name made lowercase.
#     book_code = models.ForeignKey(Accountbooks, models.DO_NOTHING, db_column='Book_Code', blank=True, null=True)  # Field name made lowercase.
#     title = models.CharField(db_column='Title', max_length=200, blank=True, null=True)  # Field name made lowercase.
#     acc_nature = models.CharField(db_column='Acc_Nature', max_length=1, blank=True, null=True)  # Field name made lowercase.
#     acc_type = models.CharField(db_column='Acc_Type', max_length=3, blank=True, null=True)  # Field name made lowercase.
#     active = models.TextField(db_column='Active', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
#     opendr = models.DecimalField(db_column='OpenDr', max_digits=25, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
#     opencr = models.DecimalField(db_column='OpenCr', max_digits=25, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
#     debit = models.DecimalField(db_column='Debit', max_digits=25, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
#     credit = models.DecimalField(db_column='Credit', max_digits=25, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
#     adjdr = models.DecimalField(db_column='AdjDr', max_digits=25, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
#     adjcr = models.DecimalField(db_column='AdjCr', max_digits=25, decimal_places=2, blank=True, null=True)  # Field name made lowercase.

#     class Meta:
#         managed = False
#         db_table = 'trialbalance'


# class Yearsystem(models.Model):
#     period_code = models.ForeignKey(Accountperiods, models.DO_NOTHING, db_column='Period_Code')  # Field name made lowercase.
#     no = models.DecimalField(db_column='No', max_digits=2, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
#     months = models.CharField(db_column='Months', max_length=15, blank=True, null=True)  # Field name made lowercase.
#     callno = models.DecimalField(db_column='CallNo', max_digits=2, decimal_places=0, blank=True, null=True)  # Field name made lowercase.

#     class Meta:
#         managed = False
#         db_table = 'yearsystem'
