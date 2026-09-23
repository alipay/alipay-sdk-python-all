#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ShortPlayChannelInfo(object):

    def __init__(self):
        self._cc_id = None
        self._channel = None
        self._public_id = None
        self._request_time = None
        self._review_id = None
        self._review_result = None
        self._review_suggest = None
        self._status = None

    @property
    def cc_id(self):
        return self._cc_id

    @cc_id.setter
    def cc_id(self, value):
        self._cc_id = value
    @property
    def channel(self):
        return self._channel

    @channel.setter
    def channel(self, value):
        self._channel = value
    @property
    def public_id(self):
        return self._public_id

    @public_id.setter
    def public_id(self, value):
        self._public_id = value
    @property
    def request_time(self):
        return self._request_time

    @request_time.setter
    def request_time(self, value):
        self._request_time = value
    @property
    def review_id(self):
        return self._review_id

    @review_id.setter
    def review_id(self, value):
        self._review_id = value
    @property
    def review_result(self):
        return self._review_result

    @review_result.setter
    def review_result(self, value):
        self._review_result = value
    @property
    def review_suggest(self):
        return self._review_suggest

    @review_suggest.setter
    def review_suggest(self, value):
        self._review_suggest = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value


    def to_alipay_dict(self):
        params = dict()
        if self.cc_id:
            if hasattr(self.cc_id, 'to_alipay_dict'):
                params['cc_id'] = self.cc_id.to_alipay_dict()
            else:
                params['cc_id'] = self.cc_id
        if self.channel:
            if hasattr(self.channel, 'to_alipay_dict'):
                params['channel'] = self.channel.to_alipay_dict()
            else:
                params['channel'] = self.channel
        if self.public_id:
            if hasattr(self.public_id, 'to_alipay_dict'):
                params['public_id'] = self.public_id.to_alipay_dict()
            else:
                params['public_id'] = self.public_id
        if self.request_time:
            if hasattr(self.request_time, 'to_alipay_dict'):
                params['request_time'] = self.request_time.to_alipay_dict()
            else:
                params['request_time'] = self.request_time
        if self.review_id:
            if hasattr(self.review_id, 'to_alipay_dict'):
                params['review_id'] = self.review_id.to_alipay_dict()
            else:
                params['review_id'] = self.review_id
        if self.review_result:
            if hasattr(self.review_result, 'to_alipay_dict'):
                params['review_result'] = self.review_result.to_alipay_dict()
            else:
                params['review_result'] = self.review_result
        if self.review_suggest:
            if hasattr(self.review_suggest, 'to_alipay_dict'):
                params['review_suggest'] = self.review_suggest.to_alipay_dict()
            else:
                params['review_suggest'] = self.review_suggest
        if self.status:
            if hasattr(self.status, 'to_alipay_dict'):
                params['status'] = self.status.to_alipay_dict()
            else:
                params['status'] = self.status
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ShortPlayChannelInfo()
        if 'cc_id' in d:
            o.cc_id = d['cc_id']
        if 'channel' in d:
            o.channel = d['channel']
        if 'public_id' in d:
            o.public_id = d['public_id']
        if 'request_time' in d:
            o.request_time = d['request_time']
        if 'review_id' in d:
            o.review_id = d['review_id']
        if 'review_result' in d:
            o.review_result = d['review_result']
        if 'review_suggest' in d:
            o.review_suggest = d['review_suggest']
        if 'status' in d:
            o.status = d['status']
        return o


