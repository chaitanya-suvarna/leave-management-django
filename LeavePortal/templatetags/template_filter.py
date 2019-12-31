from django import template
from LeavePortal.models import Resource,Leave

register = template.Library()

@register.simple_tag
def get_leave(resourceleave, month, day):
    myleave_type = [leave.leave_type.id for leave in resourceleave.leaves if int(leave.leave_date.strftime("%-d")) == day and leave.leave_date.strftime("%-m") == month]
    if myleave_type == [2]:
        return "alert alert-danger"
    elif myleave_type == [3]:
        return "alert alert-info"
    elif myleave_type == [4]:
        return "alert alert-primary"
    else:
        return "alert alert-light"
