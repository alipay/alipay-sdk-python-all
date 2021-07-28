#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayOpenLotteryRegionCreateModel(object):

    def __init__(self):
        self._env = None

    @property
    def env(self):
        return self._env

    @env.setter
    def env(self, value):
        self._env = value


    def to_alipay_dict(self):
        params = dict()
        if self.env:
            if hasattr(self.env, 'to_alipay_dict'):
                params['env'] = self.env.to_alipay_dict()
            else:
                params['env'] = self.env
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayOpenLotteryRegionCreateModel()
        if 'env' in d:
            o.env = d['env']
        return o


