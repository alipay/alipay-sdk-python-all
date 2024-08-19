#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AIChatWelcomeMessage(object):

    def __init__(self):
        self._msgtype = None
        self._text = None

    @property
    def msgtype(self):
        return self._msgtype

    @msgtype.setter
    def msgtype(self, value):
        self._msgtype = value
    @property
    def text(self):
        return self._text

    @text.setter
    def text(self, value):
        self._text = value


    def to_alipay_dict(self):
        params = dict()
        if self.msgtype:
            if hasattr(self.msgtype, 'to_alipay_dict'):
                params['msgtype'] = self.msgtype.to_alipay_dict()
            else:
                params['msgtype'] = self.msgtype
        if self.text:
            if hasattr(self.text, 'to_alipay_dict'):
                params['text'] = self.text.to_alipay_dict()
            else:
                params['text'] = self.text
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AIChatWelcomeMessage()
        if 'msgtype' in d:
            o.msgtype = d['msgtype']
        if 'text' in d:
            o.text = d['text']
        return o


