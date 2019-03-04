#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.ClientInfo import ClientInfo
from alipay.aop.api.domain.LocationInfo import LocationInfo


class AlipayOpenDataServiceQueryModel(object):

    def __init__(self):
        self._client_info = None
        self._limit_size = None
        self._location_info = None
        self._query = None
        self._scene_code = None
        self._search_id = None
        self._session_id = None
        self._start_num = None
        self._user_id = None

    @property
    def client_info(self):
        return self._client_info

    @client_info.setter
    def client_info(self, value):
        if isinstance(value, ClientInfo):
            self._client_info = value
        else:
            self._client_info = ClientInfo.from_alipay_dict(value)
    @property
    def limit_size(self):
        return self._limit_size

    @limit_size.setter
    def limit_size(self, value):
        self._limit_size = value
    @property
    def location_info(self):
        return self._location_info

    @location_info.setter
    def location_info(self, value):
        if isinstance(value, LocationInfo):
            self._location_info = value
        else:
            self._location_info = LocationInfo.from_alipay_dict(value)
    @property
    def query(self):
        return self._query

    @query.setter
    def query(self, value):
        self._query = value
    @property
    def scene_code(self):
        return self._scene_code

    @scene_code.setter
    def scene_code(self, value):
        self._scene_code = value
    @property
    def search_id(self):
        return self._search_id

    @search_id.setter
    def search_id(self, value):
        self._search_id = value
    @property
    def session_id(self):
        return self._session_id

    @session_id.setter
    def session_id(self, value):
        self._session_id = value
    @property
    def start_num(self):
        return self._start_num

    @start_num.setter
    def start_num(self, value):
        self._start_num = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.client_info:
            if hasattr(self.client_info, 'to_alipay_dict'):
                params['client_info'] = self.client_info.to_alipay_dict()
            else:
                params['client_info'] = self.client_info
        if self.limit_size:
            if hasattr(self.limit_size, 'to_alipay_dict'):
                params['limit_size'] = self.limit_size.to_alipay_dict()
            else:
                params['limit_size'] = self.limit_size
        if self.location_info:
            if hasattr(self.location_info, 'to_alipay_dict'):
                params['location_info'] = self.location_info.to_alipay_dict()
            else:
                params['location_info'] = self.location_info
        if self.query:
            if hasattr(self.query, 'to_alipay_dict'):
                params['query'] = self.query.to_alipay_dict()
            else:
                params['query'] = self.query
        if self.scene_code:
            if hasattr(self.scene_code, 'to_alipay_dict'):
                params['scene_code'] = self.scene_code.to_alipay_dict()
            else:
                params['scene_code'] = self.scene_code
        if self.search_id:
            if hasattr(self.search_id, 'to_alipay_dict'):
                params['search_id'] = self.search_id.to_alipay_dict()
            else:
                params['search_id'] = self.search_id
        if self.session_id:
            if hasattr(self.session_id, 'to_alipay_dict'):
                params['session_id'] = self.session_id.to_alipay_dict()
            else:
                params['session_id'] = self.session_id
        if self.start_num:
            if hasattr(self.start_num, 'to_alipay_dict'):
                params['start_num'] = self.start_num.to_alipay_dict()
            else:
                params['start_num'] = self.start_num
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
        o = AlipayOpenDataServiceQueryModel()
        if 'client_info' in d:
            o.client_info = d['client_info']
        if 'limit_size' in d:
            o.limit_size = d['limit_size']
        if 'location_info' in d:
            o.location_info = d['location_info']
        if 'query' in d:
            o.query = d['query']
        if 'scene_code' in d:
            o.scene_code = d['scene_code']
        if 'search_id' in d:
            o.search_id = d['search_id']
        if 'session_id' in d:
            o.session_id = d['session_id']
        if 'start_num' in d:
            o.start_num = d['start_num']
        if 'user_id' in d:
            o.user_id = d['user_id']
        return o


