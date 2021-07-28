#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayUserDtbankcustActivityorderQueryModel(object):

    def __init__(self):
        self._activity_order_id = None

    @property
    def activity_order_id(self):
        return self._activity_order_id

    @activity_order_id.setter
    def activity_order_id(self, value):
        self._activity_order_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.activity_order_id:
            if hasattr(self.activity_order_id, 'to_alipay_dict'):
                params['activity_order_id'] = self.activity_order_id.to_alipay_dict()
            else:
                params['activity_order_id'] = self.activity_order_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayUserDtbankcustActivityorderQueryModel()
        if 'activity_order_id' in d:
            o.activity_order_id = d['activity_order_id']
        return o


