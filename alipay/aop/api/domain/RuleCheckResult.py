#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class RuleCheckResult(object):

    def __init__(self):
        self._action = None
        self._display_text = None
        self._display_title = None

    @property
    def action(self):
        return self._action

    @action.setter
    def action(self, value):
        self._action = value
    @property
    def display_text(self):
        return self._display_text

    @display_text.setter
    def display_text(self, value):
        self._display_text = value
    @property
    def display_title(self):
        return self._display_title

    @display_title.setter
    def display_title(self, value):
        self._display_title = value


    def to_alipay_dict(self):
        params = dict()
        if self.action:
            if hasattr(self.action, 'to_alipay_dict'):
                params['action'] = self.action.to_alipay_dict()
            else:
                params['action'] = self.action
        if self.display_text:
            if hasattr(self.display_text, 'to_alipay_dict'):
                params['display_text'] = self.display_text.to_alipay_dict()
            else:
                params['display_text'] = self.display_text
        if self.display_title:
            if hasattr(self.display_title, 'to_alipay_dict'):
                params['display_title'] = self.display_title.to_alipay_dict()
            else:
                params['display_title'] = self.display_title
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = RuleCheckResult()
        if 'action' in d:
            o.action = d['action']
        if 'display_text' in d:
            o.display_text = d['display_text']
        if 'display_title' in d:
            o.display_title = d['display_title']
        return o


