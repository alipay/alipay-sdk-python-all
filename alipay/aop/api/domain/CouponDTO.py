#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class CouponDTO(object):

    def __init__(self):
        self._prize_instance_id = None

    @property
    def prize_instance_id(self):
        return self._prize_instance_id

    @prize_instance_id.setter
    def prize_instance_id(self, value):
        self._prize_instance_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.prize_instance_id:
            if hasattr(self.prize_instance_id, 'to_alipay_dict'):
                params['prize_instance_id'] = self.prize_instance_id.to_alipay_dict()
            else:
                params['prize_instance_id'] = self.prize_instance_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = CouponDTO()
        if 'prize_instance_id' in d:
            o.prize_instance_id = d['prize_instance_id']
        return o


