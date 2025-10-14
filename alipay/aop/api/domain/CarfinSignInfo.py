#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.CarfinKeyWord import CarfinKeyWord
from alipay.aop.api.domain.CarfinKeyWord import CarfinKeyWord


class CarfinSignInfo(object):

    def __init__(self):
        self._sign_keyword = None
        self._signer = None
        self._time_keyword = None

    @property
    def sign_keyword(self):
        return self._sign_keyword

    @sign_keyword.setter
    def sign_keyword(self, value):
        if isinstance(value, CarfinKeyWord):
            self._sign_keyword = value
        else:
            self._sign_keyword = CarfinKeyWord.from_alipay_dict(value)
    @property
    def signer(self):
        return self._signer

    @signer.setter
    def signer(self, value):
        self._signer = value
    @property
    def time_keyword(self):
        return self._time_keyword

    @time_keyword.setter
    def time_keyword(self, value):
        if isinstance(value, CarfinKeyWord):
            self._time_keyword = value
        else:
            self._time_keyword = CarfinKeyWord.from_alipay_dict(value)


    def to_alipay_dict(self):
        params = dict()
        if self.sign_keyword:
            if hasattr(self.sign_keyword, 'to_alipay_dict'):
                params['sign_keyword'] = self.sign_keyword.to_alipay_dict()
            else:
                params['sign_keyword'] = self.sign_keyword
        if self.signer:
            if hasattr(self.signer, 'to_alipay_dict'):
                params['signer'] = self.signer.to_alipay_dict()
            else:
                params['signer'] = self.signer
        if self.time_keyword:
            if hasattr(self.time_keyword, 'to_alipay_dict'):
                params['time_keyword'] = self.time_keyword.to_alipay_dict()
            else:
                params['time_keyword'] = self.time_keyword
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = CarfinSignInfo()
        if 'sign_keyword' in d:
            o.sign_keyword = d['sign_keyword']
        if 'signer' in d:
            o.signer = d['signer']
        if 'time_keyword' in d:
            o.time_keyword = d['time_keyword']
        return o


