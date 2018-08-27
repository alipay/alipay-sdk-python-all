#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayInsAutoUserPointQueryModel(object):

    def __init__(self):
        self._auto_campaign_type = None
        self._user_id = None

    @property
    def auto_campaign_type(self):
        return self._auto_campaign_type

    @auto_campaign_type.setter
    def auto_campaign_type(self, value):
        self._auto_campaign_type = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.auto_campaign_type:
            if hasattr(self.auto_campaign_type, 'to_alipay_dict'):
                params['auto_campaign_type'] = self.auto_campaign_type.to_alipay_dict()
            else:
                params['auto_campaign_type'] = self.auto_campaign_type
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
        o = AlipayInsAutoUserPointQueryModel()
        if 'auto_campaign_type' in d:
            o.auto_campaign_type = d['auto_campaign_type']
        if 'user_id' in d:
            o.user_id = d['user_id']
        return o


