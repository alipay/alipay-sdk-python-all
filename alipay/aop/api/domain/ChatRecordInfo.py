#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ChatRecordInfo(object):

    def __init__(self):
        self._msg_content = None
        self._nick_name = None

    @property
    def msg_content(self):
        return self._msg_content

    @msg_content.setter
    def msg_content(self, value):
        self._msg_content = value
    @property
    def nick_name(self):
        return self._nick_name

    @nick_name.setter
    def nick_name(self, value):
        self._nick_name = value


    def to_alipay_dict(self):
        params = dict()
        if self.msg_content:
            if hasattr(self.msg_content, 'to_alipay_dict'):
                params['msg_content'] = self.msg_content.to_alipay_dict()
            else:
                params['msg_content'] = self.msg_content
        if self.nick_name:
            if hasattr(self.nick_name, 'to_alipay_dict'):
                params['nick_name'] = self.nick_name.to_alipay_dict()
            else:
                params['nick_name'] = self.nick_name
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ChatRecordInfo()
        if 'msg_content' in d:
            o.msg_content = d['msg_content']
        if 'nick_name' in d:
            o.nick_name = d['nick_name']
        return o


