#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayIserviceCliveReadmessageBatchsendModel(object):

    def __init__(self):
        self._conversation_id = None
        self._message_ids = None
        self._read_time = None

    @property
    def conversation_id(self):
        return self._conversation_id

    @conversation_id.setter
    def conversation_id(self, value):
        self._conversation_id = value
    @property
    def message_ids(self):
        return self._message_ids

    @message_ids.setter
    def message_ids(self, value):
        if isinstance(value, list):
            self._message_ids = list()
            for i in value:
                self._message_ids.append(i)
    @property
    def read_time(self):
        return self._read_time

    @read_time.setter
    def read_time(self, value):
        self._read_time = value


    def to_alipay_dict(self):
        params = dict()
        if self.conversation_id:
            if hasattr(self.conversation_id, 'to_alipay_dict'):
                params['conversation_id'] = self.conversation_id.to_alipay_dict()
            else:
                params['conversation_id'] = self.conversation_id
        if self.message_ids:
            if isinstance(self.message_ids, list):
                for i in range(0, len(self.message_ids)):
                    element = self.message_ids[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.message_ids[i] = element.to_alipay_dict()
            if hasattr(self.message_ids, 'to_alipay_dict'):
                params['message_ids'] = self.message_ids.to_alipay_dict()
            else:
                params['message_ids'] = self.message_ids
        if self.read_time:
            if hasattr(self.read_time, 'to_alipay_dict'):
                params['read_time'] = self.read_time.to_alipay_dict()
            else:
                params['read_time'] = self.read_time
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayIserviceCliveReadmessageBatchsendModel()
        if 'conversation_id' in d:
            o.conversation_id = d['conversation_id']
        if 'message_ids' in d:
            o.message_ids = d['message_ids']
        if 'read_time' in d:
            o.read_time = d['read_time']
        return o


