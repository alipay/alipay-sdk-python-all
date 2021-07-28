#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayOverseasTravelRatePromotionVerifyModel(object):

    def __init__(self):
        self._extend_param = None
        self._travel_promotion_id = None
        self._user_id = None

    @property
    def extend_param(self):
        return self._extend_param

    @extend_param.setter
    def extend_param(self, value):
        self._extend_param = value
    @property
    def travel_promotion_id(self):
        return self._travel_promotion_id

    @travel_promotion_id.setter
    def travel_promotion_id(self, value):
        self._travel_promotion_id = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.extend_param:
            if hasattr(self.extend_param, 'to_alipay_dict'):
                params['extend_param'] = self.extend_param.to_alipay_dict()
            else:
                params['extend_param'] = self.extend_param
        if self.travel_promotion_id:
            if hasattr(self.travel_promotion_id, 'to_alipay_dict'):
                params['travel_promotion_id'] = self.travel_promotion_id.to_alipay_dict()
            else:
                params['travel_promotion_id'] = self.travel_promotion_id
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
        o = AlipayOverseasTravelRatePromotionVerifyModel()
        if 'extend_param' in d:
            o.extend_param = d['extend_param']
        if 'travel_promotion_id' in d:
            o.travel_promotion_id = d['travel_promotion_id']
        if 'user_id' in d:
            o.user_id = d['user_id']
        return o


