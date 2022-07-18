#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class KoubeiShopMantestsdsSendModel(object):

    def __init__(self):
        self._opopo = None

    @property
    def opopo(self):
        return self._opopo

    @opopo.setter
    def opopo(self, value):
        self._opopo = value


    def to_alipay_dict(self):
        params = dict()
        if self.opopo:
            if hasattr(self.opopo, 'to_alipay_dict'):
                params['opopo'] = self.opopo.to_alipay_dict()
            else:
                params['opopo'] = self.opopo
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = KoubeiShopMantestsdsSendModel()
        if 'opopo' in d:
            o.opopo = d['opopo']
        return o


