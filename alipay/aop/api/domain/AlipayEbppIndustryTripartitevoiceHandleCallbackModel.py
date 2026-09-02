#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayEbppIndustryTripartitevoiceHandleCallbackModel(object):

    def __init__(self):
        self._handle_time = None
        self._reason = None
        self._status = None
        self._voice_id = None

    @property
    def handle_time(self):
        return self._handle_time

    @handle_time.setter
    def handle_time(self, value):
        self._handle_time = value
    @property
    def reason(self):
        return self._reason

    @reason.setter
    def reason(self, value):
        self._reason = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value
    @property
    def voice_id(self):
        return self._voice_id

    @voice_id.setter
    def voice_id(self, value):
        self._voice_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.handle_time:
            if hasattr(self.handle_time, 'to_alipay_dict'):
                params['handle_time'] = self.handle_time.to_alipay_dict()
            else:
                params['handle_time'] = self.handle_time
        if self.reason:
            if hasattr(self.reason, 'to_alipay_dict'):
                params['reason'] = self.reason.to_alipay_dict()
            else:
                params['reason'] = self.reason
        if self.status:
            if hasattr(self.status, 'to_alipay_dict'):
                params['status'] = self.status.to_alipay_dict()
            else:
                params['status'] = self.status
        if self.voice_id:
            if hasattr(self.voice_id, 'to_alipay_dict'):
                params['voice_id'] = self.voice_id.to_alipay_dict()
            else:
                params['voice_id'] = self.voice_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayEbppIndustryTripartitevoiceHandleCallbackModel()
        if 'handle_time' in d:
            o.handle_time = d['handle_time']
        if 'reason' in d:
            o.reason = d['reason']
        if 'status' in d:
            o.status = d['status']
        if 'voice_id' in d:
            o.voice_id = d['voice_id']
        return o


