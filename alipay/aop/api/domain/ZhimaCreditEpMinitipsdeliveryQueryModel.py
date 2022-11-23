#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ZhimaCreditEpMinitipsdeliveryQueryModel(object):

    def __init__(self):
        self._hhh = None
        self._xx = None
        self._xx_open_id = None

    @property
    def hhh(self):
        return self._hhh

    @hhh.setter
    def hhh(self, value):
        self._hhh = value
    @property
    def xx(self):
        return self._xx

    @xx.setter
    def xx(self, value):
        self._xx = value
    @property
    def xx_open_id(self):
        return self._xx_open_id

    @xx_open_id.setter
    def xx_open_id(self, value):
        self._xx_open_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.hhh:
            if hasattr(self.hhh, 'to_alipay_dict'):
                params['hhh'] = self.hhh.to_alipay_dict()
            else:
                params['hhh'] = self.hhh
        if self.xx:
            if hasattr(self.xx, 'to_alipay_dict'):
                params['xx'] = self.xx.to_alipay_dict()
            else:
                params['xx'] = self.xx
        if self.xx_open_id:
            if hasattr(self.xx_open_id, 'to_alipay_dict'):
                params['xx_open_id'] = self.xx_open_id.to_alipay_dict()
            else:
                params['xx_open_id'] = self.xx_open_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ZhimaCreditEpMinitipsdeliveryQueryModel()
        if 'hhh' in d:
            o.hhh = d['hhh']
        if 'xx' in d:
            o.xx = d['xx']
        if 'xx_open_id' in d:
            o.xx_open_id = d['xx_open_id']
        return o


