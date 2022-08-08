#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayMerchantQipanCrowdQueryModel(object):

    def __init__(self):
        self._crowd_code = None
        self._external_crowd_code = None

    @property
    def crowd_code(self):
        return self._crowd_code

    @crowd_code.setter
    def crowd_code(self, value):
        self._crowd_code = value
    @property
    def external_crowd_code(self):
        return self._external_crowd_code

    @external_crowd_code.setter
    def external_crowd_code(self, value):
        self._external_crowd_code = value


    def to_alipay_dict(self):
        params = dict()
        if self.crowd_code:
            if hasattr(self.crowd_code, 'to_alipay_dict'):
                params['crowd_code'] = self.crowd_code.to_alipay_dict()
            else:
                params['crowd_code'] = self.crowd_code
        if self.external_crowd_code:
            if hasattr(self.external_crowd_code, 'to_alipay_dict'):
                params['external_crowd_code'] = self.external_crowd_code.to_alipay_dict()
            else:
                params['external_crowd_code'] = self.external_crowd_code
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayMerchantQipanCrowdQueryModel()
        if 'crowd_code' in d:
            o.crowd_code = d['crowd_code']
        if 'external_crowd_code' in d:
            o.external_crowd_code = d['external_crowd_code']
        return o


