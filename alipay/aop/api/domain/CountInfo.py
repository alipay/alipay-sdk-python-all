#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class CountInfo(object):

    def __init__(self):
        self._content_id = None
        self._support_count = None
        self._total_page_view_count = None

    @property
    def content_id(self):
        return self._content_id

    @content_id.setter
    def content_id(self, value):
        self._content_id = value
    @property
    def support_count(self):
        return self._support_count

    @support_count.setter
    def support_count(self, value):
        self._support_count = value
    @property
    def total_page_view_count(self):
        return self._total_page_view_count

    @total_page_view_count.setter
    def total_page_view_count(self, value):
        self._total_page_view_count = value


    def to_alipay_dict(self):
        params = dict()
        if self.content_id:
            if hasattr(self.content_id, 'to_alipay_dict'):
                params['content_id'] = self.content_id.to_alipay_dict()
            else:
                params['content_id'] = self.content_id
        if self.support_count:
            if hasattr(self.support_count, 'to_alipay_dict'):
                params['support_count'] = self.support_count.to_alipay_dict()
            else:
                params['support_count'] = self.support_count
        if self.total_page_view_count:
            if hasattr(self.total_page_view_count, 'to_alipay_dict'):
                params['total_page_view_count'] = self.total_page_view_count.to_alipay_dict()
            else:
                params['total_page_view_count'] = self.total_page_view_count
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = CountInfo()
        if 'content_id' in d:
            o.content_id = d['content_id']
        if 'support_count' in d:
            o.support_count = d['support_count']
        if 'total_page_view_count' in d:
            o.total_page_view_count = d['total_page_view_count']
        return o


