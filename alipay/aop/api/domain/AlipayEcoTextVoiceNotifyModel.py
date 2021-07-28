#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.SpiVoiceCallback import SpiVoiceCallback


class AlipayEcoTextVoiceNotifyModel(object):

    def __init__(self):
        self._callbacks = None

    @property
    def callbacks(self):
        return self._callbacks

    @callbacks.setter
    def callbacks(self, value):
        if isinstance(value, list):
            self._callbacks = list()
            for i in value:
                if isinstance(i, SpiVoiceCallback):
                    self._callbacks.append(i)
                else:
                    self._callbacks.append(SpiVoiceCallback.from_alipay_dict(i))


    def to_alipay_dict(self):
        params = dict()
        if self.callbacks:
            if isinstance(self.callbacks, list):
                for i in range(0, len(self.callbacks)):
                    element = self.callbacks[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.callbacks[i] = element.to_alipay_dict()
            if hasattr(self.callbacks, 'to_alipay_dict'):
                params['callbacks'] = self.callbacks.to_alipay_dict()
            else:
                params['callbacks'] = self.callbacks
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayEcoTextVoiceNotifyModel()
        if 'callbacks' in d:
            o.callbacks = d['callbacks']
        return o


