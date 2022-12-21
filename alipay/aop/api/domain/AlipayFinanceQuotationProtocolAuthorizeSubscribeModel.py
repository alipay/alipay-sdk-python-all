#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayFinanceQuotationProtocolAuthorizeSubscribeModel(object):

    def __init__(self):
        self._open_id = None
        self._protocol_type_list = None
        self._sign_content = None
        self._symbols = None
        self._user_id = None

    @property
    def open_id(self):
        return self._open_id

    @open_id.setter
    def open_id(self, value):
        self._open_id = value
    @property
    def protocol_type_list(self):
        return self._protocol_type_list

    @protocol_type_list.setter
    def protocol_type_list(self, value):
        if isinstance(value, list):
            self._protocol_type_list = list()
            for i in value:
                self._protocol_type_list.append(i)
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
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.open_id:
            if hasattr(self.open_id, 'to_alipay_dict'):
                params['open_id'] = self.open_id.to_alipay_dict()
            else:
                params['open_id'] = self.open_id
        if self.protocol_type_list:
            if isinstance(self.protocol_type_list, list):
                for i in range(0, len(self.protocol_type_list)):
                    element = self.protocol_type_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.protocol_type_list[i] = element.to_alipay_dict()
            if hasattr(self.protocol_type_list, 'to_alipay_dict'):
                params['protocol_type_list'] = self.protocol_type_list.to_alipay_dict()
            else:
                params['protocol_type_list'] = self.protocol_type_list
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
        if self.user_id:
            if hasattr(self.user_id, 'to_alipay_dict'):
                params['user_id'] = self.user_id.to_alipay_dict()
            else:
                params['user_id'] = self.user_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayFinanceQuotationProtocolAuthorizeSubscribeModel()
        if 'open_id' in d:
            o.open_id = d['open_id']
        if 'protocol_type_list' in d:
            o.protocol_type_list = d['protocol_type_list']
        if 'sign_content' in d:
            o.sign_content = d['sign_content']
        if 'symbols' in d:
            o.symbols = d['symbols']
        if 'user_id' in d:
            o.user_id = d['user_id']
        return o


