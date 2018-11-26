#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.TestCaseParam import TestCaseParam


class AlipayEcoAcceptanceTaskCreateModel(object):

    def __init__(self):
        self._case_list = None
        self._channel = None
        self._company_id = None
        self._company_name = None
        self._creator_id = None
        self._creator_nick = None
        self._creator_user_type = None
        self._industry = None
        self._out_id = None
        self._topic = None

    @property
    def case_list(self):
        return self._case_list

    @case_list.setter
    def case_list(self, value):
        if isinstance(value, list):
            self._case_list = list()
            for i in value:
                if isinstance(i, TestCaseParam):
                    self._case_list.append(i)
                else:
                    self._case_list.append(TestCaseParam.from_alipay_dict(i))
    @property
    def channel(self):
        return self._channel

    @channel.setter
    def channel(self, value):
        self._channel = value
    @property
    def company_id(self):
        return self._company_id

    @company_id.setter
    def company_id(self, value):
        self._company_id = value
    @property
    def company_name(self):
        return self._company_name

    @company_name.setter
    def company_name(self, value):
        self._company_name = value
    @property
    def creator_id(self):
        return self._creator_id

    @creator_id.setter
    def creator_id(self, value):
        self._creator_id = value
    @property
    def creator_nick(self):
        return self._creator_nick

    @creator_nick.setter
    def creator_nick(self, value):
        self._creator_nick = value
    @property
    def creator_user_type(self):
        return self._creator_user_type

    @creator_user_type.setter
    def creator_user_type(self, value):
        self._creator_user_type = value
    @property
    def industry(self):
        return self._industry

    @industry.setter
    def industry(self, value):
        self._industry = value
    @property
    def out_id(self):
        return self._out_id

    @out_id.setter
    def out_id(self, value):
        self._out_id = value
    @property
    def topic(self):
        return self._topic

    @topic.setter
    def topic(self, value):
        self._topic = value


    def to_alipay_dict(self):
        params = dict()
        if self.case_list:
            if isinstance(self.case_list, list):
                for i in range(0, len(self.case_list)):
                    element = self.case_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.case_list[i] = element.to_alipay_dict()
            if hasattr(self.case_list, 'to_alipay_dict'):
                params['case_list'] = self.case_list.to_alipay_dict()
            else:
                params['case_list'] = self.case_list
        if self.channel:
            if hasattr(self.channel, 'to_alipay_dict'):
                params['channel'] = self.channel.to_alipay_dict()
            else:
                params['channel'] = self.channel
        if self.company_id:
            if hasattr(self.company_id, 'to_alipay_dict'):
                params['company_id'] = self.company_id.to_alipay_dict()
            else:
                params['company_id'] = self.company_id
        if self.company_name:
            if hasattr(self.company_name, 'to_alipay_dict'):
                params['company_name'] = self.company_name.to_alipay_dict()
            else:
                params['company_name'] = self.company_name
        if self.creator_id:
            if hasattr(self.creator_id, 'to_alipay_dict'):
                params['creator_id'] = self.creator_id.to_alipay_dict()
            else:
                params['creator_id'] = self.creator_id
        if self.creator_nick:
            if hasattr(self.creator_nick, 'to_alipay_dict'):
                params['creator_nick'] = self.creator_nick.to_alipay_dict()
            else:
                params['creator_nick'] = self.creator_nick
        if self.creator_user_type:
            if hasattr(self.creator_user_type, 'to_alipay_dict'):
                params['creator_user_type'] = self.creator_user_type.to_alipay_dict()
            else:
                params['creator_user_type'] = self.creator_user_type
        if self.industry:
            if hasattr(self.industry, 'to_alipay_dict'):
                params['industry'] = self.industry.to_alipay_dict()
            else:
                params['industry'] = self.industry
        if self.out_id:
            if hasattr(self.out_id, 'to_alipay_dict'):
                params['out_id'] = self.out_id.to_alipay_dict()
            else:
                params['out_id'] = self.out_id
        if self.topic:
            if hasattr(self.topic, 'to_alipay_dict'):
                params['topic'] = self.topic.to_alipay_dict()
            else:
                params['topic'] = self.topic
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayEcoAcceptanceTaskCreateModel()
        if 'case_list' in d:
            o.case_list = d['case_list']
        if 'channel' in d:
            o.channel = d['channel']
        if 'company_id' in d:
            o.company_id = d['company_id']
        if 'company_name' in d:
            o.company_name = d['company_name']
        if 'creator_id' in d:
            o.creator_id = d['creator_id']
        if 'creator_nick' in d:
            o.creator_nick = d['creator_nick']
        if 'creator_user_type' in d:
            o.creator_user_type = d['creator_user_type']
        if 'industry' in d:
            o.industry = d['industry']
        if 'out_id' in d:
            o.out_id = d['out_id']
        if 'topic' in d:
            o.topic = d['topic']
        return o


