#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AdSeriesAppCompilationResp(object):

    def __init__(self):
        self._compilation_id = None
        self._cover_url = None
        self._hover = None
        self._status = None
        self._title = None

    @property
    def compilation_id(self):
        return self._compilation_id

    @compilation_id.setter
    def compilation_id(self, value):
        self._compilation_id = value
    @property
    def cover_url(self):
        return self._cover_url

    @cover_url.setter
    def cover_url(self, value):
        self._cover_url = value
    @property
    def hover(self):
        return self._hover

    @hover.setter
    def hover(self, value):
        self._hover = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value
    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        self._title = value


    def to_alipay_dict(self):
        params = dict()
        if self.compilation_id:
            if hasattr(self.compilation_id, 'to_alipay_dict'):
                params['compilation_id'] = self.compilation_id.to_alipay_dict()
            else:
                params['compilation_id'] = self.compilation_id
        if self.cover_url:
            if hasattr(self.cover_url, 'to_alipay_dict'):
                params['cover_url'] = self.cover_url.to_alipay_dict()
            else:
                params['cover_url'] = self.cover_url
        if self.hover:
            if hasattr(self.hover, 'to_alipay_dict'):
                params['hover'] = self.hover.to_alipay_dict()
            else:
                params['hover'] = self.hover
        if self.status:
            if hasattr(self.status, 'to_alipay_dict'):
                params['status'] = self.status.to_alipay_dict()
            else:
                params['status'] = self.status
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
        o = AdSeriesAppCompilationResp()
        if 'compilation_id' in d:
            o.compilation_id = d['compilation_id']
        if 'cover_url' in d:
            o.cover_url = d['cover_url']
        if 'hover' in d:
            o.hover = d['hover']
        if 'status' in d:
            o.status = d['status']
        if 'title' in d:
            o.title = d['title']
        return o


