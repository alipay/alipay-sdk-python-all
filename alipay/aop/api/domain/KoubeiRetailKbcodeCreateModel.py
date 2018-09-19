#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.RetailKbcodeCreateVo import RetailKbcodeCreateVo


class KoubeiRetailKbcodeCreateModel(object):

    def __init__(self):
        self._code_info_list = None
        self._code_template = None
        self._code_type = None
        self._request_id = None

    @property
    def code_info_list(self):
        return self._code_info_list

    @code_info_list.setter
    def code_info_list(self, value):
        if isinstance(value, list):
            self._code_info_list = list()
            for i in value:
                if isinstance(i, RetailKbcodeCreateVo):
                    self._code_info_list.append(i)
                else:
                    self._code_info_list.append(RetailKbcodeCreateVo.from_alipay_dict(i))
    @property
    def code_template(self):
        return self._code_template

    @code_template.setter
    def code_template(self, value):
        self._code_template = value
    @property
    def code_type(self):
        return self._code_type

    @code_type.setter
    def code_type(self, value):
        self._code_type = value
    @property
    def request_id(self):
        return self._request_id

    @request_id.setter
    def request_id(self, value):
        self._request_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.code_info_list:
            if isinstance(self.code_info_list, list):
                for i in range(0, len(self.code_info_list)):
                    element = self.code_info_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.code_info_list[i] = element.to_alipay_dict()
            if hasattr(self.code_info_list, 'to_alipay_dict'):
                params['code_info_list'] = self.code_info_list.to_alipay_dict()
            else:
                params['code_info_list'] = self.code_info_list
        if self.code_template:
            if hasattr(self.code_template, 'to_alipay_dict'):
                params['code_template'] = self.code_template.to_alipay_dict()
            else:
                params['code_template'] = self.code_template
        if self.code_type:
            if hasattr(self.code_type, 'to_alipay_dict'):
                params['code_type'] = self.code_type.to_alipay_dict()
            else:
                params['code_type'] = self.code_type
        if self.request_id:
            if hasattr(self.request_id, 'to_alipay_dict'):
                params['request_id'] = self.request_id.to_alipay_dict()
            else:
                params['request_id'] = self.request_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = KoubeiRetailKbcodeCreateModel()
        if 'code_info_list' in d:
            o.code_info_list = d['code_info_list']
        if 'code_template' in d:
            o.code_template = d['code_template']
        if 'code_type' in d:
            o.code_type = d['code_type']
        if 'request_id' in d:
            o.request_id = d['request_id']
        return o


