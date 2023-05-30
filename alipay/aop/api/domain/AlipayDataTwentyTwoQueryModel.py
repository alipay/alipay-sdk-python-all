#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayDataTwentyTwoQueryModel(object):

    def __init__(self):
        self._body = None
        self._body_a = None
        self._id = None
        self._id_open_id = None
        self._path = None
        self._query = None

    @property
    def body(self):
        return self._body

    @body.setter
    def body(self, value):
        self._body = value
    @property
    def body_a(self):
        return self._body_a

    @body_a.setter
    def body_a(self, value):
        self._body_a = value
    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        self._id = value
    @property
    def id_open_id(self):
        return self._id_open_id

    @id_open_id.setter
    def id_open_id(self, value):
        self._id_open_id = value
    @property
    def path(self):
        return self._path

    @path.setter
    def path(self, value):
        self._path = value
    @property
    def query(self):
        return self._query

    @query.setter
    def query(self, value):
        self._query = value


    def to_alipay_dict(self):
        params = dict()
        if self.body:
            if hasattr(self.body, 'to_alipay_dict'):
                params['body'] = self.body.to_alipay_dict()
            else:
                params['body'] = self.body
        if self.body_a:
            if hasattr(self.body_a, 'to_alipay_dict'):
                params['body_a'] = self.body_a.to_alipay_dict()
            else:
                params['body_a'] = self.body_a
        if self.id:
            if hasattr(self.id, 'to_alipay_dict'):
                params['id'] = self.id.to_alipay_dict()
            else:
                params['id'] = self.id
        if self.id_open_id:
            if hasattr(self.id_open_id, 'to_alipay_dict'):
                params['id_open_id'] = self.id_open_id.to_alipay_dict()
            else:
                params['id_open_id'] = self.id_open_id
        if self.path:
            if hasattr(self.path, 'to_alipay_dict'):
                params['path'] = self.path.to_alipay_dict()
            else:
                params['path'] = self.path
        if self.query:
            if hasattr(self.query, 'to_alipay_dict'):
                params['query'] = self.query.to_alipay_dict()
            else:
                params['query'] = self.query
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayDataTwentyTwoQueryModel()
        if 'body' in d:
            o.body = d['body']
        if 'body_a' in d:
            o.body_a = d['body_a']
        if 'id' in d:
            o.id = d['id']
        if 'id_open_id' in d:
            o.id_open_id = d['id_open_id']
        if 'path' in d:
            o.path = d['path']
        if 'query' in d:
            o.query = d['query']
        return o


