#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.Channels import Channels


class MessageConfig(object):

    def __init__(self):
        self._channels = None
        self._dispatch_mode = None

    @property
    def channels(self):
        return self._channels

    @channels.setter
    def channels(self, value):
        if isinstance(value, list):
            self._channels = list()
            for i in value:
                if isinstance(i, Channels):
                    self._channels.append(i)
                else:
                    self._channels.append(Channels.from_alipay_dict(i))
    @property
    def dispatch_mode(self):
        return self._dispatch_mode

    @dispatch_mode.setter
    def dispatch_mode(self, value):
        self._dispatch_mode = value


    def to_alipay_dict(self):
        params = dict()
        if self.channels:
            if isinstance(self.channels, list):
                for i in range(0, len(self.channels)):
                    element = self.channels[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.channels[i] = element.to_alipay_dict()
            if hasattr(self.channels, 'to_alipay_dict'):
                params['channels'] = self.channels.to_alipay_dict()
            else:
                params['channels'] = self.channels
        if self.dispatch_mode:
            if hasattr(self.dispatch_mode, 'to_alipay_dict'):
                params['dispatch_mode'] = self.dispatch_mode.to_alipay_dict()
            else:
                params['dispatch_mode'] = self.dispatch_mode
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = MessageConfig()
        if 'channels' in d:
            o.channels = d['channels']
        if 'dispatch_mode' in d:
            o.dispatch_mode = d['dispatch_mode']
        return o


