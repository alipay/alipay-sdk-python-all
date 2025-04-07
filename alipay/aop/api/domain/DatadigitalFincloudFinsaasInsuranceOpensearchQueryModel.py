#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class DatadigitalFincloudFinsaasInsuranceOpensearchQueryModel(object):

    def __init__(self):
        self._domain = None
        self._page_size = None
        self._query = None
        self._scene = None
        self._search_mode = None

    @property
    def domain(self):
        return self._domain

    @domain.setter
    def domain(self, value):
        self._domain = value
    @property
    def page_size(self):
        return self._page_size

    @page_size.setter
    def page_size(self, value):
        self._page_size = value
    @property
    def query(self):
        return self._query

    @query.setter
    def query(self, value):
        self._query = value
    @property
    def scene(self):
        return self._scene

    @scene.setter
    def scene(self, value):
        self._scene = value
    @property
    def search_mode(self):
        return self._search_mode

    @search_mode.setter
    def search_mode(self, value):
        self._search_mode = value


    def to_alipay_dict(self):
        params = dict()
        if self.domain:
            if hasattr(self.domain, 'to_alipay_dict'):
                params['domain'] = self.domain.to_alipay_dict()
            else:
                params['domain'] = self.domain
        if self.page_size:
            if hasattr(self.page_size, 'to_alipay_dict'):
                params['page_size'] = self.page_size.to_alipay_dict()
            else:
                params['page_size'] = self.page_size
        if self.query:
            if hasattr(self.query, 'to_alipay_dict'):
                params['query'] = self.query.to_alipay_dict()
            else:
                params['query'] = self.query
        if self.scene:
            if hasattr(self.scene, 'to_alipay_dict'):
                params['scene'] = self.scene.to_alipay_dict()
            else:
                params['scene'] = self.scene
        if self.search_mode:
            if hasattr(self.search_mode, 'to_alipay_dict'):
                params['search_mode'] = self.search_mode.to_alipay_dict()
            else:
                params['search_mode'] = self.search_mode
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = DatadigitalFincloudFinsaasInsuranceOpensearchQueryModel()
        if 'domain' in d:
            o.domain = d['domain']
        if 'page_size' in d:
            o.page_size = d['page_size']
        if 'query' in d:
            o.query = d['query']
        if 'scene' in d:
            o.scene = d['scene']
        if 'search_mode' in d:
            o.search_mode = d['search_mode']
        return o


