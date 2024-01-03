#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class RecommendDetail(object):

    def __init__(self):
        self._knowledge_id = None
        self._library_id = None
        self._title = None

    @property
    def knowledge_id(self):
        return self._knowledge_id

    @knowledge_id.setter
    def knowledge_id(self, value):
        self._knowledge_id = value
    @property
    def library_id(self):
        return self._library_id

    @library_id.setter
    def library_id(self, value):
        self._library_id = value
    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        self._title = value


    def to_alipay_dict(self):
        params = dict()
        if self.knowledge_id:
            if hasattr(self.knowledge_id, 'to_alipay_dict'):
                params['knowledge_id'] = self.knowledge_id.to_alipay_dict()
            else:
                params['knowledge_id'] = self.knowledge_id
        if self.library_id:
            if hasattr(self.library_id, 'to_alipay_dict'):
                params['library_id'] = self.library_id.to_alipay_dict()
            else:
                params['library_id'] = self.library_id
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
        o = RecommendDetail()
        if 'knowledge_id' in d:
            o.knowledge_id = d['knowledge_id']
        if 'library_id' in d:
            o.library_id = d['library_id']
        if 'title' in d:
            o.title = d['title']
        return o


