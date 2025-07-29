#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipaySecurityDataQingliangceshiCeshiceshiceshiQueryModel(object):

    def __init__(self):
        self._blance = None

    @property
    def blance(self):
        return self._blance

    @blance.setter
    def blance(self, value):
        self._blance = value


    def to_alipay_dict(self):
        params = dict()
        if self.blance:
            if hasattr(self.blance, 'to_alipay_dict'):
                params['blance'] = self.blance.to_alipay_dict()
            else:
                params['blance'] = self.blance
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipaySecurityDataQingliangceshiCeshiceshiceshiQueryModel()
        if 'blance' in d:
            o.blance = d['blance']
        return o


