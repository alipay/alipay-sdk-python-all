#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class PromoActActivity(object):

    def __init__(self):
        self._action_type = None
        self._promo_activity_id = None

    @property
    def action_type(self):
        return self._action_type

    @action_type.setter
    def action_type(self, value):
        self._action_type = value
    @property
    def promo_activity_id(self):
        return self._promo_activity_id

    @promo_activity_id.setter
    def promo_activity_id(self, value):
        self._promo_activity_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.action_type:
            if hasattr(self.action_type, 'to_alipay_dict'):
                params['action_type'] = self.action_type.to_alipay_dict()
            else:
                params['action_type'] = self.action_type
        if self.promo_activity_id:
            if hasattr(self.promo_activity_id, 'to_alipay_dict'):
                params['promo_activity_id'] = self.promo_activity_id.to_alipay_dict()
            else:
                params['promo_activity_id'] = self.promo_activity_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = PromoActActivity()
        if 'action_type' in d:
            o.action_type = d['action_type']
        if 'promo_activity_id' in d:
            o.promo_activity_id = d['promo_activity_id']
        return o


