#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class IntentQueryRequest(object):

    def __init__(self):
        self._action_src = None
        self._client_os = None
        self._client_version = None
        self._current_city = None
        self._location = None
        self._nlu_json_param = None
        self._query = None
        self._query_id = None
        self._scene_code = None
        self._search_src = None
        self._session_id = None
        self._uid = None

    @property
    def action_src(self):
        return self._action_src

    @action_src.setter
    def action_src(self, value):
        self._action_src = value
    @property
    def client_os(self):
        return self._client_os

    @client_os.setter
    def client_os(self, value):
        self._client_os = value
    @property
    def client_version(self):
        return self._client_version

    @client_version.setter
    def client_version(self, value):
        self._client_version = value
    @property
    def current_city(self):
        return self._current_city

    @current_city.setter
    def current_city(self, value):
        self._current_city = value
    @property
    def location(self):
        return self._location

    @location.setter
    def location(self, value):
        self._location = value
    @property
    def nlu_json_param(self):
        return self._nlu_json_param

    @nlu_json_param.setter
    def nlu_json_param(self, value):
        self._nlu_json_param = value
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
    def scene_code(self):
        return self._scene_code

    @scene_code.setter
    def scene_code(self, value):
        self._scene_code = value
    @property
    def search_src(self):
        return self._search_src

    @search_src.setter
    def search_src(self, value):
        self._search_src = value
    @property
    def session_id(self):
        return self._session_id

    @session_id.setter
    def session_id(self, value):
        self._session_id = value
    @property
    def uid(self):
        return self._uid

    @uid.setter
    def uid(self, value):
        self._uid = value


    def to_alipay_dict(self):
        params = dict()
        if self.action_src:
            if hasattr(self.action_src, 'to_alipay_dict'):
                params['action_src'] = self.action_src.to_alipay_dict()
            else:
                params['action_src'] = self.action_src
        if self.client_os:
            if hasattr(self.client_os, 'to_alipay_dict'):
                params['client_os'] = self.client_os.to_alipay_dict()
            else:
                params['client_os'] = self.client_os
        if self.client_version:
            if hasattr(self.client_version, 'to_alipay_dict'):
                params['client_version'] = self.client_version.to_alipay_dict()
            else:
                params['client_version'] = self.client_version
        if self.current_city:
            if hasattr(self.current_city, 'to_alipay_dict'):
                params['current_city'] = self.current_city.to_alipay_dict()
            else:
                params['current_city'] = self.current_city
        if self.location:
            if hasattr(self.location, 'to_alipay_dict'):
                params['location'] = self.location.to_alipay_dict()
            else:
                params['location'] = self.location
        if self.nlu_json_param:
            if hasattr(self.nlu_json_param, 'to_alipay_dict'):
                params['nlu_json_param'] = self.nlu_json_param.to_alipay_dict()
            else:
                params['nlu_json_param'] = self.nlu_json_param
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
        if self.scene_code:
            if hasattr(self.scene_code, 'to_alipay_dict'):
                params['scene_code'] = self.scene_code.to_alipay_dict()
            else:
                params['scene_code'] = self.scene_code
        if self.search_src:
            if hasattr(self.search_src, 'to_alipay_dict'):
                params['search_src'] = self.search_src.to_alipay_dict()
            else:
                params['search_src'] = self.search_src
        if self.session_id:
            if hasattr(self.session_id, 'to_alipay_dict'):
                params['session_id'] = self.session_id.to_alipay_dict()
            else:
                params['session_id'] = self.session_id
        if self.uid:
            if hasattr(self.uid, 'to_alipay_dict'):
                params['uid'] = self.uid.to_alipay_dict()
            else:
                params['uid'] = self.uid
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = IntentQueryRequest()
        if 'action_src' in d:
            o.action_src = d['action_src']
        if 'client_os' in d:
            o.client_os = d['client_os']
        if 'client_version' in d:
            o.client_version = d['client_version']
        if 'current_city' in d:
            o.current_city = d['current_city']
        if 'location' in d:
            o.location = d['location']
        if 'nlu_json_param' in d:
            o.nlu_json_param = d['nlu_json_param']
        if 'query' in d:
            o.query = d['query']
        if 'query_id' in d:
            o.query_id = d['query_id']
        if 'scene_code' in d:
            o.scene_code = d['scene_code']
        if 'search_src' in d:
            o.search_src = d['search_src']
        if 'session_id' in d:
            o.session_id = d['session_id']
        if 'uid' in d:
            o.uid = d['uid']
        return o


