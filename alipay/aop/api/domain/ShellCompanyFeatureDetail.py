#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ShellCompanyFeatureDetail(object):

    def __init__(self):
        self._content = None
        self._main_title = None
        self._sub_title = None
        self._update_time = None

    @property
    def content(self):
        return self._content

    @content.setter
    def content(self, value):
        self._content = value
    @property
    def main_title(self):
        return self._main_title

    @main_title.setter
    def main_title(self, value):
        self._main_title = value
    @property
    def sub_title(self):
        return self._sub_title

    @sub_title.setter
    def sub_title(self, value):
        self._sub_title = value
    @property
    def update_time(self):
        return self._update_time

    @update_time.setter
    def update_time(self, value):
        self._update_time = value


    def to_alipay_dict(self):
        params = dict()
        if self.content:
            if hasattr(self.content, 'to_alipay_dict'):
                params['content'] = self.content.to_alipay_dict()
            else:
                params['content'] = self.content
        if self.main_title:
            if hasattr(self.main_title, 'to_alipay_dict'):
                params['main_title'] = self.main_title.to_alipay_dict()
            else:
                params['main_title'] = self.main_title
        if self.sub_title:
            if hasattr(self.sub_title, 'to_alipay_dict'):
                params['sub_title'] = self.sub_title.to_alipay_dict()
            else:
                params['sub_title'] = self.sub_title
        if self.update_time:
            if hasattr(self.update_time, 'to_alipay_dict'):
                params['update_time'] = self.update_time.to_alipay_dict()
            else:
                params['update_time'] = self.update_time
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ShellCompanyFeatureDetail()
        if 'content' in d:
            o.content = d['content']
        if 'main_title' in d:
            o.main_title = d['main_title']
        if 'sub_title' in d:
            o.sub_title = d['sub_title']
        if 'update_time' in d:
            o.update_time = d['update_time']
        return o


