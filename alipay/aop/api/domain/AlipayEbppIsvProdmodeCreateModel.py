#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayEbppIsvProdmodeCreateModel(object):

    def __init__(self):
        self._biz_data = None

    @property
    def biz_data(self):
        return self._biz_data

    @biz_data.setter
    def biz_data(self, value):
        self._biz_data = value


    def to_alipay_dict(self):
        params = dict()
        if self.biz_data:
            if hasattr(self.biz_data, 'to_alipay_dict'):
                params['biz_data'] = self.biz_data.to_alipay_dict()
            else:
                params['biz_data'] = self.biz_data
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayEbppIsvProdmodeCreateModel()
        if 'biz_data' in d:
            o.biz_data = d['biz_data']
        return o


