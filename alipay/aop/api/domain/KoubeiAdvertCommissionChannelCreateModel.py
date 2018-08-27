#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.KbAdvertAddChannelRequest import KbAdvertAddChannelRequest


class KoubeiAdvertCommissionChannelCreateModel(object):

    def __init__(self):
        self._channels = None

    @property
    def channels(self):
        return self._channels

    @channels.setter
    def channels(self, value):
        if isinstance(value, list):
            self._channels = list()
            for i in value:
                if isinstance(i, KbAdvertAddChannelRequest):
                    self._channels.append(i)
                else:
                    self._channels.append(KbAdvertAddChannelRequest.from_alipay_dict(i))


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
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = KoubeiAdvertCommissionChannelCreateModel()
        if 'channels' in d:
            o.channels = d['channels']
        return o


