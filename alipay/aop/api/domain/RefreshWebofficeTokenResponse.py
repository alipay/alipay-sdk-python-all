#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class RefreshWebofficeTokenResponse(object):

    def __init__(self):
        self._access_token = None
        self._access_token_expired_time = None
        self._refresh_token = None
        self._refresh_token_expired_time = None
        self._request_id = None

    @property
    def access_token(self):
        return self._access_token

    @access_token.setter
    def access_token(self, value):
        self._access_token = value
    @property
    def access_token_expired_time(self):
        return self._access_token_expired_time

    @access_token_expired_time.setter
    def access_token_expired_time(self, value):
        self._access_token_expired_time = value
    @property
    def refresh_token(self):
        return self._refresh_token

    @refresh_token.setter
    def refresh_token(self, value):
        self._refresh_token = value
    @property
    def refresh_token_expired_time(self):
        return self._refresh_token_expired_time

    @refresh_token_expired_time.setter
    def refresh_token_expired_time(self, value):
        self._refresh_token_expired_time = value
    @property
    def request_id(self):
        return self._request_id

    @request_id.setter
    def request_id(self, value):
        self._request_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.access_token:
            if hasattr(self.access_token, 'to_alipay_dict'):
                params['access_token'] = self.access_token.to_alipay_dict()
            else:
                params['access_token'] = self.access_token
        if self.access_token_expired_time:
            if hasattr(self.access_token_expired_time, 'to_alipay_dict'):
                params['access_token_expired_time'] = self.access_token_expired_time.to_alipay_dict()
            else:
                params['access_token_expired_time'] = self.access_token_expired_time
        if self.refresh_token:
            if hasattr(self.refresh_token, 'to_alipay_dict'):
                params['refresh_token'] = self.refresh_token.to_alipay_dict()
            else:
                params['refresh_token'] = self.refresh_token
        if self.refresh_token_expired_time:
            if hasattr(self.refresh_token_expired_time, 'to_alipay_dict'):
                params['refresh_token_expired_time'] = self.refresh_token_expired_time.to_alipay_dict()
            else:
                params['refresh_token_expired_time'] = self.refresh_token_expired_time
        if self.request_id:
            if hasattr(self.request_id, 'to_alipay_dict'):
                params['request_id'] = self.request_id.to_alipay_dict()
            else:
                params['request_id'] = self.request_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = RefreshWebofficeTokenResponse()
        if 'access_token' in d:
            o.access_token = d['access_token']
        if 'access_token_expired_time' in d:
            o.access_token_expired_time = d['access_token_expired_time']
        if 'refresh_token' in d:
            o.refresh_token = d['refresh_token']
        if 'refresh_token_expired_time' in d:
            o.refresh_token_expired_time = d['refresh_token_expired_time']
        if 'request_id' in d:
            o.request_id = d['request_id']
        return o


