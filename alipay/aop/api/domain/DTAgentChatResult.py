#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.DTAgentChatContent import DTAgentChatContent


class DTAgentChatResult(object):

    def __init__(self):
        self._chat_contents = None
        self._chat_message_id = None

    @property
    def chat_contents(self):
        return self._chat_contents

    @chat_contents.setter
    def chat_contents(self, value):
        if isinstance(value, list):
            self._chat_contents = list()
            for i in value:
                if isinstance(i, DTAgentChatContent):
                    self._chat_contents.append(i)
                else:
                    self._chat_contents.append(DTAgentChatContent.from_alipay_dict(i))
    @property
    def chat_message_id(self):
        return self._chat_message_id

    @chat_message_id.setter
    def chat_message_id(self, value):
        self._chat_message_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.chat_contents:
            if isinstance(self.chat_contents, list):
                for i in range(0, len(self.chat_contents)):
                    element = self.chat_contents[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.chat_contents[i] = element.to_alipay_dict()
            if hasattr(self.chat_contents, 'to_alipay_dict'):
                params['chat_contents'] = self.chat_contents.to_alipay_dict()
            else:
                params['chat_contents'] = self.chat_contents
        if self.chat_message_id:
            if hasattr(self.chat_message_id, 'to_alipay_dict'):
                params['chat_message_id'] = self.chat_message_id.to_alipay_dict()
            else:
                params['chat_message_id'] = self.chat_message_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = DTAgentChatResult()
        if 'chat_contents' in d:
            o.chat_contents = d['chat_contents']
        if 'chat_message_id' in d:
            o.chat_message_id = d['chat_message_id']
        return o


