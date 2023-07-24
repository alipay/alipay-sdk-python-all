#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.MallReceivePrRequest import MallReceivePrRequest


class AlipayDigitalmgmtPunchoutPrCreateModel(object):

    def __init__(self):
        self._pur_req = None

    @property
    def pur_req(self):
        return self._pur_req

    @pur_req.setter
    def pur_req(self, value):
        if isinstance(value, MallReceivePrRequest):
            self._pur_req = value
        else:
            self._pur_req = MallReceivePrRequest.from_alipay_dict(value)


    def to_alipay_dict(self):
        params = dict()
        if self.pur_req:
            if hasattr(self.pur_req, 'to_alipay_dict'):
                params['pur_req'] = self.pur_req.to_alipay_dict()
            else:
                params['pur_req'] = self.pur_req
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayDigitalmgmtPunchoutPrCreateModel()
        if 'pur_req' in d:
            o.pur_req = d['pur_req']
        return o


