#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ShortPlayPublishChannelInfo(object):

    def __init__(self):
        self._cc_id = None
        self._channel = None
        self._review_id = None
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
    def review_id(self):
        return self._review_id

    @review_id.setter
    def review_id(self, value):
        self._review_id = value
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
        if self.review_id:
            if hasattr(self.review_id, 'to_alipay_dict'):
                params['review_id'] = self.review_id.to_alipay_dict()
            else:
                params['review_id'] = self.review_id
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
        o = ShortPlayPublishChannelInfo()
        if 'cc_id' in d:
            o.cc_id = d['cc_id']
        if 'channel' in d:
            o.channel = d['channel']
        if 'review_id' in d:
            o.review_id = d['review_id']
        if 'status' in d:
            o.status = d['status']
        return o


