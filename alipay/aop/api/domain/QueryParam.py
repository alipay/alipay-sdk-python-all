#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.ShowText import ShowText


class QueryParam(object):

    def __init__(self):
        self._ftoken = None
        self._show_text = None
        self._trade_no = None

    @property
    def ftoken(self):
        return self._ftoken

    @ftoken.setter
    def ftoken(self, value):
        self._ftoken = value
    @property
    def show_text(self):
        return self._show_text

    @show_text.setter
    def show_text(self, value):
        if isinstance(value, ShowText):
            self._show_text = value
        else:
            self._show_text = ShowText.from_alipay_dict(value)
    @property
    def trade_no(self):
        return self._trade_no

    @trade_no.setter
    def trade_no(self, value):
        self._trade_no = value


    def to_alipay_dict(self):
        params = dict()
        if self.ftoken:
            if hasattr(self.ftoken, 'to_alipay_dict'):
                params['ftoken'] = self.ftoken.to_alipay_dict()
            else:
                params['ftoken'] = self.ftoken
        if self.show_text:
            if hasattr(self.show_text, 'to_alipay_dict'):
                params['show_text'] = self.show_text.to_alipay_dict()
            else:
                params['show_text'] = self.show_text
        if self.trade_no:
            if hasattr(self.trade_no, 'to_alipay_dict'):
                params['trade_no'] = self.trade_no.to_alipay_dict()
            else:
                params['trade_no'] = self.trade_no
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = QueryParam()
        if 'ftoken' in d:
            o.ftoken = d['ftoken']
        if 'show_text' in d:
            o.show_text = d['show_text']
        if 'trade_no' in d:
            o.trade_no = d['trade_no']
        return o


