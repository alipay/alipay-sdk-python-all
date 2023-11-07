#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.LegalAIChatHistory import LegalAIChatHistory


class AlipayBossProdAlusdpChatQueryModel(object):

    def __init__(self):
        self._beam_width = None
        self._chain_name = None
        self._history = None
        self._query = None
        self._scene_name = None
        self._temperature = None
        self._top_k = None
        self._top_p = None

    @property
    def beam_width(self):
        return self._beam_width

    @beam_width.setter
    def beam_width(self, value):
        self._beam_width = value
    @property
    def chain_name(self):
        return self._chain_name

    @chain_name.setter
    def chain_name(self, value):
        self._chain_name = value
    @property
    def history(self):
        return self._history

    @history.setter
    def history(self, value):
        if isinstance(value, list):
            self._history = list()
            for i in value:
                if isinstance(i, LegalAIChatHistory):
                    self._history.append(i)
                else:
                    self._history.append(LegalAIChatHistory.from_alipay_dict(i))
    @property
    def query(self):
        return self._query

    @query.setter
    def query(self, value):
        self._query = value
    @property
    def scene_name(self):
        return self._scene_name

    @scene_name.setter
    def scene_name(self, value):
        self._scene_name = value
    @property
    def temperature(self):
        return self._temperature

    @temperature.setter
    def temperature(self, value):
        self._temperature = value
    @property
    def top_k(self):
        return self._top_k

    @top_k.setter
    def top_k(self, value):
        self._top_k = value
    @property
    def top_p(self):
        return self._top_p

    @top_p.setter
    def top_p(self, value):
        self._top_p = value


    def to_alipay_dict(self):
        params = dict()
        if self.beam_width:
            if hasattr(self.beam_width, 'to_alipay_dict'):
                params['beam_width'] = self.beam_width.to_alipay_dict()
            else:
                params['beam_width'] = self.beam_width
        if self.chain_name:
            if hasattr(self.chain_name, 'to_alipay_dict'):
                params['chain_name'] = self.chain_name.to_alipay_dict()
            else:
                params['chain_name'] = self.chain_name
        if self.history:
            if isinstance(self.history, list):
                for i in range(0, len(self.history)):
                    element = self.history[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.history[i] = element.to_alipay_dict()
            if hasattr(self.history, 'to_alipay_dict'):
                params['history'] = self.history.to_alipay_dict()
            else:
                params['history'] = self.history
        if self.query:
            if hasattr(self.query, 'to_alipay_dict'):
                params['query'] = self.query.to_alipay_dict()
            else:
                params['query'] = self.query
        if self.scene_name:
            if hasattr(self.scene_name, 'to_alipay_dict'):
                params['scene_name'] = self.scene_name.to_alipay_dict()
            else:
                params['scene_name'] = self.scene_name
        if self.temperature:
            if hasattr(self.temperature, 'to_alipay_dict'):
                params['temperature'] = self.temperature.to_alipay_dict()
            else:
                params['temperature'] = self.temperature
        if self.top_k:
            if hasattr(self.top_k, 'to_alipay_dict'):
                params['top_k'] = self.top_k.to_alipay_dict()
            else:
                params['top_k'] = self.top_k
        if self.top_p:
            if hasattr(self.top_p, 'to_alipay_dict'):
                params['top_p'] = self.top_p.to_alipay_dict()
            else:
                params['top_p'] = self.top_p
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayBossProdAlusdpChatQueryModel()
        if 'beam_width' in d:
            o.beam_width = d['beam_width']
        if 'chain_name' in d:
            o.chain_name = d['chain_name']
        if 'history' in d:
            o.history = d['history']
        if 'query' in d:
            o.query = d['query']
        if 'scene_name' in d:
            o.scene_name = d['scene_name']
        if 'temperature' in d:
            o.temperature = d['temperature']
        if 'top_k' in d:
            o.top_k = d['top_k']
        if 'top_p' in d:
            o.top_p = d['top_p']
        return o


