#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayEbppIndustryBotVoteSubmitModel(object):

    def __init__(self):
        self._bot_id = None
        self._chat_id = None
        self._identify_id = None
        self._open_id = None
        self._session_id = None
        self._user_id = None
        self._vote_reason = None
        self._vote_type = None

    @property
    def bot_id(self):
        return self._bot_id

    @bot_id.setter
    def bot_id(self, value):
        self._bot_id = value
    @property
    def chat_id(self):
        return self._chat_id

    @chat_id.setter
    def chat_id(self, value):
        self._chat_id = value
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
    @property
    def vote_reason(self):
        return self._vote_reason

    @vote_reason.setter
    def vote_reason(self, value):
        self._vote_reason = value
    @property
    def vote_type(self):
        return self._vote_type

    @vote_type.setter
    def vote_type(self, value):
        self._vote_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.bot_id:
            if hasattr(self.bot_id, 'to_alipay_dict'):
                params['bot_id'] = self.bot_id.to_alipay_dict()
            else:
                params['bot_id'] = self.bot_id
        if self.chat_id:
            if hasattr(self.chat_id, 'to_alipay_dict'):
                params['chat_id'] = self.chat_id.to_alipay_dict()
            else:
                params['chat_id'] = self.chat_id
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
        if self.vote_reason:
            if hasattr(self.vote_reason, 'to_alipay_dict'):
                params['vote_reason'] = self.vote_reason.to_alipay_dict()
            else:
                params['vote_reason'] = self.vote_reason
        if self.vote_type:
            if hasattr(self.vote_type, 'to_alipay_dict'):
                params['vote_type'] = self.vote_type.to_alipay_dict()
            else:
                params['vote_type'] = self.vote_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayEbppIndustryBotVoteSubmitModel()
        if 'bot_id' in d:
            o.bot_id = d['bot_id']
        if 'chat_id' in d:
            o.chat_id = d['chat_id']
        if 'identify_id' in d:
            o.identify_id = d['identify_id']
        if 'open_id' in d:
            o.open_id = d['open_id']
        if 'session_id' in d:
            o.session_id = d['session_id']
        if 'user_id' in d:
            o.user_id = d['user_id']
        if 'vote_reason' in d:
            o.vote_reason = d['vote_reason']
        if 'vote_type' in d:
            o.vote_type = d['vote_type']
        return o


