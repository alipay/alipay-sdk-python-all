#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayInsAutoAutoinsprodPolicyCancelModel(object):

    def __init__(self):
        self._trade_biz_id = None

    @property
    def trade_biz_id(self):
        return self._trade_biz_id

    @trade_biz_id.setter
    def trade_biz_id(self, value):
        self._trade_biz_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.trade_biz_id:
            if hasattr(self.trade_biz_id, 'to_alipay_dict'):
                params['trade_biz_id'] = self.trade_biz_id.to_alipay_dict()
            else:
                params['trade_biz_id'] = self.trade_biz_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayInsAutoAutoinsprodPolicyCancelModel()
        if 'trade_biz_id' in d:
            o.trade_biz_id = d['trade_biz_id']
        return o


