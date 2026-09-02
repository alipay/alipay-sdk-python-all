#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ResourceAihrInterviewRoomModifyModel(object):

    def __init__(self):
        self._ai_interview_id = None
        self._channel = None
        self._end_time = None

    @property
    def ai_interview_id(self):
        return self._ai_interview_id

    @ai_interview_id.setter
    def ai_interview_id(self, value):
        self._ai_interview_id = value
    @property
    def channel(self):
        return self._channel

    @channel.setter
    def channel(self, value):
        self._channel = value
    @property
    def end_time(self):
        return self._end_time

    @end_time.setter
    def end_time(self, value):
        self._end_time = value


    def to_alipay_dict(self):
        params = dict()
        if self.ai_interview_id:
            if hasattr(self.ai_interview_id, 'to_alipay_dict'):
                params['ai_interview_id'] = self.ai_interview_id.to_alipay_dict()
            else:
                params['ai_interview_id'] = self.ai_interview_id
        if self.channel:
            if hasattr(self.channel, 'to_alipay_dict'):
                params['channel'] = self.channel.to_alipay_dict()
            else:
                params['channel'] = self.channel
        if self.end_time:
            if hasattr(self.end_time, 'to_alipay_dict'):
                params['end_time'] = self.end_time.to_alipay_dict()
            else:
                params['end_time'] = self.end_time
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ResourceAihrInterviewRoomModifyModel()
        if 'ai_interview_id' in d:
            o.ai_interview_id = d['ai_interview_id']
        if 'channel' in d:
            o.channel = d['channel']
        if 'end_time' in d:
            o.end_time = d['end_time']
        return o


