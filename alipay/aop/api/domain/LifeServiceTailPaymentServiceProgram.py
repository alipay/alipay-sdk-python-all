#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class LifeServiceTailPaymentServiceProgram(object):

    def __init__(self):
        self._service_program_count = None
        self._service_program_name = None
        self._service_program_unit_price_yuan = None

    @property
    def service_program_count(self):
        return self._service_program_count

    @service_program_count.setter
    def service_program_count(self, value):
        self._service_program_count = value
    @property
    def service_program_name(self):
        return self._service_program_name

    @service_program_name.setter
    def service_program_name(self, value):
        self._service_program_name = value
    @property
    def service_program_unit_price_yuan(self):
        return self._service_program_unit_price_yuan

    @service_program_unit_price_yuan.setter
    def service_program_unit_price_yuan(self, value):
        self._service_program_unit_price_yuan = value


    def to_alipay_dict(self):
        params = dict()
        if self.service_program_count:
            if hasattr(self.service_program_count, 'to_alipay_dict'):
                params['service_program_count'] = self.service_program_count.to_alipay_dict()
            else:
                params['service_program_count'] = self.service_program_count
        if self.service_program_name:
            if hasattr(self.service_program_name, 'to_alipay_dict'):
                params['service_program_name'] = self.service_program_name.to_alipay_dict()
            else:
                params['service_program_name'] = self.service_program_name
        if self.service_program_unit_price_yuan:
            if hasattr(self.service_program_unit_price_yuan, 'to_alipay_dict'):
                params['service_program_unit_price_yuan'] = self.service_program_unit_price_yuan.to_alipay_dict()
            else:
                params['service_program_unit_price_yuan'] = self.service_program_unit_price_yuan
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = LifeServiceTailPaymentServiceProgram()
        if 'service_program_count' in d:
            o.service_program_count = d['service_program_count']
        if 'service_program_name' in d:
            o.service_program_name = d['service_program_name']
        if 'service_program_unit_price_yuan' in d:
            o.service_program_unit_price_yuan = d['service_program_unit_price_yuan']
        return o


