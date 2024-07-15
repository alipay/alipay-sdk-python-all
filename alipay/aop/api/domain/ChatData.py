#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.ChatChunk import ChatChunk
from alipay.aop.api.domain.ChatError import ChatError
from alipay.aop.api.domain.ChatHeader import ChatHeader


class ChatData(object):

    def __init__(self):
        self._chunk = None
        self._error = None
        self._header = None
        self._type = None

    @property
    def chunk(self):
        return self._chunk

    @chunk.setter
    def chunk(self, value):
        if isinstance(value, ChatChunk):
            self._chunk = value
        else:
            self._chunk = ChatChunk.from_alipay_dict(value)
    @property
    def error(self):
        return self._error

    @error.setter
    def error(self, value):
        if isinstance(value, ChatError):
            self._error = value
        else:
            self._error = ChatError.from_alipay_dict(value)
    @property
    def header(self):
        return self._header

    @header.setter
    def header(self, value):
        if isinstance(value, ChatHeader):
            self._header = value
        else:
            self._header = ChatHeader.from_alipay_dict(value)
    @property
    def type(self):
        return self._type

    @type.setter
    def type(self, value):
        self._type = value


    def to_alipay_dict(self):
        params = dict()
        if self.chunk:
            if hasattr(self.chunk, 'to_alipay_dict'):
                params['chunk'] = self.chunk.to_alipay_dict()
            else:
                params['chunk'] = self.chunk
        if self.error:
            if hasattr(self.error, 'to_alipay_dict'):
                params['error'] = self.error.to_alipay_dict()
            else:
                params['error'] = self.error
        if self.header:
            if hasattr(self.header, 'to_alipay_dict'):
                params['header'] = self.header.to_alipay_dict()
            else:
                params['header'] = self.header
        if self.type:
            if hasattr(self.type, 'to_alipay_dict'):
                params['type'] = self.type.to_alipay_dict()
            else:
                params['type'] = self.type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ChatData()
        if 'chunk' in d:
            o.chunk = d['chunk']
        if 'error' in d:
            o.error = d['error']
        if 'header' in d:
            o.header = d['header']
        if 'type' in d:
            o.type = d['type']
        return o


