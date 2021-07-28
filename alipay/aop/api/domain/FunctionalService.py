#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.OrderExtInfo import OrderExtInfo


class FunctionalService(object):

    def __init__(self):
        self._content = None
        self._ext_info = None
        self._function_code = None
        self._function_name = None
        self._function_type = None
        self._function_url = None
        self._memo = None

    @property
    def content(self):
        return self._content

    @content.setter
    def content(self, value):
        self._content = value
    @property
    def ext_info(self):
        return self._ext_info

    @ext_info.setter
    def ext_info(self, value):
        if isinstance(value, list):
            self._ext_info = list()
            for i in value:
                if isinstance(i, OrderExtInfo):
                    self._ext_info.append(i)
                else:
                    self._ext_info.append(OrderExtInfo.from_alipay_dict(i))
    @property
    def function_code(self):
        return self._function_code

    @function_code.setter
    def function_code(self, value):
        self._function_code = value
    @property
    def function_name(self):
        return self._function_name

    @function_name.setter
    def function_name(self, value):
        self._function_name = value
    @property
    def function_type(self):
        return self._function_type

    @function_type.setter
    def function_type(self, value):
        self._function_type = value
    @property
    def function_url(self):
        return self._function_url

    @function_url.setter
    def function_url(self, value):
        self._function_url = value
    @property
    def memo(self):
        return self._memo

    @memo.setter
    def memo(self, value):
        self._memo = value


    def to_alipay_dict(self):
        params = dict()
        if self.content:
            if hasattr(self.content, 'to_alipay_dict'):
                params['content'] = self.content.to_alipay_dict()
            else:
                params['content'] = self.content
        if self.ext_info:
            if isinstance(self.ext_info, list):
                for i in range(0, len(self.ext_info)):
                    element = self.ext_info[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.ext_info[i] = element.to_alipay_dict()
            if hasattr(self.ext_info, 'to_alipay_dict'):
                params['ext_info'] = self.ext_info.to_alipay_dict()
            else:
                params['ext_info'] = self.ext_info
        if self.function_code:
            if hasattr(self.function_code, 'to_alipay_dict'):
                params['function_code'] = self.function_code.to_alipay_dict()
            else:
                params['function_code'] = self.function_code
        if self.function_name:
            if hasattr(self.function_name, 'to_alipay_dict'):
                params['function_name'] = self.function_name.to_alipay_dict()
            else:
                params['function_name'] = self.function_name
        if self.function_type:
            if hasattr(self.function_type, 'to_alipay_dict'):
                params['function_type'] = self.function_type.to_alipay_dict()
            else:
                params['function_type'] = self.function_type
        if self.function_url:
            if hasattr(self.function_url, 'to_alipay_dict'):
                params['function_url'] = self.function_url.to_alipay_dict()
            else:
                params['function_url'] = self.function_url
        if self.memo:
            if hasattr(self.memo, 'to_alipay_dict'):
                params['memo'] = self.memo.to_alipay_dict()
            else:
                params['memo'] = self.memo
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = FunctionalService()
        if 'content' in d:
            o.content = d['content']
        if 'ext_info' in d:
            o.ext_info = d['ext_info']
        if 'function_code' in d:
            o.function_code = d['function_code']
        if 'function_name' in d:
            o.function_name = d['function_name']
        if 'function_type' in d:
            o.function_type = d['function_type']
        if 'function_url' in d:
            o.function_url = d['function_url']
        if 'memo' in d:
            o.memo = d['memo']
        return o


