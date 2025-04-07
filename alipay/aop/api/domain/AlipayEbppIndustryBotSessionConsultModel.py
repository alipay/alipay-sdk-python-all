#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.BotBizInfo import BotBizInfo


class AlipayEbppIndustryBotSessionConsultModel(object):

    def __init__(self):
        self._biz_info = None
        self._bot_id = None
        self._channel = None
        self._identify_id = None
        self._open_id = None
        self._query = None
        self._ref_chat_id = None
        self._scene_code = None
        self._session_id = None
        self._stream_output = None
        self._think_output = None
        self._user_id = None

    @property
    def biz_info(self):
        return self._biz_info

    @biz_info.setter
    def biz_info(self, value):
        if isinstance(value, BotBizInfo):
            self._biz_info = value
        else:
            self._biz_info = BotBizInfo.from_alipay_dict(value)
    @property
    def bot_id(self):
        return self._bot_id

    @bot_id.setter
    def bot_id(self, value):
        self._bot_id = value
    @property
    def channel(self):
        return self._channel

    @channel.setter
    def channel(self, value):
        self._channel = value
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
    def query(self):
        return self._query

    @query.setter
    def query(self, value):
        self._query = value
    @property
    def ref_chat_id(self):
        return self._ref_chat_id

    @ref_chat_id.setter
    def ref_chat_id(self, value):
        self._ref_chat_id = value
    @property
    def scene_code(self):
        return self._scene_code

    @scene_code.setter
    def scene_code(self, value):
        self._scene_code = value
    @property
    def session_id(self):
        return self._session_id

    @session_id.setter
    def session_id(self, value):
        self._session_id = value
    @property
    def stream_output(self):
        return self._stream_output

    @stream_output.setter
    def stream_output(self, value):
        self._stream_output = value
    @property
    def think_output(self):
        return self._think_output

    @think_output.setter
    def think_output(self, value):
        self._think_output = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.biz_info:
            if hasattr(self.biz_info, 'to_alipay_dict'):
                params['biz_info'] = self.biz_info.to_alipay_dict()
            else:
                params['biz_info'] = self.biz_info
        if self.bot_id:
            if hasattr(self.bot_id, 'to_alipay_dict'):
                params['bot_id'] = self.bot_id.to_alipay_dict()
            else:
                params['bot_id'] = self.bot_id
        if self.channel:
            if hasattr(self.channel, 'to_alipay_dict'):
                params['channel'] = self.channel.to_alipay_dict()
            else:
                params['channel'] = self.channel
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
        if self.query:
            if hasattr(self.query, 'to_alipay_dict'):
                params['query'] = self.query.to_alipay_dict()
            else:
                params['query'] = self.query
        if self.ref_chat_id:
            if hasattr(self.ref_chat_id, 'to_alipay_dict'):
                params['ref_chat_id'] = self.ref_chat_id.to_alipay_dict()
            else:
                params['ref_chat_id'] = self.ref_chat_id
        if self.scene_code:
            if hasattr(self.scene_code, 'to_alipay_dict'):
                params['scene_code'] = self.scene_code.to_alipay_dict()
            else:
                params['scene_code'] = self.scene_code
        if self.session_id:
            if hasattr(self.session_id, 'to_alipay_dict'):
                params['session_id'] = self.session_id.to_alipay_dict()
            else:
                params['session_id'] = self.session_id
        if self.stream_output:
            if hasattr(self.stream_output, 'to_alipay_dict'):
                params['stream_output'] = self.stream_output.to_alipay_dict()
            else:
                params['stream_output'] = self.stream_output
        if self.think_output:
            if hasattr(self.think_output, 'to_alipay_dict'):
                params['think_output'] = self.think_output.to_alipay_dict()
            else:
                params['think_output'] = self.think_output
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
        o = AlipayEbppIndustryBotSessionConsultModel()
        if 'biz_info' in d:
            o.biz_info = d['biz_info']
        if 'bot_id' in d:
            o.bot_id = d['bot_id']
        if 'channel' in d:
            o.channel = d['channel']
        if 'identify_id' in d:
            o.identify_id = d['identify_id']
        if 'open_id' in d:
            o.open_id = d['open_id']
        if 'query' in d:
            o.query = d['query']
        if 'ref_chat_id' in d:
            o.ref_chat_id = d['ref_chat_id']
        if 'scene_code' in d:
            o.scene_code = d['scene_code']
        if 'session_id' in d:
            o.session_id = d['session_id']
        if 'stream_output' in d:
            o.stream_output = d['stream_output']
        if 'think_output' in d:
            o.think_output = d['think_output']
        if 'user_id' in d:
            o.user_id = d['user_id']
        return o


