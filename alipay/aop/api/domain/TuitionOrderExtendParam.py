#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class TuitionOrderExtendParam(object):

    def __init__(self):
        self._returnback_url = None

    @property
    def returnback_url(self):
        return self._returnback_url

    @returnback_url.setter
    def returnback_url(self, value):
        self._returnback_url = value


    def to_alipay_dict(self):
        params = dict()
        if self.returnback_url:
            if hasattr(self.returnback_url, 'to_alipay_dict'):
                params['returnback_url'] = self.returnback_url.to_alipay_dict()
            else:
                params['returnback_url'] = self.returnback_url
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = TuitionOrderExtendParam()
        if 'returnback_url' in d:
            o.returnback_url = d['returnback_url']
        return o


