from django.forms import ModelForm, PasswordInput

from maker.models import S3Storage
from .storage import StorageCreateView, StorageUpdateView, StorageDeleteView


class S3StorageForm(ModelForm):
    class Meta:
        model = S3Storage
        fields = ['region', 'bucket', 'accesskeyid', 'secretkey']
        labels = {
            'bucket': 'Bucket Name',
            'accesskeyid': 'Access Key ID',
            'secretkey': 'Secret Access Key',
        }
        help_texts = {
            'region': 'Other regions are currently not supported.',
        }
        widgets = {
            'secretkey': PasswordInput(),
        }


class S3StorageCreate(StorageCreateView):
    model = S3Storage
    form_class = S3StorageForm


class S3StorageUpdate(StorageUpdateView):
    model = S3Storage
    form_class = S3StorageForm


class S3StorageDelete(StorageDeleteView):
    model = S3Storage
