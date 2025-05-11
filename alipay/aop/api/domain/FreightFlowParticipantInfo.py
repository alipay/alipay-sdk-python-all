#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class FreightFlowParticipantInfo(object):

    def __init__(self):
        self._participant_customer_type = None
        self._participant_id = None
        self._participant_inst_code = None
        self._participant_name = None
        self._participant_type = None

    @property
    def participant_customer_type(self):
        return self._participant_customer_type

    @participant_customer_type.setter
    def participant_customer_type(self, value):
        self._participant_customer_type = value
    @property
    def participant_id(self):
        return self._participant_id

    @participant_id.setter
    def participant_id(self, value):
        self._participant_id = value
    @property
    def participant_inst_code(self):
        return self._participant_inst_code

    @participant_inst_code.setter
    def participant_inst_code(self, value):
        self._participant_inst_code = value
    @property
    def participant_name(self):
        return self._participant_name

    @participant_name.setter
    def participant_name(self, value):
        self._participant_name = value
    @property
    def participant_type(self):
        return self._participant_type

    @participant_type.setter
    def participant_type(self, value):
        self._participant_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.participant_customer_type:
            if hasattr(self.participant_customer_type, 'to_alipay_dict'):
                params['participant_customer_type'] = self.participant_customer_type.to_alipay_dict()
            else:
                params['participant_customer_type'] = self.participant_customer_type
        if self.participant_id:
            if hasattr(self.participant_id, 'to_alipay_dict'):
                params['participant_id'] = self.participant_id.to_alipay_dict()
            else:
                params['participant_id'] = self.participant_id
        if self.participant_inst_code:
            if hasattr(self.participant_inst_code, 'to_alipay_dict'):
                params['participant_inst_code'] = self.participant_inst_code.to_alipay_dict()
            else:
                params['participant_inst_code'] = self.participant_inst_code
        if self.participant_name:
            if hasattr(self.participant_name, 'to_alipay_dict'):
                params['participant_name'] = self.participant_name.to_alipay_dict()
            else:
                params['participant_name'] = self.participant_name
        if self.participant_type:
            if hasattr(self.participant_type, 'to_alipay_dict'):
                params['participant_type'] = self.participant_type.to_alipay_dict()
            else:
                params['participant_type'] = self.participant_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = FreightFlowParticipantInfo()
        if 'participant_customer_type' in d:
            o.participant_customer_type = d['participant_customer_type']
        if 'participant_id' in d:
            o.participant_id = d['participant_id']
        if 'participant_inst_code' in d:
            o.participant_inst_code = d['participant_inst_code']
        if 'participant_name' in d:
            o.participant_name = d['participant_name']
        if 'participant_type' in d:
            o.participant_type = d['participant_type']
        return o


