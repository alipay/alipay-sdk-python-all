#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.IcrowdUseContext import IcrowdUseContext


class IcrowdUseParam(object):

    def __init__(self):
        self._context = None
        self._external_info = None
        self._method_id = None

    @property
    def context(self):
        return self._context

    @context.setter
    def context(self, value):
        if isinstance(value, IcrowdUseContext):
            self._context = value
        else:
            self._context = IcrowdUseContext.from_alipay_dict(value)
    @property
    def external_info(self):
        return self._external_info

    @external_info.setter
    def external_info(self, value):
        if isinstance(value, list):
            self._external_info = list()
            for i in value:
                self._external_info.append(i)
    @property
    def method_id(self):
        return self._method_id

    @method_id.setter
    def method_id(self, value):
        self._method_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.context:
            if hasattr(self.context, 'to_alipay_dict'):
                params['context'] = self.context.to_alipay_dict()
            else:
                params['context'] = self.context
        if self.external_info:
            if isinstance(self.external_info, list):
                for i in range(0, len(self.external_info)):
                    element = self.external_info[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.external_info[i] = element.to_alipay_dict()
            if hasattr(self.external_info, 'to_alipay_dict'):
                params['external_info'] = self.external_info.to_alipay_dict()
            else:
                params['external_info'] = self.external_info
        if self.method_id:
            if hasattr(self.method_id, 'to_alipay_dict'):
                params['method_id'] = self.method_id.to_alipay_dict()
            else:
                params['method_id'] = self.method_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = IcrowdUseParam()
        if 'context' in d:
            o.context = d['context']
        if 'external_info' in d:
            o.external_info = d['external_info']
        if 'method_id' in d:
            o.method_id = d['method_id']
        return o


