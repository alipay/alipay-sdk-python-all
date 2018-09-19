#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceCityfacilitatorVoucherGenerateModel(object):

    def __init__(self):
        self._city_code = None
        self._site_begin = None
        self._site_end = None
        self._ticket_num = None
        self._ticket_price = None
        self._ticket_type = None
        self._total_fee = None
        self._trade_no = None

    @property
    def city_code(self):
        return self._city_code

    @city_code.setter
    def city_code(self, value):
        self._city_code = value
    @property
    def site_begin(self):
        return self._site_begin

    @site_begin.setter
    def site_begin(self, value):
        self._site_begin = value
    @property
    def site_end(self):
        return self._site_end

    @site_end.setter
    def site_end(self, value):
        self._site_end = value
    @property
    def ticket_num(self):
        return self._ticket_num

    @ticket_num.setter
    def ticket_num(self, value):
        self._ticket_num = value
    @property
    def ticket_price(self):
        return self._ticket_price

    @ticket_price.setter
    def ticket_price(self, value):
        self._ticket_price = value
    @property
    def ticket_type(self):
        return self._ticket_type

    @ticket_type.setter
    def ticket_type(self, value):
        self._ticket_type = value
    @property
    def total_fee(self):
        return self._total_fee

    @total_fee.setter
    def total_fee(self, value):
        self._total_fee = value
    @property
    def trade_no(self):
        return self._trade_no

    @trade_no.setter
    def trade_no(self, value):
        self._trade_no = value


    def to_alipay_dict(self):
        params = dict()
        if self.city_code:
            if hasattr(self.city_code, 'to_alipay_dict'):
                params['city_code'] = self.city_code.to_alipay_dict()
            else:
                params['city_code'] = self.city_code
        if self.site_begin:
            if hasattr(self.site_begin, 'to_alipay_dict'):
                params['site_begin'] = self.site_begin.to_alipay_dict()
            else:
                params['site_begin'] = self.site_begin
        if self.site_end:
            if hasattr(self.site_end, 'to_alipay_dict'):
                params['site_end'] = self.site_end.to_alipay_dict()
            else:
                params['site_end'] = self.site_end
        if self.ticket_num:
            if hasattr(self.ticket_num, 'to_alipay_dict'):
                params['ticket_num'] = self.ticket_num.to_alipay_dict()
            else:
                params['ticket_num'] = self.ticket_num
        if self.ticket_price:
            if hasattr(self.ticket_price, 'to_alipay_dict'):
                params['ticket_price'] = self.ticket_price.to_alipay_dict()
            else:
                params['ticket_price'] = self.ticket_price
        if self.ticket_type:
            if hasattr(self.ticket_type, 'to_alipay_dict'):
                params['ticket_type'] = self.ticket_type.to_alipay_dict()
            else:
                params['ticket_type'] = self.ticket_type
        if self.total_fee:
            if hasattr(self.total_fee, 'to_alipay_dict'):
                params['total_fee'] = self.total_fee.to_alipay_dict()
            else:
                params['total_fee'] = self.total_fee
        if self.trade_no:
            if hasattr(self.trade_no, 'to_alipay_dict'):
                params['trade_no'] = self.trade_no.to_alipay_dict()
            else:
                params['trade_no'] = self.trade_no
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceCityfacilitatorVoucherGenerateModel()
        if 'city_code' in d:
            o.city_code = d['city_code']
        if 'site_begin' in d:
            o.site_begin = d['site_begin']
        if 'site_end' in d:
            o.site_end = d['site_end']
        if 'ticket_num' in d:
            o.ticket_num = d['ticket_num']
        if 'ticket_price' in d:
            o.ticket_price = d['ticket_price']
        if 'ticket_type' in d:
            o.ticket_type = d['ticket_type']
        if 'total_fee' in d:
            o.total_fee = d['total_fee']
        if 'trade_no' in d:
            o.trade_no = d['trade_no']
        return o


