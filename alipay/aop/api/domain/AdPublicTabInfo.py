#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AdPublicTabInfo(object):

    def __init__(self):
        self._public_id = None
        self._public_logo_url = None
        self._public_name = None

    @property
    def public_id(self):
        return self._public_id

    @public_id.setter
    def public_id(self, value):
        self._public_id = value
    @property
    def public_logo_url(self):
        return self._public_logo_url

    @public_logo_url.setter
    def public_logo_url(self, value):
        self._public_logo_url = value
    @property
    def public_name(self):
        return self._public_name

    @public_name.setter
    def public_name(self, value):
        self._public_name = value


    def to_alipay_dict(self):
        params = dict()
        if self.public_id:
            if hasattr(self.public_id, 'to_alipay_dict'):
                params['public_id'] = self.public_id.to_alipay_dict()
            else:
                params['public_id'] = self.public_id
        if self.public_logo_url:
            if hasattr(self.public_logo_url, 'to_alipay_dict'):
                params['public_logo_url'] = self.public_logo_url.to_alipay_dict()
            else:
                params['public_logo_url'] = self.public_logo_url
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
        o = AdPublicTabInfo()
        if 'public_id' in d:
            o.public_id = d['public_id']
        if 'public_logo_url' in d:
            o.public_logo_url = d['public_logo_url']
        if 'public_name' in d:
            o.public_name = d['public_name']
        return o


