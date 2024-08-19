#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class QuestionInfo(object):

    def __init__(self):
        self._group_name = None
        self._hits = None
        self._id = None
        self._library_id = None
        self._title = None

    @property
    def group_name(self):
        return self._group_name

    @group_name.setter
    def group_name(self, value):
        self._group_name = value
    @property
    def hits(self):
        return self._hits

    @hits.setter
    def hits(self, value):
        self._hits = value
    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        self._id = value
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
        if self.group_name:
            if hasattr(self.group_name, 'to_alipay_dict'):
                params['group_name'] = self.group_name.to_alipay_dict()
            else:
                params['group_name'] = self.group_name
        if self.hits:
            if hasattr(self.hits, 'to_alipay_dict'):
                params['hits'] = self.hits.to_alipay_dict()
            else:
                params['hits'] = self.hits
        if self.id:
            if hasattr(self.id, 'to_alipay_dict'):
                params['id'] = self.id.to_alipay_dict()
            else:
                params['id'] = self.id
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
        o = QuestionInfo()
        if 'group_name' in d:
            o.group_name = d['group_name']
        if 'hits' in d:
            o.hits = d['hits']
        if 'id' in d:
            o.id = d['id']
        if 'library_id' in d:
            o.library_id = d['library_id']
        if 'title' in d:
            o.title = d['title']
        return o


