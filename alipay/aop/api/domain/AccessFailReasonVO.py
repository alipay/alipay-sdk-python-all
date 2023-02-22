#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AccessFailReasonVO(object):

    def __init__(self):
        self._action_url = None
        self._reason_text = None

    @property
    def action_url(self):
        return self._action_url

    @action_url.setter
    def action_url(self, value):
        self._action_url = value
    @property
    def reason_text(self):
        return self._reason_text

    @reason_text.setter
    def reason_text(self, value):
        self._reason_text = value


    def to_alipay_dict(self):
        params = dict()
        if self.action_url:
            if hasattr(self.action_url, 'to_alipay_dict'):
                params['action_url'] = self.action_url.to_alipay_dict()
            else:
                params['action_url'] = self.action_url
        if self.reason_text:
            if hasattr(self.reason_text, 'to_alipay_dict'):
                params['reason_text'] = self.reason_text.to_alipay_dict()
            else:
                params['reason_text'] = self.reason_text
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AccessFailReasonVO()
        if 'action_url' in d:
            o.action_url = d['action_url']
        if 'reason_text' in d:
            o.reason_text = d['reason_text']
        return o


