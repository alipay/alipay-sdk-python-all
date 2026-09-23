#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class DatadigitalAicsDevinWorkerPageQueryModel(object):

    def __init__(self):
        self._code_list = None
        self._name = None
        self._page_num = None
        self._page_size = None
        self._status = None
        self._tenant_id = None
        self._type = None
        self._version_type = None

    @property
    def code_list(self):
        return self._code_list

    @code_list.setter
    def code_list(self, value):
        if isinstance(value, list):
            self._code_list = list()
            for i in value:
                self._code_list.append(i)
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
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value
    @property
    def tenant_id(self):
        return self._tenant_id

    @tenant_id.setter
    def tenant_id(self, value):
        self._tenant_id = value
    @property
    def type(self):
        return self._type

    @type.setter
    def type(self, value):
        self._type = value
    @property
    def version_type(self):
        return self._version_type

    @version_type.setter
    def version_type(self, value):
        self._version_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.code_list:
            if isinstance(self.code_list, list):
                for i in range(0, len(self.code_list)):
                    element = self.code_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.code_list[i] = element.to_alipay_dict()
            if hasattr(self.code_list, 'to_alipay_dict'):
                params['code_list'] = self.code_list.to_alipay_dict()
            else:
                params['code_list'] = self.code_list
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
        if self.status:
            if hasattr(self.status, 'to_alipay_dict'):
                params['status'] = self.status.to_alipay_dict()
            else:
                params['status'] = self.status
        if self.tenant_id:
            if hasattr(self.tenant_id, 'to_alipay_dict'):
                params['tenant_id'] = self.tenant_id.to_alipay_dict()
            else:
                params['tenant_id'] = self.tenant_id
        if self.type:
            if hasattr(self.type, 'to_alipay_dict'):
                params['type'] = self.type.to_alipay_dict()
            else:
                params['type'] = self.type
        if self.version_type:
            if hasattr(self.version_type, 'to_alipay_dict'):
                params['version_type'] = self.version_type.to_alipay_dict()
            else:
                params['version_type'] = self.version_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = DatadigitalAicsDevinWorkerPageQueryModel()
        if 'code_list' in d:
            o.code_list = d['code_list']
        if 'name' in d:
            o.name = d['name']
        if 'page_num' in d:
            o.page_num = d['page_num']
        if 'page_size' in d:
            o.page_size = d['page_size']
        if 'status' in d:
            o.status = d['status']
        if 'tenant_id' in d:
            o.tenant_id = d['tenant_id']
        if 'type' in d:
            o.type = d['type']
        if 'version_type' in d:
            o.version_type = d['version_type']
        return o


