#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class EpTrademarkSecondClassCodeInfo(object):

    def __init__(self):
        self._coding = None
        self._designation = None

    @property
    def coding(self):
        return self._coding

    @coding.setter
    def coding(self, value):
        self._coding = value
    @property
    def designation(self):
        return self._designation

    @designation.setter
    def designation(self, value):
        self._designation = value


    def to_alipay_dict(self):
        params = dict()
        if self.coding:
            if hasattr(self.coding, 'to_alipay_dict'):
                params['coding'] = self.coding.to_alipay_dict()
            else:
                params['coding'] = self.coding
        if self.designation:
            if hasattr(self.designation, 'to_alipay_dict'):
                params['designation'] = self.designation.to_alipay_dict()
            else:
                params['designation'] = self.designation
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = EpTrademarkSecondClassCodeInfo()
        if 'coding' in d:
            o.coding = d['coding']
        if 'designation' in d:
            o.designation = d['designation']
        return o


