#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceMedicalHomedoctorUserinfoShareModel(object):

    def __init__(self):
        self._aq_access_token = None
        self._aq_open_id = None

    @property
    def aq_access_token(self):
        return self._aq_access_token

    @aq_access_token.setter
    def aq_access_token(self, value):
        self._aq_access_token = value
    @property
    def aq_open_id(self):
        return self._aq_open_id

    @aq_open_id.setter
    def aq_open_id(self, value):
        self._aq_open_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.aq_access_token:
            if hasattr(self.aq_access_token, 'to_alipay_dict'):
                params['aq_access_token'] = self.aq_access_token.to_alipay_dict()
            else:
                params['aq_access_token'] = self.aq_access_token
        if self.aq_open_id:
            if hasattr(self.aq_open_id, 'to_alipay_dict'):
                params['aq_open_id'] = self.aq_open_id.to_alipay_dict()
            else:
                params['aq_open_id'] = self.aq_open_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceMedicalHomedoctorUserinfoShareModel()
        if 'aq_access_token' in d:
            o.aq_access_token = d['aq_access_token']
        if 'aq_open_id' in d:
            o.aq_open_id = d['aq_open_id']
        return o


