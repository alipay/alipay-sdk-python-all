#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ChunkConfig(object):

    def __init__(self):
        self._length = None
        self._overlap = None
        self._strategy = None
        self._symbols = None

    @property
    def length(self):
        return self._length

    @length.setter
    def length(self, value):
        self._length = value
    @property
    def overlap(self):
        return self._overlap

    @overlap.setter
    def overlap(self, value):
        self._overlap = value
    @property
    def strategy(self):
        return self._strategy

    @strategy.setter
    def strategy(self, value):
        self._strategy = value
    @property
    def symbols(self):
        return self._symbols

    @symbols.setter
    def symbols(self, value):
        if isinstance(value, list):
            self._symbols = list()
            for i in value:
                self._symbols.append(i)


    def to_alipay_dict(self):
        params = dict()
        if self.length:
            if hasattr(self.length, 'to_alipay_dict'):
                params['length'] = self.length.to_alipay_dict()
            else:
                params['length'] = self.length
        if self.overlap:
            if hasattr(self.overlap, 'to_alipay_dict'):
                params['overlap'] = self.overlap.to_alipay_dict()
            else:
                params['overlap'] = self.overlap
        if self.strategy:
            if hasattr(self.strategy, 'to_alipay_dict'):
                params['strategy'] = self.strategy.to_alipay_dict()
            else:
                params['strategy'] = self.strategy
        if self.symbols:
            if isinstance(self.symbols, list):
                for i in range(0, len(self.symbols)):
                    element = self.symbols[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.symbols[i] = element.to_alipay_dict()
            if hasattr(self.symbols, 'to_alipay_dict'):
                params['symbols'] = self.symbols.to_alipay_dict()
            else:
                params['symbols'] = self.symbols
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ChunkConfig()
        if 'length' in d:
            o.length = d['length']
        if 'overlap' in d:
            o.overlap = d['overlap']
        if 'strategy' in d:
            o.strategy = d['strategy']
        if 'symbols' in d:
            o.symbols = d['symbols']
        return o


