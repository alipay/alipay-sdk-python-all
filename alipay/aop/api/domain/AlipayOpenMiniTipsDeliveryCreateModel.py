#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayOpenMiniTipsDeliveryCreateModel(object):

    def __init__(self):
        self._delivery_content = None
        self._delivery_name = None
        self._end_time = None
        self._match_type = None
        self._match_url = None
        self._start_time = None

    @property
    def delivery_content(self):
        return self._delivery_content

    @delivery_content.setter
    def delivery_content(self, value):
        self._delivery_content = value
    @property
    def delivery_name(self):
        return self._delivery_name

    @delivery_name.setter
    def delivery_name(self, value):
        self._delivery_name = value
    @property
    def end_time(self):
        return self._end_time

    @end_time.setter
    def end_time(self, value):
        self._end_time = value
    @property
    def match_type(self):
        return self._match_type

    @match_type.setter
    def match_type(self, value):
        self._match_type = value
    @property
    def match_url(self):
        return self._match_url

    @match_url.setter
    def match_url(self, value):
        self._match_url = value
    @property
    def start_time(self):
        return self._start_time

    @start_time.setter
    def start_time(self, value):
        self._start_time = value


    def to_alipay_dict(self):
        params = dict()
        if self.delivery_content:
            if hasattr(self.delivery_content, 'to_alipay_dict'):
                params['delivery_content'] = self.delivery_content.to_alipay_dict()
            else:
                params['delivery_content'] = self.delivery_content
        if self.delivery_name:
            if hasattr(self.delivery_name, 'to_alipay_dict'):
                params['delivery_name'] = self.delivery_name.to_alipay_dict()
            else:
                params['delivery_name'] = self.delivery_name
        if self.end_time:
            if hasattr(self.end_time, 'to_alipay_dict'):
                params['end_time'] = self.end_time.to_alipay_dict()
            else:
                params['end_time'] = self.end_time
        if self.match_type:
            if hasattr(self.match_type, 'to_alipay_dict'):
                params['match_type'] = self.match_type.to_alipay_dict()
            else:
                params['match_type'] = self.match_type
        if self.match_url:
            if hasattr(self.match_url, 'to_alipay_dict'):
                params['match_url'] = self.match_url.to_alipay_dict()
            else:
                params['match_url'] = self.match_url
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
        o = AlipayOpenMiniTipsDeliveryCreateModel()
        if 'delivery_content' in d:
            o.delivery_content = d['delivery_content']
        if 'delivery_name' in d:
            o.delivery_name = d['delivery_name']
        if 'end_time' in d:
            o.end_time = d['end_time']
        if 'match_type' in d:
            o.match_type = d['match_type']
        if 'match_url' in d:
            o.match_url = d['match_url']
        if 'start_time' in d:
            o.start_time = d['start_time']
        return o


