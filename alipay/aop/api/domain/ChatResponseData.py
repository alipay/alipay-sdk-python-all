#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.ChatUsage import ChatUsage


class ChatResponseData(object):

    def __init__(self):
        self._agent_id = None
        self._agent_version = None
        self._bot_id = None
        self._bot_version = None
        self._business_data = None
        self._chat_id = None
        self._completed_time = None
        self._content = None
        self._content_type = None
        self._conversation_id = None
        self._created_time = None
        self._last_error = None
        self._message_id = None
        self._role = None
        self._status = None
        self._type = None
        self._updated_time = None
        self._usage = None

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
    def bot_id(self):
        return self._bot_id

    @bot_id.setter
    def bot_id(self, value):
        self._bot_id = value
    @property
    def bot_version(self):
        return self._bot_version

    @bot_version.setter
    def bot_version(self, value):
        self._bot_version = value
    @property
    def business_data(self):
        return self._business_data

    @business_data.setter
    def business_data(self, value):
        self._business_data = value
    @property
    def chat_id(self):
        return self._chat_id

    @chat_id.setter
    def chat_id(self, value):
        self._chat_id = value
    @property
    def completed_time(self):
        return self._completed_time

    @completed_time.setter
    def completed_time(self, value):
        self._completed_time = value
    @property
    def content(self):
        return self._content

    @content.setter
    def content(self, value):
        self._content = value
    @property
    def content_type(self):
        return self._content_type

    @content_type.setter
    def content_type(self, value):
        self._content_type = value
    @property
    def conversation_id(self):
        return self._conversation_id

    @conversation_id.setter
    def conversation_id(self, value):
        self._conversation_id = value
    @property
    def created_time(self):
        return self._created_time

    @created_time.setter
    def created_time(self, value):
        self._created_time = value
    @property
    def last_error(self):
        return self._last_error

    @last_error.setter
    def last_error(self, value):
        self._last_error = value
    @property
    def message_id(self):
        return self._message_id

    @message_id.setter
    def message_id(self, value):
        self._message_id = value
    @property
    def role(self):
        return self._role

    @role.setter
    def role(self, value):
        self._role = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value
    @property
    def type(self):
        return self._type

    @type.setter
    def type(self, value):
        self._type = value
    @property
    def updated_time(self):
        return self._updated_time

    @updated_time.setter
    def updated_time(self, value):
        self._updated_time = value
    @property
    def usage(self):
        return self._usage

    @usage.setter
    def usage(self, value):
        if isinstance(value, ChatUsage):
            self._usage = value
        else:
            self._usage = ChatUsage.from_alipay_dict(value)


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
        if self.bot_id:
            if hasattr(self.bot_id, 'to_alipay_dict'):
                params['bot_id'] = self.bot_id.to_alipay_dict()
            else:
                params['bot_id'] = self.bot_id
        if self.bot_version:
            if hasattr(self.bot_version, 'to_alipay_dict'):
                params['bot_version'] = self.bot_version.to_alipay_dict()
            else:
                params['bot_version'] = self.bot_version
        if self.business_data:
            if hasattr(self.business_data, 'to_alipay_dict'):
                params['business_data'] = self.business_data.to_alipay_dict()
            else:
                params['business_data'] = self.business_data
        if self.chat_id:
            if hasattr(self.chat_id, 'to_alipay_dict'):
                params['chat_id'] = self.chat_id.to_alipay_dict()
            else:
                params['chat_id'] = self.chat_id
        if self.completed_time:
            if hasattr(self.completed_time, 'to_alipay_dict'):
                params['completed_time'] = self.completed_time.to_alipay_dict()
            else:
                params['completed_time'] = self.completed_time
        if self.content:
            if hasattr(self.content, 'to_alipay_dict'):
                params['content'] = self.content.to_alipay_dict()
            else:
                params['content'] = self.content
        if self.content_type:
            if hasattr(self.content_type, 'to_alipay_dict'):
                params['content_type'] = self.content_type.to_alipay_dict()
            else:
                params['content_type'] = self.content_type
        if self.conversation_id:
            if hasattr(self.conversation_id, 'to_alipay_dict'):
                params['conversation_id'] = self.conversation_id.to_alipay_dict()
            else:
                params['conversation_id'] = self.conversation_id
        if self.created_time:
            if hasattr(self.created_time, 'to_alipay_dict'):
                params['created_time'] = self.created_time.to_alipay_dict()
            else:
                params['created_time'] = self.created_time
        if self.last_error:
            if hasattr(self.last_error, 'to_alipay_dict'):
                params['last_error'] = self.last_error.to_alipay_dict()
            else:
                params['last_error'] = self.last_error
        if self.message_id:
            if hasattr(self.message_id, 'to_alipay_dict'):
                params['message_id'] = self.message_id.to_alipay_dict()
            else:
                params['message_id'] = self.message_id
        if self.role:
            if hasattr(self.role, 'to_alipay_dict'):
                params['role'] = self.role.to_alipay_dict()
            else:
                params['role'] = self.role
        if self.status:
            if hasattr(self.status, 'to_alipay_dict'):
                params['status'] = self.status.to_alipay_dict()
            else:
                params['status'] = self.status
        if self.type:
            if hasattr(self.type, 'to_alipay_dict'):
                params['type'] = self.type.to_alipay_dict()
            else:
                params['type'] = self.type
        if self.updated_time:
            if hasattr(self.updated_time, 'to_alipay_dict'):
                params['updated_time'] = self.updated_time.to_alipay_dict()
            else:
                params['updated_time'] = self.updated_time
        if self.usage:
            if hasattr(self.usage, 'to_alipay_dict'):
                params['usage'] = self.usage.to_alipay_dict()
            else:
                params['usage'] = self.usage
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ChatResponseData()
        if 'agent_id' in d:
            o.agent_id = d['agent_id']
        if 'agent_version' in d:
            o.agent_version = d['agent_version']
        if 'bot_id' in d:
            o.bot_id = d['bot_id']
        if 'bot_version' in d:
            o.bot_version = d['bot_version']
        if 'business_data' in d:
            o.business_data = d['business_data']
        if 'chat_id' in d:
            o.chat_id = d['chat_id']
        if 'completed_time' in d:
            o.completed_time = d['completed_time']
        if 'content' in d:
            o.content = d['content']
        if 'content_type' in d:
            o.content_type = d['content_type']
        if 'conversation_id' in d:
            o.conversation_id = d['conversation_id']
        if 'created_time' in d:
            o.created_time = d['created_time']
        if 'last_error' in d:
            o.last_error = d['last_error']
        if 'message_id' in d:
            o.message_id = d['message_id']
        if 'role' in d:
            o.role = d['role']
        if 'status' in d:
            o.status = d['status']
        if 'type' in d:
            o.type = d['type']
        if 'updated_time' in d:
            o.updated_time = d['updated_time']
        if 'usage' in d:
            o.usage = d['usage']
        return o


