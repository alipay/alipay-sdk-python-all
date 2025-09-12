#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayAipaySubscribeTimesSaveModel(object):

    def __init__(self):
        self._channel = None
        self._out_request_no = None
        self._plan_id = None
        self._use_times = None
        self._uuid = None

    @property
    def channel(self):
        return self._channel

    @channel.setter
    def channel(self, value):
        self._channel = value
    @property
    def out_request_no(self):
        return self._out_request_no

    @out_request_no.setter
    def out_request_no(self, value):
        self._out_request_no = value
    @property
    def plan_id(self):
        return self._plan_id

    @plan_id.setter
    def plan_id(self, value):
        self._plan_id = value
    @property
    def use_times(self):
        return self._use_times

    @use_times.setter
    def use_times(self, value):
        self._use_times = value
    @property
    def uuid(self):
        return self._uuid

    @uuid.setter
    def uuid(self, value):
        self._uuid = value


    def to_alipay_dict(self):
        params = dict()
        if self.channel:
            if hasattr(self.channel, 'to_alipay_dict'):
                params['channel'] = self.channel.to_alipay_dict()
            else:
                params['channel'] = self.channel
        if self.out_request_no:
            if hasattr(self.out_request_no, 'to_alipay_dict'):
                params['out_request_no'] = self.out_request_no.to_alipay_dict()
            else:
                params['out_request_no'] = self.out_request_no
        if self.plan_id:
            if hasattr(self.plan_id, 'to_alipay_dict'):
                params['plan_id'] = self.plan_id.to_alipay_dict()
            else:
                params['plan_id'] = self.plan_id
        if self.use_times:
            if hasattr(self.use_times, 'to_alipay_dict'):
                params['use_times'] = self.use_times.to_alipay_dict()
            else:
                params['use_times'] = self.use_times
        if self.uuid:
            if hasattr(self.uuid, 'to_alipay_dict'):
                params['uuid'] = self.uuid.to_alipay_dict()
            else:
                params['uuid'] = self.uuid
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayAipaySubscribeTimesSaveModel()
        if 'channel' in d:
            o.channel = d['channel']
        if 'out_request_no' in d:
            o.out_request_no = d['out_request_no']
        if 'plan_id' in d:
            o.plan_id = d['plan_id']
        if 'use_times' in d:
            o.use_times = d['use_times']
        if 'uuid' in d:
            o.uuid = d['uuid']
        return o


