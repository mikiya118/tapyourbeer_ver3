from django.db import models
from django.contrib import admin
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils import timezone
from core import consts as CONST

# Create your models here.
class Brewery(models.Model):
    """
    ブルワリーモデル
    """
    def __unicode__(self):
        return self.name
    # 名前
    name = models.CharField(max_length=200)
    # logo
    logo = models.CharField(max_length=200, null=True)
    # 住所
    address = models.CharField(max_length=200, null=True)
    # 説明
    description = models.CharField(max_length=200, null=True)
    #アクティブか非アクティブか
    is_active = models.BooleanField(default=True)

    def encode(self):
        return {
            'name': self.name,
            'logo': self.logo,
            'address': self.address,
            'description': self.description,
            'is_active': self.is_active,
        }

class Beer(models.Model):
    """
    ビールモデル
    """
    def __unicode__(self):
        return self.name
    # 名前
    name = models.CharField(max_length=200)
    # style
    style = models.CharField(max_length=200)
    # 説明
    description = models.CharField(max_length=200, null=True)
    # ibu（苦さ）
    ibu = models.CharField(max_length=200, null=True)
    # abv（アルコール度数）
    abv = models.CharField(max_length=200, null=True)
    # ブルワリー
    brewery = models.ForeignKey(Brewery, on_delete=models.PROTECT)
    # photo (画像）
    photo = models.CharField(max_length=200, null=True)
    # アクティブか非アクティブか
    is_active = models.BooleanField(default=True)

    def encode(self):
        return {
                'name': self.name,
                'style': self.style,
                'description': self.description,
                'ibu': self.ibu,
                'abv': self.abv,
                'brewery': self.team.encode(),
                'photo': self.photo,
                'is_active': self.is_active,
                }

class Venue(models.Model):
    """
    店モデル
    """
    #ぐるなびID
    gurunavi_id = models.IntegerField(null=True)
    # 名前
    name = models.CharField(max_length=200)
    # アクティブか非アクティブか
    is_active = models.BooleanField(default=True)

    def encode(self):
        return {
            'gurunavi_id': self.gurunavi_id,
            'name': self.name,
        }

class Comment(models.Model):
    """
    味評価モデル
    """
    # ビール
    beer = models.ForeignKey(Beer, on_delete=models.PROTECT)
    # コメントしたユーザ
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    # 提供している店
    venue = models.ForeignKey(Venue, on_delete=models.SET_NULL, null=True)
    # 画像
    photo = models.CharField(max_length=200, null=True)
    # 苦味
    bitterness = models.IntegerField(choices=CONST.EVALUATION_CHOICES)
    # 香り
    aroma = models.IntegerField(choices=CONST.EVALUATION_CHOICES)
    # ボディ
    body= models.IntegerField(choices=CONST.EVALUATION_CHOICES)
    # 飲みやすさ
    drinkability = models.IntegerField(choices=CONST.EVALUATION_CHOICES)
    # 圧
    pressure = models.IntegerField(choices=CONST.EVALUATION_CHOICES)
    # 苦味
    specialness = models.IntegerField(choices=CONST.EVALUATION_CHOICES)
    # 総合
    overall = models.IntegerField(choices=CONST.EVALUATION_CHOICES)
    # コメント
    comment = models.CharField(max_length=200, null=True)

    def encode(self):
        return {
            'beer': self.beer.encode(),
            'user': self.user.encode(),
            'venue': self.venue.encode(),
            'photo': self.photo,
            'bitterness': self.bitterness,
            'aroma': self.aroma,
            'body': self.body,
            'drinkability': self.drinkability,
            'pressure': self.pressure,
            'specialness': self.specialness,
            'overall': self.overall,
            'comment': self.comment,
        }

class TodaysTap(models.Model):
    """
    本日のタップモデル
    """
    # 店
    venue = models.ForeignKey(Venue, on_delete=models.PROTECT)
    # ビール
    beer = models.ForeignKey(Beer, on_delete=models.PROTECT)
    # 登録日
    registered_date = models.DateTimeField(default=timezone.now)
    # アクティブか非アクティブか
    is_active = models.BooleanField(default=False)

    def encode(self):
        return {
            'venue': self.venue.encode(),
            'beer': self.beer.encode(),
            'registered_date': self.registered_date,
            'is_active': self.is_active,
        }

class Profile(models.Model):
    """
    ユーザー拡張モデル
    """
    # djangoユーザモデル
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # 性別スタイル
    gender_style = models.CharField(max_length=200, choices=CONST.GENDER_STYLE_CHOICES)
    # 誕生日
    birthday = models.DateField()
    # 住んでいる国
    living_country = models.CharField(max_length=200, choices=CONST.COUNTRY_CHOICES)
    # 住んでいる地域
    living_area = models.CharField(max_length=200, null=True)
    # アプリ管理者
    is_admin = models.BooleanField(default=False)
    # ブルワリー管理者
    is_managing_brewery = models.BooleanField(default=False)
    # 店舗管理者
    is_managing_venue = models.BooleanField(default=False)
    # 画像
    photo = models.CharField(max_length=200, null=True)
    # ユーザランク
    user_rank = models.IntegerField(default=1, choices=CONST.USER_RANK_CHOICES)

    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.profile.save()

class Follow(models.Model):
    """
    フォローモデル
    """
    # ユーザ
    user = models.ForeignKey(User, related_name='following_user', on_delete=models.CASCADE)
    # フォロー
    follow = models.ForeignKey(User, related_name='followed_user', on_delete=models.CASCADE)

    class Meta:
        unique_together = ('user', 'follow')


class TCBFParticipant(models.Model):
    """
    TCBF参加ブルワリーモデル
    """
    # ブルワリー
    brewery = models.ForeignKey(Brewery, on_delete=models.PROTECT)
    # 参加年度
    year = models.IntegerField()

    class Meta:
        unique_together = ('brewery', 'year')

class BreweryManager(models.Model):
    """
    ブルワリー管理者モデル
    """
    # ブルワリー
    brewery = models.ForeignKey(Brewery, on_delete=models.PROTECT)
    # ユーザー
    user = models.ForeignKey(User, on_delete=models.PROTECT)

    class Meta:
        unique_together = ('brewery', 'user')

class VenueManager(models.Model):
    """
    店舗管理者モデル
    """
    # 店舗
    venue = models.ForeignKey(Venue, on_delete=models.PROTECT)
    # ユーザー
    user = models.ForeignKey(User, on_delete=models.PROTECT)

    class Meta:
        unique_together = ('venue', 'user')

class Like(models.Model):
    """
    いいねモデル
    """
    #　コメント
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE)
    # ユーザー
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('comment', 'user')


admin.site.register(Beer)
admin.site.register(Brewery)
admin.site.register(Venue)
admin.site.register(Comment)
admin.site.register(TodaysTap)
admin.site.register(Profile)
admin.site.register(Follow)
admin.site.register(TCBFParticipant)
admin.site.register(BreweryManager)
admin.site.register(VenueManager)
admin.site.register(Like)
