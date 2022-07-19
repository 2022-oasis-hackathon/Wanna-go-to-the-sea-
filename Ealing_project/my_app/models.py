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



class recommend_place(models.Model):
    profile_img = models.TextField() # 프로필이미지 주소
    img1 = models.TextField() # 작은이미지 주소
    img2 = models.TextField() # 작은이미지 주소
    img3 = models.TextField() # 작은이미지 주소
    img4 = models.TextField() # 작은이미지 주소
    img_big = models.TextField() # 작은이미지 주소
    
    name = models.CharField(max_length=20) # 지역 이름
    type = models.CharField(max_length=20) # 유형 ex)정원
    address = models.TextField() # 숙박이미지주소
    reputation = models.FloatField(max_length=20) # 평점

    title = models.CharField(max_length=30) #추천스팟제목
    content = models.CharField(max_length=500) #추천스팟내용

    small_title1 = models.CharField(max_length=30) #추천스팟제목
    small_content1 = models.CharField(max_length=500) #추천스팟제목
    small_title2 = models.CharField(max_length=30) #추천스팟제목
    small_content2 = models.CharField(max_length=500) #추천스팟제목

    recommend_load_img = models.TextField() # 추천코스이미지주소

    

	#uploadedFile = models.FileField(upload_to="")

    def __str__(self):
        return f"{self.name}"
