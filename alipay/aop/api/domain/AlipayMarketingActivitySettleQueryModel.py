#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayMarketingActivitySettleQueryModel(object):

    def __init__(self):
        self._activity_id = None
        self._order_no = None
        self._settle_no = None

    @property
    def activity_id(self):
        return self._activity_id

    @activity_id.setter
    def activity_id(self, value):
        self._activity_id = value
    @property
    def order_no(self):
        return self._order_no

    @order_no.setter
    def order_no(self, value):
        self._order_no = value
    @property
    def settle_no(self):
        return self._settle_no

    @settle_no.setter
    def settle_no(self, value):
        self._settle_no = value


    def to_alipay_dict(self):
        params = dict()
        if self.activity_id:
            if hasattr(self.activity_id, 'to_alipay_dict'):
                params['activity_id'] = self.activity_id.to_alipay_dict()
            else:
                params['activity_id'] = self.activity_id
        if self.order_no:
            if hasattr(self.order_no, 'to_alipay_dict'):
                params['order_no'] = self.order_no.to_alipay_dict()
            else:
                params['order_no'] = self.order_no
        if self.settle_no:
            if hasattr(self.settle_no, 'to_alipay_dict'):
                params['settle_no'] = self.settle_no.to_alipay_dict()
            else:
                params['settle_no'] = self.settle_no
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayMarketingActivitySettleQueryModel()
        if 'activity_id' in d:
            o.activity_id = d['activity_id']
        if 'order_no' in d:
            o.order_no = d['order_no']
        if 'settle_no' in d:
            o.settle_no = d['settle_no']
        return o


