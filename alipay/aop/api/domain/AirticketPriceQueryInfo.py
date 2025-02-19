#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AirticketPriceQueryInfo(object):

    def __init__(self):
        self._arr_city_code = None
        self._dep_city_code = None
        self._dep_date = None
        self._flight_no = None
        self._has_lowest = None
        self._has_transfer = None
        self._lowest_price = None
        self._transit_city_code = None

    @property
    def arr_city_code(self):
        return self._arr_city_code

    @arr_city_code.setter
    def arr_city_code(self, value):
        self._arr_city_code = value
    @property
    def dep_city_code(self):
        return self._dep_city_code

    @dep_city_code.setter
    def dep_city_code(self, value):
        self._dep_city_code = value
    @property
    def dep_date(self):
        return self._dep_date

    @dep_date.setter
    def dep_date(self, value):
        self._dep_date = value
    @property
    def flight_no(self):
        return self._flight_no

    @flight_no.setter
    def flight_no(self, value):
        if isinstance(value, list):
            self._flight_no = list()
            for i in value:
                self._flight_no.append(i)
    @property
    def has_lowest(self):
        return self._has_lowest

    @has_lowest.setter
    def has_lowest(self, value):
        self._has_lowest = value
    @property
    def has_transfer(self):
        return self._has_transfer

    @has_transfer.setter
    def has_transfer(self, value):
        self._has_transfer = value
    @property
    def lowest_price(self):
        return self._lowest_price

    @lowest_price.setter
    def lowest_price(self, value):
        self._lowest_price = value
    @property
    def transit_city_code(self):
        return self._transit_city_code

    @transit_city_code.setter
    def transit_city_code(self, value):
        self._transit_city_code = value


    def to_alipay_dict(self):
        params = dict()
        if self.arr_city_code:
            if hasattr(self.arr_city_code, 'to_alipay_dict'):
                params['arr_city_code'] = self.arr_city_code.to_alipay_dict()
            else:
                params['arr_city_code'] = self.arr_city_code
        if self.dep_city_code:
            if hasattr(self.dep_city_code, 'to_alipay_dict'):
                params['dep_city_code'] = self.dep_city_code.to_alipay_dict()
            else:
                params['dep_city_code'] = self.dep_city_code
        if self.dep_date:
            if hasattr(self.dep_date, 'to_alipay_dict'):
                params['dep_date'] = self.dep_date.to_alipay_dict()
            else:
                params['dep_date'] = self.dep_date
        if self.flight_no:
            if isinstance(self.flight_no, list):
                for i in range(0, len(self.flight_no)):
                    element = self.flight_no[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.flight_no[i] = element.to_alipay_dict()
            if hasattr(self.flight_no, 'to_alipay_dict'):
                params['flight_no'] = self.flight_no.to_alipay_dict()
            else:
                params['flight_no'] = self.flight_no
        if self.has_lowest:
            if hasattr(self.has_lowest, 'to_alipay_dict'):
                params['has_lowest'] = self.has_lowest.to_alipay_dict()
            else:
                params['has_lowest'] = self.has_lowest
        if self.has_transfer:
            if hasattr(self.has_transfer, 'to_alipay_dict'):
                params['has_transfer'] = self.has_transfer.to_alipay_dict()
            else:
                params['has_transfer'] = self.has_transfer
        if self.lowest_price:
            if hasattr(self.lowest_price, 'to_alipay_dict'):
                params['lowest_price'] = self.lowest_price.to_alipay_dict()
            else:
                params['lowest_price'] = self.lowest_price
        if self.transit_city_code:
            if hasattr(self.transit_city_code, 'to_alipay_dict'):
                params['transit_city_code'] = self.transit_city_code.to_alipay_dict()
            else:
                params['transit_city_code'] = self.transit_city_code
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AirticketPriceQueryInfo()
        if 'arr_city_code' in d:
            o.arr_city_code = d['arr_city_code']
        if 'dep_city_code' in d:
            o.dep_city_code = d['dep_city_code']
        if 'dep_date' in d:
            o.dep_date = d['dep_date']
        if 'flight_no' in d:
            o.flight_no = d['flight_no']
        if 'has_lowest' in d:
            o.has_lowest = d['has_lowest']
        if 'has_transfer' in d:
            o.has_transfer = d['has_transfer']
        if 'lowest_price' in d:
            o.lowest_price = d['lowest_price']
        if 'transit_city_code' in d:
            o.transit_city_code = d['transit_city_code']
        return o


