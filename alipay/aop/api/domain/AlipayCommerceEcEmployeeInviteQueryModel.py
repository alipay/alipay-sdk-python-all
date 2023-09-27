#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceEcEmployeeInviteQueryModel(object):

    def __init__(self):
        self._create_share_code = None
        self._employee_id = None
        self._enterprise_id = None
        self._page_content_code = None
        self._withholding_sign_str = None

    @property
    def create_share_code(self):
        return self._create_share_code

    @create_share_code.setter
    def create_share_code(self, value):
        self._create_share_code = value
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
    @property
    def withholding_sign_str(self):
        return self._withholding_sign_str

    @withholding_sign_str.setter
    def withholding_sign_str(self, value):
        self._withholding_sign_str = value


    def to_alipay_dict(self):
        params = dict()
        if self.create_share_code:
            if hasattr(self.create_share_code, 'to_alipay_dict'):
                params['create_share_code'] = self.create_share_code.to_alipay_dict()
            else:
                params['create_share_code'] = self.create_share_code
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
        if self.withholding_sign_str:
            if hasattr(self.withholding_sign_str, 'to_alipay_dict'):
                params['withholding_sign_str'] = self.withholding_sign_str.to_alipay_dict()
            else:
                params['withholding_sign_str'] = self.withholding_sign_str
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceEcEmployeeInviteQueryModel()
        if 'create_share_code' in d:
            o.create_share_code = d['create_share_code']
        if 'employee_id' in d:
            o.employee_id = d['employee_id']
        if 'enterprise_id' in d:
            o.enterprise_id = d['enterprise_id']
        if 'page_content_code' in d:
            o.page_content_code = d['page_content_code']
        if 'withholding_sign_str' in d:
            o.withholding_sign_str = d['withholding_sign_str']
        return o


