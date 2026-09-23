#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class SaasEbankInstInfo(object):

    def __init__(self):
        self._inst_id = None
        self._inst_logo_url = None
        self._inst_name = None

    @property
    def inst_id(self):
        return self._inst_id

    @inst_id.setter
    def inst_id(self, value):
        self._inst_id = value
    @property
    def inst_logo_url(self):
        return self._inst_logo_url

    @inst_logo_url.setter
    def inst_logo_url(self, value):
        self._inst_logo_url = value
    @property
    def inst_name(self):
        return self._inst_name

    @inst_name.setter
    def inst_name(self, value):
        self._inst_name = value


    def to_alipay_dict(self):
        params = dict()
        if self.inst_id:
            if hasattr(self.inst_id, 'to_alipay_dict'):
                params['inst_id'] = self.inst_id.to_alipay_dict()
            else:
                params['inst_id'] = self.inst_id
        if self.inst_logo_url:
            if hasattr(self.inst_logo_url, 'to_alipay_dict'):
                params['inst_logo_url'] = self.inst_logo_url.to_alipay_dict()
            else:
                params['inst_logo_url'] = self.inst_logo_url
        if self.inst_name:
            if hasattr(self.inst_name, 'to_alipay_dict'):
                params['inst_name'] = self.inst_name.to_alipay_dict()
            else:
                params['inst_name'] = self.inst_name
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = SaasEbankInstInfo()
        if 'inst_id' in d:
            o.inst_id = d['inst_id']
        if 'inst_logo_url' in d:
            o.inst_logo_url = d['inst_logo_url']
        if 'inst_name' in d:
            o.inst_name = d['inst_name']
        return o


