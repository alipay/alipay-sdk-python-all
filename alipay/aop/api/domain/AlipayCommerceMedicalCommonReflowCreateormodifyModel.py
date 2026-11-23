#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceMedicalCommonReflowCreateormodifyModel(object):

    def __init__(self):
        self._bar_code = None
        self._channel = None
        self._consign_time = None
        self._mac_id = None
        self._order_create_time = None
        self._order_id = None
        self._order_status = None
        self._order_type = None
        self._param_info = None
        self._pay_time = None
        self._refund_time = None

    @property
    def bar_code(self):
        return self._bar_code

    @bar_code.setter
    def bar_code(self, value):
        self._bar_code = value
    @property
    def channel(self):
        return self._channel

    @channel.setter
    def channel(self, value):
        self._channel = value
    @property
    def consign_time(self):
        return self._consign_time

    @consign_time.setter
    def consign_time(self, value):
        self._consign_time = value
    @property
    def mac_id(self):
        return self._mac_id

    @mac_id.setter
    def mac_id(self, value):
        self._mac_id = value
    @property
    def order_create_time(self):
        return self._order_create_time

    @order_create_time.setter
    def order_create_time(self, value):
        self._order_create_time = value
    @property
    def order_id(self):
        return self._order_id

    @order_id.setter
    def order_id(self, value):
        self._order_id = value
    @property
    def order_status(self):
        return self._order_status

    @order_status.setter
    def order_status(self, value):
        self._order_status = value
    @property
    def order_type(self):
        return self._order_type

    @order_type.setter
    def order_type(self, value):
        self._order_type = value
    @property
    def param_info(self):
        return self._param_info

    @param_info.setter
    def param_info(self, value):
        self._param_info = value
    @property
    def pay_time(self):
        return self._pay_time

    @pay_time.setter
    def pay_time(self, value):
        self._pay_time = value
    @property
    def refund_time(self):
        return self._refund_time

    @refund_time.setter
    def refund_time(self, value):
        self._refund_time = value


    def to_alipay_dict(self):
        params = dict()
        if self.bar_code:
            if hasattr(self.bar_code, 'to_alipay_dict'):
                params['bar_code'] = self.bar_code.to_alipay_dict()
            else:
                params['bar_code'] = self.bar_code
        if self.channel:
            if hasattr(self.channel, 'to_alipay_dict'):
                params['channel'] = self.channel.to_alipay_dict()
            else:
                params['channel'] = self.channel
        if self.consign_time:
            if hasattr(self.consign_time, 'to_alipay_dict'):
                params['consign_time'] = self.consign_time.to_alipay_dict()
            else:
                params['consign_time'] = self.consign_time
        if self.mac_id:
            if hasattr(self.mac_id, 'to_alipay_dict'):
                params['mac_id'] = self.mac_id.to_alipay_dict()
            else:
                params['mac_id'] = self.mac_id
        if self.order_create_time:
            if hasattr(self.order_create_time, 'to_alipay_dict'):
                params['order_create_time'] = self.order_create_time.to_alipay_dict()
            else:
                params['order_create_time'] = self.order_create_time
        if self.order_id:
            if hasattr(self.order_id, 'to_alipay_dict'):
                params['order_id'] = self.order_id.to_alipay_dict()
            else:
                params['order_id'] = self.order_id
        if self.order_status:
            if hasattr(self.order_status, 'to_alipay_dict'):
                params['order_status'] = self.order_status.to_alipay_dict()
            else:
                params['order_status'] = self.order_status
        if self.order_type:
            if hasattr(self.order_type, 'to_alipay_dict'):
                params['order_type'] = self.order_type.to_alipay_dict()
            else:
                params['order_type'] = self.order_type
        if self.param_info:
            if hasattr(self.param_info, 'to_alipay_dict'):
                params['param_info'] = self.param_info.to_alipay_dict()
            else:
                params['param_info'] = self.param_info
        if self.pay_time:
            if hasattr(self.pay_time, 'to_alipay_dict'):
                params['pay_time'] = self.pay_time.to_alipay_dict()
            else:
                params['pay_time'] = self.pay_time
        if self.refund_time:
            if hasattr(self.refund_time, 'to_alipay_dict'):
                params['refund_time'] = self.refund_time.to_alipay_dict()
            else:
                params['refund_time'] = self.refund_time
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceMedicalCommonReflowCreateormodifyModel()
        if 'bar_code' in d:
            o.bar_code = d['bar_code']
        if 'channel' in d:
            o.channel = d['channel']
        if 'consign_time' in d:
            o.consign_time = d['consign_time']
        if 'mac_id' in d:
            o.mac_id = d['mac_id']
        if 'order_create_time' in d:
            o.order_create_time = d['order_create_time']
        if 'order_id' in d:
            o.order_id = d['order_id']
        if 'order_status' in d:
            o.order_status = d['order_status']
        if 'order_type' in d:
            o.order_type = d['order_type']
        if 'param_info' in d:
            o.param_info = d['param_info']
        if 'pay_time' in d:
            o.pay_time = d['pay_time']
        if 'refund_time' in d:
            o.refund_time = d['refund_time']
        return o


