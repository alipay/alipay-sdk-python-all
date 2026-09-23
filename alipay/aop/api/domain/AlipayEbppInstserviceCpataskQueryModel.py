#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayEbppInstserviceCpataskQueryModel(object):

    def __init__(self):
        self._channel = None
        self._sub_task_id = None
        self._user_id = None

    @property
    def channel(self):
        return self._channel

    @channel.setter
    def channel(self, value):
        self._channel = value
    @property
    def sub_task_id(self):
        return self._sub_task_id

    @sub_task_id.setter
    def sub_task_id(self, value):
        self._sub_task_id = value
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
        if self.sub_task_id:
            if hasattr(self.sub_task_id, 'to_alipay_dict'):
                params['sub_task_id'] = self.sub_task_id.to_alipay_dict()
            else:
                params['sub_task_id'] = self.sub_task_id
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
        o = AlipayEbppInstserviceCpataskQueryModel()
        if 'channel' in d:
            o.channel = d['channel']
        if 'sub_task_id' in d:
            o.sub_task_id = d['sub_task_id']
        if 'user_id' in d:
            o.user_id = d['user_id']
        return o


