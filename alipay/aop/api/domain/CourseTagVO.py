#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class CourseTagVO(object):

    def __init__(self):
        self._tag_desc = None
        self._tag_key = None
        self._tag_url = None
        self._tag_value = None

    @property
    def tag_desc(self):
        return self._tag_desc

    @tag_desc.setter
    def tag_desc(self, value):
        self._tag_desc = value
    @property
    def tag_key(self):
        return self._tag_key

    @tag_key.setter
    def tag_key(self, value):
        self._tag_key = value
    @property
    def tag_url(self):
        return self._tag_url

    @tag_url.setter
    def tag_url(self, value):
        self._tag_url = value
    @property
    def tag_value(self):
        return self._tag_value

    @tag_value.setter
    def tag_value(self, value):
        self._tag_value = value


    def to_alipay_dict(self):
        params = dict()
        if self.tag_desc:
            if hasattr(self.tag_desc, 'to_alipay_dict'):
                params['tag_desc'] = self.tag_desc.to_alipay_dict()
            else:
                params['tag_desc'] = self.tag_desc
        if self.tag_key:
            if hasattr(self.tag_key, 'to_alipay_dict'):
                params['tag_key'] = self.tag_key.to_alipay_dict()
            else:
                params['tag_key'] = self.tag_key
        if self.tag_url:
            if hasattr(self.tag_url, 'to_alipay_dict'):
                params['tag_url'] = self.tag_url.to_alipay_dict()
            else:
                params['tag_url'] = self.tag_url
        if self.tag_value:
            if hasattr(self.tag_value, 'to_alipay_dict'):
                params['tag_value'] = self.tag_value.to_alipay_dict()
            else:
                params['tag_value'] = self.tag_value
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = CourseTagVO()
        if 'tag_desc' in d:
            o.tag_desc = d['tag_desc']
        if 'tag_key' in d:
            o.tag_key = d['tag_key']
        if 'tag_url' in d:
            o.tag_url = d['tag_url']
        if 'tag_value' in d:
            o.tag_value = d['tag_value']
        return o


