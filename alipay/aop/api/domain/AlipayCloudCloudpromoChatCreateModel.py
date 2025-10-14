#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.ChatExtraParams import ChatExtraParams
from alipay.aop.api.domain.MediaContent import MediaContent


class AlipayCloudCloudpromoChatCreateModel(object):

    def __init__(self):
        self._agent_id = None
        self._agent_version = None
        self._business_data = None
        self._conversation_id = None
        self._extra_params = None
        self._inc_access_id = None
        self._load_test = None
        self._media_contents = None
        self._question = None
        self._retry = None
        self._session_id = None
        self._user_id = None

    @property
    def agent_id(self):
        return self._agent_id

    @agent_id.setter
    def agent_id(self, value):
        self._agent_id = value
    @property
    def agent_version(self):
        return self._agent_version

    @agent_version.setter
    def agent_version(self, value):
        self._agent_version = value
    @property
    def business_data(self):
        return self._business_data

    @business_data.setter
    def business_data(self, value):
        self._business_data = value
    @property
    def conversation_id(self):
        return self._conversation_id

    @conversation_id.setter
    def conversation_id(self, value):
        self._conversation_id = value
    @property
    def extra_params(self):
        return self._extra_params

    @extra_params.setter
    def extra_params(self, value):
        if isinstance(value, ChatExtraParams):
            self._extra_params = value
        else:
            self._extra_params = ChatExtraParams.from_alipay_dict(value)
    @property
    def inc_access_id(self):
        return self._inc_access_id

    @inc_access_id.setter
    def inc_access_id(self, value):
        self._inc_access_id = value
    @property
    def load_test(self):
        return self._load_test

    @load_test.setter
    def load_test(self, value):
        self._load_test = value
    @property
    def media_contents(self):
        return self._media_contents

    @media_contents.setter
    def media_contents(self, value):
        if isinstance(value, list):
            self._media_contents = list()
            for i in value:
                if isinstance(i, MediaContent):
                    self._media_contents.append(i)
                else:
                    self._media_contents.append(MediaContent.from_alipay_dict(i))
    @property
    def question(self):
        return self._question

    @question.setter
    def question(self, value):
        self._question = value
    @property
    def retry(self):
        return self._retry

    @retry.setter
    def retry(self, value):
        self._retry = value
    @property
    def session_id(self):
        return self._session_id

    @session_id.setter
    def session_id(self, value):
        self._session_id = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.agent_id:
            if hasattr(self.agent_id, 'to_alipay_dict'):
                params['agent_id'] = self.agent_id.to_alipay_dict()
            else:
                params['agent_id'] = self.agent_id
        if self.agent_version:
            if hasattr(self.agent_version, 'to_alipay_dict'):
                params['agent_version'] = self.agent_version.to_alipay_dict()
            else:
                params['agent_version'] = self.agent_version
        if self.business_data:
            if hasattr(self.business_data, 'to_alipay_dict'):
                params['business_data'] = self.business_data.to_alipay_dict()
            else:
                params['business_data'] = self.business_data
        if self.conversation_id:
            if hasattr(self.conversation_id, 'to_alipay_dict'):
                params['conversation_id'] = self.conversation_id.to_alipay_dict()
            else:
                params['conversation_id'] = self.conversation_id
        if self.extra_params:
            if hasattr(self.extra_params, 'to_alipay_dict'):
                params['extra_params'] = self.extra_params.to_alipay_dict()
            else:
                params['extra_params'] = self.extra_params
        if self.inc_access_id:
            if hasattr(self.inc_access_id, 'to_alipay_dict'):
                params['inc_access_id'] = self.inc_access_id.to_alipay_dict()
            else:
                params['inc_access_id'] = self.inc_access_id
        if self.load_test:
            if hasattr(self.load_test, 'to_alipay_dict'):
                params['load_test'] = self.load_test.to_alipay_dict()
            else:
                params['load_test'] = self.load_test
        if self.media_contents:
            if isinstance(self.media_contents, list):
                for i in range(0, len(self.media_contents)):
                    element = self.media_contents[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.media_contents[i] = element.to_alipay_dict()
            if hasattr(self.media_contents, 'to_alipay_dict'):
                params['media_contents'] = self.media_contents.to_alipay_dict()
            else:
                params['media_contents'] = self.media_contents
        if self.question:
            if hasattr(self.question, 'to_alipay_dict'):
                params['question'] = self.question.to_alipay_dict()
            else:
                params['question'] = self.question
        if self.retry:
            if hasattr(self.retry, 'to_alipay_dict'):
                params['retry'] = self.retry.to_alipay_dict()
            else:
                params['retry'] = self.retry
        if self.session_id:
            if hasattr(self.session_id, 'to_alipay_dict'):
                params['session_id'] = self.session_id.to_alipay_dict()
            else:
                params['session_id'] = self.session_id
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
        o = AlipayCloudCloudpromoChatCreateModel()
        if 'agent_id' in d:
            o.agent_id = d['agent_id']
        if 'agent_version' in d:
            o.agent_version = d['agent_version']
        if 'business_data' in d:
            o.business_data = d['business_data']
        if 'conversation_id' in d:
            o.conversation_id = d['conversation_id']
        if 'extra_params' in d:
            o.extra_params = d['extra_params']
        if 'inc_access_id' in d:
            o.inc_access_id = d['inc_access_id']
        if 'load_test' in d:
            o.load_test = d['load_test']
        if 'media_contents' in d:
            o.media_contents = d['media_contents']
        if 'question' in d:
            o.question = d['question']
        if 'retry' in d:
            o.retry = d['retry']
        if 'session_id' in d:
            o.session_id = d['session_id']
        if 'user_id' in d:
            o.user_id = d['user_id']
        return o


