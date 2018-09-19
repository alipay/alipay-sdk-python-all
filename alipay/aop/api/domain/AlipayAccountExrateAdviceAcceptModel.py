#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.AdviceVO import AdviceVO


class AlipayAccountExrateAdviceAcceptModel(object):

    def __init__(self):
        self._advice = None

    @property
    def advice(self):
        return self._advice

    @advice.setter
    def advice(self, value):
        if isinstance(value, AdviceVO):
            self._advice = value
        else:
            self._advice = AdviceVO.from_alipay_dict(value)


    def to_alipay_dict(self):
        params = dict()
        if self.advice:
            if hasattr(self.advice, 'to_alipay_dict'):
                params['advice'] = self.advice.to_alipay_dict()
            else:
                params['advice'] = self.advice
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayAccountExrateAdviceAcceptModel()
        if 'advice' in d:
            o.advice = d['advice']
        return o


