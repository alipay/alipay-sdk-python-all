#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceTransportParkingReserveConfirmModel(object):

    def __init__(self):
        self._conf_reslut = None
        self._desc = None
        self._order_id = None
        self._out_trade_no = None
        self._parking_id = None

    @property
    def conf_reslut(self):
        return self._conf_reslut

    @conf_reslut.setter
    def conf_reslut(self, value):
        self._conf_reslut = value
    @property
    def desc(self):
        return self._desc

    @desc.setter
    def desc(self, value):
        self._desc = value
    @property
    def order_id(self):
        return self._order_id

    @order_id.setter
    def order_id(self, value):
        self._order_id = value
    @property
    def out_trade_no(self):
        return self._out_trade_no

    @out_trade_no.setter
    def out_trade_no(self, value):
        self._out_trade_no = value
    @property
    def parking_id(self):
        return self._parking_id

    @parking_id.setter
    def parking_id(self, value):
        self._parking_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.conf_reslut:
            if hasattr(self.conf_reslut, 'to_alipay_dict'):
                params['conf_reslut'] = self.conf_reslut.to_alipay_dict()
            else:
                params['conf_reslut'] = self.conf_reslut
        if self.desc:
            if hasattr(self.desc, 'to_alipay_dict'):
                params['desc'] = self.desc.to_alipay_dict()
            else:
                params['desc'] = self.desc
        if self.order_id:
            if hasattr(self.order_id, 'to_alipay_dict'):
                params['order_id'] = self.order_id.to_alipay_dict()
            else:
                params['order_id'] = self.order_id
        if self.out_trade_no:
            if hasattr(self.out_trade_no, 'to_alipay_dict'):
                params['out_trade_no'] = self.out_trade_no.to_alipay_dict()
            else:
                params['out_trade_no'] = self.out_trade_no
        if self.parking_id:
            if hasattr(self.parking_id, 'to_alipay_dict'):
                params['parking_id'] = self.parking_id.to_alipay_dict()
            else:
                params['parking_id'] = self.parking_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceTransportParkingReserveConfirmModel()
        if 'conf_reslut' in d:
            o.conf_reslut = d['conf_reslut']
        if 'desc' in d:
            o.desc = d['desc']
        if 'order_id' in d:
            o.order_id = d['order_id']
        if 'out_trade_no' in d:
            o.out_trade_no = d['out_trade_no']
        if 'parking_id' in d:
            o.parking_id = d['parking_id']
        return o


