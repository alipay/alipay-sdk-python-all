#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayAssetPointAccountlogQueryModel(object):

    def __init__(self):
        self._account_date_begin = None
        self._account_date_end = None
        self._page_number = None
        self._page_size = None
        self._sub_trans_code = None
        self._trans_code = None
        self._user_symbol = None
        self._user_symbol_type = None

    @property
    def account_date_begin(self):
        return self._account_date_begin

    @account_date_begin.setter
    def account_date_begin(self, value):
        self._account_date_begin = value
    @property
    def account_date_end(self):
        return self._account_date_end

    @account_date_end.setter
    def account_date_end(self, value):
        self._account_date_end = value
    @property
    def page_number(self):
        return self._page_number

    @page_number.setter
    def page_number(self, value):
        self._page_number = value
    @property
    def page_size(self):
        return self._page_size

    @page_size.setter
    def page_size(self, value):
        self._page_size = value
    @property
    def sub_trans_code(self):
        return self._sub_trans_code

    @sub_trans_code.setter
    def sub_trans_code(self, value):
        if isinstance(value, list):
            self._sub_trans_code = list()
            for i in value:
                self._sub_trans_code.append(i)
    @property
    def trans_code(self):
        return self._trans_code

    @trans_code.setter
    def trans_code(self, value):
        if isinstance(value, list):
            self._trans_code = list()
            for i in value:
                self._trans_code.append(i)
    @property
    def user_symbol(self):
        return self._user_symbol

    @user_symbol.setter
    def user_symbol(self, value):
        self._user_symbol = value
    @property
    def user_symbol_type(self):
        return self._user_symbol_type

    @user_symbol_type.setter
    def user_symbol_type(self, value):
        self._user_symbol_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.account_date_begin:
            if hasattr(self.account_date_begin, 'to_alipay_dict'):
                params['account_date_begin'] = self.account_date_begin.to_alipay_dict()
            else:
                params['account_date_begin'] = self.account_date_begin
        if self.account_date_end:
            if hasattr(self.account_date_end, 'to_alipay_dict'):
                params['account_date_end'] = self.account_date_end.to_alipay_dict()
            else:
                params['account_date_end'] = self.account_date_end
        if self.page_number:
            if hasattr(self.page_number, 'to_alipay_dict'):
                params['page_number'] = self.page_number.to_alipay_dict()
            else:
                params['page_number'] = self.page_number
        if self.page_size:
            if hasattr(self.page_size, 'to_alipay_dict'):
                params['page_size'] = self.page_size.to_alipay_dict()
            else:
                params['page_size'] = self.page_size
        if self.sub_trans_code:
            if isinstance(self.sub_trans_code, list):
                for i in range(0, len(self.sub_trans_code)):
                    element = self.sub_trans_code[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.sub_trans_code[i] = element.to_alipay_dict()
            if hasattr(self.sub_trans_code, 'to_alipay_dict'):
                params['sub_trans_code'] = self.sub_trans_code.to_alipay_dict()
            else:
                params['sub_trans_code'] = self.sub_trans_code
        if self.trans_code:
            if isinstance(self.trans_code, list):
                for i in range(0, len(self.trans_code)):
                    element = self.trans_code[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.trans_code[i] = element.to_alipay_dict()
            if hasattr(self.trans_code, 'to_alipay_dict'):
                params['trans_code'] = self.trans_code.to_alipay_dict()
            else:
                params['trans_code'] = self.trans_code
        if self.user_symbol:
            if hasattr(self.user_symbol, 'to_alipay_dict'):
                params['user_symbol'] = self.user_symbol.to_alipay_dict()
            else:
                params['user_symbol'] = self.user_symbol
        if self.user_symbol_type:
            if hasattr(self.user_symbol_type, 'to_alipay_dict'):
                params['user_symbol_type'] = self.user_symbol_type.to_alipay_dict()
            else:
                params['user_symbol_type'] = self.user_symbol_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayAssetPointAccountlogQueryModel()
        if 'account_date_begin' in d:
            o.account_date_begin = d['account_date_begin']
        if 'account_date_end' in d:
            o.account_date_end = d['account_date_end']
        if 'page_number' in d:
            o.page_number = d['page_number']
        if 'page_size' in d:
            o.page_size = d['page_size']
        if 'sub_trans_code' in d:
            o.sub_trans_code = d['sub_trans_code']
        if 'trans_code' in d:
            o.trans_code = d['trans_code']
        if 'user_symbol' in d:
            o.user_symbol = d['user_symbol']
        if 'user_symbol_type' in d:
            o.user_symbol_type = d['user_symbol_type']
        return o


