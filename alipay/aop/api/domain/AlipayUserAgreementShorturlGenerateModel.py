#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayUserAgreementShorturlGenerateModel(object):

    def __init__(self):
        self._long_url = None

    @property
    def long_url(self):
        return self._long_url

    @long_url.setter
    def long_url(self, value):
        self._long_url = value


    def to_alipay_dict(self):
        params = dict()
        if self.long_url:
            if hasattr(self.long_url, 'to_alipay_dict'):
                params['long_url'] = self.long_url.to_alipay_dict()
            else:
                params['long_url'] = self.long_url
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayUserAgreementShorturlGenerateModel()
        if 'long_url' in d:
            o.long_url = d['long_url']
        return o


