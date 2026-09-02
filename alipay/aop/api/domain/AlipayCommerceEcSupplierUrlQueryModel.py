#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceEcSupplierUrlQueryModel(object):

    def __init__(self):
        self._employee_id = None
        self._enterprise_id = None
        self._expense_rule_id = None
        self._need_sign_url = None
        self._order_id = None
        self._service_id = None
        self._url_type = None

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
    def expense_rule_id(self):
        return self._expense_rule_id

    @expense_rule_id.setter
    def expense_rule_id(self, value):
        self._expense_rule_id = value
    @property
    def need_sign_url(self):
        return self._need_sign_url

    @need_sign_url.setter
    def need_sign_url(self, value):
        self._need_sign_url = value
    @property
    def order_id(self):
        return self._order_id

    @order_id.setter
    def order_id(self, value):
        self._order_id = value
    @property
    def service_id(self):
        return self._service_id

    @service_id.setter
    def service_id(self, value):
        self._service_id = value
    @property
    def url_type(self):
        return self._url_type

    @url_type.setter
    def url_type(self, value):
        self._url_type = value


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
        if self.expense_rule_id:
            if hasattr(self.expense_rule_id, 'to_alipay_dict'):
                params['expense_rule_id'] = self.expense_rule_id.to_alipay_dict()
            else:
                params['expense_rule_id'] = self.expense_rule_id
        if self.need_sign_url:
            if hasattr(self.need_sign_url, 'to_alipay_dict'):
                params['need_sign_url'] = self.need_sign_url.to_alipay_dict()
            else:
                params['need_sign_url'] = self.need_sign_url
        if self.order_id:
            if hasattr(self.order_id, 'to_alipay_dict'):
                params['order_id'] = self.order_id.to_alipay_dict()
            else:
                params['order_id'] = self.order_id
        if self.service_id:
            if hasattr(self.service_id, 'to_alipay_dict'):
                params['service_id'] = self.service_id.to_alipay_dict()
            else:
                params['service_id'] = self.service_id
        if self.url_type:
            if hasattr(self.url_type, 'to_alipay_dict'):
                params['url_type'] = self.url_type.to_alipay_dict()
            else:
                params['url_type'] = self.url_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceEcSupplierUrlQueryModel()
        if 'employee_id' in d:
            o.employee_id = d['employee_id']
        if 'enterprise_id' in d:
            o.enterprise_id = d['enterprise_id']
        if 'expense_rule_id' in d:
            o.expense_rule_id = d['expense_rule_id']
        if 'need_sign_url' in d:
            o.need_sign_url = d['need_sign_url']
        if 'order_id' in d:
            o.order_id = d['order_id']
        if 'service_id' in d:
            o.service_id = d['service_id']
        if 'url_type' in d:
            o.url_type = d['url_type']
        return o


