#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class LiabilityQuoteInfo(object):

    def __init__(self):
        self._effect_end_time = None
        self._effect_start_time = None
        self._iop_premium = None
        self._liability_no = None
        self._liability_premium = None
        self._sum_insured = None

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
    def iop_premium(self):
        return self._iop_premium

    @iop_premium.setter
    def iop_premium(self, value):
        self._iop_premium = value
    @property
    def liability_no(self):
        return self._liability_no

    @liability_no.setter
    def liability_no(self, value):
        self._liability_no = value
    @property
    def liability_premium(self):
        return self._liability_premium

    @liability_premium.setter
    def liability_premium(self, value):
        self._liability_premium = value
    @property
    def sum_insured(self):
        return self._sum_insured

    @sum_insured.setter
    def sum_insured(self, value):
        self._sum_insured = value


    def to_alipay_dict(self):
        params = dict()
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
        if self.iop_premium:
            if hasattr(self.iop_premium, 'to_alipay_dict'):
                params['iop_premium'] = self.iop_premium.to_alipay_dict()
            else:
                params['iop_premium'] = self.iop_premium
        if self.liability_no:
            if hasattr(self.liability_no, 'to_alipay_dict'):
                params['liability_no'] = self.liability_no.to_alipay_dict()
            else:
                params['liability_no'] = self.liability_no
        if self.liability_premium:
            if hasattr(self.liability_premium, 'to_alipay_dict'):
                params['liability_premium'] = self.liability_premium.to_alipay_dict()
            else:
                params['liability_premium'] = self.liability_premium
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
        o = LiabilityQuoteInfo()
        if 'effect_end_time' in d:
            o.effect_end_time = d['effect_end_time']
        if 'effect_start_time' in d:
            o.effect_start_time = d['effect_start_time']
        if 'iop_premium' in d:
            o.iop_premium = d['iop_premium']
        if 'liability_no' in d:
            o.liability_no = d['liability_no']
        if 'liability_premium' in d:
            o.liability_premium = d['liability_premium']
        if 'sum_insured' in d:
            o.sum_insured = d['sum_insured']
        return o


