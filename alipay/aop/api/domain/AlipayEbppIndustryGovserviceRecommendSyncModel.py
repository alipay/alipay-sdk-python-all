#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.FeedbackRecord import FeedbackRecord


class AlipayEbppIndustryGovserviceRecommendSyncModel(object):

    def __init__(self):
        self._channel = None
        self._feedback_record_list = None
        self._identify_id = None
        self._open_id = None
        self._pid = None
        self._user_id = None

    @property
    def channel(self):
        return self._channel

    @channel.setter
    def channel(self, value):
        self._channel = value
    @property
    def feedback_record_list(self):
        return self._feedback_record_list

    @feedback_record_list.setter
    def feedback_record_list(self, value):
        if isinstance(value, list):
            self._feedback_record_list = list()
            for i in value:
                if isinstance(i, FeedbackRecord):
                    self._feedback_record_list.append(i)
                else:
                    self._feedback_record_list.append(FeedbackRecord.from_alipay_dict(i))
    @property
    def identify_id(self):
        return self._identify_id

    @identify_id.setter
    def identify_id(self, value):
        self._identify_id = value
    @property
    def open_id(self):
        return self._open_id

    @open_id.setter
    def open_id(self, value):
        self._open_id = value
    @property
    def pid(self):
        return self._pid

    @pid.setter
    def pid(self, value):
        self._pid = value
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
        if self.feedback_record_list:
            if isinstance(self.feedback_record_list, list):
                for i in range(0, len(self.feedback_record_list)):
                    element = self.feedback_record_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.feedback_record_list[i] = element.to_alipay_dict()
            if hasattr(self.feedback_record_list, 'to_alipay_dict'):
                params['feedback_record_list'] = self.feedback_record_list.to_alipay_dict()
            else:
                params['feedback_record_list'] = self.feedback_record_list
        if self.identify_id:
            if hasattr(self.identify_id, 'to_alipay_dict'):
                params['identify_id'] = self.identify_id.to_alipay_dict()
            else:
                params['identify_id'] = self.identify_id
        if self.open_id:
            if hasattr(self.open_id, 'to_alipay_dict'):
                params['open_id'] = self.open_id.to_alipay_dict()
            else:
                params['open_id'] = self.open_id
        if self.pid:
            if hasattr(self.pid, 'to_alipay_dict'):
                params['pid'] = self.pid.to_alipay_dict()
            else:
                params['pid'] = self.pid
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
        o = AlipayEbppIndustryGovserviceRecommendSyncModel()
        if 'channel' in d:
            o.channel = d['channel']
        if 'feedback_record_list' in d:
            o.feedback_record_list = d['feedback_record_list']
        if 'identify_id' in d:
            o.identify_id = d['identify_id']
        if 'open_id' in d:
            o.open_id = d['open_id']
        if 'pid' in d:
            o.pid = d['pid']
        if 'user_id' in d:
            o.user_id = d['user_id']
        return o


