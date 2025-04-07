#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class DatadigitalFincloudFinsaasOpensearchQueryModel(object):

    def __init__(self):
        self._domain = None
        self._pagesize = None
        self._query = None
        self._scene = None
        self._searchmode = None

    @property
    def domain(self):
        return self._domain

    @domain.setter
    def domain(self, value):
        self._domain = value
    @property
    def pagesize(self):
        return self._pagesize

    @pagesize.setter
    def pagesize(self, value):
        self._pagesize = value
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
    def searchmode(self):
        return self._searchmode

    @searchmode.setter
    def searchmode(self, value):
        self._searchmode = value


    def to_alipay_dict(self):
        params = dict()
        if self.domain:
            if hasattr(self.domain, 'to_alipay_dict'):
                params['domain'] = self.domain.to_alipay_dict()
            else:
                params['domain'] = self.domain
        if self.pagesize:
            if hasattr(self.pagesize, 'to_alipay_dict'):
                params['pagesize'] = self.pagesize.to_alipay_dict()
            else:
                params['pagesize'] = self.pagesize
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
        if self.searchmode:
            if hasattr(self.searchmode, 'to_alipay_dict'):
                params['searchmode'] = self.searchmode.to_alipay_dict()
            else:
                params['searchmode'] = self.searchmode
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = DatadigitalFincloudFinsaasOpensearchQueryModel()
        if 'domain' in d:
            o.domain = d['domain']
        if 'pagesize' in d:
            o.pagesize = d['pagesize']
        if 'query' in d:
            o.query = d['query']
        if 'scene' in d:
            o.scene = d['scene']
        if 'searchmode' in d:
            o.searchmode = d['searchmode']
        return o


