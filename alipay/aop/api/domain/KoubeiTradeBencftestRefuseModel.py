#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class KoubeiTradeBencftestRefuseModel(object):

    def __init__(self):
        self._wp = None

    @property
    def wp(self):
        return self._wp

    @wp.setter
    def wp(self, value):
        self._wp = value


    def to_alipay_dict(self):
        params = dict()
        if self.wp:
            if hasattr(self.wp, 'to_alipay_dict'):
                params['wp'] = self.wp.to_alipay_dict()
            else:
                params['wp'] = self.wp
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = KoubeiTradeBencftestRefuseModel()
        if 'wp' in d:
            o.wp = d['wp']
        return o


