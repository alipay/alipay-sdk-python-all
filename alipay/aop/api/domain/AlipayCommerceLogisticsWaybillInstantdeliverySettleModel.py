#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceLogisticsWaybillInstantdeliverySettleModel(object):

    def __init__(self):
        self._cancel_fee = None
        self._logistics_code = None
        self._order_no = None
        self._out_settle_request_no = None
        self._waybill_no = None
        self._waybill_status = None

    @property
    def cancel_fee(self):
        return self._cancel_fee

    @cancel_fee.setter
    def cancel_fee(self, value):
        self._cancel_fee = value
    @property
    def logistics_code(self):
        return self._logistics_code

    @logistics_code.setter
    def logistics_code(self, value):
        self._logistics_code = value
    @property
    def order_no(self):
        return self._order_no

    @order_no.setter
    def order_no(self, value):
        self._order_no = value
    @property
    def out_settle_request_no(self):
        return self._out_settle_request_no

    @out_settle_request_no.setter
    def out_settle_request_no(self, value):
        self._out_settle_request_no = value
    @property
    def waybill_no(self):
        return self._waybill_no

    @waybill_no.setter
    def waybill_no(self, value):
        self._waybill_no = value
    @property
    def waybill_status(self):
        return self._waybill_status

    @waybill_status.setter
    def waybill_status(self, value):
        self._waybill_status = value


    def to_alipay_dict(self):
        params = dict()
        if self.cancel_fee:
            if hasattr(self.cancel_fee, 'to_alipay_dict'):
                params['cancel_fee'] = self.cancel_fee.to_alipay_dict()
            else:
                params['cancel_fee'] = self.cancel_fee
        if self.logistics_code:
            if hasattr(self.logistics_code, 'to_alipay_dict'):
                params['logistics_code'] = self.logistics_code.to_alipay_dict()
            else:
                params['logistics_code'] = self.logistics_code
        if self.order_no:
            if hasattr(self.order_no, 'to_alipay_dict'):
                params['order_no'] = self.order_no.to_alipay_dict()
            else:
                params['order_no'] = self.order_no
        if self.out_settle_request_no:
            if hasattr(self.out_settle_request_no, 'to_alipay_dict'):
                params['out_settle_request_no'] = self.out_settle_request_no.to_alipay_dict()
            else:
                params['out_settle_request_no'] = self.out_settle_request_no
        if self.waybill_no:
            if hasattr(self.waybill_no, 'to_alipay_dict'):
                params['waybill_no'] = self.waybill_no.to_alipay_dict()
            else:
                params['waybill_no'] = self.waybill_no
        if self.waybill_status:
            if hasattr(self.waybill_status, 'to_alipay_dict'):
                params['waybill_status'] = self.waybill_status.to_alipay_dict()
            else:
                params['waybill_status'] = self.waybill_status
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceLogisticsWaybillInstantdeliverySettleModel()
        if 'cancel_fee' in d:
            o.cancel_fee = d['cancel_fee']
        if 'logistics_code' in d:
            o.logistics_code = d['logistics_code']
        if 'order_no' in d:
            o.order_no = d['order_no']
        if 'out_settle_request_no' in d:
            o.out_settle_request_no = d['out_settle_request_no']
        if 'waybill_no' in d:
            o.waybill_no = d['waybill_no']
        if 'waybill_status' in d:
            o.waybill_status = d['waybill_status']
        return o


