#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class OverseasExtendParams(object):

    def __init__(self):
        self._goods_detail = None

    @property
    def goods_detail(self):
        return self._goods_detail

    @goods_detail.setter
    def goods_detail(self, value):
        self._goods_detail = value


    def to_alipay_dict(self):
        params = dict()
        if self.goods_detail:
            if hasattr(self.goods_detail, 'to_alipay_dict'):
                params['goods_detail'] = self.goods_detail.to_alipay_dict()
            else:
                params['goods_detail'] = self.goods_detail
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = OverseasExtendParams()
        if 'goods_detail' in d:
            o.goods_detail = d['goods_detail']
        return o


