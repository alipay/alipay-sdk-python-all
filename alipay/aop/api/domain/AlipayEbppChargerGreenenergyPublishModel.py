#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.ChargeOrderInfo import ChargeOrderInfo


class AlipayEbppChargerGreenenergyPublishModel(object):

    def __init__(self):
        self._charge_order_info = None
        self._charge_power = None
        self._operator_id = None
        self._order_type = None
        self._out_biz_no = None
        self._pay_mode = None
        self._trade_no = None
        self._user_id = None

    @property
    def charge_order_info(self):
        return self._charge_order_info

    @charge_order_info.setter
    def charge_order_info(self, value):
        if isinstance(value, ChargeOrderInfo):
            self._charge_order_info = value
        else:
            self._charge_order_info = ChargeOrderInfo.from_alipay_dict(value)
    @property
    def charge_power(self):
        return self._charge_power

    @charge_power.setter
    def charge_power(self, value):
        self._charge_power = value
    @property
    def operator_id(self):
        return self._operator_id

    @operator_id.setter
    def operator_id(self, value):
        self._operator_id = value
    @property
    def order_type(self):
        return self._order_type

    @order_type.setter
    def order_type(self, value):
        self._order_type = value
    @property
    def out_biz_no(self):
        return self._out_biz_no

    @out_biz_no.setter
    def out_biz_no(self, value):
        self._out_biz_no = value
    @property
    def pay_mode(self):
        return self._pay_mode

    @pay_mode.setter
    def pay_mode(self, value):
        self._pay_mode = value
    @property
    def trade_no(self):
        return self._trade_no

    @trade_no.setter
    def trade_no(self, value):
        self._trade_no = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.charge_order_info:
            if hasattr(self.charge_order_info, 'to_alipay_dict'):
                params['charge_order_info'] = self.charge_order_info.to_alipay_dict()
            else:
                params['charge_order_info'] = self.charge_order_info
        if self.charge_power:
            if hasattr(self.charge_power, 'to_alipay_dict'):
                params['charge_power'] = self.charge_power.to_alipay_dict()
            else:
                params['charge_power'] = self.charge_power
        if self.operator_id:
            if hasattr(self.operator_id, 'to_alipay_dict'):
                params['operator_id'] = self.operator_id.to_alipay_dict()
            else:
                params['operator_id'] = self.operator_id
        if self.order_type:
            if hasattr(self.order_type, 'to_alipay_dict'):
                params['order_type'] = self.order_type.to_alipay_dict()
            else:
                params['order_type'] = self.order_type
        if self.out_biz_no:
            if hasattr(self.out_biz_no, 'to_alipay_dict'):
                params['out_biz_no'] = self.out_biz_no.to_alipay_dict()
            else:
                params['out_biz_no'] = self.out_biz_no
        if self.pay_mode:
            if hasattr(self.pay_mode, 'to_alipay_dict'):
                params['pay_mode'] = self.pay_mode.to_alipay_dict()
            else:
                params['pay_mode'] = self.pay_mode
        if self.trade_no:
            if hasattr(self.trade_no, 'to_alipay_dict'):
                params['trade_no'] = self.trade_no.to_alipay_dict()
            else:
                params['trade_no'] = self.trade_no
        if self.user_id:
            if hasattr(self.user_id, 'to_alipay_dict'):
                params['user_id'] = self.user_id.to_alipay_dict()
            else:
                params['user_id'] = self.user_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayEbppChargerGreenenergyPublishModel()
        if 'charge_order_info' in d:
            o.charge_order_info = d['charge_order_info']
        if 'charge_power' in d:
            o.charge_power = d['charge_power']
        if 'operator_id' in d:
            o.operator_id = d['operator_id']
        if 'order_type' in d:
            o.order_type = d['order_type']
        if 'out_biz_no' in d:
            o.out_biz_no = d['out_biz_no']
        if 'pay_mode' in d:
            o.pay_mode = d['pay_mode']
        if 'trade_no' in d:
            o.trade_no = d['trade_no']
        if 'user_id' in d:
            o.user_id = d['user_id']
        return o


