#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.ContentUnit import ContentUnit


class StreamMessage(object):

    def __init__(self):
        self._api_chat_id = None
        self._chat_id = None
        self._contents = None
        self._create_time = None
        self._intention = None
        self._msg_id = None
        self._org_id = None
        self._reply_cmd = None
        self._session_id = None
        self._turn = None

    @property
    def api_chat_id(self):
        return self._api_chat_id

    @api_chat_id.setter
    def api_chat_id(self, value):
        self._api_chat_id = value
    @property
    def chat_id(self):
        return self._chat_id

    @chat_id.setter
    def chat_id(self, value):
        self._chat_id = value
    @property
    def contents(self):
        return self._contents

    @contents.setter
    def contents(self, value):
        if isinstance(value, list):
            self._contents = list()
            for i in value:
                if isinstance(i, ContentUnit):
                    self._contents.append(i)
                else:
                    self._contents.append(ContentUnit.from_alipay_dict(i))
    @property
    def create_time(self):
        return self._create_time

    @create_time.setter
    def create_time(self, value):
        self._create_time = value
    @property
    def intention(self):
        return self._intention

    @intention.setter
    def intention(self, value):
        self._intention = value
    @property
    def msg_id(self):
        return self._msg_id

    @msg_id.setter
    def msg_id(self, value):
        self._msg_id = value
    @property
    def org_id(self):
        return self._org_id

    @org_id.setter
    def org_id(self, value):
        self._org_id = value
    @property
    def reply_cmd(self):
        return self._reply_cmd

    @reply_cmd.setter
    def reply_cmd(self, value):
        self._reply_cmd = value
    @property
    def session_id(self):
        return self._session_id

    @session_id.setter
    def session_id(self, value):
        self._session_id = value
    @property
    def turn(self):
        return self._turn

    @turn.setter
    def turn(self, value):
        self._turn = value


    def to_alipay_dict(self):
        params = dict()
        if self.api_chat_id:
            if hasattr(self.api_chat_id, 'to_alipay_dict'):
                params['api_chat_id'] = self.api_chat_id.to_alipay_dict()
            else:
                params['api_chat_id'] = self.api_chat_id
        if self.chat_id:
            if hasattr(self.chat_id, 'to_alipay_dict'):
                params['chat_id'] = self.chat_id.to_alipay_dict()
            else:
                params['chat_id'] = self.chat_id
        if self.contents:
            if isinstance(self.contents, list):
                for i in range(0, len(self.contents)):
                    element = self.contents[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.contents[i] = element.to_alipay_dict()
            if hasattr(self.contents, 'to_alipay_dict'):
                params['contents'] = self.contents.to_alipay_dict()
            else:
                params['contents'] = self.contents
        if self.create_time:
            if hasattr(self.create_time, 'to_alipay_dict'):
                params['create_time'] = self.create_time.to_alipay_dict()
            else:
                params['create_time'] = self.create_time
        if self.intention:
            if hasattr(self.intention, 'to_alipay_dict'):
                params['intention'] = self.intention.to_alipay_dict()
            else:
                params['intention'] = self.intention
        if self.msg_id:
            if hasattr(self.msg_id, 'to_alipay_dict'):
                params['msg_id'] = self.msg_id.to_alipay_dict()
            else:
                params['msg_id'] = self.msg_id
        if self.org_id:
            if hasattr(self.org_id, 'to_alipay_dict'):
                params['org_id'] = self.org_id.to_alipay_dict()
            else:
                params['org_id'] = self.org_id
        if self.reply_cmd:
            if hasattr(self.reply_cmd, 'to_alipay_dict'):
                params['reply_cmd'] = self.reply_cmd.to_alipay_dict()
            else:
                params['reply_cmd'] = self.reply_cmd
        if self.session_id:
            if hasattr(self.session_id, 'to_alipay_dict'):
                params['session_id'] = self.session_id.to_alipay_dict()
            else:
                params['session_id'] = self.session_id
        if self.turn:
            if hasattr(self.turn, 'to_alipay_dict'):
                params['turn'] = self.turn.to_alipay_dict()
            else:
                params['turn'] = self.turn
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = StreamMessage()
        if 'api_chat_id' in d:
            o.api_chat_id = d['api_chat_id']
        if 'chat_id' in d:
            o.chat_id = d['chat_id']
        if 'contents' in d:
            o.contents = d['contents']
        if 'create_time' in d:
            o.create_time = d['create_time']
        if 'intention' in d:
            o.intention = d['intention']
        if 'msg_id' in d:
            o.msg_id = d['msg_id']
        if 'org_id' in d:
            o.org_id = d['org_id']
        if 'reply_cmd' in d:
            o.reply_cmd = d['reply_cmd']
        if 'session_id' in d:
            o.session_id = d['session_id']
        if 'turn' in d:
            o.turn = d['turn']
        return o


