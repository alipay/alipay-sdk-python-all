#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayAlipayAmaQueryModel(object):

    def __init__(self):
        self._biz = None
        self._image = None
        self._open_id = None
        self._query = None
        self._query_id = None
        self._session_id = None
        self._user_id = None

    @property
    def biz(self):
        return self._biz

    @biz.setter
    def biz(self, value):
        self._biz = value
    @property
    def image(self):
        return self._image

    @image.setter
    def image(self, value):
        self._image = value
    @property
    def open_id(self):
        return self._open_id

    @open_id.setter
    def open_id(self, value):
        self._open_id = value
    @property
    def query(self):
        return self._query

    @query.setter
    def query(self, value):
        self._query = value
    @property
    def query_id(self):
        return self._query_id

    @query_id.setter
    def query_id(self, value):
        self._query_id = value
    @property
    def session_id(self):
        return self._session_id

    @session_id.setter
    def session_id(self, value):
        self._session_id = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.biz:
            if hasattr(self.biz, 'to_alipay_dict'):
                params['biz'] = self.biz.to_alipay_dict()
            else:
                params['biz'] = self.biz
        if self.image:
            if hasattr(self.image, 'to_alipay_dict'):
                params['image'] = self.image.to_alipay_dict()
            else:
                params['image'] = self.image
        if self.open_id:
            if hasattr(self.open_id, 'to_alipay_dict'):
                params['open_id'] = self.open_id.to_alipay_dict()
            else:
                params['open_id'] = self.open_id
        if self.query:
            if hasattr(self.query, 'to_alipay_dict'):
                params['query'] = self.query.to_alipay_dict()
            else:
                params['query'] = self.query
        if self.query_id:
            if hasattr(self.query_id, 'to_alipay_dict'):
                params['query_id'] = self.query_id.to_alipay_dict()
            else:
                params['query_id'] = self.query_id
        if self.session_id:
            if hasattr(self.session_id, 'to_alipay_dict'):
                params['session_id'] = self.session_id.to_alipay_dict()
            else:
                params['session_id'] = self.session_id
        if self.user_id:
            if hasattr(self.user_id, 'to_alipay_dict'):
                params['user_id'] = self.user_id.to_alipay_dict()
            else:
                params['user_id'] = self.user_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayAlipayAmaQueryModel()
        if 'biz' in d:
            o.biz = d['biz']
        if 'image' in d:
            o.image = d['image']
        if 'open_id' in d:
            o.open_id = d['open_id']
        if 'query' in d:
            o.query = d['query']
        if 'query_id' in d:
            o.query_id = d['query_id']
        if 'session_id' in d:
            o.session_id = d['session_id']
        if 'user_id' in d:
            o.user_id = d['user_id']
        return o


