#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayOpenServicemarketOrderRejectModel(object):

    def __init__(self):
        self._commodity_order_id = None
        self._reject_reason = None

    @property
    def commodity_order_id(self):
        return self._commodity_order_id

    @commodity_order_id.setter
    def commodity_order_id(self, value):
        self._commodity_order_id = value
    @property
    def reject_reason(self):
        return self._reject_reason

    @reject_reason.setter
    def reject_reason(self, value):
        self._reject_reason = value


    def to_alipay_dict(self):
        params = dict()
        if self.commodity_order_id:
            if hasattr(self.commodity_order_id, 'to_alipay_dict'):
                params['commodity_order_id'] = self.commodity_order_id.to_alipay_dict()
            else:
                params['commodity_order_id'] = self.commodity_order_id
        if self.reject_reason:
            if hasattr(self.reject_reason, 'to_alipay_dict'):
                params['reject_reason'] = self.reject_reason.to_alipay_dict()
            else:
                params['reject_reason'] = self.reject_reason
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayOpenServicemarketOrderRejectModel()
        if 'commodity_order_id' in d:
            o.commodity_order_id = d['commodity_order_id']
        if 'reject_reason' in d:
            o.reject_reason = d['reject_reason']
        return o


