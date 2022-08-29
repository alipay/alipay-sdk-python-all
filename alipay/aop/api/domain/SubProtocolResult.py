#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class SubProtocolResult(object):

    def __init__(self):
        self._protocol_type = None
        self._result = None
        self._sign_content = None
        self._symbols = None

    @property
    def protocol_type(self):
        return self._protocol_type

    @protocol_type.setter
    def protocol_type(self, value):
        self._protocol_type = value
    @property
    def result(self):
        return self._result

    @result.setter
    def result(self, value):
        self._result = value
    @property
    def sign_content(self):
        return self._sign_content

    @sign_content.setter
    def sign_content(self, value):
        self._sign_content = value
    @property
    def symbols(self):
        return self._symbols

    @symbols.setter
    def symbols(self, value):
        if isinstance(value, list):
            self._symbols = list()
            for i in value:
                self._symbols.append(i)


    def to_alipay_dict(self):
        params = dict()
        if self.protocol_type:
            if hasattr(self.protocol_type, 'to_alipay_dict'):
                params['protocol_type'] = self.protocol_type.to_alipay_dict()
            else:
                params['protocol_type'] = self.protocol_type
        if self.result:
            if hasattr(self.result, 'to_alipay_dict'):
                params['result'] = self.result.to_alipay_dict()
            else:
                params['result'] = self.result
        if self.sign_content:
            if hasattr(self.sign_content, 'to_alipay_dict'):
                params['sign_content'] = self.sign_content.to_alipay_dict()
            else:
                params['sign_content'] = self.sign_content
        if self.symbols:
            if isinstance(self.symbols, list):
                for i in range(0, len(self.symbols)):
                    element = self.symbols[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.symbols[i] = element.to_alipay_dict()
            if hasattr(self.symbols, 'to_alipay_dict'):
                params['symbols'] = self.symbols.to_alipay_dict()
            else:
                params['symbols'] = self.symbols
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = SubProtocolResult()
        if 'protocol_type' in d:
            o.protocol_type = d['protocol_type']
        if 'result' in d:
            o.result = d['result']
        if 'sign_content' in d:
            o.sign_content = d['sign_content']
        if 'symbols' in d:
            o.symbols = d['symbols']
        return o


