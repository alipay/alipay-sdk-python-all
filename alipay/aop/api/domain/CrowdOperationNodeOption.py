#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.CrowdOperationNodeOptionDetail import CrowdOperationNodeOptionDetail


class CrowdOperationNodeOption(object):

    def __init__(self):
        self._code = None
        self._id = None
        self._name = None
        self._option_id_list = None
        self._option_list = None
        self._option_text_list = None
        self._option_value_list = None

    @property
    def code(self):
        return self._code

    @code.setter
    def code(self, value):
        self._code = value
    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        self._id = value
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value
    @property
    def option_id_list(self):
        return self._option_id_list

    @option_id_list.setter
    def option_id_list(self, value):
        self._option_id_list = value
    @property
    def option_list(self):
        return self._option_list

    @option_list.setter
    def option_list(self, value):
        if isinstance(value, list):
            self._option_list = list()
            for i in value:
                if isinstance(i, CrowdOperationNodeOptionDetail):
                    self._option_list.append(i)
                else:
                    self._option_list.append(CrowdOperationNodeOptionDetail.from_alipay_dict(i))
    @property
    def option_text_list(self):
        return self._option_text_list

    @option_text_list.setter
    def option_text_list(self, value):
        self._option_text_list = value
    @property
    def option_value_list(self):
        return self._option_value_list

    @option_value_list.setter
    def option_value_list(self, value):
        self._option_value_list = value


    def to_alipay_dict(self):
        params = dict()
        if self.code:
            if hasattr(self.code, 'to_alipay_dict'):
                params['code'] = self.code.to_alipay_dict()
            else:
                params['code'] = self.code
        if self.id:
            if hasattr(self.id, 'to_alipay_dict'):
                params['id'] = self.id.to_alipay_dict()
            else:
                params['id'] = self.id
        if self.name:
            if hasattr(self.name, 'to_alipay_dict'):
                params['name'] = self.name.to_alipay_dict()
            else:
                params['name'] = self.name
        if self.option_id_list:
            if hasattr(self.option_id_list, 'to_alipay_dict'):
                params['option_id_list'] = self.option_id_list.to_alipay_dict()
            else:
                params['option_id_list'] = self.option_id_list
        if self.option_list:
            if isinstance(self.option_list, list):
                for i in range(0, len(self.option_list)):
                    element = self.option_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.option_list[i] = element.to_alipay_dict()
            if hasattr(self.option_list, 'to_alipay_dict'):
                params['option_list'] = self.option_list.to_alipay_dict()
            else:
                params['option_list'] = self.option_list
        if self.option_text_list:
            if hasattr(self.option_text_list, 'to_alipay_dict'):
                params['option_text_list'] = self.option_text_list.to_alipay_dict()
            else:
                params['option_text_list'] = self.option_text_list
        if self.option_value_list:
            if hasattr(self.option_value_list, 'to_alipay_dict'):
                params['option_value_list'] = self.option_value_list.to_alipay_dict()
            else:
                params['option_value_list'] = self.option_value_list
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = CrowdOperationNodeOption()
        if 'code' in d:
            o.code = d['code']
        if 'id' in d:
            o.id = d['id']
        if 'name' in d:
            o.name = d['name']
        if 'option_id_list' in d:
            o.option_id_list = d['option_id_list']
        if 'option_list' in d:
            o.option_list = d['option_list']
        if 'option_text_list' in d:
            o.option_text_list = d['option_text_list']
        if 'option_value_list' in d:
            o.option_value_list = d['option_value_list']
        return o


