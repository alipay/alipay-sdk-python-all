#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class RecycleSubOrderSettleConfirmVO(object):

    def __init__(self):
        self._sub_order_id = None
        self._sub_out_order_id = None

    @property
    def sub_order_id(self):
        return self._sub_order_id

    @sub_order_id.setter
    def sub_order_id(self, value):
        self._sub_order_id = value
    @property
    def sub_out_order_id(self):
        return self._sub_out_order_id

    @sub_out_order_id.setter
    def sub_out_order_id(self, value):
        self._sub_out_order_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.sub_order_id:
            if hasattr(self.sub_order_id, 'to_alipay_dict'):
                params['sub_order_id'] = self.sub_order_id.to_alipay_dict()
            else:
                params['sub_order_id'] = self.sub_order_id
        if self.sub_out_order_id:
            if hasattr(self.sub_out_order_id, 'to_alipay_dict'):
                params['sub_out_order_id'] = self.sub_out_order_id.to_alipay_dict()
            else:
                params['sub_out_order_id'] = self.sub_out_order_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = RecycleSubOrderSettleConfirmVO()
        if 'sub_order_id' in d:
            o.sub_order_id = d['sub_order_id']
        if 'sub_out_order_id' in d:
            o.sub_out_order_id = d['sub_out_order_id']
        return o


