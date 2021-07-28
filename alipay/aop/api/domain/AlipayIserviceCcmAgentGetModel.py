#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayIserviceCcmAgentGetModel(object):

    def __init__(self):
        self._external_user_id = None
        self._id = None
        self._job_number = None
        self._user_channel = None

    @property
    def external_user_id(self):
        return self._external_user_id

    @external_user_id.setter
    def external_user_id(self, value):
        self._external_user_id = value
    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        self._id = value
    @property
    def job_number(self):
        return self._job_number

    @job_number.setter
    def job_number(self, value):
        self._job_number = value
    @property
    def user_channel(self):
        return self._user_channel

    @user_channel.setter
    def user_channel(self, value):
        self._user_channel = value


    def to_alipay_dict(self):
        params = dict()
        if self.external_user_id:
            if hasattr(self.external_user_id, 'to_alipay_dict'):
                params['external_user_id'] = self.external_user_id.to_alipay_dict()
            else:
                params['external_user_id'] = self.external_user_id
        if self.id:
            if hasattr(self.id, 'to_alipay_dict'):
                params['id'] = self.id.to_alipay_dict()
            else:
                params['id'] = self.id
        if self.job_number:
            if hasattr(self.job_number, 'to_alipay_dict'):
                params['job_number'] = self.job_number.to_alipay_dict()
            else:
                params['job_number'] = self.job_number
        if self.user_channel:
            if hasattr(self.user_channel, 'to_alipay_dict'):
                params['user_channel'] = self.user_channel.to_alipay_dict()
            else:
                params['user_channel'] = self.user_channel
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayIserviceCcmAgentGetModel()
        if 'external_user_id' in d:
            o.external_user_id = d['external_user_id']
        if 'id' in d:
            o.id = d['id']
        if 'job_number' in d:
            o.job_number = d['job_number']
        if 'user_channel' in d:
            o.user_channel = d['user_channel']
        return o


