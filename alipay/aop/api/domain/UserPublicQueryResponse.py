#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class UserPublicQueryResponse(object):

    def __init__(self):
        self._expire_time = None
        self._public_id = None
        self._public_logo = None
        self._public_name = None

    @property
    def expire_time(self):
        return self._expire_time

    @expire_time.setter
    def expire_time(self, value):
        self._expire_time = value
    @property
    def public_id(self):
        return self._public_id

    @public_id.setter
    def public_id(self, value):
        self._public_id = value
    @property
    def public_logo(self):
        return self._public_logo

    @public_logo.setter
    def public_logo(self, value):
        self._public_logo = value
    @property
    def public_name(self):
        return self._public_name

    @public_name.setter
    def public_name(self, value):
        self._public_name = value


    def to_alipay_dict(self):
        params = dict()
        if self.expire_time:
            if hasattr(self.expire_time, 'to_alipay_dict'):
                params['expire_time'] = self.expire_time.to_alipay_dict()
            else:
                params['expire_time'] = self.expire_time
        if self.public_id:
            if hasattr(self.public_id, 'to_alipay_dict'):
                params['public_id'] = self.public_id.to_alipay_dict()
            else:
                params['public_id'] = self.public_id
        if self.public_logo:
            if hasattr(self.public_logo, 'to_alipay_dict'):
                params['public_logo'] = self.public_logo.to_alipay_dict()
            else:
                params['public_logo'] = self.public_logo
        if self.public_name:
            if hasattr(self.public_name, 'to_alipay_dict'):
                params['public_name'] = self.public_name.to_alipay_dict()
            else:
                params['public_name'] = self.public_name
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = UserPublicQueryResponse()
        if 'expire_time' in d:
            o.expire_time = d['expire_time']
        if 'public_id' in d:
            o.public_id = d['public_id']
        if 'public_logo' in d:
            o.public_logo = d['public_logo']
        if 'public_name' in d:
            o.public_name = d['public_name']
        return o


