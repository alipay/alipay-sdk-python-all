#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class MybankCreditSceneprodInstAuthConsultModel(object):

    def __init__(self):
        self._consult_content = None
        self._org_code = None
        self._product_code = None

    @property
    def consult_content(self):
        return self._consult_content

    @consult_content.setter
    def consult_content(self, value):
        self._consult_content = value
    @property
    def org_code(self):
        return self._org_code

    @org_code.setter
    def org_code(self, value):
        self._org_code = value
    @property
    def product_code(self):
        return self._product_code

    @product_code.setter
    def product_code(self, value):
        self._product_code = value


    def to_alipay_dict(self):
        params = dict()
        if self.consult_content:
            if hasattr(self.consult_content, 'to_alipay_dict'):
                params['consult_content'] = self.consult_content.to_alipay_dict()
            else:
                params['consult_content'] = self.consult_content
        if self.org_code:
            if hasattr(self.org_code, 'to_alipay_dict'):
                params['org_code'] = self.org_code.to_alipay_dict()
            else:
                params['org_code'] = self.org_code
        if self.product_code:
            if hasattr(self.product_code, 'to_alipay_dict'):
                params['product_code'] = self.product_code.to_alipay_dict()
            else:
                params['product_code'] = self.product_code
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = MybankCreditSceneprodInstAuthConsultModel()
        if 'consult_content' in d:
            o.consult_content = d['consult_content']
        if 'org_code' in d:
            o.org_code = d['org_code']
        if 'product_code' in d:
            o.product_code = d['product_code']
        return o


