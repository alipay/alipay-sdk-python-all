#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.EcoContractDetailInfo import EcoContractDetailInfo
from alipay.aop.api.domain.EcoContractParticipantInfo import EcoContractParticipantInfo


class EcoContractInfo(object):

    def __init__(self):
        self._contract_end_time = None
        self._contract_start_time = None
        self._detail_info = None
        self._name = None
        self._out_contract_id = None
        self._participant = None
        self._sign_deadline_time = None
        self._sign_end_time = None
        self._sign_start_time = None
        self._start_time = None
        self._status = None

    @property
    def contract_end_time(self):
        return self._contract_end_time

    @contract_end_time.setter
    def contract_end_time(self, value):
        self._contract_end_time = value
    @property
    def contract_start_time(self):
        return self._contract_start_time

    @contract_start_time.setter
    def contract_start_time(self, value):
        self._contract_start_time = value
    @property
    def detail_info(self):
        return self._detail_info

    @detail_info.setter
    def detail_info(self, value):
        if isinstance(value, EcoContractDetailInfo):
            self._detail_info = value
        else:
            self._detail_info = EcoContractDetailInfo.from_alipay_dict(value)
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value
    @property
    def out_contract_id(self):
        return self._out_contract_id

    @out_contract_id.setter
    def out_contract_id(self, value):
        self._out_contract_id = value
    @property
    def participant(self):
        return self._participant

    @participant.setter
    def participant(self, value):
        if isinstance(value, list):
            self._participant = list()
            for i in value:
                if isinstance(i, EcoContractParticipantInfo):
                    self._participant.append(i)
                else:
                    self._participant.append(EcoContractParticipantInfo.from_alipay_dict(i))
    @property
    def sign_deadline_time(self):
        return self._sign_deadline_time

    @sign_deadline_time.setter
    def sign_deadline_time(self, value):
        self._sign_deadline_time = value
    @property
    def sign_end_time(self):
        return self._sign_end_time

    @sign_end_time.setter
    def sign_end_time(self, value):
        self._sign_end_time = value
    @property
    def sign_start_time(self):
        return self._sign_start_time

    @sign_start_time.setter
    def sign_start_time(self, value):
        self._sign_start_time = value
    @property
    def start_time(self):
        return self._start_time

    @start_time.setter
    def start_time(self, value):
        self._start_time = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value


    def to_alipay_dict(self):
        params = dict()
        if self.contract_end_time:
            if hasattr(self.contract_end_time, 'to_alipay_dict'):
                params['contract_end_time'] = self.contract_end_time.to_alipay_dict()
            else:
                params['contract_end_time'] = self.contract_end_time
        if self.contract_start_time:
            if hasattr(self.contract_start_time, 'to_alipay_dict'):
                params['contract_start_time'] = self.contract_start_time.to_alipay_dict()
            else:
                params['contract_start_time'] = self.contract_start_time
        if self.detail_info:
            if hasattr(self.detail_info, 'to_alipay_dict'):
                params['detail_info'] = self.detail_info.to_alipay_dict()
            else:
                params['detail_info'] = self.detail_info
        if self.name:
            if hasattr(self.name, 'to_alipay_dict'):
                params['name'] = self.name.to_alipay_dict()
            else:
                params['name'] = self.name
        if self.out_contract_id:
            if hasattr(self.out_contract_id, 'to_alipay_dict'):
                params['out_contract_id'] = self.out_contract_id.to_alipay_dict()
            else:
                params['out_contract_id'] = self.out_contract_id
        if self.participant:
            if isinstance(self.participant, list):
                for i in range(0, len(self.participant)):
                    element = self.participant[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.participant[i] = element.to_alipay_dict()
            if hasattr(self.participant, 'to_alipay_dict'):
                params['participant'] = self.participant.to_alipay_dict()
            else:
                params['participant'] = self.participant
        if self.sign_deadline_time:
            if hasattr(self.sign_deadline_time, 'to_alipay_dict'):
                params['sign_deadline_time'] = self.sign_deadline_time.to_alipay_dict()
            else:
                params['sign_deadline_time'] = self.sign_deadline_time
        if self.sign_end_time:
            if hasattr(self.sign_end_time, 'to_alipay_dict'):
                params['sign_end_time'] = self.sign_end_time.to_alipay_dict()
            else:
                params['sign_end_time'] = self.sign_end_time
        if self.sign_start_time:
            if hasattr(self.sign_start_time, 'to_alipay_dict'):
                params['sign_start_time'] = self.sign_start_time.to_alipay_dict()
            else:
                params['sign_start_time'] = self.sign_start_time
        if self.start_time:
            if hasattr(self.start_time, 'to_alipay_dict'):
                params['start_time'] = self.start_time.to_alipay_dict()
            else:
                params['start_time'] = self.start_time
        if self.status:
            if hasattr(self.status, 'to_alipay_dict'):
                params['status'] = self.status.to_alipay_dict()
            else:
                params['status'] = self.status
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = EcoContractInfo()
        if 'contract_end_time' in d:
            o.contract_end_time = d['contract_end_time']
        if 'contract_start_time' in d:
            o.contract_start_time = d['contract_start_time']
        if 'detail_info' in d:
            o.detail_info = d['detail_info']
        if 'name' in d:
            o.name = d['name']
        if 'out_contract_id' in d:
            o.out_contract_id = d['out_contract_id']
        if 'participant' in d:
            o.participant = d['participant']
        if 'sign_deadline_time' in d:
            o.sign_deadline_time = d['sign_deadline_time']
        if 'sign_end_time' in d:
            o.sign_end_time = d['sign_end_time']
        if 'sign_start_time' in d:
            o.sign_start_time = d['sign_start_time']
        if 'start_time' in d:
            o.start_time = d['start_time']
        if 'status' in d:
            o.status = d['status']
        return o


