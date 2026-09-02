#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceEducateSportsWhiteDeleteModel(object):

    def __init__(self):
        self._employee_no = None
        self._organization_code = None
        self._white_type = None

    @property
    def employee_no(self):
        return self._employee_no

    @employee_no.setter
    def employee_no(self, value):
        self._employee_no = value
    @property
    def organization_code(self):
        return self._organization_code

    @organization_code.setter
    def organization_code(self, value):
        self._organization_code = value
    @property
    def white_type(self):
        return self._white_type

    @white_type.setter
    def white_type(self, value):
        self._white_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.employee_no:
            if hasattr(self.employee_no, 'to_alipay_dict'):
                params['employee_no'] = self.employee_no.to_alipay_dict()
            else:
                params['employee_no'] = self.employee_no
        if self.organization_code:
            if hasattr(self.organization_code, 'to_alipay_dict'):
                params['organization_code'] = self.organization_code.to_alipay_dict()
            else:
                params['organization_code'] = self.organization_code
        if self.white_type:
            if hasattr(self.white_type, 'to_alipay_dict'):
                params['white_type'] = self.white_type.to_alipay_dict()
            else:
                params['white_type'] = self.white_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceEducateSportsWhiteDeleteModel()
        if 'employee_no' in d:
            o.employee_no = d['employee_no']
        if 'organization_code' in d:
            o.organization_code = d['organization_code']
        if 'white_type' in d:
            o.white_type = d['white_type']
        return o


