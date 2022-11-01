#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.ServeParamInfo import ServeParamInfo
from alipay.aop.api.domain.Precondition import Precondition


class UseCaseStepInfo(object):

    def __init__(self):
        self._method_desc = None
        self._method_name = None
        self._operate = None
        self._param_info_list = None
        self._precondition_list = None
        self._response_data = None
        self._step_note = None
        self._type = None

    @property
    def method_desc(self):
        return self._method_desc

    @method_desc.setter
    def method_desc(self, value):
        self._method_desc = value
    @property
    def method_name(self):
        return self._method_name

    @method_name.setter
    def method_name(self, value):
        self._method_name = value
    @property
    def operate(self):
        return self._operate

    @operate.setter
    def operate(self, value):
        self._operate = value
    @property
    def param_info_list(self):
        return self._param_info_list

    @param_info_list.setter
    def param_info_list(self, value):
        if isinstance(value, list):
            self._param_info_list = list()
            for i in value:
                if isinstance(i, ServeParamInfo):
                    self._param_info_list.append(i)
                else:
                    self._param_info_list.append(ServeParamInfo.from_alipay_dict(i))
    @property
    def precondition_list(self):
        return self._precondition_list

    @precondition_list.setter
    def precondition_list(self, value):
        if isinstance(value, list):
            self._precondition_list = list()
            for i in value:
                if isinstance(i, Precondition):
                    self._precondition_list.append(i)
                else:
                    self._precondition_list.append(Precondition.from_alipay_dict(i))
    @property
    def response_data(self):
        return self._response_data

    @response_data.setter
    def response_data(self, value):
        self._response_data = value
    @property
    def step_note(self):
        return self._step_note

    @step_note.setter
    def step_note(self, value):
        self._step_note = value
    @property
    def type(self):
        return self._type

    @type.setter
    def type(self, value):
        self._type = value


    def to_alipay_dict(self):
        params = dict()
        if self.method_desc:
            if hasattr(self.method_desc, 'to_alipay_dict'):
                params['method_desc'] = self.method_desc.to_alipay_dict()
            else:
                params['method_desc'] = self.method_desc
        if self.method_name:
            if hasattr(self.method_name, 'to_alipay_dict'):
                params['method_name'] = self.method_name.to_alipay_dict()
            else:
                params['method_name'] = self.method_name
        if self.operate:
            if hasattr(self.operate, 'to_alipay_dict'):
                params['operate'] = self.operate.to_alipay_dict()
            else:
                params['operate'] = self.operate
        if self.param_info_list:
            if isinstance(self.param_info_list, list):
                for i in range(0, len(self.param_info_list)):
                    element = self.param_info_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.param_info_list[i] = element.to_alipay_dict()
            if hasattr(self.param_info_list, 'to_alipay_dict'):
                params['param_info_list'] = self.param_info_list.to_alipay_dict()
            else:
                params['param_info_list'] = self.param_info_list
        if self.precondition_list:
            if isinstance(self.precondition_list, list):
                for i in range(0, len(self.precondition_list)):
                    element = self.precondition_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.precondition_list[i] = element.to_alipay_dict()
            if hasattr(self.precondition_list, 'to_alipay_dict'):
                params['precondition_list'] = self.precondition_list.to_alipay_dict()
            else:
                params['precondition_list'] = self.precondition_list
        if self.response_data:
            if hasattr(self.response_data, 'to_alipay_dict'):
                params['response_data'] = self.response_data.to_alipay_dict()
            else:
                params['response_data'] = self.response_data
        if self.step_note:
            if hasattr(self.step_note, 'to_alipay_dict'):
                params['step_note'] = self.step_note.to_alipay_dict()
            else:
                params['step_note'] = self.step_note
        if self.type:
            if hasattr(self.type, 'to_alipay_dict'):
                params['type'] = self.type.to_alipay_dict()
            else:
                params['type'] = self.type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = UseCaseStepInfo()
        if 'method_desc' in d:
            o.method_desc = d['method_desc']
        if 'method_name' in d:
            o.method_name = d['method_name']
        if 'operate' in d:
            o.operate = d['operate']
        if 'param_info_list' in d:
            o.param_info_list = d['param_info_list']
        if 'precondition_list' in d:
            o.precondition_list = d['precondition_list']
        if 'response_data' in d:
            o.response_data = d['response_data']
        if 'step_note' in d:
            o.step_note = d['step_note']
        if 'type' in d:
            o.type = d['type']
        return o


