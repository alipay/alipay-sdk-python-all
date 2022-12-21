#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayMerchantLiveChannelQueryModel(object):

    def __init__(self):
        self._secret = None

    @property
    def secret(self):
        return self._secret

    @secret.setter
    def secret(self, value):
        self._secret = value


    def to_alipay_dict(self):
        params = dict()
        if self.secret:
            if hasattr(self.secret, 'to_alipay_dict'):
                params['secret'] = self.secret.to_alipay_dict()
            else:
                params['secret'] = self.secret
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayMerchantLiveChannelQueryModel()
        if 'secret' in d:
            o.secret = d['secret']
        return o


