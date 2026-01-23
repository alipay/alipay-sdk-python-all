#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class LlmChatHistoryVO(object):

    def __init__(self):
        self._agent_id = None
        self._biz_info = None
        self._chat_id = None
        self._chat_type = None
        self._content = None
        self._open_id = None
        self._query = None
        self._query_type = None
        self._session_id = None
        self._template_data = None
        self._template_id = None
        self._template_type = None
        self._time = None
        self._user_id = None

    @property
    def agent_id(self):
        return self._agent_id

    @agent_id.setter
    def agent_id(self, value):
        self._agent_id = value
    @property
    def biz_info(self):
        return self._biz_info

    @biz_info.setter
    def biz_info(self, value):
        self._biz_info = value
    @property
    def chat_id(self):
        return self._chat_id

    @chat_id.setter
    def chat_id(self, value):
        self._chat_id = value
    @property
    def chat_type(self):
        return self._chat_type

    @chat_type.setter
    def chat_type(self, value):
        self._chat_type = value
    @property
    def content(self):
        return self._content

    @content.setter
    def content(self, value):
        self._content = value
    @property
    def open_id(self):
        return self._open_id

    @open_id.setter
    def open_id(self, value):
        self._open_id = value
    @property
    def query(self):
        return self._query

    @query.setter
    def query(self, value):
        self._query = value
    @property
    def query_type(self):
        return self._query_type

    @query_type.setter
    def query_type(self, value):
        self._query_type = value
    @property
    def session_id(self):
        return self._session_id

    @session_id.setter
    def session_id(self, value):
        self._session_id = value
    @property
    def template_data(self):
        return self._template_data

    @template_data.setter
    def template_data(self, value):
        self._template_data = value
    @property
    def template_id(self):
        return self._template_id

    @template_id.setter
    def template_id(self, value):
        self._template_id = value
    @property
    def template_type(self):
        return self._template_type

    @template_type.setter
    def template_type(self, value):
        self._template_type = value
    @property
    def time(self):
        return self._time

    @time.setter
    def time(self, value):
        self._time = value
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
        if self.biz_info:
            if hasattr(self.biz_info, 'to_alipay_dict'):
                params['biz_info'] = self.biz_info.to_alipay_dict()
            else:
                params['biz_info'] = self.biz_info
        if self.chat_id:
            if hasattr(self.chat_id, 'to_alipay_dict'):
                params['chat_id'] = self.chat_id.to_alipay_dict()
            else:
                params['chat_id'] = self.chat_id
        if self.chat_type:
            if hasattr(self.chat_type, 'to_alipay_dict'):
                params['chat_type'] = self.chat_type.to_alipay_dict()
            else:
                params['chat_type'] = self.chat_type
        if self.content:
            if hasattr(self.content, 'to_alipay_dict'):
                params['content'] = self.content.to_alipay_dict()
            else:
                params['content'] = self.content
        if self.open_id:
            if hasattr(self.open_id, 'to_alipay_dict'):
                params['open_id'] = self.open_id.to_alipay_dict()
            else:
                params['open_id'] = self.open_id
        if self.query:
            if hasattr(self.query, 'to_alipay_dict'):
                params['query'] = self.query.to_alipay_dict()
            else:
                params['query'] = self.query
        if self.query_type:
            if hasattr(self.query_type, 'to_alipay_dict'):
                params['query_type'] = self.query_type.to_alipay_dict()
            else:
                params['query_type'] = self.query_type
        if self.session_id:
            if hasattr(self.session_id, 'to_alipay_dict'):
                params['session_id'] = self.session_id.to_alipay_dict()
            else:
                params['session_id'] = self.session_id
        if self.template_data:
            if hasattr(self.template_data, 'to_alipay_dict'):
                params['template_data'] = self.template_data.to_alipay_dict()
            else:
                params['template_data'] = self.template_data
        if self.template_id:
            if hasattr(self.template_id, 'to_alipay_dict'):
                params['template_id'] = self.template_id.to_alipay_dict()
            else:
                params['template_id'] = self.template_id
        if self.template_type:
            if hasattr(self.template_type, 'to_alipay_dict'):
                params['template_type'] = self.template_type.to_alipay_dict()
            else:
                params['template_type'] = self.template_type
        if self.time:
            if hasattr(self.time, 'to_alipay_dict'):
                params['time'] = self.time.to_alipay_dict()
            else:
                params['time'] = self.time
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
        o = LlmChatHistoryVO()
        if 'agent_id' in d:
            o.agent_id = d['agent_id']
        if 'biz_info' in d:
            o.biz_info = d['biz_info']
        if 'chat_id' in d:
            o.chat_id = d['chat_id']
        if 'chat_type' in d:
            o.chat_type = d['chat_type']
        if 'content' in d:
            o.content = d['content']
        if 'open_id' in d:
            o.open_id = d['open_id']
        if 'query' in d:
            o.query = d['query']
        if 'query_type' in d:
            o.query_type = d['query_type']
        if 'session_id' in d:
            o.session_id = d['session_id']
        if 'template_data' in d:
            o.template_data = d['template_data']
        if 'template_id' in d:
            o.template_id = d['template_id']
        if 'template_type' in d:
            o.template_type = d['template_type']
        if 'time' in d:
            o.time = d['time']
        if 'user_id' in d:
            o.user_id = d['user_id']
        return o


