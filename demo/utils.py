from django.core.files import File
from django.core.files.images import ImageFile
from django.core.files.uploadedfile import UploadedFile
from django.core.files.images import get_image_dimensions
from django.core.mail import send_mail
from django.core.urlresolvers import reverse
from django.core.exceptions import ImproperlyConfigured, ObjectDoesNotExist
from django.core.exceptions import PermissionDenied

from django.utils.translation import ugettext_lazy as _
from django.utils.translation import ugettext as _
from django.utils.decorators import method_decorator
from django.utils import simplejson
from django.utils.safestring import mark_safe
from django.utils.encoding import smart_unicode
from django.utils.datastructures import SortedDict