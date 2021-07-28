#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class Liability(object):

    def __init__(self):
        self._iop = None
        self._liability_no = None
        self._sum_insured = None

    @property
    def iop(self):
        return self._iop

    @iop.setter
    def iop(self, value):
        self._iop = value
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
        if self.iop:
            if hasattr(self.iop, 'to_alipay_dict'):
                params['iop'] = self.iop.to_alipay_dict()
            else:
                params['iop'] = self.iop
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
        o = Liability()
        if 'iop' in d:
            o.iop = d['iop']
        if 'liability_no' in d:
            o.liability_no = d['liability_no']
        if 'sum_insured' in d:
            o.sum_insured = d['sum_insured']
        return o


