#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceTransportTaxiHighvalueorderSyncModel(object):

    def __init__(self):
        self._channel_type = None
        self._dispatch_amount = None
        self._driver_id = None
        self._estimate_amount = None
        self._estimate_duration = None
        self._estimate_mileage = None
        self._estimate_pick_up_time = None
        self._order_id = None
        self._order_type = None
        self._request_time = None
        self._start_time = None
        self._status = None

    @property
    def channel_type(self):
        return self._channel_type

    @channel_type.setter
    def channel_type(self, value):
        self._channel_type = value
    @property
    def dispatch_amount(self):
        return self._dispatch_amount

    @dispatch_amount.setter
    def dispatch_amount(self, value):
        self._dispatch_amount = value
    @property
    def driver_id(self):
        return self._driver_id

    @driver_id.setter
    def driver_id(self, value):
        self._driver_id = value
    @property
    def estimate_amount(self):
        return self._estimate_amount

    @estimate_amount.setter
    def estimate_amount(self, value):
        self._estimate_amount = value
    @property
    def estimate_duration(self):
        return self._estimate_duration

    @estimate_duration.setter
    def estimate_duration(self, value):
        self._estimate_duration = value
    @property
    def estimate_mileage(self):
        return self._estimate_mileage

    @estimate_mileage.setter
    def estimate_mileage(self, value):
        self._estimate_mileage = value
    @property
    def estimate_pick_up_time(self):
        return self._estimate_pick_up_time

    @estimate_pick_up_time.setter
    def estimate_pick_up_time(self, value):
        self._estimate_pick_up_time = value
    @property
    def order_id(self):
        return self._order_id

    @order_id.setter
    def order_id(self, value):
        self._order_id = value
    @property
    def order_type(self):
        return self._order_type

    @order_type.setter
    def order_type(self, value):
        self._order_type = value
    @property
    def request_time(self):
        return self._request_time

    @request_time.setter
    def request_time(self, value):
        self._request_time = value
    @property
    def start_time(self):
        return self._start_time

    @start_time.setter
    def start_time(self, value):
        self._start_time = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value


    def to_alipay_dict(self):
        params = dict()
        if self.channel_type:
            if hasattr(self.channel_type, 'to_alipay_dict'):
                params['channel_type'] = self.channel_type.to_alipay_dict()
            else:
                params['channel_type'] = self.channel_type
        if self.dispatch_amount:
            if hasattr(self.dispatch_amount, 'to_alipay_dict'):
                params['dispatch_amount'] = self.dispatch_amount.to_alipay_dict()
            else:
                params['dispatch_amount'] = self.dispatch_amount
        if self.driver_id:
            if hasattr(self.driver_id, 'to_alipay_dict'):
                params['driver_id'] = self.driver_id.to_alipay_dict()
            else:
                params['driver_id'] = self.driver_id
        if self.estimate_amount:
            if hasattr(self.estimate_amount, 'to_alipay_dict'):
                params['estimate_amount'] = self.estimate_amount.to_alipay_dict()
            else:
                params['estimate_amount'] = self.estimate_amount
        if self.estimate_duration:
            if hasattr(self.estimate_duration, 'to_alipay_dict'):
                params['estimate_duration'] = self.estimate_duration.to_alipay_dict()
            else:
                params['estimate_duration'] = self.estimate_duration
        if self.estimate_mileage:
            if hasattr(self.estimate_mileage, 'to_alipay_dict'):
                params['estimate_mileage'] = self.estimate_mileage.to_alipay_dict()
            else:
                params['estimate_mileage'] = self.estimate_mileage
        if self.estimate_pick_up_time:
            if hasattr(self.estimate_pick_up_time, 'to_alipay_dict'):
                params['estimate_pick_up_time'] = self.estimate_pick_up_time.to_alipay_dict()
            else:
                params['estimate_pick_up_time'] = self.estimate_pick_up_time
        if self.order_id:
            if hasattr(self.order_id, 'to_alipay_dict'):
                params['order_id'] = self.order_id.to_alipay_dict()
            else:
                params['order_id'] = self.order_id
        if self.order_type:
            if hasattr(self.order_type, 'to_alipay_dict'):
                params['order_type'] = self.order_type.to_alipay_dict()
            else:
                params['order_type'] = self.order_type
        if self.request_time:
            if hasattr(self.request_time, 'to_alipay_dict'):
                params['request_time'] = self.request_time.to_alipay_dict()
            else:
                params['request_time'] = self.request_time
        if self.start_time:
            if hasattr(self.start_time, 'to_alipay_dict'):
                params['start_time'] = self.start_time.to_alipay_dict()
            else:
                params['start_time'] = self.start_time
        if self.status:
            if hasattr(self.status, 'to_alipay_dict'):
                params['status'] = self.status.to_alipay_dict()
            else:
                params['status'] = self.status
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceTransportTaxiHighvalueorderSyncModel()
        if 'channel_type' in d:
            o.channel_type = d['channel_type']
        if 'dispatch_amount' in d:
            o.dispatch_amount = d['dispatch_amount']
        if 'driver_id' in d:
            o.driver_id = d['driver_id']
        if 'estimate_amount' in d:
            o.estimate_amount = d['estimate_amount']
        if 'estimate_duration' in d:
            o.estimate_duration = d['estimate_duration']
        if 'estimate_mileage' in d:
            o.estimate_mileage = d['estimate_mileage']
        if 'estimate_pick_up_time' in d:
            o.estimate_pick_up_time = d['estimate_pick_up_time']
        if 'order_id' in d:
            o.order_id = d['order_id']
        if 'order_type' in d:
            o.order_type = d['order_type']
        if 'request_time' in d:
            o.request_time = d['request_time']
        if 'start_time' in d:
            o.start_time = d['start_time']
        if 'status' in d:
            o.status = d['status']
        return o


