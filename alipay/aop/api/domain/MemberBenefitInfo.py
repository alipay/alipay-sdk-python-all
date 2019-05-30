#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class MemberBenefitInfo(object):

    def __init__(self):
        self._action_url = None
        self._icon_url = None
        self._title = None
        self._value = None

    @property
    def action_url(self):
        return self._action_url

    @action_url.setter
    def action_url(self, value):
        self._action_url = value
    @property
    def icon_url(self):
        return self._icon_url

    @icon_url.setter
    def icon_url(self, value):
        self._icon_url = value
    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        self._title = value
    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        self._value = value


    def to_alipay_dict(self):
        params = dict()
        if self.action_url:
            if hasattr(self.action_url, 'to_alipay_dict'):
                params['action_url'] = self.action_url.to_alipay_dict()
            else:
                params['action_url'] = self.action_url
        if self.icon_url:
            if hasattr(self.icon_url, 'to_alipay_dict'):
                params['icon_url'] = self.icon_url.to_alipay_dict()
            else:
                params['icon_url'] = self.icon_url
        if self.title:
            if hasattr(self.title, 'to_alipay_dict'):
                params['title'] = self.title.to_alipay_dict()
            else:
                params['title'] = self.title
        if self.value:
            if hasattr(self.value, 'to_alipay_dict'):
                params['value'] = self.value.to_alipay_dict()
            else:
                params['value'] = self.value
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = MemberBenefitInfo()
        if 'action_url' in d:
            o.action_url = d['action_url']
        if 'icon_url' in d:
            o.icon_url = d['icon_url']
        if 'title' in d:
            o.title = d['title']
        if 'value' in d:
            o.value = d['value']
        return o


