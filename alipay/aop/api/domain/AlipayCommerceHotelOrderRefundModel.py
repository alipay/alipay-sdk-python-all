#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.EtravelHotelSupplyPriceDTO import EtravelHotelSupplyPriceDTO


class AlipayCommerceHotelOrderRefundModel(object):

    def __init__(self):
        self._alipay_hotel_order_id = None
        self._open_id = None
        self._outer_order_id = None
        self._reason = None
        self._refund_amount = None
        self._refund_bill_no = None

    @property
    def alipay_hotel_order_id(self):
        return self._alipay_hotel_order_id

    @alipay_hotel_order_id.setter
    def alipay_hotel_order_id(self, value):
        self._alipay_hotel_order_id = value
    @property
    def open_id(self):
        return self._open_id

    @open_id.setter
    def open_id(self, value):
        self._open_id = value
    @property
    def outer_order_id(self):
        return self._outer_order_id

    @outer_order_id.setter
    def outer_order_id(self, value):
        self._outer_order_id = value
    @property
    def reason(self):
        return self._reason

    @reason.setter
    def reason(self, value):
        self._reason = value
    @property
    def refund_amount(self):
        return self._refund_amount

    @refund_amount.setter
    def refund_amount(self, value):
        if isinstance(value, EtravelHotelSupplyPriceDTO):
            self._refund_amount = value
        else:
            self._refund_amount = EtravelHotelSupplyPriceDTO.from_alipay_dict(value)
    @property
    def refund_bill_no(self):
        return self._refund_bill_no

    @refund_bill_no.setter
    def refund_bill_no(self, value):
        self._refund_bill_no = value


    def to_alipay_dict(self):
        params = dict()
        if self.alipay_hotel_order_id:
            if hasattr(self.alipay_hotel_order_id, 'to_alipay_dict'):
                params['alipay_hotel_order_id'] = self.alipay_hotel_order_id.to_alipay_dict()
            else:
                params['alipay_hotel_order_id'] = self.alipay_hotel_order_id
        if self.open_id:
            if hasattr(self.open_id, 'to_alipay_dict'):
                params['open_id'] = self.open_id.to_alipay_dict()
            else:
                params['open_id'] = self.open_id
        if self.outer_order_id:
            if hasattr(self.outer_order_id, 'to_alipay_dict'):
                params['outer_order_id'] = self.outer_order_id.to_alipay_dict()
            else:
                params['outer_order_id'] = self.outer_order_id
        if self.reason:
            if hasattr(self.reason, 'to_alipay_dict'):
                params['reason'] = self.reason.to_alipay_dict()
            else:
                params['reason'] = self.reason
        if self.refund_amount:
            if hasattr(self.refund_amount, 'to_alipay_dict'):
                params['refund_amount'] = self.refund_amount.to_alipay_dict()
            else:
                params['refund_amount'] = self.refund_amount
        if self.refund_bill_no:
            if hasattr(self.refund_bill_no, 'to_alipay_dict'):
                params['refund_bill_no'] = self.refund_bill_no.to_alipay_dict()
            else:
                params['refund_bill_no'] = self.refund_bill_no
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceHotelOrderRefundModel()
        if 'alipay_hotel_order_id' in d:
            o.alipay_hotel_order_id = d['alipay_hotel_order_id']
        if 'open_id' in d:
            o.open_id = d['open_id']
        if 'outer_order_id' in d:
            o.outer_order_id = d['outer_order_id']
        if 'reason' in d:
            o.reason = d['reason']
        if 'refund_amount' in d:
            o.refund_amount = d['refund_amount']
        if 'refund_bill_no' in d:
            o.refund_bill_no = d['refund_bill_no']
        return o


