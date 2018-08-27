#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class KoubeiMarketingCampaignItemMerchantactivityQueryModel(object):

    def __init__(self):
        self._activity_id = None
        self._external_unique_id = None

    @property
    def activity_id(self):
        return self._activity_id

    @activity_id.setter
    def activity_id(self, value):
        self._activity_id = value
    @property
    def external_unique_id(self):
        return self._external_unique_id

    @external_unique_id.setter
    def external_unique_id(self, value):
        self._external_unique_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.activity_id:
            if hasattr(self.activity_id, 'to_alipay_dict'):
                params['activity_id'] = self.activity_id.to_alipay_dict()
            else:
                params['activity_id'] = self.activity_id
        if self.external_unique_id:
            if hasattr(self.external_unique_id, 'to_alipay_dict'):
                params['external_unique_id'] = self.external_unique_id.to_alipay_dict()
            else:
                params['external_unique_id'] = self.external_unique_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = KoubeiMarketingCampaignItemMerchantactivityQueryModel()
        if 'activity_id' in d:
            o.activity_id = d['activity_id']
        if 'external_unique_id' in d:
            o.external_unique_id = d['external_unique_id']
        return o


