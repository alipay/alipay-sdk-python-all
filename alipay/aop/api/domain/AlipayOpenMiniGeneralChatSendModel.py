#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.AmpeDeviceInfo import AmpeDeviceInfo
from alipay.aop.api.domain.ChatLocation import ChatLocation


class AlipayOpenMiniGeneralChatSendModel(object):

    def __init__(self):
        self._ampe_device_id = None
        self._ampe_product_id = None
        self._device_info = None
        self._intent_code = None
        self._locations = None
        self._open_id = None
        self._query = None
        self._req_no = None
        self._session_id = None
        self._user_id = None

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
    def device_info(self):
        return self._device_info

    @device_info.setter
    def device_info(self, value):
        if isinstance(value, AmpeDeviceInfo):
            self._device_info = value
        else:
            self._device_info = AmpeDeviceInfo.from_alipay_dict(value)
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
        if isinstance(value, ChatLocation):
            self._locations = value
        else:
            self._locations = ChatLocation.from_alipay_dict(value)
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
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value


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
        if self.device_info:
            if hasattr(self.device_info, 'to_alipay_dict'):
                params['device_info'] = self.device_info.to_alipay_dict()
            else:
                params['device_info'] = self.device_info
        if self.intent_code:
            if hasattr(self.intent_code, 'to_alipay_dict'):
                params['intent_code'] = self.intent_code.to_alipay_dict()
            else:
                params['intent_code'] = self.intent_code
        if self.locations:
            if hasattr(self.locations, 'to_alipay_dict'):
                params['locations'] = self.locations.to_alipay_dict()
            else:
                params['locations'] = self.locations
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
        o = AlipayOpenMiniGeneralChatSendModel()
        if 'ampe_device_id' in d:
            o.ampe_device_id = d['ampe_device_id']
        if 'ampe_product_id' in d:
            o.ampe_product_id = d['ampe_product_id']
        if 'device_info' in d:
            o.device_info = d['device_info']
        if 'intent_code' in d:
            o.intent_code = d['intent_code']
        if 'locations' in d:
            o.locations = d['locations']
        if 'open_id' in d:
            o.open_id = d['open_id']
        if 'query' in d:
            o.query = d['query']
        if 'req_no' in d:
            o.req_no = d['req_no']
        if 'session_id' in d:
            o.session_id = d['session_id']
        if 'user_id' in d:
            o.user_id = d['user_id']
        return o


