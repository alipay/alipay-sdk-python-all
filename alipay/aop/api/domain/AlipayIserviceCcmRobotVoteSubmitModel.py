#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayIserviceCcmRobotVoteSubmitModel(object):

    def __init__(self):
        self._chat_uuid = None
        self._session_id = None
        self._vote_type = None

    @property
    def chat_uuid(self):
        return self._chat_uuid

    @chat_uuid.setter
    def chat_uuid(self, value):
        self._chat_uuid = value
    @property
    def session_id(self):
        return self._session_id

    @session_id.setter
    def session_id(self, value):
        self._session_id = value
    @property
    def vote_type(self):
        return self._vote_type

    @vote_type.setter
    def vote_type(self, value):
        self._vote_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.chat_uuid:
            if hasattr(self.chat_uuid, 'to_alipay_dict'):
                params['chat_uuid'] = self.chat_uuid.to_alipay_dict()
            else:
                params['chat_uuid'] = self.chat_uuid
        if self.session_id:
            if hasattr(self.session_id, 'to_alipay_dict'):
                params['session_id'] = self.session_id.to_alipay_dict()
            else:
                params['session_id'] = self.session_id
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
        o = AlipayIserviceCcmRobotVoteSubmitModel()
        if 'chat_uuid' in d:
            o.chat_uuid = d['chat_uuid']
        if 'session_id' in d:
            o.session_id = d['session_id']
        if 'vote_type' in d:
            o.vote_type = d['vote_type']
        return o


