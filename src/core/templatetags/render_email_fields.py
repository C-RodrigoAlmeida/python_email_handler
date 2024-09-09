from django import template

register = template.Library()

@register.inclusion_tag('components/email_field.html')
def render_email_field(request, field_name, recipients, groups):
    return {
        'method': f'{request.GET.get(field_name + "_method", "")}',
        'field_name': field_name,
        'recipients': recipients,
        'groups': groups,
        'value': f'{request.GET.get(field_name, "")}'
    }
