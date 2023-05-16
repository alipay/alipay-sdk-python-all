#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class DatadigitalFincloudFinsaasDigitalrmbSendSyncModel(object):

    def __init__(self):
        self._cred_id = None
        self._person_id = None
        self._phone_no = None

    @property
    def cred_id(self):
        return self._cred_id

    @cred_id.setter
    def cred_id(self, value):
        self._cred_id = value
    @property
    def person_id(self):
        return self._person_id

    @person_id.setter
    def person_id(self, value):
        self._person_id = value
    @property
    def phone_no(self):
        return self._phone_no

    @phone_no.setter
    def phone_no(self, value):
        self._phone_no = value


    def to_alipay_dict(self):
        params = dict()
        if self.cred_id:
            if hasattr(self.cred_id, 'to_alipay_dict'):
                params['cred_id'] = self.cred_id.to_alipay_dict()
            else:
                params['cred_id'] = self.cred_id
        if self.person_id:
            if hasattr(self.person_id, 'to_alipay_dict'):
                params['person_id'] = self.person_id.to_alipay_dict()
            else:
                params['person_id'] = self.person_id
        if self.phone_no:
            if hasattr(self.phone_no, 'to_alipay_dict'):
                params['phone_no'] = self.phone_no.to_alipay_dict()
            else:
                params['phone_no'] = self.phone_no
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = DatadigitalFincloudFinsaasDigitalrmbSendSyncModel()
        if 'cred_id' in d:
            o.cred_id = d['cred_id']
        if 'person_id' in d:
            o.person_id = d['person_id']
        if 'phone_no' in d:
            o.phone_no = d['phone_no']
        return o


