#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class IdTypeTestComplexParam(object):

    def __init__(self):
        self._a_id_type = None
        self._a_open_id = None
        self._a_user_id = None
        self._b_id_type_list = None
        self._b_open_id_list = None
        self._b_user_id_list = None
        self._expect_a_id_type = None
        self._expect_a_open_id = None
        self._expect_a_user_id = None
        self._expect_b_id_type_list = None
        self._expect_b_open_id_list = None
        self._expect_b_user_id_list = None

    @property
    def a_id_type(self):
        return self._a_id_type

    @a_id_type.setter
    def a_id_type(self, value):
        self._a_id_type = value
    @property
    def a_open_id(self):
        return self._a_open_id

    @a_open_id.setter
    def a_open_id(self, value):
        self._a_open_id = value
    @property
    def a_user_id(self):
        return self._a_user_id

    @a_user_id.setter
    def a_user_id(self, value):
        self._a_user_id = value
    @property
    def b_id_type_list(self):
        return self._b_id_type_list

    @b_id_type_list.setter
    def b_id_type_list(self, value):
        self._b_id_type_list = value
    @property
    def b_open_id_list(self):
        return self._b_open_id_list

    @b_open_id_list.setter
    def b_open_id_list(self, value):
        if isinstance(value, list):
            self._b_open_id_list = list()
            for i in value:
                self._b_open_id_list.append(i)
    @property
    def b_user_id_list(self):
        return self._b_user_id_list

    @b_user_id_list.setter
    def b_user_id_list(self, value):
        if isinstance(value, list):
            self._b_user_id_list = list()
            for i in value:
                self._b_user_id_list.append(i)
    @property
    def expect_a_id_type(self):
        return self._expect_a_id_type

    @expect_a_id_type.setter
    def expect_a_id_type(self, value):
        self._expect_a_id_type = value
    @property
    def expect_a_open_id(self):
        return self._expect_a_open_id

    @expect_a_open_id.setter
    def expect_a_open_id(self, value):
        self._expect_a_open_id = value
    @property
    def expect_a_user_id(self):
        return self._expect_a_user_id

    @expect_a_user_id.setter
    def expect_a_user_id(self, value):
        self._expect_a_user_id = value
    @property
    def expect_b_id_type_list(self):
        return self._expect_b_id_type_list

    @expect_b_id_type_list.setter
    def expect_b_id_type_list(self, value):
        self._expect_b_id_type_list = value
    @property
    def expect_b_open_id_list(self):
        return self._expect_b_open_id_list

    @expect_b_open_id_list.setter
    def expect_b_open_id_list(self, value):
        if isinstance(value, list):
            self._expect_b_open_id_list = list()
            for i in value:
                self._expect_b_open_id_list.append(i)
    @property
    def expect_b_user_id_list(self):
        return self._expect_b_user_id_list

    @expect_b_user_id_list.setter
    def expect_b_user_id_list(self, value):
        if isinstance(value, list):
            self._expect_b_user_id_list = list()
            for i in value:
                self._expect_b_user_id_list.append(i)


    def to_alipay_dict(self):
        params = dict()
        if self.a_id_type:
            if hasattr(self.a_id_type, 'to_alipay_dict'):
                params['a_id_type'] = self.a_id_type.to_alipay_dict()
            else:
                params['a_id_type'] = self.a_id_type
        if self.a_open_id:
            if hasattr(self.a_open_id, 'to_alipay_dict'):
                params['a_open_id'] = self.a_open_id.to_alipay_dict()
            else:
                params['a_open_id'] = self.a_open_id
        if self.a_user_id:
            if hasattr(self.a_user_id, 'to_alipay_dict'):
                params['a_user_id'] = self.a_user_id.to_alipay_dict()
            else:
                params['a_user_id'] = self.a_user_id
        if self.b_id_type_list:
            if hasattr(self.b_id_type_list, 'to_alipay_dict'):
                params['b_id_type_list'] = self.b_id_type_list.to_alipay_dict()
            else:
                params['b_id_type_list'] = self.b_id_type_list
        if self.b_open_id_list:
            if isinstance(self.b_open_id_list, list):
                for i in range(0, len(self.b_open_id_list)):
                    element = self.b_open_id_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.b_open_id_list[i] = element.to_alipay_dict()
            if hasattr(self.b_open_id_list, 'to_alipay_dict'):
                params['b_open_id_list'] = self.b_open_id_list.to_alipay_dict()
            else:
                params['b_open_id_list'] = self.b_open_id_list
        if self.b_user_id_list:
            if isinstance(self.b_user_id_list, list):
                for i in range(0, len(self.b_user_id_list)):
                    element = self.b_user_id_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.b_user_id_list[i] = element.to_alipay_dict()
            if hasattr(self.b_user_id_list, 'to_alipay_dict'):
                params['b_user_id_list'] = self.b_user_id_list.to_alipay_dict()
            else:
                params['b_user_id_list'] = self.b_user_id_list
        if self.expect_a_id_type:
            if hasattr(self.expect_a_id_type, 'to_alipay_dict'):
                params['expect_a_id_type'] = self.expect_a_id_type.to_alipay_dict()
            else:
                params['expect_a_id_type'] = self.expect_a_id_type
        if self.expect_a_open_id:
            if hasattr(self.expect_a_open_id, 'to_alipay_dict'):
                params['expect_a_open_id'] = self.expect_a_open_id.to_alipay_dict()
            else:
                params['expect_a_open_id'] = self.expect_a_open_id
        if self.expect_a_user_id:
            if hasattr(self.expect_a_user_id, 'to_alipay_dict'):
                params['expect_a_user_id'] = self.expect_a_user_id.to_alipay_dict()
            else:
                params['expect_a_user_id'] = self.expect_a_user_id
        if self.expect_b_id_type_list:
            if hasattr(self.expect_b_id_type_list, 'to_alipay_dict'):
                params['expect_b_id_type_list'] = self.expect_b_id_type_list.to_alipay_dict()
            else:
                params['expect_b_id_type_list'] = self.expect_b_id_type_list
        if self.expect_b_open_id_list:
            if isinstance(self.expect_b_open_id_list, list):
                for i in range(0, len(self.expect_b_open_id_list)):
                    element = self.expect_b_open_id_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.expect_b_open_id_list[i] = element.to_alipay_dict()
            if hasattr(self.expect_b_open_id_list, 'to_alipay_dict'):
                params['expect_b_open_id_list'] = self.expect_b_open_id_list.to_alipay_dict()
            else:
                params['expect_b_open_id_list'] = self.expect_b_open_id_list
        if self.expect_b_user_id_list:
            if isinstance(self.expect_b_user_id_list, list):
                for i in range(0, len(self.expect_b_user_id_list)):
                    element = self.expect_b_user_id_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.expect_b_user_id_list[i] = element.to_alipay_dict()
            if hasattr(self.expect_b_user_id_list, 'to_alipay_dict'):
                params['expect_b_user_id_list'] = self.expect_b_user_id_list.to_alipay_dict()
            else:
                params['expect_b_user_id_list'] = self.expect_b_user_id_list
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = IdTypeTestComplexParam()
        if 'a_id_type' in d:
            o.a_id_type = d['a_id_type']
        if 'a_open_id' in d:
            o.a_open_id = d['a_open_id']
        if 'a_user_id' in d:
            o.a_user_id = d['a_user_id']
        if 'b_id_type_list' in d:
            o.b_id_type_list = d['b_id_type_list']
        if 'b_open_id_list' in d:
            o.b_open_id_list = d['b_open_id_list']
        if 'b_user_id_list' in d:
            o.b_user_id_list = d['b_user_id_list']
        if 'expect_a_id_type' in d:
            o.expect_a_id_type = d['expect_a_id_type']
        if 'expect_a_open_id' in d:
            o.expect_a_open_id = d['expect_a_open_id']
        if 'expect_a_user_id' in d:
            o.expect_a_user_id = d['expect_a_user_id']
        if 'expect_b_id_type_list' in d:
            o.expect_b_id_type_list = d['expect_b_id_type_list']
        if 'expect_b_open_id_list' in d:
            o.expect_b_open_id_list = d['expect_b_open_id_list']
        if 'expect_b_user_id_list' in d:
            o.expect_b_user_id_list = d['expect_b_user_id_list']
        return o


