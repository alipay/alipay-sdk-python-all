#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayTradeOrderinfoSyncModel(object):

    def __init__(self):
        self._biz_type = None
        self._order_biz_info = None
        self._orig_request_no = None
        self._out_request_no = None
        self._trade_no = None

    @property
    def biz_type(self):
        return self._biz_type

    @biz_type.setter
    def biz_type(self, value):
        self._biz_type = value
    @property
    def order_biz_info(self):
        return self._order_biz_info

    @order_biz_info.setter
    def order_biz_info(self, value):
        self._order_biz_info = value
    @property
    def orig_request_no(self):
        return self._orig_request_no

    @orig_request_no.setter
    def orig_request_no(self, value):
        self._orig_request_no = value
    @property
    def out_request_no(self):
        return self._out_request_no

    @out_request_no.setter
    def out_request_no(self, value):
        self._out_request_no = value
    @property
    def trade_no(self):
        return self._trade_no

    @trade_no.setter
    def trade_no(self, value):
        self._trade_no = value


    def to_alipay_dict(self):
        params = dict()
        if self.biz_type:
            if hasattr(self.biz_type, 'to_alipay_dict'):
                params['biz_type'] = self.biz_type.to_alipay_dict()
            else:
                params['biz_type'] = self.biz_type
        if self.order_biz_info:
            if hasattr(self.order_biz_info, 'to_alipay_dict'):
                params['order_biz_info'] = self.order_biz_info.to_alipay_dict()
            else:
                params['order_biz_info'] = self.order_biz_info
        if self.orig_request_no:
            if hasattr(self.orig_request_no, 'to_alipay_dict'):
                params['orig_request_no'] = self.orig_request_no.to_alipay_dict()
            else:
                params['orig_request_no'] = self.orig_request_no
        if self.out_request_no:
            if hasattr(self.out_request_no, 'to_alipay_dict'):
                params['out_request_no'] = self.out_request_no.to_alipay_dict()
            else:
                params['out_request_no'] = self.out_request_no
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
        o = AlipayTradeOrderinfoSyncModel()
        if 'biz_type' in d:
            o.biz_type = d['biz_type']
        if 'order_biz_info' in d:
            o.order_biz_info = d['order_biz_info']
        if 'orig_request_no' in d:
            o.orig_request_no = d['orig_request_no']
        if 'out_request_no' in d:
            o.out_request_no = d['out_request_no']
        if 'trade_no' in d:
            o.trade_no = d['trade_no']
        return o


