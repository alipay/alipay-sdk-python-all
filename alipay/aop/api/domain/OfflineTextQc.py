#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.QcDialog import QcDialog


class OfflineTextQc(object):

    def __init__(self):
        self._caller_phone = None
        self._channel = None
        self._content = None
        self._incoming_time = None
        self._rounds = None

    @property
    def caller_phone(self):
        return self._caller_phone

    @caller_phone.setter
    def caller_phone(self, value):
        self._caller_phone = value
    @property
    def channel(self):
        return self._channel

    @channel.setter
    def channel(self, value):
        self._channel = value
    @property
    def content(self):
        return self._content

    @content.setter
    def content(self, value):
        if isinstance(value, list):
            self._content = list()
            for i in value:
                if isinstance(i, QcDialog):
                    self._content.append(i)
                else:
                    self._content.append(QcDialog.from_alipay_dict(i))
    @property
    def incoming_time(self):
        return self._incoming_time

    @incoming_time.setter
    def incoming_time(self, value):
        self._incoming_time = value
    @property
    def rounds(self):
        return self._rounds

    @rounds.setter
    def rounds(self, value):
        self._rounds = value


    def to_alipay_dict(self):
        params = dict()
        if self.caller_phone:
            if hasattr(self.caller_phone, 'to_alipay_dict'):
                params['caller_phone'] = self.caller_phone.to_alipay_dict()
            else:
                params['caller_phone'] = self.caller_phone
        if self.channel:
            if hasattr(self.channel, 'to_alipay_dict'):
                params['channel'] = self.channel.to_alipay_dict()
            else:
                params['channel'] = self.channel
        if self.content:
            if isinstance(self.content, list):
                for i in range(0, len(self.content)):
                    element = self.content[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.content[i] = element.to_alipay_dict()
            if hasattr(self.content, 'to_alipay_dict'):
                params['content'] = self.content.to_alipay_dict()
            else:
                params['content'] = self.content
        if self.incoming_time:
            if hasattr(self.incoming_time, 'to_alipay_dict'):
                params['incoming_time'] = self.incoming_time.to_alipay_dict()
            else:
                params['incoming_time'] = self.incoming_time
        if self.rounds:
            if hasattr(self.rounds, 'to_alipay_dict'):
                params['rounds'] = self.rounds.to_alipay_dict()
            else:
                params['rounds'] = self.rounds
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = OfflineTextQc()
        if 'caller_phone' in d:
            o.caller_phone = d['caller_phone']
        if 'channel' in d:
            o.channel = d['channel']
        if 'content' in d:
            o.content = d['content']
        if 'incoming_time' in d:
            o.incoming_time = d['incoming_time']
        if 'rounds' in d:
            o.rounds = d['rounds']
        return o


