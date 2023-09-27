#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class OpenCertifyMerchantConfigs(object):

    def __init__(self):
        self._face_reserve_strategy = None
        self._return_url = None

    @property
    def face_reserve_strategy(self):
        return self._face_reserve_strategy

    @face_reserve_strategy.setter
    def face_reserve_strategy(self, value):
        self._face_reserve_strategy = value
    @property
    def return_url(self):
        return self._return_url

    @return_url.setter
    def return_url(self, value):
        self._return_url = value


    def to_alipay_dict(self):
        params = dict()
        if self.face_reserve_strategy:
            if hasattr(self.face_reserve_strategy, 'to_alipay_dict'):
                params['face_reserve_strategy'] = self.face_reserve_strategy.to_alipay_dict()
            else:
                params['face_reserve_strategy'] = self.face_reserve_strategy
        if self.return_url:
            if hasattr(self.return_url, 'to_alipay_dict'):
                params['return_url'] = self.return_url.to_alipay_dict()
            else:
                params['return_url'] = self.return_url
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = OpenCertifyMerchantConfigs()
        if 'face_reserve_strategy' in d:
            o.face_reserve_strategy = d['face_reserve_strategy']
        if 'return_url' in d:
            o.return_url = d['return_url']
        return o


