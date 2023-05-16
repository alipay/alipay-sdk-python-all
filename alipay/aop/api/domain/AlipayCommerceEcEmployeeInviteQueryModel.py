#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceEcEmployeeInviteQueryModel(object):

    def __init__(self):
        self._employee_id = None
        self._enterprise_id = None
        self._page_content_code = None

    @property
    def employee_id(self):
        return self._employee_id

    @employee_id.setter
    def employee_id(self, value):
        self._employee_id = value
    @property
    def enterprise_id(self):
        return self._enterprise_id

    @enterprise_id.setter
    def enterprise_id(self, value):
        self._enterprise_id = value
    @property
    def page_content_code(self):
        return self._page_content_code

    @page_content_code.setter
    def page_content_code(self, value):
        self._page_content_code = value


    def to_alipay_dict(self):
        params = dict()
        if self.employee_id:
            if hasattr(self.employee_id, 'to_alipay_dict'):
                params['employee_id'] = self.employee_id.to_alipay_dict()
            else:
                params['employee_id'] = self.employee_id
        if self.enterprise_id:
            if hasattr(self.enterprise_id, 'to_alipay_dict'):
                params['enterprise_id'] = self.enterprise_id.to_alipay_dict()
            else:
                params['enterprise_id'] = self.enterprise_id
        if self.page_content_code:
            if hasattr(self.page_content_code, 'to_alipay_dict'):
                params['page_content_code'] = self.page_content_code.to_alipay_dict()
            else:
                params['page_content_code'] = self.page_content_code
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceEcEmployeeInviteQueryModel()
        if 'employee_id' in d:
            o.employee_id = d['employee_id']
        if 'enterprise_id' in d:
            o.enterprise_id = d['enterprise_id']
        if 'page_content_code' in d:
            o.page_content_code = d['page_content_code']
        return o


