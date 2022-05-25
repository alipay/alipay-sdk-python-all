#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ManjiangTesttttttt(object):

    def __init__(self):
        self._qqq = None

    @property
    def qqq(self):
        return self._qqq

    @qqq.setter
    def qqq(self, value):
        self._qqq = value


    def to_alipay_dict(self):
        params = dict()
        if self.qqq:
            if hasattr(self.qqq, 'to_alipay_dict'):
                params['qqq'] = self.qqq.to_alipay_dict()
            else:
                params['qqq'] = self.qqq
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ManjiangTesttttttt()
        if 'qqq' in d:
            o.qqq = d['qqq']
        return o


