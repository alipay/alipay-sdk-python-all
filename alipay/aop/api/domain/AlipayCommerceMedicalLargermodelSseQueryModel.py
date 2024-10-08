#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceMedicalLargermodelSseQueryModel(object):

    def __init__(self):
        self._alive_time = None
        self._app_type = None
        self._city_code = None
        self._city_name = None
        self._ext_params = None
        self._latitude = None
        self._longitude = None
        self._open_id = None
        self._org_id = None
        self._out_user_id = None
        self._out_user_type = None
        self._pre_intention = None
        self._query = None
        self._query_type = None
        self._scene_code = None
        self._session_id = None

    @property
    def alive_time(self):
        return self._alive_time

    @alive_time.setter
    def alive_time(self, value):
        self._alive_time = value
    @property
    def app_type(self):
        return self._app_type

    @app_type.setter
    def app_type(self, value):
        self._app_type = value
    @property
    def city_code(self):
        return self._city_code

    @city_code.setter
    def city_code(self, value):
        self._city_code = value
    @property
    def city_name(self):
        return self._city_name

    @city_name.setter
    def city_name(self, value):
        self._city_name = value
    @property
    def ext_params(self):
        return self._ext_params

    @ext_params.setter
    def ext_params(self, value):
        self._ext_params = value
    @property
    def latitude(self):
        return self._latitude

    @latitude.setter
    def latitude(self, value):
        self._latitude = value
    @property
    def longitude(self):
        return self._longitude

    @longitude.setter
    def longitude(self, value):
        self._longitude = value
    @property
    def open_id(self):
        return self._open_id

    @open_id.setter
    def open_id(self, value):
        self._open_id = value
    @property
    def org_id(self):
        return self._org_id

    @org_id.setter
    def org_id(self, value):
        self._org_id = value
    @property
    def out_user_id(self):
        return self._out_user_id

    @out_user_id.setter
    def out_user_id(self, value):
        self._out_user_id = value
    @property
    def out_user_type(self):
        return self._out_user_type

    @out_user_type.setter
    def out_user_type(self, value):
        self._out_user_type = value
    @property
    def pre_intention(self):
        return self._pre_intention

    @pre_intention.setter
    def pre_intention(self, value):
        self._pre_intention = value
    @property
    def query(self):
        return self._query

    @query.setter
    def query(self, value):
        self._query = value
    @property
    def query_type(self):
        return self._query_type

    @query_type.setter
    def query_type(self, value):
        self._query_type = value
    @property
    def scene_code(self):
        return self._scene_code

    @scene_code.setter
    def scene_code(self, value):
        self._scene_code = value
    @property
    def session_id(self):
        return self._session_id

    @session_id.setter
    def session_id(self, value):
        self._session_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.alive_time:
            if hasattr(self.alive_time, 'to_alipay_dict'):
                params['alive_time'] = self.alive_time.to_alipay_dict()
            else:
                params['alive_time'] = self.alive_time
        if self.app_type:
            if hasattr(self.app_type, 'to_alipay_dict'):
                params['app_type'] = self.app_type.to_alipay_dict()
            else:
                params['app_type'] = self.app_type
        if self.city_code:
            if hasattr(self.city_code, 'to_alipay_dict'):
                params['city_code'] = self.city_code.to_alipay_dict()
            else:
                params['city_code'] = self.city_code
        if self.city_name:
            if hasattr(self.city_name, 'to_alipay_dict'):
                params['city_name'] = self.city_name.to_alipay_dict()
            else:
                params['city_name'] = self.city_name
        if self.ext_params:
            if hasattr(self.ext_params, 'to_alipay_dict'):
                params['ext_params'] = self.ext_params.to_alipay_dict()
            else:
                params['ext_params'] = self.ext_params
        if self.latitude:
            if hasattr(self.latitude, 'to_alipay_dict'):
                params['latitude'] = self.latitude.to_alipay_dict()
            else:
                params['latitude'] = self.latitude
        if self.longitude:
            if hasattr(self.longitude, 'to_alipay_dict'):
                params['longitude'] = self.longitude.to_alipay_dict()
            else:
                params['longitude'] = self.longitude
        if self.open_id:
            if hasattr(self.open_id, 'to_alipay_dict'):
                params['open_id'] = self.open_id.to_alipay_dict()
            else:
                params['open_id'] = self.open_id
        if self.org_id:
            if hasattr(self.org_id, 'to_alipay_dict'):
                params['org_id'] = self.org_id.to_alipay_dict()
            else:
                params['org_id'] = self.org_id
        if self.out_user_id:
            if hasattr(self.out_user_id, 'to_alipay_dict'):
                params['out_user_id'] = self.out_user_id.to_alipay_dict()
            else:
                params['out_user_id'] = self.out_user_id
        if self.out_user_type:
            if hasattr(self.out_user_type, 'to_alipay_dict'):
                params['out_user_type'] = self.out_user_type.to_alipay_dict()
            else:
                params['out_user_type'] = self.out_user_type
        if self.pre_intention:
            if hasattr(self.pre_intention, 'to_alipay_dict'):
                params['pre_intention'] = self.pre_intention.to_alipay_dict()
            else:
                params['pre_intention'] = self.pre_intention
        if self.query:
            if hasattr(self.query, 'to_alipay_dict'):
                params['query'] = self.query.to_alipay_dict()
            else:
                params['query'] = self.query
        if self.query_type:
            if hasattr(self.query_type, 'to_alipay_dict'):
                params['query_type'] = self.query_type.to_alipay_dict()
            else:
                params['query_type'] = self.query_type
        if self.scene_code:
            if hasattr(self.scene_code, 'to_alipay_dict'):
                params['scene_code'] = self.scene_code.to_alipay_dict()
            else:
                params['scene_code'] = self.scene_code
        if self.session_id:
            if hasattr(self.session_id, 'to_alipay_dict'):
                params['session_id'] = self.session_id.to_alipay_dict()
            else:
                params['session_id'] = self.session_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceMedicalLargermodelSseQueryModel()
        if 'alive_time' in d:
            o.alive_time = d['alive_time']
        if 'app_type' in d:
            o.app_type = d['app_type']
        if 'city_code' in d:
            o.city_code = d['city_code']
        if 'city_name' in d:
            o.city_name = d['city_name']
        if 'ext_params' in d:
            o.ext_params = d['ext_params']
        if 'latitude' in d:
            o.latitude = d['latitude']
        if 'longitude' in d:
            o.longitude = d['longitude']
        if 'open_id' in d:
            o.open_id = d['open_id']
        if 'org_id' in d:
            o.org_id = d['org_id']
        if 'out_user_id' in d:
            o.out_user_id = d['out_user_id']
        if 'out_user_type' in d:
            o.out_user_type = d['out_user_type']
        if 'pre_intention' in d:
            o.pre_intention = d['pre_intention']
        if 'query' in d:
            o.query = d['query']
        if 'query_type' in d:
            o.query_type = d['query_type']
        if 'scene_code' in d:
            o.scene_code = d['scene_code']
        if 'session_id' in d:
            o.session_id = d['session_id']
        return o


