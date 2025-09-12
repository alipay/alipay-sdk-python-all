#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class BarLinkInfo(object):

    def __init__(self):
        self._action_code = None
        self._display_name = None
        self._link = None
        self._log_url = None

    @property
    def action_code(self):
        return self._action_code

    @action_code.setter
    def action_code(self, value):
        self._action_code = value
    @property
    def display_name(self):
        return self._display_name

    @display_name.setter
    def display_name(self, value):
        self._display_name = value
    @property
    def link(self):
        return self._link

    @link.setter
    def link(self, value):
        self._link = value
    @property
    def log_url(self):
        return self._log_url

    @log_url.setter
    def log_url(self, value):
        self._log_url = value


    def to_alipay_dict(self):
        params = dict()
        if self.action_code:
            if hasattr(self.action_code, 'to_alipay_dict'):
                params['action_code'] = self.action_code.to_alipay_dict()
            else:
                params['action_code'] = self.action_code
        if self.display_name:
            if hasattr(self.display_name, 'to_alipay_dict'):
                params['display_name'] = self.display_name.to_alipay_dict()
            else:
                params['display_name'] = self.display_name
        if self.link:
            if hasattr(self.link, 'to_alipay_dict'):
                params['link'] = self.link.to_alipay_dict()
            else:
                params['link'] = self.link
        if self.log_url:
            if hasattr(self.log_url, 'to_alipay_dict'):
                params['log_url'] = self.log_url.to_alipay_dict()
            else:
                params['log_url'] = self.log_url
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = BarLinkInfo()
        if 'action_code' in d:
            o.action_code = d['action_code']
        if 'display_name' in d:
            o.display_name = d['display_name']
        if 'link' in d:
            o.link = d['link']
        if 'log_url' in d:
            o.log_url = d['log_url']
        return o


