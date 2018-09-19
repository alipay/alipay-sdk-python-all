#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class KoubeiMarketingAdvertisingModifyModel(object):

    def __init__(self):
        self._action_url = None
        self._ad_id = None
        self._content = None
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
    def ad_id(self):
        return self._ad_id

    @ad_id.setter
    def ad_id(self, value):
        self._ad_id = value
    @property
    def content(self):
        return self._content

    @content.setter
    def content(self, value):
        self._content = value
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
        if self.ad_id:
            if hasattr(self.ad_id, 'to_alipay_dict'):
                params['ad_id'] = self.ad_id.to_alipay_dict()
            else:
                params['ad_id'] = self.ad_id
        if self.content:
            if hasattr(self.content, 'to_alipay_dict'):
                params['content'] = self.content.to_alipay_dict()
            else:
                params['content'] = self.content
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
        o = KoubeiMarketingAdvertisingModifyModel()
        if 'action_url' in d:
            o.action_url = d['action_url']
        if 'ad_id' in d:
            o.ad_id = d['ad_id']
        if 'content' in d:
            o.content = d['content']
        if 'end_time' in d:
            o.end_time = d['end_time']
        if 'height' in d:
            o.height = d['height']
        if 'start_time' in d:
            o.start_time = d['start_time']
        return o


