from django.db import models


class DEFINITION(models.Model):
    def_id = models.IntegerField()
    title = models.CharField(max_length=100, blank=True)
    category = models.BinaryField(1)
    def_text = models.CharField(max_length=100)

    def __str__(self):
        return self.def_id

sql = 'INSERT INTO `definition`(`def_id`, `title`, `category`, `def_text`) VALUES ("1","%s","%s","%s")'


class ORGANIZATION(models.Model):
    org_id = models.IntegerField()
    title = models.CharField(max_length=100)
    name_proc = models.CharField(max_length=100)
    child_id = models.IntegerField()
    org_name = models.CharField(max_length=100)
    org_task = models.CharField(max_length=100)
    parent_id = models.IntegerField()
    org_type = models.BinaryField()

    def __str__(self):
        return self.org_id
sql = 'INSERT INTO `organization`(`org_id`, `title`, `name_proc`, `child_id`, `org_name`, `org_task`, `parent_id`, `org_type`)' \
      ' VALUES  ("test","test","test","test","test","%S","%S","%s")'


class STATUS(models.Model):
    parent_id = models.IntegerField()
    parent_name = models.CharField(max_length=100)
    child_id = models.IntegerField()
    child_name = models.CharField(max_length=100)

    def __str__(self):
        return self.parent_id

sql = 'INSERT INTO `status`(`parent_id`, `parent_name`, `child_id`, `child_name`) VALUES ("test","test","test","test")'


class LAWS_DOC(models.Model):
    laws_id = models.IntegerField()
    made = models.IntegerField()
    tabsare = models.CharField(max_length=100)
    org_id = models.IntegerField()

    def __str__(self):
        return self.laws_id


sql = 'INSERT INTO `laws_doc`(`laws_id`, `made`, `tabsare`, `org_id`) VALUES ("%s","%s","%s","%s")'

# Create your models here.
