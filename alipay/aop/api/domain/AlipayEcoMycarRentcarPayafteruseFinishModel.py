#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayEcoMycarRentcarPayafteruseFinishModel(object):

    def __init__(self):
        self._is_fulfilled = None
        self._open_id = None
        self._out_order_no = None
        self._user_id = None

    @property
    def is_fulfilled(self):
        return self._is_fulfilled

    @is_fulfilled.setter
    def is_fulfilled(self, value):
        self._is_fulfilled = value
    @property
    def open_id(self):
        return self._open_id

    @open_id.setter
    def open_id(self, value):
        self._open_id = value
    @property
    def out_order_no(self):
        return self._out_order_no

    @out_order_no.setter
    def out_order_no(self, value):
        self._out_order_no = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.is_fulfilled:
            if hasattr(self.is_fulfilled, 'to_alipay_dict'):
                params['is_fulfilled'] = self.is_fulfilled.to_alipay_dict()
            else:
                params['is_fulfilled'] = self.is_fulfilled
        if self.open_id:
            if hasattr(self.open_id, 'to_alipay_dict'):
                params['open_id'] = self.open_id.to_alipay_dict()
            else:
                params['open_id'] = self.open_id
        if self.out_order_no:
            if hasattr(self.out_order_no, 'to_alipay_dict'):
                params['out_order_no'] = self.out_order_no.to_alipay_dict()
            else:
                params['out_order_no'] = self.out_order_no
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
        o = AlipayEcoMycarRentcarPayafteruseFinishModel()
        if 'is_fulfilled' in d:
            o.is_fulfilled = d['is_fulfilled']
        if 'open_id' in d:
            o.open_id = d['open_id']
        if 'out_order_no' in d:
            o.out_order_no = d['out_order_no']
        if 'user_id' in d:
            o.user_id = d['user_id']
        return o


