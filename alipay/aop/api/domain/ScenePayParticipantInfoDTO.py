#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.ScenePayParticipantBizParamDTO import ScenePayParticipantBizParamDTO


class ScenePayParticipantInfoDTO(object):

    def __init__(self):
        self._mcc = None
        self._name = None
        self._participant_biz_param = None
        self._participant_id = None
        self._participant_id_type = None

    @property
    def mcc(self):
        return self._mcc

    @mcc.setter
    def mcc(self, value):
        self._mcc = value
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value
    @property
    def participant_biz_param(self):
        return self._participant_biz_param

    @participant_biz_param.setter
    def participant_biz_param(self, value):
        if isinstance(value, ScenePayParticipantBizParamDTO):
            self._participant_biz_param = value
        else:
            self._participant_biz_param = ScenePayParticipantBizParamDTO.from_alipay_dict(value)
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
        if self.mcc:
            if hasattr(self.mcc, 'to_alipay_dict'):
                params['mcc'] = self.mcc.to_alipay_dict()
            else:
                params['mcc'] = self.mcc
        if self.name:
            if hasattr(self.name, 'to_alipay_dict'):
                params['name'] = self.name.to_alipay_dict()
            else:
                params['name'] = self.name
        if self.participant_biz_param:
            if hasattr(self.participant_biz_param, 'to_alipay_dict'):
                params['participant_biz_param'] = self.participant_biz_param.to_alipay_dict()
            else:
                params['participant_biz_param'] = self.participant_biz_param
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
        o = ScenePayParticipantInfoDTO()
        if 'mcc' in d:
            o.mcc = d['mcc']
        if 'name' in d:
            o.name = d['name']
        if 'participant_biz_param' in d:
            o.participant_biz_param = d['participant_biz_param']
        if 'participant_id' in d:
            o.participant_id = d['participant_id']
        if 'participant_id_type' in d:
            o.participant_id_type = d['participant_id_type']
        return o


