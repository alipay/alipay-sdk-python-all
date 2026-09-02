#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class XingheLendassistCarfinauctionCloseNotifyModel(object):

    def __init__(self):
        self._apply_no = None
        self._close_reason = None
        self._close_time = None
        self._close_type = None
        self._out_order_no = None

    @property
    def apply_no(self):
        return self._apply_no

    @apply_no.setter
    def apply_no(self, value):
        self._apply_no = value
    @property
    def close_reason(self):
        return self._close_reason

    @close_reason.setter
    def close_reason(self, value):
        self._close_reason = value
    @property
    def close_time(self):
        return self._close_time

    @close_time.setter
    def close_time(self, value):
        self._close_time = value
    @property
    def close_type(self):
        return self._close_type

    @close_type.setter
    def close_type(self, value):
        self._close_type = value
    @property
    def out_order_no(self):
        return self._out_order_no

    @out_order_no.setter
    def out_order_no(self, value):
        self._out_order_no = value


    def to_alipay_dict(self):
        params = dict()
        if self.apply_no:
            if hasattr(self.apply_no, 'to_alipay_dict'):
                params['apply_no'] = self.apply_no.to_alipay_dict()
            else:
                params['apply_no'] = self.apply_no
        if self.close_reason:
            if hasattr(self.close_reason, 'to_alipay_dict'):
                params['close_reason'] = self.close_reason.to_alipay_dict()
            else:
                params['close_reason'] = self.close_reason
        if self.close_time:
            if hasattr(self.close_time, 'to_alipay_dict'):
                params['close_time'] = self.close_time.to_alipay_dict()
            else:
                params['close_time'] = self.close_time
        if self.close_type:
            if hasattr(self.close_type, 'to_alipay_dict'):
                params['close_type'] = self.close_type.to_alipay_dict()
            else:
                params['close_type'] = self.close_type
        if self.out_order_no:
            if hasattr(self.out_order_no, 'to_alipay_dict'):
                params['out_order_no'] = self.out_order_no.to_alipay_dict()
            else:
                params['out_order_no'] = self.out_order_no
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = XingheLendassistCarfinauctionCloseNotifyModel()
        if 'apply_no' in d:
            o.apply_no = d['apply_no']
        if 'close_reason' in d:
            o.close_reason = d['close_reason']
        if 'close_time' in d:
            o.close_time = d['close_time']
        if 'close_type' in d:
            o.close_type = d['close_type']
        if 'out_order_no' in d:
            o.out_order_no = d['out_order_no']
        return o


