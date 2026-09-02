#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceMedicalDoctorgwHomecacheDeleteModel(object):

    def __init__(self):
        self._delete_all = None
        self._module_codes = None
        self._open_id = None
        self._out_user_id = None
        self._out_user_type = None

    @property
    def delete_all(self):
        return self._delete_all

    @delete_all.setter
    def delete_all(self, value):
        self._delete_all = value
    @property
    def module_codes(self):
        return self._module_codes

    @module_codes.setter
    def module_codes(self, value):
        if isinstance(value, list):
            self._module_codes = list()
            for i in value:
                self._module_codes.append(i)
    @property
    def open_id(self):
        return self._open_id

    @open_id.setter
    def open_id(self, value):
        self._open_id = value
    @property
    def out_user_id(self):
        return self._out_user_id

    @out_user_id.setter
    def out_user_id(self, value):
        self._out_user_id = value
    @property
    def out_user_type(self):
        return self._out_user_type

    @out_user_type.setter
    def out_user_type(self, value):
        self._out_user_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.delete_all:
            if hasattr(self.delete_all, 'to_alipay_dict'):
                params['delete_all'] = self.delete_all.to_alipay_dict()
            else:
                params['delete_all'] = self.delete_all
        if self.module_codes:
            if isinstance(self.module_codes, list):
                for i in range(0, len(self.module_codes)):
                    element = self.module_codes[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.module_codes[i] = element.to_alipay_dict()
            if hasattr(self.module_codes, 'to_alipay_dict'):
                params['module_codes'] = self.module_codes.to_alipay_dict()
            else:
                params['module_codes'] = self.module_codes
        if self.open_id:
            if hasattr(self.open_id, 'to_alipay_dict'):
                params['open_id'] = self.open_id.to_alipay_dict()
            else:
                params['open_id'] = self.open_id
        if self.out_user_id:
            if hasattr(self.out_user_id, 'to_alipay_dict'):
                params['out_user_id'] = self.out_user_id.to_alipay_dict()
            else:
                params['out_user_id'] = self.out_user_id
        if self.out_user_type:
            if hasattr(self.out_user_type, 'to_alipay_dict'):
                params['out_user_type'] = self.out_user_type.to_alipay_dict()
            else:
                params['out_user_type'] = self.out_user_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceMedicalDoctorgwHomecacheDeleteModel()
        if 'delete_all' in d:
            o.delete_all = d['delete_all']
        if 'module_codes' in d:
            o.module_codes = d['module_codes']
        if 'open_id' in d:
            o.open_id = d['open_id']
        if 'out_user_id' in d:
            o.out_user_id = d['out_user_id']
        if 'out_user_type' in d:
            o.out_user_type = d['out_user_type']
        return o


