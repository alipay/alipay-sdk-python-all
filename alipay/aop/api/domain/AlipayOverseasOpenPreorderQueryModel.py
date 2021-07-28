#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayOverseasOpenPreorderQueryModel(object):

    def __init__(self):
        self._pre_order_id = None

    @property
    def pre_order_id(self):
        return self._pre_order_id

    @pre_order_id.setter
    def pre_order_id(self, value):
        self._pre_order_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.pre_order_id:
            if hasattr(self.pre_order_id, 'to_alipay_dict'):
                params['pre_order_id'] = self.pre_order_id.to_alipay_dict()
            else:
                params['pre_order_id'] = self.pre_order_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayOverseasOpenPreorderQueryModel()
        if 'pre_order_id' in d:
            o.pre_order_id = d['pre_order_id']
        return o


