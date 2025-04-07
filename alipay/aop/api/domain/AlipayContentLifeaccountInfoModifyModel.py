#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayContentLifeaccountInfoModifyModel(object):

    def __init__(self):
        self._doctor_desc = None
        self._logo_url = None
        self._public_desc = None
        self._public_id = None
        self._public_name = None

    @property
    def doctor_desc(self):
        return self._doctor_desc

    @doctor_desc.setter
    def doctor_desc(self, value):
        self._doctor_desc = value
    @property
    def logo_url(self):
        return self._logo_url

    @logo_url.setter
    def logo_url(self, value):
        self._logo_url = value
    @property
    def public_desc(self):
        return self._public_desc

    @public_desc.setter
    def public_desc(self, value):
        self._public_desc = value
    @property
    def public_id(self):
        return self._public_id

    @public_id.setter
    def public_id(self, value):
        self._public_id = value
    @property
    def public_name(self):
        return self._public_name

    @public_name.setter
    def public_name(self, value):
        self._public_name = value


    def to_alipay_dict(self):
        params = dict()
        if self.doctor_desc:
            if hasattr(self.doctor_desc, 'to_alipay_dict'):
                params['doctor_desc'] = self.doctor_desc.to_alipay_dict()
            else:
                params['doctor_desc'] = self.doctor_desc
        if self.logo_url:
            if hasattr(self.logo_url, 'to_alipay_dict'):
                params['logo_url'] = self.logo_url.to_alipay_dict()
            else:
                params['logo_url'] = self.logo_url
        if self.public_desc:
            if hasattr(self.public_desc, 'to_alipay_dict'):
                params['public_desc'] = self.public_desc.to_alipay_dict()
            else:
                params['public_desc'] = self.public_desc
        if self.public_id:
            if hasattr(self.public_id, 'to_alipay_dict'):
                params['public_id'] = self.public_id.to_alipay_dict()
            else:
                params['public_id'] = self.public_id
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
        o = AlipayContentLifeaccountInfoModifyModel()
        if 'doctor_desc' in d:
            o.doctor_desc = d['doctor_desc']
        if 'logo_url' in d:
            o.logo_url = d['logo_url']
        if 'public_desc' in d:
            o.public_desc = d['public_desc']
        if 'public_id' in d:
            o.public_id = d['public_id']
        if 'public_name' in d:
            o.public_name = d['public_name']
        return o


