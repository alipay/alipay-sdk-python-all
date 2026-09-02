#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceMedicalHdfopenmqImSendModel(object):

    def __init__(self):
        self._bizid = None
        self._content = None
        self._msgid = None

    @property
    def bizid(self):
        return self._bizid

    @bizid.setter
    def bizid(self, value):
        self._bizid = value
    @property
    def content(self):
        return self._content

    @content.setter
    def content(self, value):
        self._content = value
    @property
    def msgid(self):
        return self._msgid

    @msgid.setter
    def msgid(self, value):
        self._msgid = value


    def to_alipay_dict(self):
        params = dict()
        if self.bizid:
            if hasattr(self.bizid, 'to_alipay_dict'):
                params['bizid'] = self.bizid.to_alipay_dict()
            else:
                params['bizid'] = self.bizid
        if self.content:
            if hasattr(self.content, 'to_alipay_dict'):
                params['content'] = self.content.to_alipay_dict()
            else:
                params['content'] = self.content
        if self.msgid:
            if hasattr(self.msgid, 'to_alipay_dict'):
                params['msgid'] = self.msgid.to_alipay_dict()
            else:
                params['msgid'] = self.msgid
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceMedicalHdfopenmqImSendModel()
        if 'bizid' in d:
            o.bizid = d['bizid']
        if 'content' in d:
            o.content = d['content']
        if 'msgid' in d:
            o.msgid = d['msgid']
        return o


