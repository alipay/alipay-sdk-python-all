#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.InsObject import InsObject
from alipay.aop.api.domain.InsPerson import InsPerson


class InsApplication(object):

    def __init__(self):
        self._biz_data = None
        self._copies = None
        self._effect_end_time = None
        self._effect_start_time = None
        self._ins_object = None
        self._insured = None
        self._period = None
        self._premium = None
        self._sum_insured = None

    @property
    def biz_data(self):
        return self._biz_data

    @biz_data.setter
    def biz_data(self, value):
        self._biz_data = value
    @property
    def copies(self):
        return self._copies

    @copies.setter
    def copies(self, value):
        self._copies = value
    @property
    def effect_end_time(self):
        return self._effect_end_time

    @effect_end_time.setter
    def effect_end_time(self, value):
        self._effect_end_time = value
    @property
    def effect_start_time(self):
        return self._effect_start_time

    @effect_start_time.setter
    def effect_start_time(self, value):
        self._effect_start_time = value
    @property
    def ins_object(self):
        return self._ins_object

    @ins_object.setter
    def ins_object(self, value):
        if isinstance(value, InsObject):
            self._ins_object = value
        else:
            self._ins_object = InsObject.from_alipay_dict(value)
    @property
    def insured(self):
        return self._insured

    @insured.setter
    def insured(self, value):
        if isinstance(value, InsPerson):
            self._insured = value
        else:
            self._insured = InsPerson.from_alipay_dict(value)
    @property
    def period(self):
        return self._period

    @period.setter
    def period(self, value):
        self._period = value
    @property
    def premium(self):
        return self._premium

    @premium.setter
    def premium(self, value):
        self._premium = value
    @property
    def sum_insured(self):
        return self._sum_insured

    @sum_insured.setter
    def sum_insured(self, value):
        self._sum_insured = value


    def to_alipay_dict(self):
        params = dict()
        if self.biz_data:
            if hasattr(self.biz_data, 'to_alipay_dict'):
                params['biz_data'] = self.biz_data.to_alipay_dict()
            else:
                params['biz_data'] = self.biz_data
        if self.copies:
            if hasattr(self.copies, 'to_alipay_dict'):
                params['copies'] = self.copies.to_alipay_dict()
            else:
                params['copies'] = self.copies
        if self.effect_end_time:
            if hasattr(self.effect_end_time, 'to_alipay_dict'):
                params['effect_end_time'] = self.effect_end_time.to_alipay_dict()
            else:
                params['effect_end_time'] = self.effect_end_time
        if self.effect_start_time:
            if hasattr(self.effect_start_time, 'to_alipay_dict'):
                params['effect_start_time'] = self.effect_start_time.to_alipay_dict()
            else:
                params['effect_start_time'] = self.effect_start_time
        if self.ins_object:
            if hasattr(self.ins_object, 'to_alipay_dict'):
                params['ins_object'] = self.ins_object.to_alipay_dict()
            else:
                params['ins_object'] = self.ins_object
        if self.insured:
            if hasattr(self.insured, 'to_alipay_dict'):
                params['insured'] = self.insured.to_alipay_dict()
            else:
                params['insured'] = self.insured
        if self.period:
            if hasattr(self.period, 'to_alipay_dict'):
                params['period'] = self.period.to_alipay_dict()
            else:
                params['period'] = self.period
        if self.premium:
            if hasattr(self.premium, 'to_alipay_dict'):
                params['premium'] = self.premium.to_alipay_dict()
            else:
                params['premium'] = self.premium
        if self.sum_insured:
            if hasattr(self.sum_insured, 'to_alipay_dict'):
                params['sum_insured'] = self.sum_insured.to_alipay_dict()
            else:
                params['sum_insured'] = self.sum_insured
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = InsApplication()
        if 'biz_data' in d:
            o.biz_data = d['biz_data']
        if 'copies' in d:
            o.copies = d['copies']
        if 'effect_end_time' in d:
            o.effect_end_time = d['effect_end_time']
        if 'effect_start_time' in d:
            o.effect_start_time = d['effect_start_time']
        if 'ins_object' in d:
            o.ins_object = d['ins_object']
        if 'insured' in d:
            o.insured = d['insured']
        if 'period' in d:
            o.period = d['period']
        if 'premium' in d:
            o.premium = d['premium']
        if 'sum_insured' in d:
            o.sum_insured = d['sum_insured']
        return o


