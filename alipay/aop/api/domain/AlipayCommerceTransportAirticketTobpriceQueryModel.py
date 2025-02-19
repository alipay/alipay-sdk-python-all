#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceTransportAirticketTobpriceQueryModel(object):

    def __init__(self):
        self._arr_city_code = None
        self._dep_city_code = None
        self._dep_date = None
        self._out_biz_no = None

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
    def out_biz_no(self):
        return self._out_biz_no

    @out_biz_no.setter
    def out_biz_no(self, value):
        self._out_biz_no = value


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
        if self.out_biz_no:
            if hasattr(self.out_biz_no, 'to_alipay_dict'):
                params['out_biz_no'] = self.out_biz_no.to_alipay_dict()
            else:
                params['out_biz_no'] = self.out_biz_no
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceTransportAirticketTobpriceQueryModel()
        if 'arr_city_code' in d:
            o.arr_city_code = d['arr_city_code']
        if 'dep_city_code' in d:
            o.dep_city_code = d['dep_city_code']
        if 'dep_date' in d:
            o.dep_date = d['dep_date']
        if 'out_biz_no' in d:
            o.out_biz_no = d['out_biz_no']
        return o


