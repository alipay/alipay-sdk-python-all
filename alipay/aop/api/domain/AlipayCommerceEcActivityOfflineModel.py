#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceEcActivityOfflineModel(object):

    def __init__(self):
        self._activity_id = None
        self._ant_shop_id = None

    @property
    def activity_id(self):
        return self._activity_id

    @activity_id.setter
    def activity_id(self, value):
        self._activity_id = value
    @property
    def ant_shop_id(self):
        return self._ant_shop_id

    @ant_shop_id.setter
    def ant_shop_id(self, value):
        self._ant_shop_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.activity_id:
            if hasattr(self.activity_id, 'to_alipay_dict'):
                params['activity_id'] = self.activity_id.to_alipay_dict()
            else:
                params['activity_id'] = self.activity_id
        if self.ant_shop_id:
            if hasattr(self.ant_shop_id, 'to_alipay_dict'):
                params['ant_shop_id'] = self.ant_shop_id.to_alipay_dict()
            else:
                params['ant_shop_id'] = self.ant_shop_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceEcActivityOfflineModel()
        if 'activity_id' in d:
            o.activity_id = d['activity_id']
        if 'ant_shop_id' in d:
            o.ant_shop_id = d['ant_shop_id']
        return o


