from rest_framework import serializers
from home.models import Student


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'

    def validate(self, data):
        if data['age'] > 18:
            raise serializers.ValidationError(
                {'error': 'Age can`t less then 18'})
        if data['name']:
            for n in data['name']:
                if n.isdigit():
                    raise serializers.ValidationError(
                        {'error': 'Name Can not be  Numarical'})
