#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceMerchantcardTailpaymentQueryModel(object):

    def __init__(self):
        self._main_booking_order_id = None
        self._main_order_id = None
        self._page_num = None
        self._page_size = None
        self._tail_payment_id = None

    @property
    def main_booking_order_id(self):
        return self._main_booking_order_id

    @main_booking_order_id.setter
    def main_booking_order_id(self, value):
        self._main_booking_order_id = value
    @property
    def main_order_id(self):
        return self._main_order_id

    @main_order_id.setter
    def main_order_id(self, value):
        self._main_order_id = value
    @property
    def page_num(self):
        return self._page_num

    @page_num.setter
    def page_num(self, value):
        self._page_num = value
    @property
    def page_size(self):
        return self._page_size

    @page_size.setter
    def page_size(self, value):
        self._page_size = value
    @property
    def tail_payment_id(self):
        return self._tail_payment_id

    @tail_payment_id.setter
    def tail_payment_id(self, value):
        self._tail_payment_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.main_booking_order_id:
            if hasattr(self.main_booking_order_id, 'to_alipay_dict'):
                params['main_booking_order_id'] = self.main_booking_order_id.to_alipay_dict()
            else:
                params['main_booking_order_id'] = self.main_booking_order_id
        if self.main_order_id:
            if hasattr(self.main_order_id, 'to_alipay_dict'):
                params['main_order_id'] = self.main_order_id.to_alipay_dict()
            else:
                params['main_order_id'] = self.main_order_id
        if self.page_num:
            if hasattr(self.page_num, 'to_alipay_dict'):
                params['page_num'] = self.page_num.to_alipay_dict()
            else:
                params['page_num'] = self.page_num
        if self.page_size:
            if hasattr(self.page_size, 'to_alipay_dict'):
                params['page_size'] = self.page_size.to_alipay_dict()
            else:
                params['page_size'] = self.page_size
        if self.tail_payment_id:
            if hasattr(self.tail_payment_id, 'to_alipay_dict'):
                params['tail_payment_id'] = self.tail_payment_id.to_alipay_dict()
            else:
                params['tail_payment_id'] = self.tail_payment_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceMerchantcardTailpaymentQueryModel()
        if 'main_booking_order_id' in d:
            o.main_booking_order_id = d['main_booking_order_id']
        if 'main_order_id' in d:
            o.main_order_id = d['main_order_id']
        if 'page_num' in d:
            o.page_num = d['page_num']
        if 'page_size' in d:
            o.page_size = d['page_size']
        if 'tail_payment_id' in d:
            o.tail_payment_id = d['tail_payment_id']
        return o


