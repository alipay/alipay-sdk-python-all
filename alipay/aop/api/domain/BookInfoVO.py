#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class BookInfoVO(object):

    def __init__(self):
        self._book_time = None
        self._out_item_id = None
        self._out_trade_no = None
        self._patient_id = None
        self._patient_name = None
        self._pay_method = None
        self._vaccine_dose = None

    @property
    def book_time(self):
        return self._book_time

    @book_time.setter
    def book_time(self, value):
        self._book_time = value
    @property
    def out_item_id(self):
        return self._out_item_id

    @out_item_id.setter
    def out_item_id(self, value):
        self._out_item_id = value
    @property
    def out_trade_no(self):
        return self._out_trade_no

    @out_trade_no.setter
    def out_trade_no(self, value):
        self._out_trade_no = value
    @property
    def patient_id(self):
        return self._patient_id

    @patient_id.setter
    def patient_id(self, value):
        self._patient_id = value
    @property
    def patient_name(self):
        return self._patient_name

    @patient_name.setter
    def patient_name(self, value):
        self._patient_name = value
    @property
    def pay_method(self):
        return self._pay_method

    @pay_method.setter
    def pay_method(self, value):
        self._pay_method = value
    @property
    def vaccine_dose(self):
        return self._vaccine_dose

    @vaccine_dose.setter
    def vaccine_dose(self, value):
        self._vaccine_dose = value


    def to_alipay_dict(self):
        params = dict()
        if self.book_time:
            if hasattr(self.book_time, 'to_alipay_dict'):
                params['book_time'] = self.book_time.to_alipay_dict()
            else:
                params['book_time'] = self.book_time
        if self.out_item_id:
            if hasattr(self.out_item_id, 'to_alipay_dict'):
                params['out_item_id'] = self.out_item_id.to_alipay_dict()
            else:
                params['out_item_id'] = self.out_item_id
        if self.out_trade_no:
            if hasattr(self.out_trade_no, 'to_alipay_dict'):
                params['out_trade_no'] = self.out_trade_no.to_alipay_dict()
            else:
                params['out_trade_no'] = self.out_trade_no
        if self.patient_id:
            if hasattr(self.patient_id, 'to_alipay_dict'):
                params['patient_id'] = self.patient_id.to_alipay_dict()
            else:
                params['patient_id'] = self.patient_id
        if self.patient_name:
            if hasattr(self.patient_name, 'to_alipay_dict'):
                params['patient_name'] = self.patient_name.to_alipay_dict()
            else:
                params['patient_name'] = self.patient_name
        if self.pay_method:
            if hasattr(self.pay_method, 'to_alipay_dict'):
                params['pay_method'] = self.pay_method.to_alipay_dict()
            else:
                params['pay_method'] = self.pay_method
        if self.vaccine_dose:
            if hasattr(self.vaccine_dose, 'to_alipay_dict'):
                params['vaccine_dose'] = self.vaccine_dose.to_alipay_dict()
            else:
                params['vaccine_dose'] = self.vaccine_dose
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = BookInfoVO()
        if 'book_time' in d:
            o.book_time = d['book_time']
        if 'out_item_id' in d:
            o.out_item_id = d['out_item_id']
        if 'out_trade_no' in d:
            o.out_trade_no = d['out_trade_no']
        if 'patient_id' in d:
            o.patient_id = d['patient_id']
        if 'patient_name' in d:
            o.patient_name = d['patient_name']
        if 'pay_method' in d:
            o.pay_method = d['pay_method']
        if 'vaccine_dose' in d:
            o.vaccine_dose = d['vaccine_dose']
        return o


