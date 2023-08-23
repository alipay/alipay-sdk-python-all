#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.ParticipantExtendParams import ParticipantExtendParams


class AttendancePariticipantInfoDTO(object):

    def __init__(self):
        self._extend_params = None
        self._name = None
        self._participant_id = None
        self._participant_id_type = None

    @property
    def extend_params(self):
        return self._extend_params

    @extend_params.setter
    def extend_params(self, value):
        if isinstance(value, ParticipantExtendParams):
            self._extend_params = value
        else:
            self._extend_params = ParticipantExtendParams.from_alipay_dict(value)
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value
    @property
    def participant_id(self):
        return self._participant_id

    @participant_id.setter
    def participant_id(self, value):
        self._participant_id = value
    @property
    def participant_id_type(self):
        return self._participant_id_type

    @participant_id_type.setter
    def participant_id_type(self, value):
        self._participant_id_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.extend_params:
            if hasattr(self.extend_params, 'to_alipay_dict'):
                params['extend_params'] = self.extend_params.to_alipay_dict()
            else:
                params['extend_params'] = self.extend_params
        if self.name:
            if hasattr(self.name, 'to_alipay_dict'):
                params['name'] = self.name.to_alipay_dict()
            else:
                params['name'] = self.name
        if self.participant_id:
            if hasattr(self.participant_id, 'to_alipay_dict'):
                params['participant_id'] = self.participant_id.to_alipay_dict()
            else:
                params['participant_id'] = self.participant_id
        if self.participant_id_type:
            if hasattr(self.participant_id_type, 'to_alipay_dict'):
                params['participant_id_type'] = self.participant_id_type.to_alipay_dict()
            else:
                params['participant_id_type'] = self.participant_id_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AttendancePariticipantInfoDTO()
        if 'extend_params' in d:
            o.extend_params = d['extend_params']
        if 'name' in d:
            o.name = d['name']
        if 'participant_id' in d:
            o.participant_id = d['participant_id']
        if 'participant_id_type' in d:
            o.participant_id_type = d['participant_id_type']
        return o


