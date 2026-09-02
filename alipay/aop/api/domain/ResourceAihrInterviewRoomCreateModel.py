#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.OpenapiInterviewJobInfoDTO import OpenapiInterviewJobInfoDTO
from alipay.aop.api.domain.OpenapiInterviewUserInfoDTO import OpenapiInterviewUserInfoDTO


class ResourceAihrInterviewRoomCreateModel(object):

    def __init__(self):
        self._ai_interview_code = None
        self._channel = None
        self._idempotent_key = None
        self._job_info = None
        self._user_info = None

    @property
    def ai_interview_code(self):
        return self._ai_interview_code

    @ai_interview_code.setter
    def ai_interview_code(self, value):
        self._ai_interview_code = value
    @property
    def channel(self):
        return self._channel

    @channel.setter
    def channel(self, value):
        self._channel = value
    @property
    def idempotent_key(self):
        return self._idempotent_key

    @idempotent_key.setter
    def idempotent_key(self, value):
        self._idempotent_key = value
    @property
    def job_info(self):
        return self._job_info

    @job_info.setter
    def job_info(self, value):
        if isinstance(value, OpenapiInterviewJobInfoDTO):
            self._job_info = value
        else:
            self._job_info = OpenapiInterviewJobInfoDTO.from_alipay_dict(value)
    @property
    def user_info(self):
        return self._user_info

    @user_info.setter
    def user_info(self, value):
        if isinstance(value, OpenapiInterviewUserInfoDTO):
            self._user_info = value
        else:
            self._user_info = OpenapiInterviewUserInfoDTO.from_alipay_dict(value)


    def to_alipay_dict(self):
        params = dict()
        if self.ai_interview_code:
            if hasattr(self.ai_interview_code, 'to_alipay_dict'):
                params['ai_interview_code'] = self.ai_interview_code.to_alipay_dict()
            else:
                params['ai_interview_code'] = self.ai_interview_code
        if self.channel:
            if hasattr(self.channel, 'to_alipay_dict'):
                params['channel'] = self.channel.to_alipay_dict()
            else:
                params['channel'] = self.channel
        if self.idempotent_key:
            if hasattr(self.idempotent_key, 'to_alipay_dict'):
                params['idempotent_key'] = self.idempotent_key.to_alipay_dict()
            else:
                params['idempotent_key'] = self.idempotent_key
        if self.job_info:
            if hasattr(self.job_info, 'to_alipay_dict'):
                params['job_info'] = self.job_info.to_alipay_dict()
            else:
                params['job_info'] = self.job_info
        if self.user_info:
            if hasattr(self.user_info, 'to_alipay_dict'):
                params['user_info'] = self.user_info.to_alipay_dict()
            else:
                params['user_info'] = self.user_info
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ResourceAihrInterviewRoomCreateModel()
        if 'ai_interview_code' in d:
            o.ai_interview_code = d['ai_interview_code']
        if 'channel' in d:
            o.channel = d['channel']
        if 'idempotent_key' in d:
            o.idempotent_key = d['idempotent_key']
        if 'job_info' in d:
            o.job_info = d['job_info']
        if 'user_info' in d:
            o.user_info = d['user_info']
        return o


