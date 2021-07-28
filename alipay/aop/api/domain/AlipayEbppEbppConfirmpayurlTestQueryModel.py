#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayEbppEbppConfirmpayurlTestQueryModel(object):

    def __init__(self):
        self._tess = None

    @property
    def tess(self):
        return self._tess

    @tess.setter
    def tess(self, value):
        self._tess = value


    def to_alipay_dict(self):
        params = dict()
        if self.tess:
            if hasattr(self.tess, 'to_alipay_dict'):
                params['tess'] = self.tess.to_alipay_dict()
            else:
                params['tess'] = self.tess
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayEbppEbppConfirmpayurlTestQueryModel()
        if 'tess' in d:
            o.tess = d['tess']
        return o


