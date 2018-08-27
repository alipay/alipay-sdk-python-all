#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayOpenAppXwbtstabcQueryModel(object):

    def __init__(self):
        self._xwbaa = None

    @property
    def xwbaa(self):
        return self._xwbaa

    @xwbaa.setter
    def xwbaa(self, value):
        self._xwbaa = value


    def to_alipay_dict(self):
        params = dict()
        if self.xwbaa:
            if hasattr(self.xwbaa, 'to_alipay_dict'):
                params['xwbaa'] = self.xwbaa.to_alipay_dict()
            else:
                params['xwbaa'] = self.xwbaa
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayOpenAppXwbtstabcQueryModel()
        if 'xwbaa' in d:
            o.xwbaa = d['xwbaa']
        return o


