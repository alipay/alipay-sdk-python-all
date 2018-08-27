#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayMarketingCdpAdvertiseCreateModel(object):

    def __init__(self):
        self._action_url = None
        self._ad_code = None
        self._ad_rules = None
        self._content = None
        self._content_type = None
        self._end_time = None
        self._height = None
        self._start_time = None

    @property
    def action_url(self):
        return self._action_url

    @action_url.setter
    def action_url(self, value):
        self._action_url = value
    @property
    def ad_code(self):
        return self._ad_code

    @ad_code.setter
    def ad_code(self, value):
        self._ad_code = value
    @property
    def ad_rules(self):
        return self._ad_rules

    @ad_rules.setter
    def ad_rules(self, value):
        self._ad_rules = value
    @property
    def content(self):
        return self._content

    @content.setter
    def content(self, value):
        self._content = value
    @property
    def content_type(self):
        return self._content_type

    @content_type.setter
    def content_type(self, value):
        self._content_type = value
    @property
    def end_time(self):
        return self._end_time

    @end_time.setter
    def end_time(self, value):
        self._end_time = value
    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        self._height = value
    @property
    def start_time(self):
        return self._start_time

    @start_time.setter
    def start_time(self, value):
        self._start_time = value


    def to_alipay_dict(self):
        params = dict()
        if self.action_url:
            if hasattr(self.action_url, 'to_alipay_dict'):
                params['action_url'] = self.action_url.to_alipay_dict()
            else:
                params['action_url'] = self.action_url
        if self.ad_code:
            if hasattr(self.ad_code, 'to_alipay_dict'):
                params['ad_code'] = self.ad_code.to_alipay_dict()
            else:
                params['ad_code'] = self.ad_code
        if self.ad_rules:
            if hasattr(self.ad_rules, 'to_alipay_dict'):
                params['ad_rules'] = self.ad_rules.to_alipay_dict()
            else:
                params['ad_rules'] = self.ad_rules
        if self.content:
            if hasattr(self.content, 'to_alipay_dict'):
                params['content'] = self.content.to_alipay_dict()
            else:
                params['content'] = self.content
        if self.content_type:
            if hasattr(self.content_type, 'to_alipay_dict'):
                params['content_type'] = self.content_type.to_alipay_dict()
            else:
                params['content_type'] = self.content_type
        if self.end_time:
            if hasattr(self.end_time, 'to_alipay_dict'):
                params['end_time'] = self.end_time.to_alipay_dict()
            else:
                params['end_time'] = self.end_time
        if self.height:
            if hasattr(self.height, 'to_alipay_dict'):
                params['height'] = self.height.to_alipay_dict()
            else:
                params['height'] = self.height
        if self.start_time:
            if hasattr(self.start_time, 'to_alipay_dict'):
                params['start_time'] = self.start_time.to_alipay_dict()
            else:
                params['start_time'] = self.start_time
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayMarketingCdpAdvertiseCreateModel()
        if 'action_url' in d:
            o.action_url = d['action_url']
        if 'ad_code' in d:
            o.ad_code = d['ad_code']
        if 'ad_rules' in d:
            o.ad_rules = d['ad_rules']
        if 'content' in d:
            o.content = d['content']
        if 'content_type' in d:
            o.content_type = d['content_type']
        if 'end_time' in d:
            o.end_time = d['end_time']
        if 'height' in d:
            o.height = d['height']
        if 'start_time' in d:
            o.start_time = d['start_time']
        return o


