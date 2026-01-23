#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceDecorationInsuranceProductSignModel(object):

    def __init__(self):
        self._contact_info = None
        self._contact_user = None
        self._credit_code = None
        self._name = None
        self._pid = None
        self._product_type_list = None

    @property
    def contact_info(self):
        return self._contact_info

    @contact_info.setter
    def contact_info(self, value):
        self._contact_info = value
    @property
    def contact_user(self):
        return self._contact_user

    @contact_user.setter
    def contact_user(self, value):
        self._contact_user = value
    @property
    def credit_code(self):
        return self._credit_code

    @credit_code.setter
    def credit_code(self, value):
        self._credit_code = value
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value
    @property
    def pid(self):
        return self._pid

    @pid.setter
    def pid(self, value):
        self._pid = value
    @property
    def product_type_list(self):
        return self._product_type_list

    @product_type_list.setter
    def product_type_list(self, value):
        if isinstance(value, list):
            self._product_type_list = list()
            for i in value:
                self._product_type_list.append(i)


    def to_alipay_dict(self):
        params = dict()
        if self.contact_info:
            if hasattr(self.contact_info, 'to_alipay_dict'):
                params['contact_info'] = self.contact_info.to_alipay_dict()
            else:
                params['contact_info'] = self.contact_info
        if self.contact_user:
            if hasattr(self.contact_user, 'to_alipay_dict'):
                params['contact_user'] = self.contact_user.to_alipay_dict()
            else:
                params['contact_user'] = self.contact_user
        if self.credit_code:
            if hasattr(self.credit_code, 'to_alipay_dict'):
                params['credit_code'] = self.credit_code.to_alipay_dict()
            else:
                params['credit_code'] = self.credit_code
        if self.name:
            if hasattr(self.name, 'to_alipay_dict'):
                params['name'] = self.name.to_alipay_dict()
            else:
                params['name'] = self.name
        if self.pid:
            if hasattr(self.pid, 'to_alipay_dict'):
                params['pid'] = self.pid.to_alipay_dict()
            else:
                params['pid'] = self.pid
        if self.product_type_list:
            if isinstance(self.product_type_list, list):
                for i in range(0, len(self.product_type_list)):
                    element = self.product_type_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.product_type_list[i] = element.to_alipay_dict()
            if hasattr(self.product_type_list, 'to_alipay_dict'):
                params['product_type_list'] = self.product_type_list.to_alipay_dict()
            else:
                params['product_type_list'] = self.product_type_list
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceDecorationInsuranceProductSignModel()
        if 'contact_info' in d:
            o.contact_info = d['contact_info']
        if 'contact_user' in d:
            o.contact_user = d['contact_user']
        if 'credit_code' in d:
            o.credit_code = d['credit_code']
        if 'name' in d:
            o.name = d['name']
        if 'pid' in d:
            o.pid = d['pid']
        if 'product_type_list' in d:
            o.product_type_list = d['product_type_list']
        return o


