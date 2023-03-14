#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.IdTypeTestComplexParam import IdTypeTestComplexParam
from alipay.aop.api.domain.IdTypeTestComplexParam import IdTypeTestComplexParam


class AlipayOpenAppIdtypetestallOpenidbizmockBatchqueryModel(object):

    def __init__(self):
        self._extra_param_input = None
        self._id_type = None
        self._id_type_list = None
        self._id_type_test_complex_param = None
        self._id_type_test_complex_param_list = None
        self._open_id = None
        self._open_id_list = None
        self._user_id = None
        self._user_id_list = None

    @property
    def extra_param_input(self):
        return self._extra_param_input

    @extra_param_input.setter
    def extra_param_input(self, value):
        self._extra_param_input = value
    @property
    def id_type(self):
        return self._id_type

    @id_type.setter
    def id_type(self, value):
        self._id_type = value
    @property
    def id_type_list(self):
        return self._id_type_list

    @id_type_list.setter
    def id_type_list(self, value):
        self._id_type_list = value
    @property
    def id_type_test_complex_param(self):
        return self._id_type_test_complex_param

    @id_type_test_complex_param.setter
    def id_type_test_complex_param(self, value):
        if isinstance(value, IdTypeTestComplexParam):
            self._id_type_test_complex_param = value
        else:
            self._id_type_test_complex_param = IdTypeTestComplexParam.from_alipay_dict(value)
    @property
    def id_type_test_complex_param_list(self):
        return self._id_type_test_complex_param_list

    @id_type_test_complex_param_list.setter
    def id_type_test_complex_param_list(self, value):
        if isinstance(value, list):
            self._id_type_test_complex_param_list = list()
            for i in value:
                if isinstance(i, IdTypeTestComplexParam):
                    self._id_type_test_complex_param_list.append(i)
                else:
                    self._id_type_test_complex_param_list.append(IdTypeTestComplexParam.from_alipay_dict(i))
    @property
    def open_id(self):
        return self._open_id

    @open_id.setter
    def open_id(self, value):
        self._open_id = value
    @property
    def open_id_list(self):
        return self._open_id_list

    @open_id_list.setter
    def open_id_list(self, value):
        if isinstance(value, list):
            self._open_id_list = list()
            for i in value:
                self._open_id_list.append(i)
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value
    @property
    def user_id_list(self):
        return self._user_id_list

    @user_id_list.setter
    def user_id_list(self, value):
        if isinstance(value, list):
            self._user_id_list = list()
            for i in value:
                self._user_id_list.append(i)


    def to_alipay_dict(self):
        params = dict()
        if self.extra_param_input:
            if hasattr(self.extra_param_input, 'to_alipay_dict'):
                params['extra_param_input'] = self.extra_param_input.to_alipay_dict()
            else:
                params['extra_param_input'] = self.extra_param_input
        if self.id_type:
            if hasattr(self.id_type, 'to_alipay_dict'):
                params['id_type'] = self.id_type.to_alipay_dict()
            else:
                params['id_type'] = self.id_type
        if self.id_type_list:
            if hasattr(self.id_type_list, 'to_alipay_dict'):
                params['id_type_list'] = self.id_type_list.to_alipay_dict()
            else:
                params['id_type_list'] = self.id_type_list
        if self.id_type_test_complex_param:
            if hasattr(self.id_type_test_complex_param, 'to_alipay_dict'):
                params['id_type_test_complex_param'] = self.id_type_test_complex_param.to_alipay_dict()
            else:
                params['id_type_test_complex_param'] = self.id_type_test_complex_param
        if self.id_type_test_complex_param_list:
            if isinstance(self.id_type_test_complex_param_list, list):
                for i in range(0, len(self.id_type_test_complex_param_list)):
                    element = self.id_type_test_complex_param_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.id_type_test_complex_param_list[i] = element.to_alipay_dict()
            if hasattr(self.id_type_test_complex_param_list, 'to_alipay_dict'):
                params['id_type_test_complex_param_list'] = self.id_type_test_complex_param_list.to_alipay_dict()
            else:
                params['id_type_test_complex_param_list'] = self.id_type_test_complex_param_list
        if self.open_id:
            if hasattr(self.open_id, 'to_alipay_dict'):
                params['open_id'] = self.open_id.to_alipay_dict()
            else:
                params['open_id'] = self.open_id
        if self.open_id_list:
            if isinstance(self.open_id_list, list):
                for i in range(0, len(self.open_id_list)):
                    element = self.open_id_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.open_id_list[i] = element.to_alipay_dict()
            if hasattr(self.open_id_list, 'to_alipay_dict'):
                params['open_id_list'] = self.open_id_list.to_alipay_dict()
            else:
                params['open_id_list'] = self.open_id_list
        if self.user_id:
            if hasattr(self.user_id, 'to_alipay_dict'):
                params['user_id'] = self.user_id.to_alipay_dict()
            else:
                params['user_id'] = self.user_id
        if self.user_id_list:
            if isinstance(self.user_id_list, list):
                for i in range(0, len(self.user_id_list)):
                    element = self.user_id_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.user_id_list[i] = element.to_alipay_dict()
            if hasattr(self.user_id_list, 'to_alipay_dict'):
                params['user_id_list'] = self.user_id_list.to_alipay_dict()
            else:
                params['user_id_list'] = self.user_id_list
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayOpenAppIdtypetestallOpenidbizmockBatchqueryModel()
        if 'extra_param_input' in d:
            o.extra_param_input = d['extra_param_input']
        if 'id_type' in d:
            o.id_type = d['id_type']
        if 'id_type_list' in d:
            o.id_type_list = d['id_type_list']
        if 'id_type_test_complex_param' in d:
            o.id_type_test_complex_param = d['id_type_test_complex_param']
        if 'id_type_test_complex_param_list' in d:
            o.id_type_test_complex_param_list = d['id_type_test_complex_param_list']
        if 'open_id' in d:
            o.open_id = d['open_id']
        if 'open_id_list' in d:
            o.open_id_list = d['open_id_list']
        if 'user_id' in d:
            o.user_id = d['user_id']
        if 'user_id_list' in d:
            o.user_id_list = d['user_id_list']
        return o


