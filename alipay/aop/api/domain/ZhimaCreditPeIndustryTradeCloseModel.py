#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ZhimaCreditPeIndustryTradeCloseModel(object):

    def __init__(self):
        self._close_time = None
        self._ext_info = None
        self._operate = None
        self._out_fund_no = None
        self._product_code = None
        self._zm_order_id = None

    @property
    def close_time(self):
        return self._close_time

    @close_time.setter
    def close_time(self, value):
        self._close_time = value
    @property
    def ext_info(self):
        return self._ext_info

    @ext_info.setter
    def ext_info(self, value):
        self._ext_info = value
    @property
    def operate(self):
        return self._operate

    @operate.setter
    def operate(self, value):
        self._operate = value
    @property
    def out_fund_no(self):
        return self._out_fund_no

    @out_fund_no.setter
    def out_fund_no(self, value):
        self._out_fund_no = value
    @property
    def product_code(self):
        return self._product_code

    @product_code.setter
    def product_code(self, value):
        self._product_code = value
    @property
    def zm_order_id(self):
        return self._zm_order_id

    @zm_order_id.setter
    def zm_order_id(self, value):
        self._zm_order_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.close_time:
            if hasattr(self.close_time, 'to_alipay_dict'):
                params['close_time'] = self.close_time.to_alipay_dict()
            else:
                params['close_time'] = self.close_time
        if self.ext_info:
            if hasattr(self.ext_info, 'to_alipay_dict'):
                params['ext_info'] = self.ext_info.to_alipay_dict()
            else:
                params['ext_info'] = self.ext_info
        if self.operate:
            if hasattr(self.operate, 'to_alipay_dict'):
                params['operate'] = self.operate.to_alipay_dict()
            else:
                params['operate'] = self.operate
        if self.out_fund_no:
            if hasattr(self.out_fund_no, 'to_alipay_dict'):
                params['out_fund_no'] = self.out_fund_no.to_alipay_dict()
            else:
                params['out_fund_no'] = self.out_fund_no
        if self.product_code:
            if hasattr(self.product_code, 'to_alipay_dict'):
                params['product_code'] = self.product_code.to_alipay_dict()
            else:
                params['product_code'] = self.product_code
        if self.zm_order_id:
            if hasattr(self.zm_order_id, 'to_alipay_dict'):
                params['zm_order_id'] = self.zm_order_id.to_alipay_dict()
            else:
                params['zm_order_id'] = self.zm_order_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ZhimaCreditPeIndustryTradeCloseModel()
        if 'close_time' in d:
            o.close_time = d['close_time']
        if 'ext_info' in d:
            o.ext_info = d['ext_info']
        if 'operate' in d:
            o.operate = d['operate']
        if 'out_fund_no' in d:
            o.out_fund_no = d['out_fund_no']
        if 'product_code' in d:
            o.product_code = d['product_code']
        if 'zm_order_id' in d:
            o.zm_order_id = d['zm_order_id']
        return o


