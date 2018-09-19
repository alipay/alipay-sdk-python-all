#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayInsUnderwriteMutualPolicyBatchqueryModel(object):

    def __init__(self):
        self._channel = None
        self._plan_no = None
        self._source = None
        self._user_id = None

    @property
    def channel(self):
        return self._channel

    @channel.setter
    def channel(self, value):
        self._channel = value
    @property
    def plan_no(self):
        return self._plan_no

    @plan_no.setter
    def plan_no(self, value):
        self._plan_no = value
    @property
    def source(self):
        return self._source

    @source.setter
    def source(self, value):
        self._source = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.channel:
            if hasattr(self.channel, 'to_alipay_dict'):
                params['channel'] = self.channel.to_alipay_dict()
            else:
                params['channel'] = self.channel
        if self.plan_no:
            if hasattr(self.plan_no, 'to_alipay_dict'):
                params['plan_no'] = self.plan_no.to_alipay_dict()
            else:
                params['plan_no'] = self.plan_no
        if self.source:
            if hasattr(self.source, 'to_alipay_dict'):
                params['source'] = self.source.to_alipay_dict()
            else:
                params['source'] = self.source
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
        o = AlipayInsUnderwriteMutualPolicyBatchqueryModel()
        if 'channel' in d:
            o.channel = d['channel']
        if 'plan_no' in d:
            o.plan_no = d['plan_no']
        if 'source' in d:
            o.source = d['source']
        if 'user_id' in d:
            o.user_id = d['user_id']
        return o


