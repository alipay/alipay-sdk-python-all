#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class TinyGameRes(object):

    def __init__(self):
        self._tiny_game_id = None
        self._tiny_game_name = None

    @property
    def tiny_game_id(self):
        return self._tiny_game_id

    @tiny_game_id.setter
    def tiny_game_id(self, value):
        self._tiny_game_id = value
    @property
    def tiny_game_name(self):
        return self._tiny_game_name

    @tiny_game_name.setter
    def tiny_game_name(self, value):
        self._tiny_game_name = value


    def to_alipay_dict(self):
        params = dict()
        if self.tiny_game_id:
            if hasattr(self.tiny_game_id, 'to_alipay_dict'):
                params['tiny_game_id'] = self.tiny_game_id.to_alipay_dict()
            else:
                params['tiny_game_id'] = self.tiny_game_id
        if self.tiny_game_name:
            if hasattr(self.tiny_game_name, 'to_alipay_dict'):
                params['tiny_game_name'] = self.tiny_game_name.to_alipay_dict()
            else:
                params['tiny_game_name'] = self.tiny_game_name
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = TinyGameRes()
        if 'tiny_game_id' in d:
            o.tiny_game_id = d['tiny_game_id']
        if 'tiny_game_name' in d:
            o.tiny_game_name = d['tiny_game_name']
        return o


