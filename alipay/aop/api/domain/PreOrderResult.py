#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class PreOrderResult(object):

    def __init__(self):
        self._app_id = None
        self._out_trade_no = None
        self._result_code = None
        self._success = None

    @property
    def app_id(self):
        return self._app_id

    @app_id.setter
    def app_id(self, value):
        self._app_id = value
    @property
    def out_trade_no(self):
        return self._out_trade_no

    @out_trade_no.setter
    def out_trade_no(self, value):
        self._out_trade_no = value
    @property
    def result_code(self):
        return self._result_code

    @result_code.setter
    def result_code(self, value):
        self._result_code = value
    @property
    def success(self):
        return self._success

    @success.setter
    def success(self, value):
        self._success = value


    def to_alipay_dict(self):
        params = dict()
        if self.app_id:
            if hasattr(self.app_id, 'to_alipay_dict'):
                params['app_id'] = self.app_id.to_alipay_dict()
            else:
                params['app_id'] = self.app_id
        if self.out_trade_no:
            if hasattr(self.out_trade_no, 'to_alipay_dict'):
                params['out_trade_no'] = self.out_trade_no.to_alipay_dict()
            else:
                params['out_trade_no'] = self.out_trade_no
        if self.result_code:
            if hasattr(self.result_code, 'to_alipay_dict'):
                params['result_code'] = self.result_code.to_alipay_dict()
            else:
                params['result_code'] = self.result_code
        if self.success:
            if hasattr(self.success, 'to_alipay_dict'):
                params['success'] = self.success.to_alipay_dict()
            else:
                params['success'] = self.success
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = PreOrderResult()
        if 'app_id' in d:
            o.app_id = d['app_id']
        if 'out_trade_no' in d:
            o.out_trade_no = d['out_trade_no']
        if 'result_code' in d:
            o.result_code = d['result_code']
        if 'success' in d:
            o.success = d['success']
        return o


