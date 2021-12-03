#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.SettleConfirmExtendParams import SettleConfirmExtendParams
from alipay.aop.api.domain.SettleInfo import SettleInfo


class AlipayTradeSettleConfirmModel(object):

    def __init__(self):
        self._extend_params = None
        self._out_request_no = None
        self._settle_info = None
        self._trade_no = None

    @property
    def extend_params(self):
        return self._extend_params

    @extend_params.setter
    def extend_params(self, value):
        if isinstance(value, SettleConfirmExtendParams):
            self._extend_params = value
        else:
            self._extend_params = SettleConfirmExtendParams.from_alipay_dict(value)
    @property
    def out_request_no(self):
        return self._out_request_no

    @out_request_no.setter
    def out_request_no(self, value):
        self._out_request_no = value
    @property
    def settle_info(self):
        return self._settle_info

    @settle_info.setter
    def settle_info(self, value):
        if isinstance(value, SettleInfo):
            self._settle_info = value
        else:
            self._settle_info = SettleInfo.from_alipay_dict(value)
    @property
    def trade_no(self):
        return self._trade_no

    @trade_no.setter
    def trade_no(self, value):
        self._trade_no = value


    def to_alipay_dict(self):
        params = dict()
        if self.extend_params:
            if hasattr(self.extend_params, 'to_alipay_dict'):
                params['extend_params'] = self.extend_params.to_alipay_dict()
            else:
                params['extend_params'] = self.extend_params
        if self.out_request_no:
            if hasattr(self.out_request_no, 'to_alipay_dict'):
                params['out_request_no'] = self.out_request_no.to_alipay_dict()
            else:
                params['out_request_no'] = self.out_request_no
        if self.settle_info:
            if hasattr(self.settle_info, 'to_alipay_dict'):
                params['settle_info'] = self.settle_info.to_alipay_dict()
            else:
                params['settle_info'] = self.settle_info
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
        o = AlipayTradeSettleConfirmModel()
        if 'extend_params' in d:
            o.extend_params = d['extend_params']
        if 'out_request_no' in d:
            o.out_request_no = d['out_request_no']
        if 'settle_info' in d:
            o.settle_info = d['settle_info']
        if 'trade_no' in d:
            o.trade_no = d['trade_no']
        return o


