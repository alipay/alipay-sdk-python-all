#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class InsOpenPolicyLiabilityDigestDTO(object):

    def __init__(self):
        self._liability_name = None
        self._liability_no = None
        self._sum_insured = None

    @property
    def liability_name(self):
        return self._liability_name

    @liability_name.setter
    def liability_name(self, value):
        self._liability_name = value
    @property
    def liability_no(self):
        return self._liability_no

    @liability_no.setter
    def liability_no(self, value):
        self._liability_no = value
    @property
    def sum_insured(self):
        return self._sum_insured

    @sum_insured.setter
    def sum_insured(self, value):
        self._sum_insured = value


    def to_alipay_dict(self):
        params = dict()
        if self.liability_name:
            if hasattr(self.liability_name, 'to_alipay_dict'):
                params['liability_name'] = self.liability_name.to_alipay_dict()
            else:
                params['liability_name'] = self.liability_name
        if self.liability_no:
            if hasattr(self.liability_no, 'to_alipay_dict'):
                params['liability_no'] = self.liability_no.to_alipay_dict()
            else:
                params['liability_no'] = self.liability_no
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
        o = InsOpenPolicyLiabilityDigestDTO()
        if 'liability_name' in d:
            o.liability_name = d['liability_name']
        if 'liability_no' in d:
            o.liability_no = d['liability_no']
        if 'sum_insured' in d:
            o.sum_insured = d['sum_insured']
        return o


