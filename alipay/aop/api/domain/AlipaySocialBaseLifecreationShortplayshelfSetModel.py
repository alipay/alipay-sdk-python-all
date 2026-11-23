#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipaySocialBaseLifecreationShortplayshelfSetModel(object):

    def __init__(self):
        self._action = None
        self._album_id = None
        self._page = None
        self._query = None

    @property
    def action(self):
        return self._action

    @action.setter
    def action(self, value):
        self._action = value
    @property
    def album_id(self):
        return self._album_id

    @album_id.setter
    def album_id(self, value):
        self._album_id = value
    @property
    def page(self):
        return self._page

    @page.setter
    def page(self, value):
        self._page = value
    @property
    def query(self):
        return self._query

    @query.setter
    def query(self, value):
        self._query = value


    def to_alipay_dict(self):
        params = dict()
        if self.action:
            if hasattr(self.action, 'to_alipay_dict'):
                params['action'] = self.action.to_alipay_dict()
            else:
                params['action'] = self.action
        if self.album_id:
            if hasattr(self.album_id, 'to_alipay_dict'):
                params['album_id'] = self.album_id.to_alipay_dict()
            else:
                params['album_id'] = self.album_id
        if self.page:
            if hasattr(self.page, 'to_alipay_dict'):
                params['page'] = self.page.to_alipay_dict()
            else:
                params['page'] = self.page
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
        o = AlipaySocialBaseLifecreationShortplayshelfSetModel()
        if 'action' in d:
            o.action = d['action']
        if 'album_id' in d:
            o.album_id = d['album_id']
        if 'page' in d:
            o.page = d['page']
        if 'query' in d:
            o.query = d['query']
        return o


