#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ProductInfoDTO(object):

    def __init__(self):
        self._estimate_premium = None

    @property
    def estimate_premium(self):
        return self._estimate_premium

    @estimate_premium.setter
    def estimate_premium(self, value):
        self._estimate_premium = value


    def to_alipay_dict(self):
        params = dict()
        if self.estimate_premium:
            if hasattr(self.estimate_premium, 'to_alipay_dict'):
                params['estimate_premium'] = self.estimate_premium.to_alipay_dict()
            else:
                params['estimate_premium'] = self.estimate_premium
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ProductInfoDTO()
        if 'estimate_premium' in d:
            o.estimate_premium = d['estimate_premium']
        return o


