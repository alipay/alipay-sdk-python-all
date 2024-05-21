#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayIserviceCcmCusomterAccountQueryModel(object):

    def __init__(self):
        self._mobile_number = None

    @property
    def mobile_number(self):
        return self._mobile_number

    @mobile_number.setter
    def mobile_number(self, value):
        self._mobile_number = value


    def to_alipay_dict(self):
        params = dict()
        if self.mobile_number:
            if hasattr(self.mobile_number, 'to_alipay_dict'):
                params['mobile_number'] = self.mobile_number.to_alipay_dict()
            else:
                params['mobile_number'] = self.mobile_number
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayIserviceCcmCusomterAccountQueryModel()
        if 'mobile_number' in d:
            o.mobile_number = d['mobile_number']
        return o


