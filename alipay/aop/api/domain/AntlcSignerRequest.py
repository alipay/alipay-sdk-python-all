#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AntlcSignerRequest(object):

    def __init__(self):
        self._name = None
        self._staff_id = None

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value
    @property
    def staff_id(self):
        return self._staff_id

    @staff_id.setter
    def staff_id(self, value):
        self._staff_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.name:
            if hasattr(self.name, 'to_alipay_dict'):
                params['name'] = self.name.to_alipay_dict()
            else:
                params['name'] = self.name
        if self.staff_id:
            if hasattr(self.staff_id, 'to_alipay_dict'):
                params['staff_id'] = self.staff_id.to_alipay_dict()
            else:
                params['staff_id'] = self.staff_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AntlcSignerRequest()
        if 'name' in d:
            o.name = d['name']
        if 'staff_id' in d:
            o.staff_id = d['staff_id']
        return o


