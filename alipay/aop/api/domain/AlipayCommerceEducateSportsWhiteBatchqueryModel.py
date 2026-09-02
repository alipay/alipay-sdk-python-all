#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceEducateSportsWhiteBatchqueryModel(object):

    def __init__(self):
        self._department_code = None
        self._organization_code = None
        self._page_num = None
        self._page_size = None
        self._white_type = None

    @property
    def department_code(self):
        return self._department_code

    @department_code.setter
    def department_code(self, value):
        self._department_code = value
    @property
    def organization_code(self):
        return self._organization_code

    @organization_code.setter
    def organization_code(self, value):
        self._organization_code = value
    @property
    def page_num(self):
        return self._page_num

    @page_num.setter
    def page_num(self, value):
        self._page_num = value
    @property
    def page_size(self):
        return self._page_size

    @page_size.setter
    def page_size(self, value):
        self._page_size = value
    @property
    def white_type(self):
        return self._white_type

    @white_type.setter
    def white_type(self, value):
        self._white_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.department_code:
            if hasattr(self.department_code, 'to_alipay_dict'):
                params['department_code'] = self.department_code.to_alipay_dict()
            else:
                params['department_code'] = self.department_code
        if self.organization_code:
            if hasattr(self.organization_code, 'to_alipay_dict'):
                params['organization_code'] = self.organization_code.to_alipay_dict()
            else:
                params['organization_code'] = self.organization_code
        if self.page_num:
            if hasattr(self.page_num, 'to_alipay_dict'):
                params['page_num'] = self.page_num.to_alipay_dict()
            else:
                params['page_num'] = self.page_num
        if self.page_size:
            if hasattr(self.page_size, 'to_alipay_dict'):
                params['page_size'] = self.page_size.to_alipay_dict()
            else:
                params['page_size'] = self.page_size
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
        o = AlipayCommerceEducateSportsWhiteBatchqueryModel()
        if 'department_code' in d:
            o.department_code = d['department_code']
        if 'organization_code' in d:
            o.organization_code = d['organization_code']
        if 'page_num' in d:
            o.page_num = d['page_num']
        if 'page_size' in d:
            o.page_size = d['page_size']
        if 'white_type' in d:
            o.white_type = d['white_type']
        return o


