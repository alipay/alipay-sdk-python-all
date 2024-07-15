#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ZhimaCreditEpRebusinessentityPersonQueryModel(object):

    def __init__(self):
        self._person_cert_no = None
        self._person_name = None
        self._platform_id_list = None
        self._platform_type_list = None
        self._product_code = None
        self._rel_type_code_list = None
        self._uscc = None

    @property
    def person_cert_no(self):
        return self._person_cert_no

    @person_cert_no.setter
    def person_cert_no(self, value):
        self._person_cert_no = value
    @property
    def person_name(self):
        return self._person_name

    @person_name.setter
    def person_name(self, value):
        self._person_name = value
    @property
    def platform_id_list(self):
        return self._platform_id_list

    @platform_id_list.setter
    def platform_id_list(self, value):
        if isinstance(value, list):
            self._platform_id_list = list()
            for i in value:
                self._platform_id_list.append(i)
    @property
    def platform_type_list(self):
        return self._platform_type_list

    @platform_type_list.setter
    def platform_type_list(self, value):
        if isinstance(value, list):
            self._platform_type_list = list()
            for i in value:
                self._platform_type_list.append(i)
    @property
    def product_code(self):
        return self._product_code

    @product_code.setter
    def product_code(self, value):
        self._product_code = value
    @property
    def rel_type_code_list(self):
        return self._rel_type_code_list

    @rel_type_code_list.setter
    def rel_type_code_list(self, value):
        if isinstance(value, list):
            self._rel_type_code_list = list()
            for i in value:
                self._rel_type_code_list.append(i)
    @property
    def uscc(self):
        return self._uscc

    @uscc.setter
    def uscc(self, value):
        self._uscc = value


    def to_alipay_dict(self):
        params = dict()
        if self.person_cert_no:
            if hasattr(self.person_cert_no, 'to_alipay_dict'):
                params['person_cert_no'] = self.person_cert_no.to_alipay_dict()
            else:
                params['person_cert_no'] = self.person_cert_no
        if self.person_name:
            if hasattr(self.person_name, 'to_alipay_dict'):
                params['person_name'] = self.person_name.to_alipay_dict()
            else:
                params['person_name'] = self.person_name
        if self.platform_id_list:
            if isinstance(self.platform_id_list, list):
                for i in range(0, len(self.platform_id_list)):
                    element = self.platform_id_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.platform_id_list[i] = element.to_alipay_dict()
            if hasattr(self.platform_id_list, 'to_alipay_dict'):
                params['platform_id_list'] = self.platform_id_list.to_alipay_dict()
            else:
                params['platform_id_list'] = self.platform_id_list
        if self.platform_type_list:
            if isinstance(self.platform_type_list, list):
                for i in range(0, len(self.platform_type_list)):
                    element = self.platform_type_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.platform_type_list[i] = element.to_alipay_dict()
            if hasattr(self.platform_type_list, 'to_alipay_dict'):
                params['platform_type_list'] = self.platform_type_list.to_alipay_dict()
            else:
                params['platform_type_list'] = self.platform_type_list
        if self.product_code:
            if hasattr(self.product_code, 'to_alipay_dict'):
                params['product_code'] = self.product_code.to_alipay_dict()
            else:
                params['product_code'] = self.product_code
        if self.rel_type_code_list:
            if isinstance(self.rel_type_code_list, list):
                for i in range(0, len(self.rel_type_code_list)):
                    element = self.rel_type_code_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.rel_type_code_list[i] = element.to_alipay_dict()
            if hasattr(self.rel_type_code_list, 'to_alipay_dict'):
                params['rel_type_code_list'] = self.rel_type_code_list.to_alipay_dict()
            else:
                params['rel_type_code_list'] = self.rel_type_code_list
        if self.uscc:
            if hasattr(self.uscc, 'to_alipay_dict'):
                params['uscc'] = self.uscc.to_alipay_dict()
            else:
                params['uscc'] = self.uscc
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ZhimaCreditEpRebusinessentityPersonQueryModel()
        if 'person_cert_no' in d:
            o.person_cert_no = d['person_cert_no']
        if 'person_name' in d:
            o.person_name = d['person_name']
        if 'platform_id_list' in d:
            o.platform_id_list = d['platform_id_list']
        if 'platform_type_list' in d:
            o.platform_type_list = d['platform_type_list']
        if 'product_code' in d:
            o.product_code = d['product_code']
        if 'rel_type_code_list' in d:
            o.rel_type_code_list = d['rel_type_code_list']
        if 'uscc' in d:
            o.uscc = d['uscc']
        return o


