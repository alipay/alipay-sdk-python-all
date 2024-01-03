#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class RentCarCancelRule(object):

    def __init__(self):
        self._content = None
        self._free_cancel = None
        self._title = None

    @property
    def content(self):
        return self._content

    @content.setter
    def content(self, value):
        self._content = value
    @property
    def free_cancel(self):
        return self._free_cancel

    @free_cancel.setter
    def free_cancel(self, value):
        self._free_cancel = value
    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        self._title = value


    def to_alipay_dict(self):
        params = dict()
        if self.content:
            if hasattr(self.content, 'to_alipay_dict'):
                params['content'] = self.content.to_alipay_dict()
            else:
                params['content'] = self.content
        if self.free_cancel:
            if hasattr(self.free_cancel, 'to_alipay_dict'):
                params['free_cancel'] = self.free_cancel.to_alipay_dict()
            else:
                params['free_cancel'] = self.free_cancel
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
        o = RentCarCancelRule()
        if 'content' in d:
            o.content = d['content']
        if 'free_cancel' in d:
            o.free_cancel = d['free_cancel']
        if 'title' in d:
            o.title = d['title']
        return o


