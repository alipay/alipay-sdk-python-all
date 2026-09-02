#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ResourceAihrInterviewReportBatchqueryModel(object):

    def __init__(self):
        self._ai_interview_id_list = None
        self._channel = None

    @property
    def ai_interview_id_list(self):
        return self._ai_interview_id_list

    @ai_interview_id_list.setter
    def ai_interview_id_list(self, value):
        if isinstance(value, list):
            self._ai_interview_id_list = list()
            for i in value:
                self._ai_interview_id_list.append(i)
    @property
    def channel(self):
        return self._channel

    @channel.setter
    def channel(self, value):
        self._channel = value


    def to_alipay_dict(self):
        params = dict()
        if self.ai_interview_id_list:
            if isinstance(self.ai_interview_id_list, list):
                for i in range(0, len(self.ai_interview_id_list)):
                    element = self.ai_interview_id_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.ai_interview_id_list[i] = element.to_alipay_dict()
            if hasattr(self.ai_interview_id_list, 'to_alipay_dict'):
                params['ai_interview_id_list'] = self.ai_interview_id_list.to_alipay_dict()
            else:
                params['ai_interview_id_list'] = self.ai_interview_id_list
        if self.channel:
            if hasattr(self.channel, 'to_alipay_dict'):
                params['channel'] = self.channel.to_alipay_dict()
            else:
                params['channel'] = self.channel
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ResourceAihrInterviewReportBatchqueryModel()
        if 'ai_interview_id_list' in d:
            o.ai_interview_id_list = d['ai_interview_id_list']
        if 'channel' in d:
            o.channel = d['channel']
        return o


