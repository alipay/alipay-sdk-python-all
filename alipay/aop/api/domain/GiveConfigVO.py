#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class GiveConfigVO(object):

    def __init__(self):
        self._give_icon = None
        self._give_title = None
        self._give_url = None
        self._give_url_title = None

    @property
    def give_icon(self):
        return self._give_icon

    @give_icon.setter
    def give_icon(self, value):
        self._give_icon = value
    @property
    def give_title(self):
        return self._give_title

    @give_title.setter
    def give_title(self, value):
        self._give_title = value
    @property
    def give_url(self):
        return self._give_url

    @give_url.setter
    def give_url(self, value):
        self._give_url = value
    @property
    def give_url_title(self):
        return self._give_url_title

    @give_url_title.setter
    def give_url_title(self, value):
        self._give_url_title = value


    def to_alipay_dict(self):
        params = dict()
        if self.give_icon:
            if hasattr(self.give_icon, 'to_alipay_dict'):
                params['give_icon'] = self.give_icon.to_alipay_dict()
            else:
                params['give_icon'] = self.give_icon
        if self.give_title:
            if hasattr(self.give_title, 'to_alipay_dict'):
                params['give_title'] = self.give_title.to_alipay_dict()
            else:
                params['give_title'] = self.give_title
        if self.give_url:
            if hasattr(self.give_url, 'to_alipay_dict'):
                params['give_url'] = self.give_url.to_alipay_dict()
            else:
                params['give_url'] = self.give_url
        if self.give_url_title:
            if hasattr(self.give_url_title, 'to_alipay_dict'):
                params['give_url_title'] = self.give_url_title.to_alipay_dict()
            else:
                params['give_url_title'] = self.give_url_title
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = GiveConfigVO()
        if 'give_icon' in d:
            o.give_icon = d['give_icon']
        if 'give_title' in d:
            o.give_title = d['give_title']
        if 'give_url' in d:
            o.give_url = d['give_url']
        if 'give_url_title' in d:
            o.give_url_title = d['give_url_title']
        return o


