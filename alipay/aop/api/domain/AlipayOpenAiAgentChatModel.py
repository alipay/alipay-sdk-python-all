#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.ChatPayload import ChatPayload
from alipay.aop.api.domain.ChatSpecifications import ChatSpecifications


class AlipayOpenAiAgentChatModel(object):

    def __init__(self):
        self._chat_payload = None
        self._ext_params = None
        self._initiator_id = None
        self._initiator_open_id = None
        self._initiator_type = None
        self._session_id = None
        self._specifications = None

    @property
    def chat_payload(self):
        return self._chat_payload

    @chat_payload.setter
    def chat_payload(self, value):
        if isinstance(value, ChatPayload):
            self._chat_payload = value
        else:
            self._chat_payload = ChatPayload.from_alipay_dict(value)
    @property
    def ext_params(self):
        return self._ext_params

    @ext_params.setter
    def ext_params(self, value):
        self._ext_params = value
    @property
    def initiator_id(self):
        return self._initiator_id

    @initiator_id.setter
    def initiator_id(self, value):
        self._initiator_id = value
    @property
    def initiator_open_id(self):
        return self._initiator_open_id

    @initiator_open_id.setter
    def initiator_open_id(self, value):
        self._initiator_open_id = value
    @property
    def initiator_type(self):
        return self._initiator_type

    @initiator_type.setter
    def initiator_type(self, value):
        self._initiator_type = value
    @property
    def session_id(self):
        return self._session_id

    @session_id.setter
    def session_id(self, value):
        self._session_id = value
    @property
    def specifications(self):
        return self._specifications

    @specifications.setter
    def specifications(self, value):
        if isinstance(value, ChatSpecifications):
            self._specifications = value
        else:
            self._specifications = ChatSpecifications.from_alipay_dict(value)


    def to_alipay_dict(self):
        params = dict()
        if self.chat_payload:
            if hasattr(self.chat_payload, 'to_alipay_dict'):
                params['chat_payload'] = self.chat_payload.to_alipay_dict()
            else:
                params['chat_payload'] = self.chat_payload
        if self.ext_params:
            if hasattr(self.ext_params, 'to_alipay_dict'):
                params['ext_params'] = self.ext_params.to_alipay_dict()
            else:
                params['ext_params'] = self.ext_params
        if self.initiator_id:
            if hasattr(self.initiator_id, 'to_alipay_dict'):
                params['initiator_id'] = self.initiator_id.to_alipay_dict()
            else:
                params['initiator_id'] = self.initiator_id
        if self.initiator_open_id:
            if hasattr(self.initiator_open_id, 'to_alipay_dict'):
                params['initiator_open_id'] = self.initiator_open_id.to_alipay_dict()
            else:
                params['initiator_open_id'] = self.initiator_open_id
        if self.initiator_type:
            if hasattr(self.initiator_type, 'to_alipay_dict'):
                params['initiator_type'] = self.initiator_type.to_alipay_dict()
            else:
                params['initiator_type'] = self.initiator_type
        if self.session_id:
            if hasattr(self.session_id, 'to_alipay_dict'):
                params['session_id'] = self.session_id.to_alipay_dict()
            else:
                params['session_id'] = self.session_id
        if self.specifications:
            if hasattr(self.specifications, 'to_alipay_dict'):
                params['specifications'] = self.specifications.to_alipay_dict()
            else:
                params['specifications'] = self.specifications
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayOpenAiAgentChatModel()
        if 'chat_payload' in d:
            o.chat_payload = d['chat_payload']
        if 'ext_params' in d:
            o.ext_params = d['ext_params']
        if 'initiator_id' in d:
            o.initiator_id = d['initiator_id']
        if 'initiator_open_id' in d:
            o.initiator_open_id = d['initiator_open_id']
        if 'initiator_type' in d:
            o.initiator_type = d['initiator_type']
        if 'session_id' in d:
            o.session_id = d['session_id']
        if 'specifications' in d:
            o.specifications = d['specifications']
        return o


