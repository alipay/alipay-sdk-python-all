#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceLogisticsActivityAccessConsultModel(object):

    def __init__(self):
        self._activity_key = None
        self._alipay_open_id = None
        self._alipay_user_id = None

    @property
    def activity_key(self):
        return self._activity_key

    @activity_key.setter
    def activity_key(self, value):
        self._activity_key = value
    @property
    def alipay_open_id(self):
        return self._alipay_open_id

    @alipay_open_id.setter
    def alipay_open_id(self, value):
        self._alipay_open_id = value
    @property
    def alipay_user_id(self):
        return self._alipay_user_id

    @alipay_user_id.setter
    def alipay_user_id(self, value):
        self._alipay_user_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.activity_key:
            if hasattr(self.activity_key, 'to_alipay_dict'):
                params['activity_key'] = self.activity_key.to_alipay_dict()
            else:
                params['activity_key'] = self.activity_key
        if self.alipay_open_id:
            if hasattr(self.alipay_open_id, 'to_alipay_dict'):
                params['alipay_open_id'] = self.alipay_open_id.to_alipay_dict()
            else:
                params['alipay_open_id'] = self.alipay_open_id
        if self.alipay_user_id:
            if hasattr(self.alipay_user_id, 'to_alipay_dict'):
                params['alipay_user_id'] = self.alipay_user_id.to_alipay_dict()
            else:
                params['alipay_user_id'] = self.alipay_user_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceLogisticsActivityAccessConsultModel()
        if 'activity_key' in d:
            o.activity_key = d['activity_key']
        if 'alipay_open_id' in d:
            o.alipay_open_id = d['alipay_open_id']
        if 'alipay_user_id' in d:
            o.alipay_user_id = d['alipay_user_id']
        return o


