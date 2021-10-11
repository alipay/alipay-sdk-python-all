#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceOperationTerminalPowerbankorderFinishModel(object):

    def __init__(self):
        self._extra_param = None
        self._out_trade_id = None
        self._sn = None
        self._status = None
        self._trade_id = None

    @property
    def extra_param(self):
        return self._extra_param

    @extra_param.setter
    def extra_param(self, value):
        self._extra_param = value
    @property
    def out_trade_id(self):
        return self._out_trade_id

    @out_trade_id.setter
    def out_trade_id(self, value):
        self._out_trade_id = value
    @property
    def sn(self):
        return self._sn

    @sn.setter
    def sn(self, value):
        self._sn = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value
    @property
    def trade_id(self):
        return self._trade_id

    @trade_id.setter
    def trade_id(self, value):
        self._trade_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.extra_param:
            if hasattr(self.extra_param, 'to_alipay_dict'):
                params['extra_param'] = self.extra_param.to_alipay_dict()
            else:
                params['extra_param'] = self.extra_param
        if self.out_trade_id:
            if hasattr(self.out_trade_id, 'to_alipay_dict'):
                params['out_trade_id'] = self.out_trade_id.to_alipay_dict()
            else:
                params['out_trade_id'] = self.out_trade_id
        if self.sn:
            if hasattr(self.sn, 'to_alipay_dict'):
                params['sn'] = self.sn.to_alipay_dict()
            else:
                params['sn'] = self.sn
        if self.status:
            if hasattr(self.status, 'to_alipay_dict'):
                params['status'] = self.status.to_alipay_dict()
            else:
                params['status'] = self.status
        if self.trade_id:
            if hasattr(self.trade_id, 'to_alipay_dict'):
                params['trade_id'] = self.trade_id.to_alipay_dict()
            else:
                params['trade_id'] = self.trade_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceOperationTerminalPowerbankorderFinishModel()
        if 'extra_param' in d:
            o.extra_param = d['extra_param']
        if 'out_trade_id' in d:
            o.out_trade_id = d['out_trade_id']
        if 'sn' in d:
            o.sn = d['sn']
        if 'status' in d:
            o.status = d['status']
        if 'trade_id' in d:
            o.trade_id = d['trade_id']
        return o


