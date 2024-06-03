#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class OpenGoodsCheckDetail(object):

    def __init__(self):
        self._check_result = None
        self._code = None
        self._detail_text = None

    @property
    def check_result(self):
        return self._check_result

    @check_result.setter
    def check_result(self, value):
        self._check_result = value
    @property
    def code(self):
        return self._code

    @code.setter
    def code(self, value):
        self._code = value
    @property
    def detail_text(self):
        return self._detail_text

    @detail_text.setter
    def detail_text(self, value):
        self._detail_text = value


    def to_alipay_dict(self):
        params = dict()
        if self.check_result:
            if hasattr(self.check_result, 'to_alipay_dict'):
                params['check_result'] = self.check_result.to_alipay_dict()
            else:
                params['check_result'] = self.check_result
        if self.code:
            if hasattr(self.code, 'to_alipay_dict'):
                params['code'] = self.code.to_alipay_dict()
            else:
                params['code'] = self.code
        if self.detail_text:
            if hasattr(self.detail_text, 'to_alipay_dict'):
                params['detail_text'] = self.detail_text.to_alipay_dict()
            else:
                params['detail_text'] = self.detail_text
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = OpenGoodsCheckDetail()
        if 'check_result' in d:
            o.check_result = d['check_result']
        if 'code' in d:
            o.code = d['code']
        if 'detail_text' in d:
            o.detail_text = d['detail_text']
        return o


