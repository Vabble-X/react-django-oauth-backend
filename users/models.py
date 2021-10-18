from django.db import models

class Users(models.Model):
    email = models.CharField(max_length=100, blank=False, default='')
    password = models.CharField(max_length=100, blank=False, default='')
    role = models.IntegerField(max_length=10, blank=False, default='')

    class Meta():
        db_table = 'users'

    # CREATE TABLE "users" (
    # 	"id"	INTEGER NOT NULL,
    # 	"email"	TEXT,
    # 	"password"	TEXT,
    # 	"role"	TEXT,
    # 	PRIMARY KEY("id" AUTOINCREMENT)
    # );