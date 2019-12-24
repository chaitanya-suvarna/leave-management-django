from django import template
from LeavePortal.models import Resource,Leave

register = template.Library()

@register.simple_tag
def get_leave(resourceleave, month, day):
    myleave_type = [leave.leave_type for leave in resourceleave.leaves if int(leave.leave_date.strftime("%-d")) == day and leave.leave_date.strftime("%-m") == month]
    if myleave_type == [0]:
        return "alert alert-danger"
    elif myleave_type == [1]:
        return "alert alert-info"
    else:
        return "alert alert-light"
