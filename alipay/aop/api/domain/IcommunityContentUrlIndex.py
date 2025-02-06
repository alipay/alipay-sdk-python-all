#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class IcommunityContentUrlIndex(object):

    def __init__(self):
        self._content_link_url = None
        self._content_link_url_name = None
        self._url_end_index = None
        self._url_start_index = None

    @property
    def content_link_url(self):
        return self._content_link_url

    @content_link_url.setter
    def content_link_url(self, value):
        self._content_link_url = value
    @property
    def content_link_url_name(self):
        return self._content_link_url_name

    @content_link_url_name.setter
    def content_link_url_name(self, value):
        self._content_link_url_name = value
    @property
    def url_end_index(self):
        return self._url_end_index

    @url_end_index.setter
    def url_end_index(self, value):
        self._url_end_index = value
    @property
    def url_start_index(self):
        return self._url_start_index

    @url_start_index.setter
    def url_start_index(self, value):
        self._url_start_index = value


    def to_alipay_dict(self):
        params = dict()
        if self.content_link_url:
            if hasattr(self.content_link_url, 'to_alipay_dict'):
                params['content_link_url'] = self.content_link_url.to_alipay_dict()
            else:
                params['content_link_url'] = self.content_link_url
        if self.content_link_url_name:
            if hasattr(self.content_link_url_name, 'to_alipay_dict'):
                params['content_link_url_name'] = self.content_link_url_name.to_alipay_dict()
            else:
                params['content_link_url_name'] = self.content_link_url_name
        if self.url_end_index:
            if hasattr(self.url_end_index, 'to_alipay_dict'):
                params['url_end_index'] = self.url_end_index.to_alipay_dict()
            else:
                params['url_end_index'] = self.url_end_index
        if self.url_start_index:
            if hasattr(self.url_start_index, 'to_alipay_dict'):
                params['url_start_index'] = self.url_start_index.to_alipay_dict()
            else:
                params['url_start_index'] = self.url_start_index
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = IcommunityContentUrlIndex()
        if 'content_link_url' in d:
            o.content_link_url = d['content_link_url']
        if 'content_link_url_name' in d:
            o.content_link_url_name = d['content_link_url_name']
        if 'url_end_index' in d:
            o.url_end_index = d['url_end_index']
        if 'url_start_index' in d:
            o.url_start_index = d['url_start_index']
        return o


