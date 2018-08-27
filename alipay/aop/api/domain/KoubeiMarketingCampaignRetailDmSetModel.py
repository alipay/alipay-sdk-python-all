#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class KoubeiMarketingCampaignRetailDmSetModel(object):

    def __init__(self):
        self._campaign_end_time = None
        self._content_id = None
        self._operate_type = None

    @property
    def campaign_end_time(self):
        return self._campaign_end_time

    @campaign_end_time.setter
    def campaign_end_time(self, value):
        self._campaign_end_time = value
    @property
    def content_id(self):
        return self._content_id

    @content_id.setter
    def content_id(self, value):
        self._content_id = value
    @property
    def operate_type(self):
        return self._operate_type

    @operate_type.setter
    def operate_type(self, value):
        self._operate_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.campaign_end_time:
            if hasattr(self.campaign_end_time, 'to_alipay_dict'):
                params['campaign_end_time'] = self.campaign_end_time.to_alipay_dict()
            else:
                params['campaign_end_time'] = self.campaign_end_time
        if self.content_id:
            if hasattr(self.content_id, 'to_alipay_dict'):
                params['content_id'] = self.content_id.to_alipay_dict()
            else:
                params['content_id'] = self.content_id
        if self.operate_type:
            if hasattr(self.operate_type, 'to_alipay_dict'):
                params['operate_type'] = self.operate_type.to_alipay_dict()
            else:
                params['operate_type'] = self.operate_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = KoubeiMarketingCampaignRetailDmSetModel()
        if 'campaign_end_time' in d:
            o.campaign_end_time = d['campaign_end_time']
        if 'content_id' in d:
            o.content_id = d['content_id']
        if 'operate_type' in d:
            o.operate_type = d['operate_type']
        return o


