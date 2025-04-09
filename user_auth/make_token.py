from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Qo‘shimcha ma’lumotlar
        token['full_name'] = user.full_name
        token['phone'] = user.phone
        token['is_admin'] = user.is_admin
        token['is_teacher'] = user.is_teacher
        token['is_student'] = user.is_student

        return token
