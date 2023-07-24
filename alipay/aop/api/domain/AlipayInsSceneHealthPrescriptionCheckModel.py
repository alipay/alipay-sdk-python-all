#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.Diagnosis import Diagnosis
from alipay.aop.api.domain.DialogueProcess import DialogueProcess


class AlipayInsSceneHealthPrescriptionCheckModel(object):

    def __init__(self):
        self._ant_ser_contract_no = None
        self._diagnosis = None
        self._dialogue_process = None
        self._doctor_id = None
        self._doctor_name = None

    @property
    def ant_ser_contract_no(self):
        return self._ant_ser_contract_no

    @ant_ser_contract_no.setter
    def ant_ser_contract_no(self, value):
        self._ant_ser_contract_no = value
    @property
    def diagnosis(self):
        return self._diagnosis

    @diagnosis.setter
    def diagnosis(self, value):
        if isinstance(value, Diagnosis):
            self._diagnosis = value
        else:
            self._diagnosis = Diagnosis.from_alipay_dict(value)
    @property
    def dialogue_process(self):
        return self._dialogue_process

    @dialogue_process.setter
    def dialogue_process(self, value):
        if isinstance(value, list):
            self._dialogue_process = list()
            for i in value:
                if isinstance(i, DialogueProcess):
                    self._dialogue_process.append(i)
                else:
                    self._dialogue_process.append(DialogueProcess.from_alipay_dict(i))
    @property
    def doctor_id(self):
        return self._doctor_id

    @doctor_id.setter
    def doctor_id(self, value):
        self._doctor_id = value
    @property
    def doctor_name(self):
        return self._doctor_name

    @doctor_name.setter
    def doctor_name(self, value):
        self._doctor_name = value


    def to_alipay_dict(self):
        params = dict()
        if self.ant_ser_contract_no:
            if hasattr(self.ant_ser_contract_no, 'to_alipay_dict'):
                params['ant_ser_contract_no'] = self.ant_ser_contract_no.to_alipay_dict()
            else:
                params['ant_ser_contract_no'] = self.ant_ser_contract_no
        if self.diagnosis:
            if hasattr(self.diagnosis, 'to_alipay_dict'):
                params['diagnosis'] = self.diagnosis.to_alipay_dict()
            else:
                params['diagnosis'] = self.diagnosis
        if self.dialogue_process:
            if isinstance(self.dialogue_process, list):
                for i in range(0, len(self.dialogue_process)):
                    element = self.dialogue_process[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.dialogue_process[i] = element.to_alipay_dict()
            if hasattr(self.dialogue_process, 'to_alipay_dict'):
                params['dialogue_process'] = self.dialogue_process.to_alipay_dict()
            else:
                params['dialogue_process'] = self.dialogue_process
        if self.doctor_id:
            if hasattr(self.doctor_id, 'to_alipay_dict'):
                params['doctor_id'] = self.doctor_id.to_alipay_dict()
            else:
                params['doctor_id'] = self.doctor_id
        if self.doctor_name:
            if hasattr(self.doctor_name, 'to_alipay_dict'):
                params['doctor_name'] = self.doctor_name.to_alipay_dict()
            else:
                params['doctor_name'] = self.doctor_name
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayInsSceneHealthPrescriptionCheckModel()
        if 'ant_ser_contract_no' in d:
            o.ant_ser_contract_no = d['ant_ser_contract_no']
        if 'diagnosis' in d:
            o.diagnosis = d['diagnosis']
        if 'dialogue_process' in d:
            o.dialogue_process = d['dialogue_process']
        if 'doctor_id' in d:
            o.doctor_id = d['doctor_id']
        if 'doctor_name' in d:
            o.doctor_name = d['doctor_name']
        return o


