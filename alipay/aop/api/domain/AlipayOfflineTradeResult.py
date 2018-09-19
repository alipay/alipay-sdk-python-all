#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayOfflineTradeResult(object):

    def __init__(self):
        self._error_code = None
        self._error_message = None
        self._message = None
        self._need_retry = None
        self._next_try_time = None
        self._out_trade_no = None
        self._result = None
        self._trade_no = None

    @property
    def error_code(self):
        return self._error_code

    @error_code.setter
    def error_code(self, value):
        self._error_code = value
    @property
    def error_message(self):
        return self._error_message

    @error_message.setter
    def error_message(self, value):
        self._error_message = value
    @property
    def message(self):
        return self._message

    @message.setter
    def message(self, value):
        self._message = value
    @property
    def need_retry(self):
        return self._need_retry

    @need_retry.setter
    def need_retry(self, value):
        self._need_retry = value
    @property
    def next_try_time(self):
        return self._next_try_time

    @next_try_time.setter
    def next_try_time(self, value):
        self._next_try_time = value
    @property
    def out_trade_no(self):
        return self._out_trade_no

    @out_trade_no.setter
    def out_trade_no(self, value):
        self._out_trade_no = value
    @property
    def result(self):
        return self._result

    @result.setter
    def result(self, value):
        self._result = value
    @property
    def trade_no(self):
        return self._trade_no

    @trade_no.setter
    def trade_no(self, value):
        self._trade_no = value


    def to_alipay_dict(self):
        params = dict()
        if self.error_code:
            if hasattr(self.error_code, 'to_alipay_dict'):
                params['error_code'] = self.error_code.to_alipay_dict()
            else:
                params['error_code'] = self.error_code
        if self.error_message:
            if hasattr(self.error_message, 'to_alipay_dict'):
                params['error_message'] = self.error_message.to_alipay_dict()
            else:
                params['error_message'] = self.error_message
        if self.message:
            if hasattr(self.message, 'to_alipay_dict'):
                params['message'] = self.message.to_alipay_dict()
            else:
                params['message'] = self.message
        if self.need_retry:
            if hasattr(self.need_retry, 'to_alipay_dict'):
                params['need_retry'] = self.need_retry.to_alipay_dict()
            else:
                params['need_retry'] = self.need_retry
        if self.next_try_time:
            if hasattr(self.next_try_time, 'to_alipay_dict'):
                params['next_try_time'] = self.next_try_time.to_alipay_dict()
            else:
                params['next_try_time'] = self.next_try_time
        if self.out_trade_no:
            if hasattr(self.out_trade_no, 'to_alipay_dict'):
                params['out_trade_no'] = self.out_trade_no.to_alipay_dict()
            else:
                params['out_trade_no'] = self.out_trade_no
        if self.result:
            if hasattr(self.result, 'to_alipay_dict'):
                params['result'] = self.result.to_alipay_dict()
            else:
                params['result'] = self.result
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
        o = AlipayOfflineTradeResult()
        if 'error_code' in d:
            o.error_code = d['error_code']
        if 'error_message' in d:
            o.error_message = d['error_message']
        if 'message' in d:
            o.message = d['message']
        if 'need_retry' in d:
            o.need_retry = d['need_retry']
        if 'next_try_time' in d:
            o.next_try_time = d['next_try_time']
        if 'out_trade_no' in d:
            o.out_trade_no = d['out_trade_no']
        if 'result' in d:
            o.result = d['result']
        if 'trade_no' in d:
            o.trade_no = d['trade_no']
        return o


