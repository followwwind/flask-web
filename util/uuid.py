# -*- encoding:utf-8 -*-
"""
@author：wind
@time：2021/3/24  19:28
@desc:
"""

import uuid


# uuid
def get_uuid():
    uid = str(uuid.uuid4())
    return ''.join(uid.split('-'))
