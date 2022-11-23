#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class WidgetActivityInfo(object):

    def __init__(self):
        self._activity_click_url = None
        self._activity_id = None
        self._activity_name = None
        self._activity_picture_urls = None

    @property
    def activity_click_url(self):
        return self._activity_click_url

    @activity_click_url.setter
    def activity_click_url(self, value):
        self._activity_click_url = value
    @property
    def activity_id(self):
        return self._activity_id

    @activity_id.setter
    def activity_id(self, value):
        self._activity_id = value
    @property
    def activity_name(self):
        return self._activity_name

    @activity_name.setter
    def activity_name(self, value):
        self._activity_name = value
    @property
    def activity_picture_urls(self):
        return self._activity_picture_urls

    @activity_picture_urls.setter
    def activity_picture_urls(self, value):
        if isinstance(value, list):
            self._activity_picture_urls = list()
            for i in value:
                self._activity_picture_urls.append(i)


    def to_alipay_dict(self):
        params = dict()
        if self.activity_click_url:
            if hasattr(self.activity_click_url, 'to_alipay_dict'):
                params['activity_click_url'] = self.activity_click_url.to_alipay_dict()
            else:
                params['activity_click_url'] = self.activity_click_url
        if self.activity_id:
            if hasattr(self.activity_id, 'to_alipay_dict'):
                params['activity_id'] = self.activity_id.to_alipay_dict()
            else:
                params['activity_id'] = self.activity_id
        if self.activity_name:
            if hasattr(self.activity_name, 'to_alipay_dict'):
                params['activity_name'] = self.activity_name.to_alipay_dict()
            else:
                params['activity_name'] = self.activity_name
        if self.activity_picture_urls:
            if isinstance(self.activity_picture_urls, list):
                for i in range(0, len(self.activity_picture_urls)):
                    element = self.activity_picture_urls[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.activity_picture_urls[i] = element.to_alipay_dict()
            if hasattr(self.activity_picture_urls, 'to_alipay_dict'):
                params['activity_picture_urls'] = self.activity_picture_urls.to_alipay_dict()
            else:
                params['activity_picture_urls'] = self.activity_picture_urls
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = WidgetActivityInfo()
        if 'activity_click_url' in d:
            o.activity_click_url = d['activity_click_url']
        if 'activity_id' in d:
            o.activity_id = d['activity_id']
        if 'activity_name' in d:
            o.activity_name = d['activity_name']
        if 'activity_picture_urls' in d:
            o.activity_picture_urls = d['activity_picture_urls']
        return o


