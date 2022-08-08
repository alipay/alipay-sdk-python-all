#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class QipanMerchantCrowd(object):

    def __init__(self):
        self._crowd_code = None
        self._crowd_desc = None
        self._crowd_name = None
        self._external_crowd_code = None
        self._status = None

    @property
    def crowd_code(self):
        return self._crowd_code

    @crowd_code.setter
    def crowd_code(self, value):
        self._crowd_code = value
    @property
    def crowd_desc(self):
        return self._crowd_desc

    @crowd_desc.setter
    def crowd_desc(self, value):
        self._crowd_desc = value
    @property
    def crowd_name(self):
        return self._crowd_name

    @crowd_name.setter
    def crowd_name(self, value):
        self._crowd_name = value
    @property
    def external_crowd_code(self):
        return self._external_crowd_code

    @external_crowd_code.setter
    def external_crowd_code(self, value):
        self._external_crowd_code = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value


    def to_alipay_dict(self):
        params = dict()
        if self.crowd_code:
            if hasattr(self.crowd_code, 'to_alipay_dict'):
                params['crowd_code'] = self.crowd_code.to_alipay_dict()
            else:
                params['crowd_code'] = self.crowd_code
        if self.crowd_desc:
            if hasattr(self.crowd_desc, 'to_alipay_dict'):
                params['crowd_desc'] = self.crowd_desc.to_alipay_dict()
            else:
                params['crowd_desc'] = self.crowd_desc
        if self.crowd_name:
            if hasattr(self.crowd_name, 'to_alipay_dict'):
                params['crowd_name'] = self.crowd_name.to_alipay_dict()
            else:
                params['crowd_name'] = self.crowd_name
        if self.external_crowd_code:
            if hasattr(self.external_crowd_code, 'to_alipay_dict'):
                params['external_crowd_code'] = self.external_crowd_code.to_alipay_dict()
            else:
                params['external_crowd_code'] = self.external_crowd_code
        if self.status:
            if hasattr(self.status, 'to_alipay_dict'):
                params['status'] = self.status.to_alipay_dict()
            else:
                params['status'] = self.status
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = QipanMerchantCrowd()
        if 'crowd_code' in d:
            o.crowd_code = d['crowd_code']
        if 'crowd_desc' in d:
            o.crowd_desc = d['crowd_desc']
        if 'crowd_name' in d:
            o.crowd_name = d['crowd_name']
        if 'external_crowd_code' in d:
            o.external_crowd_code = d['external_crowd_code']
        if 'status' in d:
            o.status = d['status']
        return o


