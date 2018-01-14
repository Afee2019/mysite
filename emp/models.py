# encoding: utf-8

from django.db import models

# Create your models here.


# class Dept(models.Model):
#     dept_no = models.IntegerField(verbose_name='部门编号')
#     name = models.CharField(max_length=50, verbose_name='部门名称')
#
#     def __str__(self):
#         return self.name
#
#
#
# class Emp(models.Model):
#     emp_no = models.IntegerField(verbose_name='工号')
#     name = models.CharField(max_length=10, verbose_name='姓名')
#     gender = models.CharField(max_length=2, verbose_name='性别')
#     dept = models.ForeignKey(Dept,verbose_name='部门', on_delete=models.CASCADE)
#     email = models.CharField(max_length=25, blank=True, null=True, verbose_name='邮箱')
#
#     def __str__(self):
#         return self.name

class e_Staff(models.Model):
    StaffID = models.IntegerField(verbose_name='编号', primary_key=True)
    StaffCode = models.CharField(max_length=50, verbose_name='工号')
    Sex = models.IntegerField(verbose_name='性别')
    StaffName = models.CharField(max_length=50, verbose_name='姓名')
    IDcardNum = models.CharField(max_length=20, verbose_name='身份证')
    PostAct = models.IntegerField()
    Birthday = models.DateField(verbose_name='生日', null=True)
    NativePlace = models.CharField(max_length=50, verbose_name='籍贯')
    DoorAddress = models.CharField(max_length=200, verbose_name='家庭住址')
    NowAddress = models.CharField(max_length=200, verbose_name='现住址')
    MailCode = models.CharField(max_length=10, verbose_name='邮政编码')
    ArchivesAddress = models.CharField(max_length=200)
    PhotoID = models.CharField(max_length=200)
    Remark = models.CharField(max_length=200)
    BideCar = models.CharField(max_length=50)
    MarriageType = models.IntegerField(verbose_name='婚姻状况')
    NationalityID = models.CharField(max_length=50)
    SchoolAge = models.IntegerField()
    DoorType = models.IntegerField()
    PolityType = models.IntegerField(verbose_name='政治面貌')
    InpartyDate = models.DateField(verbose_name='入党时间')
    WorkAddressID = models.IntegerField()
    CasteName = models.IntegerField()
    Isdelete = models.SmallIntegerField(verbose_name='删除标志')
    IsGis = models.IntegerField()
    IsBaoxian = models.IntegerField()
    LeaveDate = models.DateField(verbose_name='离职时间')
    Regdate = models.DateField(verbose_name='入职时间')
    CwBaoBiaoType = models.IntegerField()

    def __str__(self):
         return self.StaffName

    class Meta:
        db_table = 'e_Staff'



