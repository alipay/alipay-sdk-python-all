#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.ChinaMobileVerificationSyncData import ChinaMobileVerificationSyncData


class ChinaMobileBody(object):

    def __init__(self):
        self._data = None
        self._reco_id = None
        self._rights_id = None
        self._verification_cancel_flag = None
        self._verification_type = None

    @property
    def data(self):
        return self._data

    @data.setter
    def data(self, value):
        if isinstance(value, list):
            self._data = list()
            for i in value:
                if isinstance(i, ChinaMobileVerificationSyncData):
                    self._data.append(i)
                else:
                    self._data.append(ChinaMobileVerificationSyncData.from_alipay_dict(i))
    @property
    def reco_id(self):
        return self._reco_id

    @reco_id.setter
    def reco_id(self, value):
        self._reco_id = value
    @property
    def rights_id(self):
        return self._rights_id

    @rights_id.setter
    def rights_id(self, value):
        self._rights_id = value
    @property
    def verification_cancel_flag(self):
        return self._verification_cancel_flag

    @verification_cancel_flag.setter
    def verification_cancel_flag(self, value):
        self._verification_cancel_flag = value
    @property
    def verification_type(self):
        return self._verification_type

    @verification_type.setter
    def verification_type(self, value):
        self._verification_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.data:
            if isinstance(self.data, list):
                for i in range(0, len(self.data)):
                    element = self.data[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.data[i] = element.to_alipay_dict()
            if hasattr(self.data, 'to_alipay_dict'):
                params['data'] = self.data.to_alipay_dict()
            else:
                params['data'] = self.data
        if self.reco_id:
            if hasattr(self.reco_id, 'to_alipay_dict'):
                params['reco_id'] = self.reco_id.to_alipay_dict()
            else:
                params['reco_id'] = self.reco_id
        if self.rights_id:
            if hasattr(self.rights_id, 'to_alipay_dict'):
                params['rights_id'] = self.rights_id.to_alipay_dict()
            else:
                params['rights_id'] = self.rights_id
        if self.verification_cancel_flag:
            if hasattr(self.verification_cancel_flag, 'to_alipay_dict'):
                params['verification_cancel_flag'] = self.verification_cancel_flag.to_alipay_dict()
            else:
                params['verification_cancel_flag'] = self.verification_cancel_flag
        if self.verification_type:
            if hasattr(self.verification_type, 'to_alipay_dict'):
                params['verification_type'] = self.verification_type.to_alipay_dict()
            else:
                params['verification_type'] = self.verification_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ChinaMobileBody()
        if 'data' in d:
            o.data = d['data']
        if 'reco_id' in d:
            o.reco_id = d['reco_id']
        if 'rights_id' in d:
            o.rights_id = d['rights_id']
        if 'verification_cancel_flag' in d:
            o.verification_cancel_flag = d['verification_cancel_flag']
        if 'verification_type' in d:
            o.verification_type = d['verification_type']
        return o


