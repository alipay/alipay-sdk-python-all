#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayOpenAppLingbalingliuQueryModel(object):

    def __init__(self):
        self._canshu = None

    @property
    def canshu(self):
        return self._canshu

    @canshu.setter
    def canshu(self, value):
        self._canshu = value


    def to_alipay_dict(self):
        params = dict()
        if self.canshu:
            if hasattr(self.canshu, 'to_alipay_dict'):
                params['canshu'] = self.canshu.to_alipay_dict()
            else:
                params['canshu'] = self.canshu
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayOpenAppLingbalingliuQueryModel()
        if 'canshu' in d:
            o.canshu = d['canshu']
        return o


