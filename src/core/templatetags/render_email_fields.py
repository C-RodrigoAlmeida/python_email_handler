from django import template

register = template.Library()

@register.inclusion_tag('components/email_field.html')
def render_email_field(method, field_name, recipients, groups, value):
    return {
        'method': method,
        'field_name': field_name,
        'recipients': recipients,
        'groups': groups,
        'value': value
    }