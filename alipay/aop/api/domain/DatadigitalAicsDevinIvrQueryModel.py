#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class DatadigitalAicsDevinIvrQueryModel(object):

    def __init__(self):
        self._complete_name = None
        self._environment = None
        self._ivr_code = None
        self._name = None
        self._page_num = None
        self._page_size = None
        self._tenant_id = None
        self._type_list = None
        self._version_no = None

    @property
    def complete_name(self):
        return self._complete_name

    @complete_name.setter
    def complete_name(self, value):
        self._complete_name = value
    @property
    def environment(self):
        return self._environment

    @environment.setter
    def environment(self, value):
        self._environment = value
    @property
    def ivr_code(self):
        return self._ivr_code

    @ivr_code.setter
    def ivr_code(self, value):
        self._ivr_code = value
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value
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
    def tenant_id(self):
        return self._tenant_id

    @tenant_id.setter
    def tenant_id(self, value):
        self._tenant_id = value
    @property
    def type_list(self):
        return self._type_list

    @type_list.setter
    def type_list(self, value):
        if isinstance(value, list):
            self._type_list = list()
            for i in value:
                self._type_list.append(i)
    @property
    def version_no(self):
        return self._version_no

    @version_no.setter
    def version_no(self, value):
        self._version_no = value


    def to_alipay_dict(self):
        params = dict()
        if self.complete_name:
            if hasattr(self.complete_name, 'to_alipay_dict'):
                params['complete_name'] = self.complete_name.to_alipay_dict()
            else:
                params['complete_name'] = self.complete_name
        if self.environment:
            if hasattr(self.environment, 'to_alipay_dict'):
                params['environment'] = self.environment.to_alipay_dict()
            else:
                params['environment'] = self.environment
        if self.ivr_code:
            if hasattr(self.ivr_code, 'to_alipay_dict'):
                params['ivr_code'] = self.ivr_code.to_alipay_dict()
            else:
                params['ivr_code'] = self.ivr_code
        if self.name:
            if hasattr(self.name, 'to_alipay_dict'):
                params['name'] = self.name.to_alipay_dict()
            else:
                params['name'] = self.name
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
        if self.tenant_id:
            if hasattr(self.tenant_id, 'to_alipay_dict'):
                params['tenant_id'] = self.tenant_id.to_alipay_dict()
            else:
                params['tenant_id'] = self.tenant_id
        if self.type_list:
            if isinstance(self.type_list, list):
                for i in range(0, len(self.type_list)):
                    element = self.type_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.type_list[i] = element.to_alipay_dict()
            if hasattr(self.type_list, 'to_alipay_dict'):
                params['type_list'] = self.type_list.to_alipay_dict()
            else:
                params['type_list'] = self.type_list
        if self.version_no:
            if hasattr(self.version_no, 'to_alipay_dict'):
                params['version_no'] = self.version_no.to_alipay_dict()
            else:
                params['version_no'] = self.version_no
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = DatadigitalAicsDevinIvrQueryModel()
        if 'complete_name' in d:
            o.complete_name = d['complete_name']
        if 'environment' in d:
            o.environment = d['environment']
        if 'ivr_code' in d:
            o.ivr_code = d['ivr_code']
        if 'name' in d:
            o.name = d['name']
        if 'page_num' in d:
            o.page_num = d['page_num']
        if 'page_size' in d:
            o.page_size = d['page_size']
        if 'tenant_id' in d:
            o.tenant_id = d['tenant_id']
        if 'type_list' in d:
            o.type_list = d['type_list']
        if 'version_no' in d:
            o.version_no = d['version_no']
        return o


