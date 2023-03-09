from distutils.command.upload import upload
from email.mime import image
from tkinter import CASCADE
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.utils.text import slugify
from django.dispatch import receiver


