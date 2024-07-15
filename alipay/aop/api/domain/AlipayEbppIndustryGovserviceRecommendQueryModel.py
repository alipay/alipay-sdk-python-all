#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayEbppIndustryGovserviceRecommendQueryModel(object):

    def __init__(self):
        self._actual_city_code = None
        self._channel = None
        self._city_code = None
        self._identify_id = None
        self._open_id = None
        self._pid = None
        self._query = None
        self._recommend_token = None
        self._user_id = None

    @property
    def actual_city_code(self):
        return self._actual_city_code

    @actual_city_code.setter
    def actual_city_code(self, value):
        self._actual_city_code = value
    @property
    def channel(self):
        return self._channel

    @channel.setter
    def channel(self, value):
        self._channel = value
    @property
    def city_code(self):
        return self._city_code

    @city_code.setter
    def city_code(self, value):
        self._city_code = value
    @property
    def identify_id(self):
        return self._identify_id

    @identify_id.setter
    def identify_id(self, value):
        self._identify_id = value
    @property
    def open_id(self):
        return self._open_id

    @open_id.setter
    def open_id(self, value):
        self._open_id = value
    @property
    def pid(self):
        return self._pid

    @pid.setter
    def pid(self, value):
        self._pid = value
    @property
    def query(self):
        return self._query

    @query.setter
    def query(self, value):
        self._query = value
    @property
    def recommend_token(self):
        return self._recommend_token

    @recommend_token.setter
    def recommend_token(self, value):
        self._recommend_token = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.actual_city_code:
            if hasattr(self.actual_city_code, 'to_alipay_dict'):
                params['actual_city_code'] = self.actual_city_code.to_alipay_dict()
            else:
                params['actual_city_code'] = self.actual_city_code
        if self.channel:
            if hasattr(self.channel, 'to_alipay_dict'):
                params['channel'] = self.channel.to_alipay_dict()
            else:
                params['channel'] = self.channel
        if self.city_code:
            if hasattr(self.city_code, 'to_alipay_dict'):
                params['city_code'] = self.city_code.to_alipay_dict()
            else:
                params['city_code'] = self.city_code
        if self.identify_id:
            if hasattr(self.identify_id, 'to_alipay_dict'):
                params['identify_id'] = self.identify_id.to_alipay_dict()
            else:
                params['identify_id'] = self.identify_id
        if self.open_id:
            if hasattr(self.open_id, 'to_alipay_dict'):
                params['open_id'] = self.open_id.to_alipay_dict()
            else:
                params['open_id'] = self.open_id
        if self.pid:
            if hasattr(self.pid, 'to_alipay_dict'):
                params['pid'] = self.pid.to_alipay_dict()
            else:
                params['pid'] = self.pid
        if self.query:
            if hasattr(self.query, 'to_alipay_dict'):
                params['query'] = self.query.to_alipay_dict()
            else:
                params['query'] = self.query
        if self.recommend_token:
            if hasattr(self.recommend_token, 'to_alipay_dict'):
                params['recommend_token'] = self.recommend_token.to_alipay_dict()
            else:
                params['recommend_token'] = self.recommend_token
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
        o = AlipayEbppIndustryGovserviceRecommendQueryModel()
        if 'actual_city_code' in d:
            o.actual_city_code = d['actual_city_code']
        if 'channel' in d:
            o.channel = d['channel']
        if 'city_code' in d:
            o.city_code = d['city_code']
        if 'identify_id' in d:
            o.identify_id = d['identify_id']
        if 'open_id' in d:
            o.open_id = d['open_id']
        if 'pid' in d:
            o.pid = d['pid']
        if 'query' in d:
            o.query = d['query']
        if 'recommend_token' in d:
            o.recommend_token = d['recommend_token']
        if 'user_id' in d:
            o.user_id = d['user_id']
        return o


