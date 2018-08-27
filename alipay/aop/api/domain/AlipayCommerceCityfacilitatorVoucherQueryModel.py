#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceCityfacilitatorVoucherQueryModel(object):

    def __init__(self):
        self._city_code = None
        self._ticket_no = None
        self._trade_no = None

    @property
    def city_code(self):
        return self._city_code

    @city_code.setter
    def city_code(self, value):
        self._city_code = value
    @property
    def ticket_no(self):
        return self._ticket_no

    @ticket_no.setter
    def ticket_no(self, value):
        self._ticket_no = value
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
        if self.ticket_no:
            if hasattr(self.ticket_no, 'to_alipay_dict'):
                params['ticket_no'] = self.ticket_no.to_alipay_dict()
            else:
                params['ticket_no'] = self.ticket_no
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
        o = AlipayCommerceCityfacilitatorVoucherQueryModel()
        if 'city_code' in d:
            o.city_code = d['city_code']
        if 'ticket_no' in d:
            o.ticket_no = d['ticket_no']
        if 'trade_no' in d:
            o.trade_no = d['trade_no']
        return o


