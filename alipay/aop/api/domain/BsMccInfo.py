#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class BsMccInfo(object):

    def __init__(self):
        self._mcc_code_1 = None
        self._mcc_code_2 = None
        self._mcc_name_1 = None
        self._mcc_name_2 = None

    @property
    def mcc_code_1(self):
        return self._mcc_code_1

    @mcc_code_1.setter
    def mcc_code_1(self, value):
        self._mcc_code_1 = value
    @property
    def mcc_code_2(self):
        return self._mcc_code_2

    @mcc_code_2.setter
    def mcc_code_2(self, value):
        self._mcc_code_2 = value
    @property
    def mcc_name_1(self):
        return self._mcc_name_1

    @mcc_name_1.setter
    def mcc_name_1(self, value):
        self._mcc_name_1 = value
    @property
    def mcc_name_2(self):
        return self._mcc_name_2

    @mcc_name_2.setter
    def mcc_name_2(self, value):
        self._mcc_name_2 = value


    def to_alipay_dict(self):
        params = dict()
        if self.mcc_code_1:
            if hasattr(self.mcc_code_1, 'to_alipay_dict'):
                params['mcc_code_1'] = self.mcc_code_1.to_alipay_dict()
            else:
                params['mcc_code_1'] = self.mcc_code_1
        if self.mcc_code_2:
            if hasattr(self.mcc_code_2, 'to_alipay_dict'):
                params['mcc_code_2'] = self.mcc_code_2.to_alipay_dict()
            else:
                params['mcc_code_2'] = self.mcc_code_2
        if self.mcc_name_1:
            if hasattr(self.mcc_name_1, 'to_alipay_dict'):
                params['mcc_name_1'] = self.mcc_name_1.to_alipay_dict()
            else:
                params['mcc_name_1'] = self.mcc_name_1
        if self.mcc_name_2:
            if hasattr(self.mcc_name_2, 'to_alipay_dict'):
                params['mcc_name_2'] = self.mcc_name_2.to_alipay_dict()
            else:
                params['mcc_name_2'] = self.mcc_name_2
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = BsMccInfo()
        if 'mcc_code_1' in d:
            o.mcc_code_1 = d['mcc_code_1']
        if 'mcc_code_2' in d:
            o.mcc_code_2 = d['mcc_code_2']
        if 'mcc_name_1' in d:
            o.mcc_name_1 = d['mcc_name_1']
        if 'mcc_name_2' in d:
            o.mcc_name_2 = d['mcc_name_2']
        return o


