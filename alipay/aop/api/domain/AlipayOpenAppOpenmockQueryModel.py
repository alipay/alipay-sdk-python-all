#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayOpenAppOpenmockQueryModel(object):

    def __init__(self):
        self._adfs = None
        self._xxsa = None

    @property
    def adfs(self):
        return self._adfs

    @adfs.setter
    def adfs(self, value):
        self._adfs = value
    @property
    def xxsa(self):
        return self._xxsa

    @xxsa.setter
    def xxsa(self, value):
        self._xxsa = value


    def to_alipay_dict(self):
        params = dict()
        if self.adfs:
            if hasattr(self.adfs, 'to_alipay_dict'):
                params['adfs'] = self.adfs.to_alipay_dict()
            else:
                params['adfs'] = self.adfs
        if self.xxsa:
            if hasattr(self.xxsa, 'to_alipay_dict'):
                params['xxsa'] = self.xxsa.to_alipay_dict()
            else:
                params['xxsa'] = self.xxsa
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayOpenAppOpenmockQueryModel()
        if 'adfs' in d:
            o.adfs = d['adfs']
        if 'xxsa' in d:
            o.xxsa = d['xxsa']
        return o


