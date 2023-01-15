#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayMarketingActivityMessageBindModel(object):

    def __init__(self):
        self._activity_id = None
        self._merchant_id = None
        self._notify_appid = None

    @property
    def activity_id(self):
        return self._activity_id

    @activity_id.setter
    def activity_id(self, value):
        self._activity_id = value
    @property
    def merchant_id(self):
        return self._merchant_id

    @merchant_id.setter
    def merchant_id(self, value):
        self._merchant_id = value
    @property
    def notify_appid(self):
        return self._notify_appid

    @notify_appid.setter
    def notify_appid(self, value):
        self._notify_appid = value


    def to_alipay_dict(self):
        params = dict()
        if self.activity_id:
            if hasattr(self.activity_id, 'to_alipay_dict'):
                params['activity_id'] = self.activity_id.to_alipay_dict()
            else:
                params['activity_id'] = self.activity_id
        if self.merchant_id:
            if hasattr(self.merchant_id, 'to_alipay_dict'):
                params['merchant_id'] = self.merchant_id.to_alipay_dict()
            else:
                params['merchant_id'] = self.merchant_id
        if self.notify_appid:
            if hasattr(self.notify_appid, 'to_alipay_dict'):
                params['notify_appid'] = self.notify_appid.to_alipay_dict()
            else:
                params['notify_appid'] = self.notify_appid
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayMarketingActivityMessageBindModel()
        if 'activity_id' in d:
            o.activity_id = d['activity_id']
        if 'merchant_id' in d:
            o.merchant_id = d['merchant_id']
        if 'notify_appid' in d:
            o.notify_appid = d['notify_appid']
        return o


