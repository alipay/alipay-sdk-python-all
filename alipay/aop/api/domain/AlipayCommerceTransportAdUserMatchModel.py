#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceTransportAdUserMatchModel(object):

    def __init__(self):
        self._third_user_id = None

    @property
    def third_user_id(self):
        return self._third_user_id

    @third_user_id.setter
    def third_user_id(self, value):
        self._third_user_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.third_user_id:
            if hasattr(self.third_user_id, 'to_alipay_dict'):
                params['third_user_id'] = self.third_user_id.to_alipay_dict()
            else:
                params['third_user_id'] = self.third_user_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceTransportAdUserMatchModel()
        if 'third_user_id' in d:
            o.third_user_id = d['third_user_id']
        return o


