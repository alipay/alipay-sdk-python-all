#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayMarketingCampaignCommoneventApplyModel(object):

    def __init__(self):
        self._content_json = None
        self._event = None

    @property
    def content_json(self):
        return self._content_json

    @content_json.setter
    def content_json(self, value):
        self._content_json = value
    @property
    def event(self):
        return self._event

    @event.setter
    def event(self, value):
        self._event = value


    def to_alipay_dict(self):
        params = dict()
        if self.content_json:
            if hasattr(self.content_json, 'to_alipay_dict'):
                params['content_json'] = self.content_json.to_alipay_dict()
            else:
                params['content_json'] = self.content_json
        if self.event:
            if hasattr(self.event, 'to_alipay_dict'):
                params['event'] = self.event.to_alipay_dict()
            else:
                params['event'] = self.event
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayMarketingCampaignCommoneventApplyModel()
        if 'content_json' in d:
            o.content_json = d['content_json']
        if 'event' in d:
            o.event = d['event']
        return o


