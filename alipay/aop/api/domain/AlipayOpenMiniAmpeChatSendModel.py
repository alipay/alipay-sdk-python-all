#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.ChatLocation import ChatLocation


class AlipayOpenMiniAmpeChatSendModel(object):

    def __init__(self):
        self._ampe_device_id = None
        self._ampe_product_id = None
        self._intent_code = None
        self._locations = None
        self._query = None
        self._req_no = None
        self._session_id = None
        self._user_key = None

    @property
    def ampe_device_id(self):
        return self._ampe_device_id

    @ampe_device_id.setter
    def ampe_device_id(self, value):
        self._ampe_device_id = value
    @property
    def ampe_product_id(self):
        return self._ampe_product_id

    @ampe_product_id.setter
    def ampe_product_id(self, value):
        self._ampe_product_id = value
    @property
    def intent_code(self):
        return self._intent_code

    @intent_code.setter
    def intent_code(self, value):
        self._intent_code = value
    @property
    def locations(self):
        return self._locations

    @locations.setter
    def locations(self, value):
        if isinstance(value, list):
            self._locations = list()
            for i in value:
                if isinstance(i, ChatLocation):
                    self._locations.append(i)
                else:
                    self._locations.append(ChatLocation.from_alipay_dict(i))
    @property
    def query(self):
        return self._query

    @query.setter
    def query(self, value):
        self._query = value
    @property
    def req_no(self):
        return self._req_no

    @req_no.setter
    def req_no(self, value):
        self._req_no = value
    @property
    def session_id(self):
        return self._session_id

    @session_id.setter
    def session_id(self, value):
        self._session_id = value
    @property
    def user_key(self):
        return self._user_key

    @user_key.setter
    def user_key(self, value):
        self._user_key = value


    def to_alipay_dict(self):
        params = dict()
        if self.ampe_device_id:
            if hasattr(self.ampe_device_id, 'to_alipay_dict'):
                params['ampe_device_id'] = self.ampe_device_id.to_alipay_dict()
            else:
                params['ampe_device_id'] = self.ampe_device_id
        if self.ampe_product_id:
            if hasattr(self.ampe_product_id, 'to_alipay_dict'):
                params['ampe_product_id'] = self.ampe_product_id.to_alipay_dict()
            else:
                params['ampe_product_id'] = self.ampe_product_id
        if self.intent_code:
            if hasattr(self.intent_code, 'to_alipay_dict'):
                params['intent_code'] = self.intent_code.to_alipay_dict()
            else:
                params['intent_code'] = self.intent_code
        if self.locations:
            if isinstance(self.locations, list):
                for i in range(0, len(self.locations)):
                    element = self.locations[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.locations[i] = element.to_alipay_dict()
            if hasattr(self.locations, 'to_alipay_dict'):
                params['locations'] = self.locations.to_alipay_dict()
            else:
                params['locations'] = self.locations
        if self.query:
            if hasattr(self.query, 'to_alipay_dict'):
                params['query'] = self.query.to_alipay_dict()
            else:
                params['query'] = self.query
        if self.req_no:
            if hasattr(self.req_no, 'to_alipay_dict'):
                params['req_no'] = self.req_no.to_alipay_dict()
            else:
                params['req_no'] = self.req_no
        if self.session_id:
            if hasattr(self.session_id, 'to_alipay_dict'):
                params['session_id'] = self.session_id.to_alipay_dict()
            else:
                params['session_id'] = self.session_id
        if self.user_key:
            if hasattr(self.user_key, 'to_alipay_dict'):
                params['user_key'] = self.user_key.to_alipay_dict()
            else:
                params['user_key'] = self.user_key
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayOpenMiniAmpeChatSendModel()
        if 'ampe_device_id' in d:
            o.ampe_device_id = d['ampe_device_id']
        if 'ampe_product_id' in d:
            o.ampe_product_id = d['ampe_product_id']
        if 'intent_code' in d:
            o.intent_code = d['intent_code']
        if 'locations' in d:
            o.locations = d['locations']
        if 'query' in d:
            o.query = d['query']
        if 'req_no' in d:
            o.req_no = d['req_no']
        if 'session_id' in d:
            o.session_id = d['session_id']
        if 'user_key' in d:
            o.user_key = d['user_key']
        return o


