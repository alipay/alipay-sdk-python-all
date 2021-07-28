#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class SummaryInfo(object):

    def __init__(self):
        self._channel = None
        self._public_id = None
        self._public_name = None
        self._status = None

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
    def public_name(self):
        return self._public_name

    @public_name.setter
    def public_name(self, value):
        self._public_name = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value


    def to_alipay_dict(self):
        params = dict()
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
        if self.public_name:
            if hasattr(self.public_name, 'to_alipay_dict'):
                params['public_name'] = self.public_name.to_alipay_dict()
            else:
                params['public_name'] = self.public_name
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
        o = SummaryInfo()
        if 'channel' in d:
            o.channel = d['channel']
        if 'public_id' in d:
            o.public_id = d['public_id']
        if 'public_name' in d:
            o.public_name = d['public_name']
        if 'status' in d:
            o.status = d['status']
        return o


