#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ApiContractParticipant(object):

    def __init__(self):
        self._biz_principal_id = None
        self._biz_principal_type = None
        self._participant_type = None
        self._principal_id = None
        self._principal_type = None

    @property
    def biz_principal_id(self):
        return self._biz_principal_id

    @biz_principal_id.setter
    def biz_principal_id(self, value):
        self._biz_principal_id = value
    @property
    def biz_principal_type(self):
        return self._biz_principal_type

    @biz_principal_type.setter
    def biz_principal_type(self, value):
        self._biz_principal_type = value
    @property
    def participant_type(self):
        return self._participant_type

    @participant_type.setter
    def participant_type(self, value):
        self._participant_type = value
    @property
    def principal_id(self):
        return self._principal_id

    @principal_id.setter
    def principal_id(self, value):
        self._principal_id = value
    @property
    def principal_type(self):
        return self._principal_type

    @principal_type.setter
    def principal_type(self, value):
        self._principal_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.biz_principal_id:
            if hasattr(self.biz_principal_id, 'to_alipay_dict'):
                params['biz_principal_id'] = self.biz_principal_id.to_alipay_dict()
            else:
                params['biz_principal_id'] = self.biz_principal_id
        if self.biz_principal_type:
            if hasattr(self.biz_principal_type, 'to_alipay_dict'):
                params['biz_principal_type'] = self.biz_principal_type.to_alipay_dict()
            else:
                params['biz_principal_type'] = self.biz_principal_type
        if self.participant_type:
            if hasattr(self.participant_type, 'to_alipay_dict'):
                params['participant_type'] = self.participant_type.to_alipay_dict()
            else:
                params['participant_type'] = self.participant_type
        if self.principal_id:
            if hasattr(self.principal_id, 'to_alipay_dict'):
                params['principal_id'] = self.principal_id.to_alipay_dict()
            else:
                params['principal_id'] = self.principal_id
        if self.principal_type:
            if hasattr(self.principal_type, 'to_alipay_dict'):
                params['principal_type'] = self.principal_type.to_alipay_dict()
            else:
                params['principal_type'] = self.principal_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ApiContractParticipant()
        if 'biz_principal_id' in d:
            o.biz_principal_id = d['biz_principal_id']
        if 'biz_principal_type' in d:
            o.biz_principal_type = d['biz_principal_type']
        if 'participant_type' in d:
            o.participant_type = d['participant_type']
        if 'principal_id' in d:
            o.principal_id = d['principal_id']
        if 'principal_type' in d:
            o.principal_type = d['principal_type']
        return o


