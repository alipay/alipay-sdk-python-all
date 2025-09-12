#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class InteOpSubOrderInfo(object):

    def __init__(self):
        self._memo = None
        self._sub_order_no = None
        self._sub_order_status = None
        self._type = None

    @property
    def memo(self):
        return self._memo

    @memo.setter
    def memo(self, value):
        self._memo = value
    @property
    def sub_order_no(self):
        return self._sub_order_no

    @sub_order_no.setter
    def sub_order_no(self, value):
        self._sub_order_no = value
    @property
    def sub_order_status(self):
        return self._sub_order_status

    @sub_order_status.setter
    def sub_order_status(self, value):
        self._sub_order_status = value
    @property
    def type(self):
        return self._type

    @type.setter
    def type(self, value):
        self._type = value


    def to_alipay_dict(self):
        params = dict()
        if self.memo:
            if hasattr(self.memo, 'to_alipay_dict'):
                params['memo'] = self.memo.to_alipay_dict()
            else:
                params['memo'] = self.memo
        if self.sub_order_no:
            if hasattr(self.sub_order_no, 'to_alipay_dict'):
                params['sub_order_no'] = self.sub_order_no.to_alipay_dict()
            else:
                params['sub_order_no'] = self.sub_order_no
        if self.sub_order_status:
            if hasattr(self.sub_order_status, 'to_alipay_dict'):
                params['sub_order_status'] = self.sub_order_status.to_alipay_dict()
            else:
                params['sub_order_status'] = self.sub_order_status
        if self.type:
            if hasattr(self.type, 'to_alipay_dict'):
                params['type'] = self.type.to_alipay_dict()
            else:
                params['type'] = self.type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = InteOpSubOrderInfo()
        if 'memo' in d:
            o.memo = d['memo']
        if 'sub_order_no' in d:
            o.sub_order_no = d['sub_order_no']
        if 'sub_order_status' in d:
            o.sub_order_status = d['sub_order_status']
        if 'type' in d:
            o.type = d['type']
        return o


