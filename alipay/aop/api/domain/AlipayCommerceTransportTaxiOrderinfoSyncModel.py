#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceTransportTaxiOrderinfoSyncModel(object):

    def __init__(self):
        self._channel_type = None
        self._dispatcher_amount = None
        self._order_id = None
        self._request_time = None
        self._status = None
        self._sys_driver_id = None

    @property
    def channel_type(self):
        return self._channel_type

    @channel_type.setter
    def channel_type(self, value):
        self._channel_type = value
    @property
    def dispatcher_amount(self):
        return self._dispatcher_amount

    @dispatcher_amount.setter
    def dispatcher_amount(self, value):
        self._dispatcher_amount = value
    @property
    def order_id(self):
        return self._order_id

    @order_id.setter
    def order_id(self, value):
        self._order_id = value
    @property
    def request_time(self):
        return self._request_time

    @request_time.setter
    def request_time(self, value):
        self._request_time = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value
    @property
    def sys_driver_id(self):
        return self._sys_driver_id

    @sys_driver_id.setter
    def sys_driver_id(self, value):
        self._sys_driver_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.channel_type:
            if hasattr(self.channel_type, 'to_alipay_dict'):
                params['channel_type'] = self.channel_type.to_alipay_dict()
            else:
                params['channel_type'] = self.channel_type
        if self.dispatcher_amount:
            if hasattr(self.dispatcher_amount, 'to_alipay_dict'):
                params['dispatcher_amount'] = self.dispatcher_amount.to_alipay_dict()
            else:
                params['dispatcher_amount'] = self.dispatcher_amount
        if self.order_id:
            if hasattr(self.order_id, 'to_alipay_dict'):
                params['order_id'] = self.order_id.to_alipay_dict()
            else:
                params['order_id'] = self.order_id
        if self.request_time:
            if hasattr(self.request_time, 'to_alipay_dict'):
                params['request_time'] = self.request_time.to_alipay_dict()
            else:
                params['request_time'] = self.request_time
        if self.status:
            if hasattr(self.status, 'to_alipay_dict'):
                params['status'] = self.status.to_alipay_dict()
            else:
                params['status'] = self.status
        if self.sys_driver_id:
            if hasattr(self.sys_driver_id, 'to_alipay_dict'):
                params['sys_driver_id'] = self.sys_driver_id.to_alipay_dict()
            else:
                params['sys_driver_id'] = self.sys_driver_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceTransportTaxiOrderinfoSyncModel()
        if 'channel_type' in d:
            o.channel_type = d['channel_type']
        if 'dispatcher_amount' in d:
            o.dispatcher_amount = d['dispatcher_amount']
        if 'order_id' in d:
            o.order_id = d['order_id']
        if 'request_time' in d:
            o.request_time = d['request_time']
        if 'status' in d:
            o.status = d['status']
        if 'sys_driver_id' in d:
            o.sys_driver_id = d['sys_driver_id']
        return o


