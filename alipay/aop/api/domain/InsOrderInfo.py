#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class InsOrderInfo(object):

    def __init__(self):
        self._biz_data = None
        self._order_accept_time = None
        self._order_actual_fee = None
        self._order_expected_time = None
        self._order_finish_time = None
        self._order_no = None
        self._order_status = None
        self._order_time = None

    @property
    def biz_data(self):
        return self._biz_data

    @biz_data.setter
    def biz_data(self, value):
        self._biz_data = value
    @property
    def order_accept_time(self):
        return self._order_accept_time

    @order_accept_time.setter
    def order_accept_time(self, value):
        self._order_accept_time = value
    @property
    def order_actual_fee(self):
        return self._order_actual_fee

    @order_actual_fee.setter
    def order_actual_fee(self, value):
        self._order_actual_fee = value
    @property
    def order_expected_time(self):
        return self._order_expected_time

    @order_expected_time.setter
    def order_expected_time(self, value):
        self._order_expected_time = value
    @property
    def order_finish_time(self):
        return self._order_finish_time

    @order_finish_time.setter
    def order_finish_time(self, value):
        self._order_finish_time = value
    @property
    def order_no(self):
        return self._order_no

    @order_no.setter
    def order_no(self, value):
        self._order_no = value
    @property
    def order_status(self):
        return self._order_status

    @order_status.setter
    def order_status(self, value):
        self._order_status = value
    @property
    def order_time(self):
        return self._order_time

    @order_time.setter
    def order_time(self, value):
        self._order_time = value


    def to_alipay_dict(self):
        params = dict()
        if self.biz_data:
            if hasattr(self.biz_data, 'to_alipay_dict'):
                params['biz_data'] = self.biz_data.to_alipay_dict()
            else:
                params['biz_data'] = self.biz_data
        if self.order_accept_time:
            if hasattr(self.order_accept_time, 'to_alipay_dict'):
                params['order_accept_time'] = self.order_accept_time.to_alipay_dict()
            else:
                params['order_accept_time'] = self.order_accept_time
        if self.order_actual_fee:
            if hasattr(self.order_actual_fee, 'to_alipay_dict'):
                params['order_actual_fee'] = self.order_actual_fee.to_alipay_dict()
            else:
                params['order_actual_fee'] = self.order_actual_fee
        if self.order_expected_time:
            if hasattr(self.order_expected_time, 'to_alipay_dict'):
                params['order_expected_time'] = self.order_expected_time.to_alipay_dict()
            else:
                params['order_expected_time'] = self.order_expected_time
        if self.order_finish_time:
            if hasattr(self.order_finish_time, 'to_alipay_dict'):
                params['order_finish_time'] = self.order_finish_time.to_alipay_dict()
            else:
                params['order_finish_time'] = self.order_finish_time
        if self.order_no:
            if hasattr(self.order_no, 'to_alipay_dict'):
                params['order_no'] = self.order_no.to_alipay_dict()
            else:
                params['order_no'] = self.order_no
        if self.order_status:
            if hasattr(self.order_status, 'to_alipay_dict'):
                params['order_status'] = self.order_status.to_alipay_dict()
            else:
                params['order_status'] = self.order_status
        if self.order_time:
            if hasattr(self.order_time, 'to_alipay_dict'):
                params['order_time'] = self.order_time.to_alipay_dict()
            else:
                params['order_time'] = self.order_time
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = InsOrderInfo()
        if 'biz_data' in d:
            o.biz_data = d['biz_data']
        if 'order_accept_time' in d:
            o.order_accept_time = d['order_accept_time']
        if 'order_actual_fee' in d:
            o.order_actual_fee = d['order_actual_fee']
        if 'order_expected_time' in d:
            o.order_expected_time = d['order_expected_time']
        if 'order_finish_time' in d:
            o.order_finish_time = d['order_finish_time']
        if 'order_no' in d:
            o.order_no = d['order_no']
        if 'order_status' in d:
            o.order_status = d['order_status']
        if 'order_time' in d:
            o.order_time = d['order_time']
        return o


