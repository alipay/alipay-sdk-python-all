#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class GetOfficePreviewURLResponse(object):

    def __init__(self):
        self._access_token = None
        self._access_token_expired_time = None
        self._preview_url = None
        self._refresh_token = None
        self._refresh_token_expired_time = None
        self._request_d = None

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
    def preview_url(self):
        return self._preview_url

    @preview_url.setter
    def preview_url(self, value):
        self._preview_url = value
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
    def request_d(self):
        return self._request_d

    @request_d.setter
    def request_d(self, value):
        self._request_d = value


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
        if self.preview_url:
            if hasattr(self.preview_url, 'to_alipay_dict'):
                params['preview_url'] = self.preview_url.to_alipay_dict()
            else:
                params['preview_url'] = self.preview_url
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
        if self.request_d:
            if hasattr(self.request_d, 'to_alipay_dict'):
                params['request_d'] = self.request_d.to_alipay_dict()
            else:
                params['request_d'] = self.request_d
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = GetOfficePreviewURLResponse()
        if 'access_token' in d:
            o.access_token = d['access_token']
        if 'access_token_expired_time' in d:
            o.access_token_expired_time = d['access_token_expired_time']
        if 'preview_url' in d:
            o.preview_url = d['preview_url']
        if 'refresh_token' in d:
            o.refresh_token = d['refresh_token']
        if 'refresh_token_expired_time' in d:
            o.refresh_token_expired_time = d['refresh_token_expired_time']
        if 'request_d' in d:
            o.request_d = d['request_d']
        return o


