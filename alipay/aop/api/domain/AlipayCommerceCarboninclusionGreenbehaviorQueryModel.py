#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceCarboninclusionGreenbehaviorQueryModel(object):

    def __init__(self):
        self._end_time = None
        self._page_size = None
        self._page_token = None
        self._request_id = None
        self._start_time = None
        self._user_code = None

    @property
    def end_time(self):
        return self._end_time

    @end_time.setter
    def end_time(self, value):
        self._end_time = value
    @property
    def page_size(self):
        return self._page_size

    @page_size.setter
    def page_size(self, value):
        self._page_size = value
    @property
    def page_token(self):
        return self._page_token

    @page_token.setter
    def page_token(self, value):
        self._page_token = value
    @property
    def request_id(self):
        return self._request_id

    @request_id.setter
    def request_id(self, value):
        self._request_id = value
    @property
    def start_time(self):
        return self._start_time

    @start_time.setter
    def start_time(self, value):
        self._start_time = value
    @property
    def user_code(self):
        return self._user_code

    @user_code.setter
    def user_code(self, value):
        self._user_code = value


    def to_alipay_dict(self):
        params = dict()
        if self.end_time:
            if hasattr(self.end_time, 'to_alipay_dict'):
                params['end_time'] = self.end_time.to_alipay_dict()
            else:
                params['end_time'] = self.end_time
        if self.page_size:
            if hasattr(self.page_size, 'to_alipay_dict'):
                params['page_size'] = self.page_size.to_alipay_dict()
            else:
                params['page_size'] = self.page_size
        if self.page_token:
            if hasattr(self.page_token, 'to_alipay_dict'):
                params['page_token'] = self.page_token.to_alipay_dict()
            else:
                params['page_token'] = self.page_token
        if self.request_id:
            if hasattr(self.request_id, 'to_alipay_dict'):
                params['request_id'] = self.request_id.to_alipay_dict()
            else:
                params['request_id'] = self.request_id
        if self.start_time:
            if hasattr(self.start_time, 'to_alipay_dict'):
                params['start_time'] = self.start_time.to_alipay_dict()
            else:
                params['start_time'] = self.start_time
        if self.user_code:
            if hasattr(self.user_code, 'to_alipay_dict'):
                params['user_code'] = self.user_code.to_alipay_dict()
            else:
                params['user_code'] = self.user_code
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceCarboninclusionGreenbehaviorQueryModel()
        if 'end_time' in d:
            o.end_time = d['end_time']
        if 'page_size' in d:
            o.page_size = d['page_size']
        if 'page_token' in d:
            o.page_token = d['page_token']
        if 'request_id' in d:
            o.request_id = d['request_id']
        if 'start_time' in d:
            o.start_time = d['start_time']
        if 'user_code' in d:
            o.user_code = d['user_code']
        return o


