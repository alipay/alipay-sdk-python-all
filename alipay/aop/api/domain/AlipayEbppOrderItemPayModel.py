#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayEbppOrderItemPayModel(object):

    def __init__(self):
        self._alipay_item_id = None

    @property
    def alipay_item_id(self):
        return self._alipay_item_id

    @alipay_item_id.setter
    def alipay_item_id(self, value):
        self._alipay_item_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.alipay_item_id:
            if hasattr(self.alipay_item_id, 'to_alipay_dict'):
                params['alipay_item_id'] = self.alipay_item_id.to_alipay_dict()
            else:
                params['alipay_item_id'] = self.alipay_item_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayEbppOrderItemPayModel()
        if 'alipay_item_id' in d:
            o.alipay_item_id = d['alipay_item_id']
        return o


