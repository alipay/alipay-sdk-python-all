#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class InviteMemberBusinessParamsDTO(object):

    def __init__(self):
        self._employee_id = None

    @property
    def employee_id(self):
        return self._employee_id

    @employee_id.setter
    def employee_id(self, value):
        self._employee_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.employee_id:
            if hasattr(self.employee_id, 'to_alipay_dict'):
                params['employee_id'] = self.employee_id.to_alipay_dict()
            else:
                params['employee_id'] = self.employee_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = InviteMemberBusinessParamsDTO()
        if 'employee_id' in d:
            o.employee_id = d['employee_id']
        return o


