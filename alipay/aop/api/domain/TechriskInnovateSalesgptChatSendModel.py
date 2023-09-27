#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class TechriskInnovateSalesgptChatSendModel(object):

    def __init__(self):
        self._chat_bot_id = None
        self._mer_pid = None
        self._message_content = None
        self._message_type = None
        self._open_id = None
        self._source_app_id = None
        self._user_id = None

    @property
    def chat_bot_id(self):
        return self._chat_bot_id

    @chat_bot_id.setter
    def chat_bot_id(self, value):
        self._chat_bot_id = value
    @property
    def mer_pid(self):
        return self._mer_pid

    @mer_pid.setter
    def mer_pid(self, value):
        self._mer_pid = value
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
    def open_id(self):
        return self._open_id

    @open_id.setter
    def open_id(self, value):
        self._open_id = value
    @property
    def source_app_id(self):
        return self._source_app_id

    @source_app_id.setter
    def source_app_id(self, value):
        self._source_app_id = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.chat_bot_id:
            if hasattr(self.chat_bot_id, 'to_alipay_dict'):
                params['chat_bot_id'] = self.chat_bot_id.to_alipay_dict()
            else:
                params['chat_bot_id'] = self.chat_bot_id
        if self.mer_pid:
            if hasattr(self.mer_pid, 'to_alipay_dict'):
                params['mer_pid'] = self.mer_pid.to_alipay_dict()
            else:
                params['mer_pid'] = self.mer_pid
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
        if self.open_id:
            if hasattr(self.open_id, 'to_alipay_dict'):
                params['open_id'] = self.open_id.to_alipay_dict()
            else:
                params['open_id'] = self.open_id
        if self.source_app_id:
            if hasattr(self.source_app_id, 'to_alipay_dict'):
                params['source_app_id'] = self.source_app_id.to_alipay_dict()
            else:
                params['source_app_id'] = self.source_app_id
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
        o = TechriskInnovateSalesgptChatSendModel()
        if 'chat_bot_id' in d:
            o.chat_bot_id = d['chat_bot_id']
        if 'mer_pid' in d:
            o.mer_pid = d['mer_pid']
        if 'message_content' in d:
            o.message_content = d['message_content']
        if 'message_type' in d:
            o.message_type = d['message_type']
        if 'open_id' in d:
            o.open_id = d['open_id']
        if 'source_app_id' in d:
            o.source_app_id = d['source_app_id']
        if 'user_id' in d:
            o.user_id = d['user_id']
        return o


