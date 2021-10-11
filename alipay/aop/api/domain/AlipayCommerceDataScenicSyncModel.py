#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceDataScenicSyncModel(object):

    def __init__(self):
        self._code_value = None
        self._isv_name = None
        self._isv_scenic_address = None
        self._isv_scenic_name = None
        self._outer_id = None
        self._scenic_app_id = None
        self._scenic_id = None

    @property
    def code_value(self):
        return self._code_value

    @code_value.setter
    def code_value(self, value):
        if isinstance(value, list):
            self._code_value = list()
            for i in value:
                self._code_value.append(i)
    @property
    def isv_name(self):
        return self._isv_name

    @isv_name.setter
    def isv_name(self, value):
        self._isv_name = value
    @property
    def isv_scenic_address(self):
        return self._isv_scenic_address

    @isv_scenic_address.setter
    def isv_scenic_address(self, value):
        self._isv_scenic_address = value
    @property
    def isv_scenic_name(self):
        return self._isv_scenic_name

    @isv_scenic_name.setter
    def isv_scenic_name(self, value):
        self._isv_scenic_name = value
    @property
    def outer_id(self):
        return self._outer_id

    @outer_id.setter
    def outer_id(self, value):
        self._outer_id = value
    @property
    def scenic_app_id(self):
        return self._scenic_app_id

    @scenic_app_id.setter
    def scenic_app_id(self, value):
        self._scenic_app_id = value
    @property
    def scenic_id(self):
        return self._scenic_id

    @scenic_id.setter
    def scenic_id(self, value):
        self._scenic_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.code_value:
            if isinstance(self.code_value, list):
                for i in range(0, len(self.code_value)):
                    element = self.code_value[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.code_value[i] = element.to_alipay_dict()
            if hasattr(self.code_value, 'to_alipay_dict'):
                params['code_value'] = self.code_value.to_alipay_dict()
            else:
                params['code_value'] = self.code_value
        if self.isv_name:
            if hasattr(self.isv_name, 'to_alipay_dict'):
                params['isv_name'] = self.isv_name.to_alipay_dict()
            else:
                params['isv_name'] = self.isv_name
        if self.isv_scenic_address:
            if hasattr(self.isv_scenic_address, 'to_alipay_dict'):
                params['isv_scenic_address'] = self.isv_scenic_address.to_alipay_dict()
            else:
                params['isv_scenic_address'] = self.isv_scenic_address
        if self.isv_scenic_name:
            if hasattr(self.isv_scenic_name, 'to_alipay_dict'):
                params['isv_scenic_name'] = self.isv_scenic_name.to_alipay_dict()
            else:
                params['isv_scenic_name'] = self.isv_scenic_name
        if self.outer_id:
            if hasattr(self.outer_id, 'to_alipay_dict'):
                params['outer_id'] = self.outer_id.to_alipay_dict()
            else:
                params['outer_id'] = self.outer_id
        if self.scenic_app_id:
            if hasattr(self.scenic_app_id, 'to_alipay_dict'):
                params['scenic_app_id'] = self.scenic_app_id.to_alipay_dict()
            else:
                params['scenic_app_id'] = self.scenic_app_id
        if self.scenic_id:
            if hasattr(self.scenic_id, 'to_alipay_dict'):
                params['scenic_id'] = self.scenic_id.to_alipay_dict()
            else:
                params['scenic_id'] = self.scenic_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceDataScenicSyncModel()
        if 'code_value' in d:
            o.code_value = d['code_value']
        if 'isv_name' in d:
            o.isv_name = d['isv_name']
        if 'isv_scenic_address' in d:
            o.isv_scenic_address = d['isv_scenic_address']
        if 'isv_scenic_name' in d:
            o.isv_scenic_name = d['isv_scenic_name']
        if 'outer_id' in d:
            o.outer_id = d['outer_id']
        if 'scenic_app_id' in d:
            o.scenic_app_id = d['scenic_app_id']
        if 'scenic_id' in d:
            o.scenic_id = d['scenic_id']
        return o


