#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayEcoDingMessageNotifyModel(object):

    def __init__(self):
        self._at_mobiles = None
        self._content = None
        self._ding_token = None

    @property
    def at_mobiles(self):
        return self._at_mobiles

    @at_mobiles.setter
    def at_mobiles(self, value):
        self._at_mobiles = value
    @property
    def content(self):
        return self._content

    @content.setter
    def content(self, value):
        self._content = value
    @property
    def ding_token(self):
        return self._ding_token

    @ding_token.setter
    def ding_token(self, value):
        self._ding_token = value


    def to_alipay_dict(self):
        params = dict()
        if self.at_mobiles:
            if hasattr(self.at_mobiles, 'to_alipay_dict'):
                params['at_mobiles'] = self.at_mobiles.to_alipay_dict()
            else:
                params['at_mobiles'] = self.at_mobiles
        if self.content:
            if hasattr(self.content, 'to_alipay_dict'):
                params['content'] = self.content.to_alipay_dict()
            else:
                params['content'] = self.content
        if self.ding_token:
            if hasattr(self.ding_token, 'to_alipay_dict'):
                params['ding_token'] = self.ding_token.to_alipay_dict()
            else:
                params['ding_token'] = self.ding_token
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayEcoDingMessageNotifyModel()
        if 'at_mobiles' in d:
            o.at_mobiles = d['at_mobiles']
        if 'content' in d:
            o.content = d['content']
        if 'ding_token' in d:
            o.ding_token = d['ding_token']
        return o


