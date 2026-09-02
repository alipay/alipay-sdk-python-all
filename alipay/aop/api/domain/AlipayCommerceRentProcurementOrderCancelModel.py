#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceRentProcurementOrderCancelModel(object):

    def __init__(self):
        self._cancel_code = None
        self._cancel_reason = None
        self._out_procurement_order_id = None
        self._procurement_order_id = None

    @property
    def cancel_code(self):
        return self._cancel_code

    @cancel_code.setter
    def cancel_code(self, value):
        self._cancel_code = value
    @property
    def cancel_reason(self):
        return self._cancel_reason

    @cancel_reason.setter
    def cancel_reason(self, value):
        self._cancel_reason = value
    @property
    def out_procurement_order_id(self):
        return self._out_procurement_order_id

    @out_procurement_order_id.setter
    def out_procurement_order_id(self, value):
        self._out_procurement_order_id = value
    @property
    def procurement_order_id(self):
        return self._procurement_order_id

    @procurement_order_id.setter
    def procurement_order_id(self, value):
        self._procurement_order_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.cancel_code:
            if hasattr(self.cancel_code, 'to_alipay_dict'):
                params['cancel_code'] = self.cancel_code.to_alipay_dict()
            else:
                params['cancel_code'] = self.cancel_code
        if self.cancel_reason:
            if hasattr(self.cancel_reason, 'to_alipay_dict'):
                params['cancel_reason'] = self.cancel_reason.to_alipay_dict()
            else:
                params['cancel_reason'] = self.cancel_reason
        if self.out_procurement_order_id:
            if hasattr(self.out_procurement_order_id, 'to_alipay_dict'):
                params['out_procurement_order_id'] = self.out_procurement_order_id.to_alipay_dict()
            else:
                params['out_procurement_order_id'] = self.out_procurement_order_id
        if self.procurement_order_id:
            if hasattr(self.procurement_order_id, 'to_alipay_dict'):
                params['procurement_order_id'] = self.procurement_order_id.to_alipay_dict()
            else:
                params['procurement_order_id'] = self.procurement_order_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceRentProcurementOrderCancelModel()
        if 'cancel_code' in d:
            o.cancel_code = d['cancel_code']
        if 'cancel_reason' in d:
            o.cancel_reason = d['cancel_reason']
        if 'out_procurement_order_id' in d:
            o.out_procurement_order_id = d['out_procurement_order_id']
        if 'procurement_order_id' in d:
            o.procurement_order_id = d['procurement_order_id']
        return o


