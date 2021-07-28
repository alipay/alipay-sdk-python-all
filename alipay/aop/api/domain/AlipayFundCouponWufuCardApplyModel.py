#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayFundCouponWufuCardApplyModel(object):

    def __init__(self):
        self._biz_id = None
        self._sence_code = None
        self._user_id = None

    @property
    def biz_id(self):
        return self._biz_id

    @biz_id.setter
    def biz_id(self, value):
        self._biz_id = value
    @property
    def sence_code(self):
        return self._sence_code

    @sence_code.setter
    def sence_code(self, value):
        self._sence_code = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.biz_id:
            if hasattr(self.biz_id, 'to_alipay_dict'):
                params['biz_id'] = self.biz_id.to_alipay_dict()
            else:
                params['biz_id'] = self.biz_id
        if self.sence_code:
            if hasattr(self.sence_code, 'to_alipay_dict'):
                params['sence_code'] = self.sence_code.to_alipay_dict()
            else:
                params['sence_code'] = self.sence_code
        if self.user_id:
            if hasattr(self.user_id, 'to_alipay_dict'):
                params['user_id'] = self.user_id.to_alipay_dict()
            else:
                params['user_id'] = self.user_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayFundCouponWufuCardApplyModel()
        if 'biz_id' in d:
            o.biz_id = d['biz_id']
        if 'sence_code' in d:
            o.sence_code = d['sence_code']
        if 'user_id' in d:
            o.user_id = d['user_id']
        return o


