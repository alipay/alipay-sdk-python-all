#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class OcrTaxiScanInfo(object):

    def __init__(self):
        self._get_off_time = None
        self._get_on_time = None
        self._invoice_code = None
        self._invoice_date = None
        self._invoice_no = None
        self._passenger = None
        self._price = None
        self._travel_dist = None

    @property
    def get_off_time(self):
        return self._get_off_time

    @get_off_time.setter
    def get_off_time(self, value):
        self._get_off_time = value
    @property
    def get_on_time(self):
        return self._get_on_time

    @get_on_time.setter
    def get_on_time(self, value):
        self._get_on_time = value
    @property
    def invoice_code(self):
        return self._invoice_code

    @invoice_code.setter
    def invoice_code(self, value):
        self._invoice_code = value
    @property
    def invoice_date(self):
        return self._invoice_date

    @invoice_date.setter
    def invoice_date(self, value):
        self._invoice_date = value
    @property
    def invoice_no(self):
        return self._invoice_no

    @invoice_no.setter
    def invoice_no(self, value):
        self._invoice_no = value
    @property
    def passenger(self):
        return self._passenger

    @passenger.setter
    def passenger(self, value):
        self._passenger = value
    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        self._price = value
    @property
    def travel_dist(self):
        return self._travel_dist

    @travel_dist.setter
    def travel_dist(self, value):
        self._travel_dist = value


    def to_alipay_dict(self):
        params = dict()
        if self.get_off_time:
            if hasattr(self.get_off_time, 'to_alipay_dict'):
                params['get_off_time'] = self.get_off_time.to_alipay_dict()
            else:
                params['get_off_time'] = self.get_off_time
        if self.get_on_time:
            if hasattr(self.get_on_time, 'to_alipay_dict'):
                params['get_on_time'] = self.get_on_time.to_alipay_dict()
            else:
                params['get_on_time'] = self.get_on_time
        if self.invoice_code:
            if hasattr(self.invoice_code, 'to_alipay_dict'):
                params['invoice_code'] = self.invoice_code.to_alipay_dict()
            else:
                params['invoice_code'] = self.invoice_code
        if self.invoice_date:
            if hasattr(self.invoice_date, 'to_alipay_dict'):
                params['invoice_date'] = self.invoice_date.to_alipay_dict()
            else:
                params['invoice_date'] = self.invoice_date
        if self.invoice_no:
            if hasattr(self.invoice_no, 'to_alipay_dict'):
                params['invoice_no'] = self.invoice_no.to_alipay_dict()
            else:
                params['invoice_no'] = self.invoice_no
        if self.passenger:
            if hasattr(self.passenger, 'to_alipay_dict'):
                params['passenger'] = self.passenger.to_alipay_dict()
            else:
                params['passenger'] = self.passenger
        if self.price:
            if hasattr(self.price, 'to_alipay_dict'):
                params['price'] = self.price.to_alipay_dict()
            else:
                params['price'] = self.price
        if self.travel_dist:
            if hasattr(self.travel_dist, 'to_alipay_dict'):
                params['travel_dist'] = self.travel_dist.to_alipay_dict()
            else:
                params['travel_dist'] = self.travel_dist
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = OcrTaxiScanInfo()
        if 'get_off_time' in d:
            o.get_off_time = d['get_off_time']
        if 'get_on_time' in d:
            o.get_on_time = d['get_on_time']
        if 'invoice_code' in d:
            o.invoice_code = d['invoice_code']
        if 'invoice_date' in d:
            o.invoice_date = d['invoice_date']
        if 'invoice_no' in d:
            o.invoice_no = d['invoice_no']
        if 'passenger' in d:
            o.passenger = d['passenger']
        if 'price' in d:
            o.price = d['price']
        if 'travel_dist' in d:
            o.travel_dist = d['travel_dist']
        return o


