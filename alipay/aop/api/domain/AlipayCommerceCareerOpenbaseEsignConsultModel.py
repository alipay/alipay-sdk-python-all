#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceCareerOpenbaseEsignConsultModel(object):

    def __init__(self):
        self._ability_code = None
        self._enterprise_no = None
        self._estimated_price = None
        self._out_biz_no = None
        self._use_time = None

    @property
    def ability_code(self):
        return self._ability_code

    @ability_code.setter
    def ability_code(self, value):
        self._ability_code = value
    @property
    def enterprise_no(self):
        return self._enterprise_no

    @enterprise_no.setter
    def enterprise_no(self, value):
        self._enterprise_no = value
    @property
    def estimated_price(self):
        return self._estimated_price

    @estimated_price.setter
    def estimated_price(self, value):
        self._estimated_price = value
    @property
    def out_biz_no(self):
        return self._out_biz_no

    @out_biz_no.setter
    def out_biz_no(self, value):
        self._out_biz_no = value
    @property
    def use_time(self):
        return self._use_time

    @use_time.setter
    def use_time(self, value):
        self._use_time = value


    def to_alipay_dict(self):
        params = dict()
        if self.ability_code:
            if hasattr(self.ability_code, 'to_alipay_dict'):
                params['ability_code'] = self.ability_code.to_alipay_dict()
            else:
                params['ability_code'] = self.ability_code
        if self.enterprise_no:
            if hasattr(self.enterprise_no, 'to_alipay_dict'):
                params['enterprise_no'] = self.enterprise_no.to_alipay_dict()
            else:
                params['enterprise_no'] = self.enterprise_no
        if self.estimated_price:
            if hasattr(self.estimated_price, 'to_alipay_dict'):
                params['estimated_price'] = self.estimated_price.to_alipay_dict()
            else:
                params['estimated_price'] = self.estimated_price
        if self.out_biz_no:
            if hasattr(self.out_biz_no, 'to_alipay_dict'):
                params['out_biz_no'] = self.out_biz_no.to_alipay_dict()
            else:
                params['out_biz_no'] = self.out_biz_no
        if self.use_time:
            if hasattr(self.use_time, 'to_alipay_dict'):
                params['use_time'] = self.use_time.to_alipay_dict()
            else:
                params['use_time'] = self.use_time
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceCareerOpenbaseEsignConsultModel()
        if 'ability_code' in d:
            o.ability_code = d['ability_code']
        if 'enterprise_no' in d:
            o.enterprise_no = d['enterprise_no']
        if 'estimated_price' in d:
            o.estimated_price = d['estimated_price']
        if 'out_biz_no' in d:
            o.out_biz_no = d['out_biz_no']
        if 'use_time' in d:
            o.use_time = d['use_time']
        return o


