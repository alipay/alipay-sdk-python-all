#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayEcoCityserviceExtOrdercompleteQueryModel(object):

    def __init__(self):
        self._order_type = None
        self._out_request_no = None
        self._out_trade_no = None
        self._sync_app_id = None

    @property
    def order_type(self):
        return self._order_type

    @order_type.setter
    def order_type(self, value):
        self._order_type = value
    @property
    def out_request_no(self):
        return self._out_request_no

    @out_request_no.setter
    def out_request_no(self, value):
        self._out_request_no = value
    @property
    def out_trade_no(self):
        return self._out_trade_no

    @out_trade_no.setter
    def out_trade_no(self, value):
        self._out_trade_no = value
    @property
    def sync_app_id(self):
        return self._sync_app_id

    @sync_app_id.setter
    def sync_app_id(self, value):
        self._sync_app_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.order_type:
            if hasattr(self.order_type, 'to_alipay_dict'):
                params['order_type'] = self.order_type.to_alipay_dict()
            else:
                params['order_type'] = self.order_type
        if self.out_request_no:
            if hasattr(self.out_request_no, 'to_alipay_dict'):
                params['out_request_no'] = self.out_request_no.to_alipay_dict()
            else:
                params['out_request_no'] = self.out_request_no
        if self.out_trade_no:
            if hasattr(self.out_trade_no, 'to_alipay_dict'):
                params['out_trade_no'] = self.out_trade_no.to_alipay_dict()
            else:
                params['out_trade_no'] = self.out_trade_no
        if self.sync_app_id:
            if hasattr(self.sync_app_id, 'to_alipay_dict'):
                params['sync_app_id'] = self.sync_app_id.to_alipay_dict()
            else:
                params['sync_app_id'] = self.sync_app_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayEcoCityserviceExtOrdercompleteQueryModel()
        if 'order_type' in d:
            o.order_type = d['order_type']
        if 'out_request_no' in d:
            o.out_request_no = d['out_request_no']
        if 'out_trade_no' in d:
            o.out_trade_no = d['out_trade_no']
        if 'sync_app_id' in d:
            o.sync_app_id = d['sync_app_id']
        return o


