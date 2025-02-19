#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayEbppIndustryBotQueryRecommendModel(object):

    def __init__(self):
        self._actual_city_code = None
        self._bot_id = None
        self._chat_id = None
        self._city_code = None
        self._identify_id = None
        self._open_id = None
        self._query = None
        self._session_id = None
        self._user_id = None

    @property
    def actual_city_code(self):
        return self._actual_city_code

    @actual_city_code.setter
    def actual_city_code(self, value):
        self._actual_city_code = value
    @property
    def bot_id(self):
        return self._bot_id

    @bot_id.setter
    def bot_id(self, value):
        self._bot_id = value
    @property
    def chat_id(self):
        return self._chat_id

    @chat_id.setter
    def chat_id(self, value):
        self._chat_id = value
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
    def query(self):
        return self._query

    @query.setter
    def query(self, value):
        self._query = value
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
        if self.actual_city_code:
            if hasattr(self.actual_city_code, 'to_alipay_dict'):
                params['actual_city_code'] = self.actual_city_code.to_alipay_dict()
            else:
                params['actual_city_code'] = self.actual_city_code
        if self.bot_id:
            if hasattr(self.bot_id, 'to_alipay_dict'):
                params['bot_id'] = self.bot_id.to_alipay_dict()
            else:
                params['bot_id'] = self.bot_id
        if self.chat_id:
            if hasattr(self.chat_id, 'to_alipay_dict'):
                params['chat_id'] = self.chat_id.to_alipay_dict()
            else:
                params['chat_id'] = self.chat_id
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
        if self.query:
            if hasattr(self.query, 'to_alipay_dict'):
                params['query'] = self.query.to_alipay_dict()
            else:
                params['query'] = self.query
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
        o = AlipayEbppIndustryBotQueryRecommendModel()
        if 'actual_city_code' in d:
            o.actual_city_code = d['actual_city_code']
        if 'bot_id' in d:
            o.bot_id = d['bot_id']
        if 'chat_id' in d:
            o.chat_id = d['chat_id']
        if 'city_code' in d:
            o.city_code = d['city_code']
        if 'identify_id' in d:
            o.identify_id = d['identify_id']
        if 'open_id' in d:
            o.open_id = d['open_id']
        if 'query' in d:
            o.query = d['query']
        if 'session_id' in d:
            o.session_id = d['session_id']
        if 'user_id' in d:
            o.user_id = d['user_id']
        return o


