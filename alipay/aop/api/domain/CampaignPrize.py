#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class CampaignPrize(object):

    def __init__(self):
        self._campaign_channel = None
        self._campaign_channel_code = None
        self._campaign_id = None
        self._idea_content = None
        self._idea_type = None
        self._link = None
        self._max_amount = None
        self._min_amount = None
        self._threshold = None

    @property
    def campaign_channel(self):
        return self._campaign_channel

    @campaign_channel.setter
    def campaign_channel(self, value):
        self._campaign_channel = value
    @property
    def campaign_channel_code(self):
        return self._campaign_channel_code

    @campaign_channel_code.setter
    def campaign_channel_code(self, value):
        self._campaign_channel_code = value
    @property
    def campaign_id(self):
        return self._campaign_id

    @campaign_id.setter
    def campaign_id(self, value):
        self._campaign_id = value
    @property
    def idea_content(self):
        return self._idea_content

    @idea_content.setter
    def idea_content(self, value):
        self._idea_content = value
    @property
    def idea_type(self):
        return self._idea_type

    @idea_type.setter
    def idea_type(self, value):
        self._idea_type = value
    @property
    def link(self):
        return self._link

    @link.setter
    def link(self, value):
        self._link = value
    @property
    def max_amount(self):
        return self._max_amount

    @max_amount.setter
    def max_amount(self, value):
        self._max_amount = value
    @property
    def min_amount(self):
        return self._min_amount

    @min_amount.setter
    def min_amount(self, value):
        self._min_amount = value
    @property
    def threshold(self):
        return self._threshold

    @threshold.setter
    def threshold(self, value):
        self._threshold = value


    def to_alipay_dict(self):
        params = dict()
        if self.campaign_channel:
            if hasattr(self.campaign_channel, 'to_alipay_dict'):
                params['campaign_channel'] = self.campaign_channel.to_alipay_dict()
            else:
                params['campaign_channel'] = self.campaign_channel
        if self.campaign_channel_code:
            if hasattr(self.campaign_channel_code, 'to_alipay_dict'):
                params['campaign_channel_code'] = self.campaign_channel_code.to_alipay_dict()
            else:
                params['campaign_channel_code'] = self.campaign_channel_code
        if self.campaign_id:
            if hasattr(self.campaign_id, 'to_alipay_dict'):
                params['campaign_id'] = self.campaign_id.to_alipay_dict()
            else:
                params['campaign_id'] = self.campaign_id
        if self.idea_content:
            if hasattr(self.idea_content, 'to_alipay_dict'):
                params['idea_content'] = self.idea_content.to_alipay_dict()
            else:
                params['idea_content'] = self.idea_content
        if self.idea_type:
            if hasattr(self.idea_type, 'to_alipay_dict'):
                params['idea_type'] = self.idea_type.to_alipay_dict()
            else:
                params['idea_type'] = self.idea_type
        if self.link:
            if hasattr(self.link, 'to_alipay_dict'):
                params['link'] = self.link.to_alipay_dict()
            else:
                params['link'] = self.link
        if self.max_amount:
            if hasattr(self.max_amount, 'to_alipay_dict'):
                params['max_amount'] = self.max_amount.to_alipay_dict()
            else:
                params['max_amount'] = self.max_amount
        if self.min_amount:
            if hasattr(self.min_amount, 'to_alipay_dict'):
                params['min_amount'] = self.min_amount.to_alipay_dict()
            else:
                params['min_amount'] = self.min_amount
        if self.threshold:
            if hasattr(self.threshold, 'to_alipay_dict'):
                params['threshold'] = self.threshold.to_alipay_dict()
            else:
                params['threshold'] = self.threshold
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = CampaignPrize()
        if 'campaign_channel' in d:
            o.campaign_channel = d['campaign_channel']
        if 'campaign_channel_code' in d:
            o.campaign_channel_code = d['campaign_channel_code']
        if 'campaign_id' in d:
            o.campaign_id = d['campaign_id']
        if 'idea_content' in d:
            o.idea_content = d['idea_content']
        if 'idea_type' in d:
            o.idea_type = d['idea_type']
        if 'link' in d:
            o.link = d['link']
        if 'max_amount' in d:
            o.max_amount = d['max_amount']
        if 'min_amount' in d:
            o.min_amount = d['min_amount']
        if 'threshold' in d:
            o.threshold = d['threshold']
        return o


