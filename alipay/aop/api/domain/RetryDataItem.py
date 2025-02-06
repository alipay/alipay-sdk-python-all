#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class RetryDataItem(object):

    def __init__(self):
        self._biz_id = None
        self._biz_messages = None

    @property
    def biz_id(self):
        return self._biz_id

    @biz_id.setter
    def biz_id(self, value):
        self._biz_id = value
    @property
    def biz_messages(self):
        return self._biz_messages

    @biz_messages.setter
    def biz_messages(self, value):
        if isinstance(value, list):
            self._biz_messages = list()
            for i in value:
                self._biz_messages.append(i)


    def to_alipay_dict(self):
        params = dict()
        if self.biz_id:
            if hasattr(self.biz_id, 'to_alipay_dict'):
                params['biz_id'] = self.biz_id.to_alipay_dict()
            else:
                params['biz_id'] = self.biz_id
        if self.biz_messages:
            if isinstance(self.biz_messages, list):
                for i in range(0, len(self.biz_messages)):
                    element = self.biz_messages[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.biz_messages[i] = element.to_alipay_dict()
            if hasattr(self.biz_messages, 'to_alipay_dict'):
                params['biz_messages'] = self.biz_messages.to_alipay_dict()
            else:
                params['biz_messages'] = self.biz_messages
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = RetryDataItem()
        if 'biz_id' in d:
            o.biz_id = d['biz_id']
        if 'biz_messages' in d:
            o.biz_messages = d['biz_messages']
        return o


