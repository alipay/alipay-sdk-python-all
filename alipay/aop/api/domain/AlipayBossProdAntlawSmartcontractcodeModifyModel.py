#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayBossProdAntlawSmartcontractcodeModifyModel(object):

    def __init__(self):
        self._biz_code = None
        self._contract_no = None
        self._request_token = None
        self._source_sys = None
        self._time_stamp = None

    @property
    def biz_code(self):
        return self._biz_code

    @biz_code.setter
    def biz_code(self, value):
        self._biz_code = value
    @property
    def contract_no(self):
        return self._contract_no

    @contract_no.setter
    def contract_no(self, value):
        self._contract_no = value
    @property
    def request_token(self):
        return self._request_token

    @request_token.setter
    def request_token(self, value):
        self._request_token = value
    @property
    def source_sys(self):
        return self._source_sys

    @source_sys.setter
    def source_sys(self, value):
        self._source_sys = value
    @property
    def time_stamp(self):
        return self._time_stamp

    @time_stamp.setter
    def time_stamp(self, value):
        self._time_stamp = value


    def to_alipay_dict(self):
        params = dict()
        if self.biz_code:
            if hasattr(self.biz_code, 'to_alipay_dict'):
                params['biz_code'] = self.biz_code.to_alipay_dict()
            else:
                params['biz_code'] = self.biz_code
        if self.contract_no:
            if hasattr(self.contract_no, 'to_alipay_dict'):
                params['contract_no'] = self.contract_no.to_alipay_dict()
            else:
                params['contract_no'] = self.contract_no
        if self.request_token:
            if hasattr(self.request_token, 'to_alipay_dict'):
                params['request_token'] = self.request_token.to_alipay_dict()
            else:
                params['request_token'] = self.request_token
        if self.source_sys:
            if hasattr(self.source_sys, 'to_alipay_dict'):
                params['source_sys'] = self.source_sys.to_alipay_dict()
            else:
                params['source_sys'] = self.source_sys
        if self.time_stamp:
            if hasattr(self.time_stamp, 'to_alipay_dict'):
                params['time_stamp'] = self.time_stamp.to_alipay_dict()
            else:
                params['time_stamp'] = self.time_stamp
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayBossProdAntlawSmartcontractcodeModifyModel()
        if 'biz_code' in d:
            o.biz_code = d['biz_code']
        if 'contract_no' in d:
            o.contract_no = d['contract_no']
        if 'request_token' in d:
            o.request_token = d['request_token']
        if 'source_sys' in d:
            o.source_sys = d['source_sys']
        if 'time_stamp' in d:
            o.time_stamp = d['time_stamp']
        return o


