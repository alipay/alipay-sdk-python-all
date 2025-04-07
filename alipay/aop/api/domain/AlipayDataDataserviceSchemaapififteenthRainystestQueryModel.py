#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayDataDataserviceSchemaapififteenthRainystestQueryModel(object):

    def __init__(self):
        self._demo_req = None

    @property
    def demo_req(self):
        return self._demo_req

    @demo_req.setter
    def demo_req(self, value):
        self._demo_req = value


    def to_alipay_dict(self):
        params = dict()
        if self.demo_req:
            if hasattr(self.demo_req, 'to_alipay_dict'):
                params['demo_req'] = self.demo_req.to_alipay_dict()
            else:
                params['demo_req'] = self.demo_req
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayDataDataserviceSchemaapififteenthRainystestQueryModel()
        if 'demo_req' in d:
            o.demo_req = d['demo_req']
        return o


