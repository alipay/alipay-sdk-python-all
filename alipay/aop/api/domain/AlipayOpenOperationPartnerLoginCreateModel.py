#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayOpenOperationPartnerLoginCreateModel(object):

    def __init__(self):
        self._staff_user_id = None

    @property
    def staff_user_id(self):
        return self._staff_user_id

    @staff_user_id.setter
    def staff_user_id(self, value):
        self._staff_user_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.staff_user_id:
            if hasattr(self.staff_user_id, 'to_alipay_dict'):
                params['staff_user_id'] = self.staff_user_id.to_alipay_dict()
            else:
                params['staff_user_id'] = self.staff_user_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayOpenOperationPartnerLoginCreateModel()
        if 'staff_user_id' in d:
            o.staff_user_id = d['staff_user_id']
        return o


