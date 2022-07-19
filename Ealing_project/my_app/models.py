from django.db import models

# Create your models here.
class house(models.Model):
    profile_img = models.TextField() # 숙박이미지주소
    name = models.CharField(max_length=20) # 지역 이름
    content = models.CharField(max_length=40) # 힐링지 설명
    price = models.CharField(max_length=20) # 가격
    reputation = models.FloatField(max_length=20) # 평점

	#uploadedFile = models.FileField(upload_to="")

    def __str__(self):
        return f"{self.name} - {self.content}"
