#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayDataDataserviceCodeRecoModel(object):

    def __init__(self):
        self._config = None
        self._content = None
        self._strategy = None

    @property
    def config(self):
        return self._config

    @config.setter
    def config(self, value):
        self._config = value
    @property
    def content(self):
        return self._content

    @content.setter
    def content(self, value):
        self._content = value
    @property
    def strategy(self):
        return self._strategy

    @strategy.setter
    def strategy(self, value):
        self._strategy = value


    def to_alipay_dict(self):
        params = dict()
        if self.config:
            if hasattr(self.config, 'to_alipay_dict'):
                params['config'] = self.config.to_alipay_dict()
            else:
                params['config'] = self.config
        if self.content:
            if hasattr(self.content, 'to_alipay_dict'):
                params['content'] = self.content.to_alipay_dict()
            else:
                params['content'] = self.content
        if self.strategy:
            if hasattr(self.strategy, 'to_alipay_dict'):
                params['strategy'] = self.strategy.to_alipay_dict()
            else:
                params['strategy'] = self.strategy
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayDataDataserviceCodeRecoModel()
        if 'config' in d:
            o.config = d['config']
        if 'content' in d:
            o.content = d['content']
        if 'strategy' in d:
            o.strategy = d['strategy']
        return o


