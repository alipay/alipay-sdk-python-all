#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class OrderTimestampInfo(object):

    def __init__(self):
        self._order_cancel_time = None
        self._order_close_time = None
        self._order_create_time = None
        self._order_deliver_time = None
        self._order_finish_time = None
        self._order_last_update_time = None
        self._order_pay_time = None
        self._order_receive_time = None

    @property
    def order_cancel_time(self):
        return self._order_cancel_time

    @order_cancel_time.setter
    def order_cancel_time(self, value):
        self._order_cancel_time = value
    @property
    def order_close_time(self):
        return self._order_close_time

    @order_close_time.setter
    def order_close_time(self, value):
        self._order_close_time = value
    @property
    def order_create_time(self):
        return self._order_create_time

    @order_create_time.setter
    def order_create_time(self, value):
        self._order_create_time = value
    @property
    def order_deliver_time(self):
        return self._order_deliver_time

    @order_deliver_time.setter
    def order_deliver_time(self, value):
        self._order_deliver_time = value
    @property
    def order_finish_time(self):
        return self._order_finish_time

    @order_finish_time.setter
    def order_finish_time(self, value):
        self._order_finish_time = value
    @property
    def order_last_update_time(self):
        return self._order_last_update_time

    @order_last_update_time.setter
    def order_last_update_time(self, value):
        self._order_last_update_time = value
    @property
    def order_pay_time(self):
        return self._order_pay_time

    @order_pay_time.setter
    def order_pay_time(self, value):
        self._order_pay_time = value
    @property
    def order_receive_time(self):
        return self._order_receive_time

    @order_receive_time.setter
    def order_receive_time(self, value):
        self._order_receive_time = value


    def to_alipay_dict(self):
        params = dict()
        if self.order_cancel_time:
            if hasattr(self.order_cancel_time, 'to_alipay_dict'):
                params['order_cancel_time'] = self.order_cancel_time.to_alipay_dict()
            else:
                params['order_cancel_time'] = self.order_cancel_time
        if self.order_close_time:
            if hasattr(self.order_close_time, 'to_alipay_dict'):
                params['order_close_time'] = self.order_close_time.to_alipay_dict()
            else:
                params['order_close_time'] = self.order_close_time
        if self.order_create_time:
            if hasattr(self.order_create_time, 'to_alipay_dict'):
                params['order_create_time'] = self.order_create_time.to_alipay_dict()
            else:
                params['order_create_time'] = self.order_create_time
        if self.order_deliver_time:
            if hasattr(self.order_deliver_time, 'to_alipay_dict'):
                params['order_deliver_time'] = self.order_deliver_time.to_alipay_dict()
            else:
                params['order_deliver_time'] = self.order_deliver_time
        if self.order_finish_time:
            if hasattr(self.order_finish_time, 'to_alipay_dict'):
                params['order_finish_time'] = self.order_finish_time.to_alipay_dict()
            else:
                params['order_finish_time'] = self.order_finish_time
        if self.order_last_update_time:
            if hasattr(self.order_last_update_time, 'to_alipay_dict'):
                params['order_last_update_time'] = self.order_last_update_time.to_alipay_dict()
            else:
                params['order_last_update_time'] = self.order_last_update_time
        if self.order_pay_time:
            if hasattr(self.order_pay_time, 'to_alipay_dict'):
                params['order_pay_time'] = self.order_pay_time.to_alipay_dict()
            else:
                params['order_pay_time'] = self.order_pay_time
        if self.order_receive_time:
            if hasattr(self.order_receive_time, 'to_alipay_dict'):
                params['order_receive_time'] = self.order_receive_time.to_alipay_dict()
            else:
                params['order_receive_time'] = self.order_receive_time
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = OrderTimestampInfo()
        if 'order_cancel_time' in d:
            o.order_cancel_time = d['order_cancel_time']
        if 'order_close_time' in d:
            o.order_close_time = d['order_close_time']
        if 'order_create_time' in d:
            o.order_create_time = d['order_create_time']
        if 'order_deliver_time' in d:
            o.order_deliver_time = d['order_deliver_time']
        if 'order_finish_time' in d:
            o.order_finish_time = d['order_finish_time']
        if 'order_last_update_time' in d:
            o.order_last_update_time = d['order_last_update_time']
        if 'order_pay_time' in d:
            o.order_pay_time = d['order_pay_time']
        if 'order_receive_time' in d:
            o.order_receive_time = d['order_receive_time']
        return o


