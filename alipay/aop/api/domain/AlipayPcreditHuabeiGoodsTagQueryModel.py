#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayPcreditHuabeiGoodsTagQueryModel(object):

    def __init__(self):
        self._biz_src = None

    @property
    def biz_src(self):
        return self._biz_src

    @biz_src.setter
    def biz_src(self, value):
        self._biz_src = value


    def to_alipay_dict(self):
        params = dict()
        if self.biz_src:
            if hasattr(self.biz_src, 'to_alipay_dict'):
                params['biz_src'] = self.biz_src.to_alipay_dict()
            else:
                params['biz_src'] = self.biz_src
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayPcreditHuabeiGoodsTagQueryModel()
        if 'biz_src' in d:
            o.biz_src = d['biz_src']
        return o


