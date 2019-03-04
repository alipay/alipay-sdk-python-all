#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayEbppOrderItemQueryModel(object):

    def __init__(self):
        self._inst_item_id = None

    @property
    def inst_item_id(self):
        return self._inst_item_id

    @inst_item_id.setter
    def inst_item_id(self, value):
        self._inst_item_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.inst_item_id:
            if hasattr(self.inst_item_id, 'to_alipay_dict'):
                params['inst_item_id'] = self.inst_item_id.to_alipay_dict()
            else:
                params['inst_item_id'] = self.inst_item_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayEbppOrderItemQueryModel()
        if 'inst_item_id' in d:
            o.inst_item_id = d['inst_item_id']
        return o


