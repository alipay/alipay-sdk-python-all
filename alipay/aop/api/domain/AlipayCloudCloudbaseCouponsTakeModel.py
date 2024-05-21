#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCloudCloudbaseCouponsTakeModel(object):

    def __init__(self):
        self._activity_code = None
        self._biz_app_id = None

    @property
    def activity_code(self):
        return self._activity_code

    @activity_code.setter
    def activity_code(self, value):
        self._activity_code = value
    @property
    def biz_app_id(self):
        return self._biz_app_id

    @biz_app_id.setter
    def biz_app_id(self, value):
        self._biz_app_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.activity_code:
            if hasattr(self.activity_code, 'to_alipay_dict'):
                params['activity_code'] = self.activity_code.to_alipay_dict()
            else:
                params['activity_code'] = self.activity_code
        if self.biz_app_id:
            if hasattr(self.biz_app_id, 'to_alipay_dict'):
                params['biz_app_id'] = self.biz_app_id.to_alipay_dict()
            else:
                params['biz_app_id'] = self.biz_app_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCloudCloudbaseCouponsTakeModel()
        if 'activity_code' in d:
            o.activity_code = d['activity_code']
        if 'biz_app_id' in d:
            o.biz_app_id = d['biz_app_id']
        return o


