from django import forms
from proyectos.models import Mensaje

class MensajeForm(forms.ModelForm):
    class Meta:
        model = Mensaje
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for visible in self.visible_fields():
            attrs = {
                'class': 'form-control',
                'placeholder': visible.field.label
            }

            # Si el campo es 'mensaje', lo tratamos como textarea personalizado
            if visible.name == 'mensaje':
                attrs['rows'] = 4  # 🔥 Esto acorta el textarea

            visible.field.widget.attrs.update(attrs)
