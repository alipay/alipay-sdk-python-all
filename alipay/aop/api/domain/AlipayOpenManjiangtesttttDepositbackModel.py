#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayOpenManjiangtesttttDepositbackModel(object):

    def __init__(self):
        self._sss = None

    @property
    def sss(self):
        return self._sss

    @sss.setter
    def sss(self, value):
        self._sss = value


    def to_alipay_dict(self):
        params = dict()
        if self.sss:
            if hasattr(self.sss, 'to_alipay_dict'):
                params['sss'] = self.sss.to_alipay_dict()
            else:
                params['sss'] = self.sss
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayOpenManjiangtesttttDepositbackModel()
        if 'sss' in d:
            o.sss = d['sss']
        return o


