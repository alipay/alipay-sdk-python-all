#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class MultipleCampaignChannel(object):

    def __init__(self):
        self._campaign_channel = None
        self._campaign_channel_code = None

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
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = MultipleCampaignChannel()
        if 'campaign_channel' in d:
            o.campaign_channel = d['campaign_channel']
        if 'campaign_channel_code' in d:
            o.campaign_channel_code = d['campaign_channel_code']
        return o


