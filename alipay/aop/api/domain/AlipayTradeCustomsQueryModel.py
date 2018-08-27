#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayTradeCustomsQueryModel(object):

    def __init__(self):
        self._out_request_nos = None

    @property
    def out_request_nos(self):
        return self._out_request_nos

    @out_request_nos.setter
    def out_request_nos(self, value):
        self._out_request_nos = value


    def to_alipay_dict(self):
        params = dict()
        if self.out_request_nos:
            if hasattr(self.out_request_nos, 'to_alipay_dict'):
                params['out_request_nos'] = self.out_request_nos.to_alipay_dict()
            else:
                params['out_request_nos'] = self.out_request_nos
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayTradeCustomsQueryModel()
        if 'out_request_nos' in d:
            o.out_request_nos = d['out_request_nos']
        return o


