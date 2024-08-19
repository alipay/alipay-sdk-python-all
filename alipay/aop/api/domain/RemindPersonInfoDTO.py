#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class RemindPersonInfoDTO(object):

    def __init__(self):
        self._channel_list = None
        self._email = None
        self._mobile = None
        self._name = None

    @property
    def channel_list(self):
        return self._channel_list

    @channel_list.setter
    def channel_list(self, value):
        if isinstance(value, list):
            self._channel_list = list()
            for i in value:
                self._channel_list.append(i)
    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, value):
        self._email = value
    @property
    def mobile(self):
        return self._mobile

    @mobile.setter
    def mobile(self, value):
        self._mobile = value
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value


    def to_alipay_dict(self):
        params = dict()
        if self.channel_list:
            if isinstance(self.channel_list, list):
                for i in range(0, len(self.channel_list)):
                    element = self.channel_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.channel_list[i] = element.to_alipay_dict()
            if hasattr(self.channel_list, 'to_alipay_dict'):
                params['channel_list'] = self.channel_list.to_alipay_dict()
            else:
                params['channel_list'] = self.channel_list
        if self.email:
            if hasattr(self.email, 'to_alipay_dict'):
                params['email'] = self.email.to_alipay_dict()
            else:
                params['email'] = self.email
        if self.mobile:
            if hasattr(self.mobile, 'to_alipay_dict'):
                params['mobile'] = self.mobile.to_alipay_dict()
            else:
                params['mobile'] = self.mobile
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
        o = RemindPersonInfoDTO()
        if 'channel_list' in d:
            o.channel_list = d['channel_list']
        if 'email' in d:
            o.email = d['email']
        if 'mobile' in d:
            o.mobile = d['mobile']
        if 'name' in d:
            o.name = d['name']
        return o


