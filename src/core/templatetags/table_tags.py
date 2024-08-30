from django import template

register = template.Library()

@register.inclusion_tag('components/table.html')
def render_table(headers, rows, title, table_url, controls, search, row_update, row_delete):
    return {
        'headers': headers,
        'rows': rows,
        'title': title,
        'table_url': table_url,
        'controls': controls,
        'search': search,
        'row_update': row_update,
        'row_delete': row_delete
    }