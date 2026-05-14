#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class XingheLendassistCarfinPremortgageCancelModel(object):

    def __init__(self):
        self._apply_no = None
        self._lend_apply_no = None
        self._mortgage_no = None
        self._out_apply_no = None
        self._out_lend_apply_no = None

    @property
    def apply_no(self):
        return self._apply_no

    @apply_no.setter
    def apply_no(self, value):
        self._apply_no = value
    @property
    def lend_apply_no(self):
        return self._lend_apply_no

    @lend_apply_no.setter
    def lend_apply_no(self, value):
        self._lend_apply_no = value
    @property
    def mortgage_no(self):
        return self._mortgage_no

    @mortgage_no.setter
    def mortgage_no(self, value):
        self._mortgage_no = value
    @property
    def out_apply_no(self):
        return self._out_apply_no

    @out_apply_no.setter
    def out_apply_no(self, value):
        self._out_apply_no = value
    @property
    def out_lend_apply_no(self):
        return self._out_lend_apply_no

    @out_lend_apply_no.setter
    def out_lend_apply_no(self, value):
        self._out_lend_apply_no = value


    def to_alipay_dict(self):
        params = dict()
        if self.apply_no:
            if hasattr(self.apply_no, 'to_alipay_dict'):
                params['apply_no'] = self.apply_no.to_alipay_dict()
            else:
                params['apply_no'] = self.apply_no
        if self.lend_apply_no:
            if hasattr(self.lend_apply_no, 'to_alipay_dict'):
                params['lend_apply_no'] = self.lend_apply_no.to_alipay_dict()
            else:
                params['lend_apply_no'] = self.lend_apply_no
        if self.mortgage_no:
            if hasattr(self.mortgage_no, 'to_alipay_dict'):
                params['mortgage_no'] = self.mortgage_no.to_alipay_dict()
            else:
                params['mortgage_no'] = self.mortgage_no
        if self.out_apply_no:
            if hasattr(self.out_apply_no, 'to_alipay_dict'):
                params['out_apply_no'] = self.out_apply_no.to_alipay_dict()
            else:
                params['out_apply_no'] = self.out_apply_no
        if self.out_lend_apply_no:
            if hasattr(self.out_lend_apply_no, 'to_alipay_dict'):
                params['out_lend_apply_no'] = self.out_lend_apply_no.to_alipay_dict()
            else:
                params['out_lend_apply_no'] = self.out_lend_apply_no
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = XingheLendassistCarfinPremortgageCancelModel()
        if 'apply_no' in d:
            o.apply_no = d['apply_no']
        if 'lend_apply_no' in d:
            o.lend_apply_no = d['lend_apply_no']
        if 'mortgage_no' in d:
            o.mortgage_no = d['mortgage_no']
        if 'out_apply_no' in d:
            o.out_apply_no = d['out_apply_no']
        if 'out_lend_apply_no' in d:
            o.out_lend_apply_no = d['out_lend_apply_no']
        return o


