#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayInsMarketingCampaignQueryModel(object):

    def __init__(self):
        self._campaign_id = None
        self._request_id = None

    @property
    def campaign_id(self):
        return self._campaign_id

    @campaign_id.setter
    def campaign_id(self, value):
        self._campaign_id = value
    @property
    def request_id(self):
        return self._request_id

    @request_id.setter
    def request_id(self, value):
        self._request_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.campaign_id:
            if hasattr(self.campaign_id, 'to_alipay_dict'):
                params['campaign_id'] = self.campaign_id.to_alipay_dict()
            else:
                params['campaign_id'] = self.campaign_id
        if self.request_id:
            if hasattr(self.request_id, 'to_alipay_dict'):
                params['request_id'] = self.request_id.to_alipay_dict()
            else:
                params['request_id'] = self.request_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayInsMarketingCampaignQueryModel()
        if 'campaign_id' in d:
            o.campaign_id = d['campaign_id']
        if 'request_id' in d:
            o.request_id = d['request_id']
        return o


