#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayOpenAppYufalingsanyaowubYufalingsanyaowubQueryModel(object):

    def __init__(self):
        self._yufaa = None

    @property
    def yufaa(self):
        return self._yufaa

    @yufaa.setter
    def yufaa(self, value):
        self._yufaa = value


    def to_alipay_dict(self):
        params = dict()
        if self.yufaa:
            if hasattr(self.yufaa, 'to_alipay_dict'):
                params['yufaa'] = self.yufaa.to_alipay_dict()
            else:
                params['yufaa'] = self.yufaa
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayOpenAppYufalingsanyaowubYufalingsanyaowubQueryModel()
        if 'yufaa' in d:
            o.yufaa = d['yufaa']
        return o


