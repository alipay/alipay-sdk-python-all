#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class PromoActivityAccessActionVO(object):

    def __init__(self):
        self._action_text = None
        self._action_url = None

    @property
    def action_text(self):
        return self._action_text

    @action_text.setter
    def action_text(self, value):
        self._action_text = value
    @property
    def action_url(self):
        return self._action_url

    @action_url.setter
    def action_url(self, value):
        self._action_url = value


    def to_alipay_dict(self):
        params = dict()
        if self.action_text:
            if hasattr(self.action_text, 'to_alipay_dict'):
                params['action_text'] = self.action_text.to_alipay_dict()
            else:
                params['action_text'] = self.action_text
        if self.action_url:
            if hasattr(self.action_url, 'to_alipay_dict'):
                params['action_url'] = self.action_url.to_alipay_dict()
            else:
                params['action_url'] = self.action_url
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = PromoActivityAccessActionVO()
        if 'action_text' in d:
            o.action_text = d['action_text']
        if 'action_url' in d:
            o.action_url = d['action_url']
        return o


