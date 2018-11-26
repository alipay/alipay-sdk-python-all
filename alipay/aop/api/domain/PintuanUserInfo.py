#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class PintuanUserInfo(object):

    def __init__(self):
        self._avatar_url = None
        self._havana_id = None
        self._nick_name = None

    @property
    def avatar_url(self):
        return self._avatar_url

    @avatar_url.setter
    def avatar_url(self, value):
        self._avatar_url = value
    @property
    def havana_id(self):
        return self._havana_id

    @havana_id.setter
    def havana_id(self, value):
        self._havana_id = value
    @property
    def nick_name(self):
        return self._nick_name

    @nick_name.setter
    def nick_name(self, value):
        self._nick_name = value


    def to_alipay_dict(self):
        params = dict()
        if self.avatar_url:
            if hasattr(self.avatar_url, 'to_alipay_dict'):
                params['avatar_url'] = self.avatar_url.to_alipay_dict()
            else:
                params['avatar_url'] = self.avatar_url
        if self.havana_id:
            if hasattr(self.havana_id, 'to_alipay_dict'):
                params['havana_id'] = self.havana_id.to_alipay_dict()
            else:
                params['havana_id'] = self.havana_id
        if self.nick_name:
            if hasattr(self.nick_name, 'to_alipay_dict'):
                params['nick_name'] = self.nick_name.to_alipay_dict()
            else:
                params['nick_name'] = self.nick_name
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = PintuanUserInfo()
        if 'avatar_url' in d:
            o.avatar_url = d['avatar_url']
        if 'havana_id' in d:
            o.havana_id = d['havana_id']
        if 'nick_name' in d:
            o.nick_name = d['nick_name']
        return o


