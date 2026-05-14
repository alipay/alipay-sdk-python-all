#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class IncomeOutBusinessItems(object):

    def __init__(self):
        self._out_business_name = None
        self._out_business_no = None
        self._out_business_sale_price = None
        self._out_custom_no = None
        self._out_settle_no = None
        self._settle_price = None
        self._settle_time = None
        self._to_subject_id = None
        self._to_subject_type = None

    @property
    def out_business_name(self):
        return self._out_business_name

    @out_business_name.setter
    def out_business_name(self, value):
        self._out_business_name = value
    @property
    def out_business_no(self):
        return self._out_business_no

    @out_business_no.setter
    def out_business_no(self, value):
        self._out_business_no = value
    @property
    def out_business_sale_price(self):
        return self._out_business_sale_price

    @out_business_sale_price.setter
    def out_business_sale_price(self, value):
        self._out_business_sale_price = value
    @property
    def out_custom_no(self):
        return self._out_custom_no

    @out_custom_no.setter
    def out_custom_no(self, value):
        self._out_custom_no = value
    @property
    def out_settle_no(self):
        return self._out_settle_no

    @out_settle_no.setter
    def out_settle_no(self, value):
        self._out_settle_no = value
    @property
    def settle_price(self):
        return self._settle_price

    @settle_price.setter
    def settle_price(self, value):
        self._settle_price = value
    @property
    def settle_time(self):
        return self._settle_time

    @settle_time.setter
    def settle_time(self, value):
        self._settle_time = value
    @property
    def to_subject_id(self):
        return self._to_subject_id

    @to_subject_id.setter
    def to_subject_id(self, value):
        self._to_subject_id = value
    @property
    def to_subject_type(self):
        return self._to_subject_type

    @to_subject_type.setter
    def to_subject_type(self, value):
        self._to_subject_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.out_business_name:
            if hasattr(self.out_business_name, 'to_alipay_dict'):
                params['out_business_name'] = self.out_business_name.to_alipay_dict()
            else:
                params['out_business_name'] = self.out_business_name
        if self.out_business_no:
            if hasattr(self.out_business_no, 'to_alipay_dict'):
                params['out_business_no'] = self.out_business_no.to_alipay_dict()
            else:
                params['out_business_no'] = self.out_business_no
        if self.out_business_sale_price:
            if hasattr(self.out_business_sale_price, 'to_alipay_dict'):
                params['out_business_sale_price'] = self.out_business_sale_price.to_alipay_dict()
            else:
                params['out_business_sale_price'] = self.out_business_sale_price
        if self.out_custom_no:
            if hasattr(self.out_custom_no, 'to_alipay_dict'):
                params['out_custom_no'] = self.out_custom_no.to_alipay_dict()
            else:
                params['out_custom_no'] = self.out_custom_no
        if self.out_settle_no:
            if hasattr(self.out_settle_no, 'to_alipay_dict'):
                params['out_settle_no'] = self.out_settle_no.to_alipay_dict()
            else:
                params['out_settle_no'] = self.out_settle_no
        if self.settle_price:
            if hasattr(self.settle_price, 'to_alipay_dict'):
                params['settle_price'] = self.settle_price.to_alipay_dict()
            else:
                params['settle_price'] = self.settle_price
        if self.settle_time:
            if hasattr(self.settle_time, 'to_alipay_dict'):
                params['settle_time'] = self.settle_time.to_alipay_dict()
            else:
                params['settle_time'] = self.settle_time
        if self.to_subject_id:
            if hasattr(self.to_subject_id, 'to_alipay_dict'):
                params['to_subject_id'] = self.to_subject_id.to_alipay_dict()
            else:
                params['to_subject_id'] = self.to_subject_id
        if self.to_subject_type:
            if hasattr(self.to_subject_type, 'to_alipay_dict'):
                params['to_subject_type'] = self.to_subject_type.to_alipay_dict()
            else:
                params['to_subject_type'] = self.to_subject_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = IncomeOutBusinessItems()
        if 'out_business_name' in d:
            o.out_business_name = d['out_business_name']
        if 'out_business_no' in d:
            o.out_business_no = d['out_business_no']
        if 'out_business_sale_price' in d:
            o.out_business_sale_price = d['out_business_sale_price']
        if 'out_custom_no' in d:
            o.out_custom_no = d['out_custom_no']
        if 'out_settle_no' in d:
            o.out_settle_no = d['out_settle_no']
        if 'settle_price' in d:
            o.settle_price = d['settle_price']
        if 'settle_time' in d:
            o.settle_time = d['settle_time']
        if 'to_subject_id' in d:
            o.to_subject_id = d['to_subject_id']
        if 'to_subject_type' in d:
            o.to_subject_type = d['to_subject_type']
        return o


