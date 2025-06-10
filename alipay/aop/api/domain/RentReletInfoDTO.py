#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class RentReletInfoDTO(object):

    def __init__(self):
        self._origin_order_id = None

    @property
    def origin_order_id(self):
        return self._origin_order_id

    @origin_order_id.setter
    def origin_order_id(self, value):
        self._origin_order_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.origin_order_id:
            if hasattr(self.origin_order_id, 'to_alipay_dict'):
                params['origin_order_id'] = self.origin_order_id.to_alipay_dict()
            else:
                params['origin_order_id'] = self.origin_order_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = RentReletInfoDTO()
        if 'origin_order_id' in d:
            o.origin_order_id = d['origin_order_id']
        return o


