#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayDataMdaMiniappofflineQueryModel(object):

    def __init__(self):
        self._use_pass = None

    @property
    def use_pass(self):
        return self._use_pass

    @use_pass.setter
    def use_pass(self, value):
        self._use_pass = value


    def to_alipay_dict(self):
        params = dict()
        if self.use_pass:
            if hasattr(self.use_pass, 'to_alipay_dict'):
                params['use_pass'] = self.use_pass.to_alipay_dict()
            else:
                params['use_pass'] = self.use_pass
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayDataMdaMiniappofflineQueryModel()
        if 'use_pass' in d:
            o.use_pass = d['use_pass']
        return o


