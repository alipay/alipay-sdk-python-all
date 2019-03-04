#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class KoubeiTradeKbdeliveryDeliveryCancelModel(object):

    def __init__(self):
        self._logistics_order_no = None
        self._reason = None

    @property
    def logistics_order_no(self):
        return self._logistics_order_no

    @logistics_order_no.setter
    def logistics_order_no(self, value):
        self._logistics_order_no = value
    @property
    def reason(self):
        return self._reason

    @reason.setter
    def reason(self, value):
        self._reason = value


    def to_alipay_dict(self):
        params = dict()
        if self.logistics_order_no:
            if hasattr(self.logistics_order_no, 'to_alipay_dict'):
                params['logistics_order_no'] = self.logistics_order_no.to_alipay_dict()
            else:
                params['logistics_order_no'] = self.logistics_order_no
        if self.reason:
            if hasattr(self.reason, 'to_alipay_dict'):
                params['reason'] = self.reason.to_alipay_dict()
            else:
                params['reason'] = self.reason
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = KoubeiTradeKbdeliveryDeliveryCancelModel()
        if 'logistics_order_no' in d:
            o.logistics_order_no = d['logistics_order_no']
        if 'reason' in d:
            o.reason = d['reason']
        return o


