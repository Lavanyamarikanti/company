from rest_framework import serializers
from .models import StudentDetails
class StudentDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentDetails
        fields = '__all__' # [name,age,marks]
        read_only_fields = ['id']
        extra_kwargs = {
            'password':{
                'write_only':True
            },
            'age':{
                'required':False,
                'default':18
            }
        }
    def validate_age(self,age): # 28 < 18
        if age < 18:
            raise serializers.ValidationError('Too Young!')
        return age

    def validate_name(self,name):
        if name.isalpha():
            return name
        else:
            raise serializers.ValidationError('Invalid Name!')

    def validate(self, data):
        if data.get('age') >= 18 and data.get('marks') >= 35:
            return data
        else:
            raise serializers.ValidationError('Pakkaki velli Aaduko!')



