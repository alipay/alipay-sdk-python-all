#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayDigitalmgmtRcvQueryModel(object):

    def __init__(self):
        self._rcv_number = None

    @property
    def rcv_number(self):
        return self._rcv_number

    @rcv_number.setter
    def rcv_number(self, value):
        self._rcv_number = value


    def to_alipay_dict(self):
        params = dict()
        if self.rcv_number:
            if hasattr(self.rcv_number, 'to_alipay_dict'):
                params['rcv_number'] = self.rcv_number.to_alipay_dict()
            else:
                params['rcv_number'] = self.rcv_number
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayDigitalmgmtRcvQueryModel()
        if 'rcv_number' in d:
            o.rcv_number = d['rcv_number']
        return o


