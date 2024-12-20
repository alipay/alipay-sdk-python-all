#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class LearnCenterContentInfo(object):

    def __init__(self):
        self._code = None
        self._description = None
        self._mobile_url = None
        self._pc_url = None
        self._publish_time = None
        self._title = None

    @property
    def code(self):
        return self._code

    @code.setter
    def code(self, value):
        self._code = value
    @property
    def description(self):
        return self._description

    @description.setter
    def description(self, value):
        self._description = value
    @property
    def mobile_url(self):
        return self._mobile_url

    @mobile_url.setter
    def mobile_url(self, value):
        self._mobile_url = value
    @property
    def pc_url(self):
        return self._pc_url

    @pc_url.setter
    def pc_url(self, value):
        self._pc_url = value
    @property
    def publish_time(self):
        return self._publish_time

    @publish_time.setter
    def publish_time(self, value):
        self._publish_time = value
    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        self._title = value


    def to_alipay_dict(self):
        params = dict()
        if self.code:
            if hasattr(self.code, 'to_alipay_dict'):
                params['code'] = self.code.to_alipay_dict()
            else:
                params['code'] = self.code
        if self.description:
            if hasattr(self.description, 'to_alipay_dict'):
                params['description'] = self.description.to_alipay_dict()
            else:
                params['description'] = self.description
        if self.mobile_url:
            if hasattr(self.mobile_url, 'to_alipay_dict'):
                params['mobile_url'] = self.mobile_url.to_alipay_dict()
            else:
                params['mobile_url'] = self.mobile_url
        if self.pc_url:
            if hasattr(self.pc_url, 'to_alipay_dict'):
                params['pc_url'] = self.pc_url.to_alipay_dict()
            else:
                params['pc_url'] = self.pc_url
        if self.publish_time:
            if hasattr(self.publish_time, 'to_alipay_dict'):
                params['publish_time'] = self.publish_time.to_alipay_dict()
            else:
                params['publish_time'] = self.publish_time
        if self.title:
            if hasattr(self.title, 'to_alipay_dict'):
                params['title'] = self.title.to_alipay_dict()
            else:
                params['title'] = self.title
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = LearnCenterContentInfo()
        if 'code' in d:
            o.code = d['code']
        if 'description' in d:
            o.description = d['description']
        if 'mobile_url' in d:
            o.mobile_url = d['mobile_url']
        if 'pc_url' in d:
            o.pc_url = d['pc_url']
        if 'publish_time' in d:
            o.publish_time = d['publish_time']
        if 'title' in d:
            o.title = d['title']
        return o


