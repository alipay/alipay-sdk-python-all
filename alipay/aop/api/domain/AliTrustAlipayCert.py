#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AliTrustAlipayCert(object):

    def __init__(self):
        self._birthday = None
        self._forward_url = None
        self._gender = None
        self._icon_url = None
        self._is_certified = None
        self._name = None

    @property
    def birthday(self):
        return self._birthday

    @birthday.setter
    def birthday(self, value):
        self._birthday = value
    @property
    def forward_url(self):
        return self._forward_url

    @forward_url.setter
    def forward_url(self, value):
        self._forward_url = value
    @property
    def gender(self):
        return self._gender

    @gender.setter
    def gender(self, value):
        self._gender = value
    @property
    def icon_url(self):
        return self._icon_url

    @icon_url.setter
    def icon_url(self, value):
        self._icon_url = value
    @property
    def is_certified(self):
        return self._is_certified

    @is_certified.setter
    def is_certified(self, value):
        self._is_certified = value
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value


    def to_alipay_dict(self):
        params = dict()
        if self.birthday:
            if hasattr(self.birthday, 'to_alipay_dict'):
                params['birthday'] = self.birthday.to_alipay_dict()
            else:
                params['birthday'] = self.birthday
        if self.forward_url:
            if hasattr(self.forward_url, 'to_alipay_dict'):
                params['forward_url'] = self.forward_url.to_alipay_dict()
            else:
                params['forward_url'] = self.forward_url
        if self.gender:
            if hasattr(self.gender, 'to_alipay_dict'):
                params['gender'] = self.gender.to_alipay_dict()
            else:
                params['gender'] = self.gender
        if self.icon_url:
            if hasattr(self.icon_url, 'to_alipay_dict'):
                params['icon_url'] = self.icon_url.to_alipay_dict()
            else:
                params['icon_url'] = self.icon_url
        if self.is_certified:
            if hasattr(self.is_certified, 'to_alipay_dict'):
                params['is_certified'] = self.is_certified.to_alipay_dict()
            else:
                params['is_certified'] = self.is_certified
        if self.name:
            if hasattr(self.name, 'to_alipay_dict'):
                params['name'] = self.name.to_alipay_dict()
            else:
                params['name'] = self.name
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AliTrustAlipayCert()
        if 'birthday' in d:
            o.birthday = d['birthday']
        if 'forward_url' in d:
            o.forward_url = d['forward_url']
        if 'gender' in d:
            o.gender = d['gender']
        if 'icon_url' in d:
            o.icon_url = d['icon_url']
        if 'is_certified' in d:
            o.is_certified = d['is_certified']
        if 'name' in d:
            o.name = d['name']
        return o


