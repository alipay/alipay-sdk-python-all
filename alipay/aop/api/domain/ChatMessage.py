#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ChatMessage(object):

    def __init__(self):
        self._message_content = None
        self._message_type = None
        self._send_time = None
        self._user_name = None
        self._user_type = None

    @property
    def message_content(self):
        return self._message_content

    @message_content.setter
    def message_content(self, value):
        self._message_content = value
    @property
    def message_type(self):
        return self._message_type

    @message_type.setter
    def message_type(self, value):
        self._message_type = value
    @property
    def send_time(self):
        return self._send_time

    @send_time.setter
    def send_time(self, value):
        self._send_time = value
    @property
    def user_name(self):
        return self._user_name

    @user_name.setter
    def user_name(self, value):
        self._user_name = value
    @property
    def user_type(self):
        return self._user_type

    @user_type.setter
    def user_type(self, value):
        self._user_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.message_content:
            if hasattr(self.message_content, 'to_alipay_dict'):
                params['message_content'] = self.message_content.to_alipay_dict()
            else:
                params['message_content'] = self.message_content
        if self.message_type:
            if hasattr(self.message_type, 'to_alipay_dict'):
                params['message_type'] = self.message_type.to_alipay_dict()
            else:
                params['message_type'] = self.message_type
        if self.send_time:
            if hasattr(self.send_time, 'to_alipay_dict'):
                params['send_time'] = self.send_time.to_alipay_dict()
            else:
                params['send_time'] = self.send_time
        if self.user_name:
            if hasattr(self.user_name, 'to_alipay_dict'):
                params['user_name'] = self.user_name.to_alipay_dict()
            else:
                params['user_name'] = self.user_name
        if self.user_type:
            if hasattr(self.user_type, 'to_alipay_dict'):
                params['user_type'] = self.user_type.to_alipay_dict()
            else:
                params['user_type'] = self.user_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ChatMessage()
        if 'message_content' in d:
            o.message_content = d['message_content']
        if 'message_type' in d:
            o.message_type = d['message_type']
        if 'send_time' in d:
            o.send_time = d['send_time']
        if 'user_name' in d:
            o.user_name = d['user_name']
        if 'user_type' in d:
            o.user_type = d['user_type']
        return o


