#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class RecycleInspectDigitalProductOpenVO(object):

    def __init__(self):
        self._imei = None

    @property
    def imei(self):
        return self._imei

    @imei.setter
    def imei(self, value):
        self._imei = value


    def to_alipay_dict(self):
        params = dict()
        if self.imei:
            if hasattr(self.imei, 'to_alipay_dict'):
                params['imei'] = self.imei.to_alipay_dict()
            else:
                params['imei'] = self.imei
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = RecycleInspectDigitalProductOpenVO()
        if 'imei' in d:
            o.imei = d['imei']
        return o


