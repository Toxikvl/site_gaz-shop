from oscar.apps.customer.forms import UserForm as CoreUserForm
from oscar.core.compat import existing_user_fields, get_user_model


class UserForm(CoreUserForm):
    class Meta:
        model = get_user_model()
        fields = CoreUserForm.Meta.fields + existing_user_fields(['user_phone'])


ProfileForm = UserForm
