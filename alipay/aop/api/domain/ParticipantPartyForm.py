#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.ParticipantPartyBizParams import ParticipantPartyBizParams


class ParticipantPartyForm(object):

    def __init__(self):
        self._identity = None
        self._identity_type = None
        self._name = None
        self._participant_party_biz_params = None

    @property
    def identity(self):
        return self._identity

    @identity.setter
    def identity(self, value):
        self._identity = value
    @property
    def identity_type(self):
        return self._identity_type

    @identity_type.setter
    def identity_type(self, value):
        self._identity_type = value
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value
    @property
    def participant_party_biz_params(self):
        return self._participant_party_biz_params

    @participant_party_biz_params.setter
    def participant_party_biz_params(self, value):
        if isinstance(value, ParticipantPartyBizParams):
            self._participant_party_biz_params = value
        else:
            self._participant_party_biz_params = ParticipantPartyBizParams.from_alipay_dict(value)


    def to_alipay_dict(self):
        params = dict()
        if self.identity:
            if hasattr(self.identity, 'to_alipay_dict'):
                params['identity'] = self.identity.to_alipay_dict()
            else:
                params['identity'] = self.identity
        if self.identity_type:
            if hasattr(self.identity_type, 'to_alipay_dict'):
                params['identity_type'] = self.identity_type.to_alipay_dict()
            else:
                params['identity_type'] = self.identity_type
        if self.name:
            if hasattr(self.name, 'to_alipay_dict'):
                params['name'] = self.name.to_alipay_dict()
            else:
                params['name'] = self.name
        if self.participant_party_biz_params:
            if hasattr(self.participant_party_biz_params, 'to_alipay_dict'):
                params['participant_party_biz_params'] = self.participant_party_biz_params.to_alipay_dict()
            else:
                params['participant_party_biz_params'] = self.participant_party_biz_params
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ParticipantPartyForm()
        if 'identity' in d:
            o.identity = d['identity']
        if 'identity_type' in d:
            o.identity_type = d['identity_type']
        if 'name' in d:
            o.name = d['name']
        if 'participant_party_biz_params' in d:
            o.participant_party_biz_params = d['participant_party_biz_params']
        return o


