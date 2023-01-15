#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayOpenAppTestQinyuQueryModel(object):

    def __init__(self):
        self._oid = None

    @property
    def oid(self):
        return self._oid

    @oid.setter
    def oid(self, value):
        self._oid = value


    def to_alipay_dict(self):
        params = dict()
        if self.oid:
            if hasattr(self.oid, 'to_alipay_dict'):
                params['oid'] = self.oid.to_alipay_dict()
            else:
                params['oid'] = self.oid
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayOpenAppTestQinyuQueryModel()
        if 'oid' in d:
            o.oid = d['oid']
        return o


