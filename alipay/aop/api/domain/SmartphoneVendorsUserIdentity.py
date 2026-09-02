#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class SmartphoneVendorsUserIdentity(object):

    def __init__(self):
        self._user_identification = None
        self._vendor_id_type = None

    @property
    def user_identification(self):
        return self._user_identification

    @user_identification.setter
    def user_identification(self, value):
        self._user_identification = value
    @property
    def vendor_id_type(self):
        return self._vendor_id_type

    @vendor_id_type.setter
    def vendor_id_type(self, value):
        self._vendor_id_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.user_identification:
            if hasattr(self.user_identification, 'to_alipay_dict'):
                params['user_identification'] = self.user_identification.to_alipay_dict()
            else:
                params['user_identification'] = self.user_identification
        if self.vendor_id_type:
            if hasattr(self.vendor_id_type, 'to_alipay_dict'):
                params['vendor_id_type'] = self.vendor_id_type.to_alipay_dict()
            else:
                params['vendor_id_type'] = self.vendor_id_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = SmartphoneVendorsUserIdentity()
        if 'user_identification' in d:
            o.user_identification = d['user_identification']
        if 'vendor_id_type' in d:
            o.vendor_id_type = d['vendor_id_type']
        return o


