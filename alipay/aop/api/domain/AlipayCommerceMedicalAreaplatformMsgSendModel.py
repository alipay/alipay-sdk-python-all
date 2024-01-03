#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.MedicalAreaPlatformMsgSendArg import MedicalAreaPlatformMsgSendArg


class AlipayCommerceMedicalAreaplatformMsgSendModel(object):

    def __init__(self):
        self._hospital = None
        self._hospital_id_type = None
        self._hospital_register_id = None
        self._msg_arg_list = None
        self._out_msg_id = None
        self._patient = None
        self._template_code = None
        self._user_card_no = None
        self._user_card_type = None

    @property
    def hospital(self):
        return self._hospital

    @hospital.setter
    def hospital(self, value):
        self._hospital = value
    @property
    def hospital_id_type(self):
        return self._hospital_id_type

    @hospital_id_type.setter
    def hospital_id_type(self, value):
        self._hospital_id_type = value
    @property
    def hospital_register_id(self):
        return self._hospital_register_id

    @hospital_register_id.setter
    def hospital_register_id(self, value):
        self._hospital_register_id = value
    @property
    def msg_arg_list(self):
        return self._msg_arg_list

    @msg_arg_list.setter
    def msg_arg_list(self, value):
        if isinstance(value, list):
            self._msg_arg_list = list()
            for i in value:
                if isinstance(i, MedicalAreaPlatformMsgSendArg):
                    self._msg_arg_list.append(i)
                else:
                    self._msg_arg_list.append(MedicalAreaPlatformMsgSendArg.from_alipay_dict(i))
    @property
    def out_msg_id(self):
        return self._out_msg_id

    @out_msg_id.setter
    def out_msg_id(self, value):
        self._out_msg_id = value
    @property
    def patient(self):
        return self._patient

    @patient.setter
    def patient(self, value):
        self._patient = value
    @property
    def template_code(self):
        return self._template_code

    @template_code.setter
    def template_code(self, value):
        self._template_code = value
    @property
    def user_card_no(self):
        return self._user_card_no

    @user_card_no.setter
    def user_card_no(self, value):
        self._user_card_no = value
    @property
    def user_card_type(self):
        return self._user_card_type

    @user_card_type.setter
    def user_card_type(self, value):
        self._user_card_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.hospital:
            if hasattr(self.hospital, 'to_alipay_dict'):
                params['hospital'] = self.hospital.to_alipay_dict()
            else:
                params['hospital'] = self.hospital
        if self.hospital_id_type:
            if hasattr(self.hospital_id_type, 'to_alipay_dict'):
                params['hospital_id_type'] = self.hospital_id_type.to_alipay_dict()
            else:
                params['hospital_id_type'] = self.hospital_id_type
        if self.hospital_register_id:
            if hasattr(self.hospital_register_id, 'to_alipay_dict'):
                params['hospital_register_id'] = self.hospital_register_id.to_alipay_dict()
            else:
                params['hospital_register_id'] = self.hospital_register_id
        if self.msg_arg_list:
            if isinstance(self.msg_arg_list, list):
                for i in range(0, len(self.msg_arg_list)):
                    element = self.msg_arg_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.msg_arg_list[i] = element.to_alipay_dict()
            if hasattr(self.msg_arg_list, 'to_alipay_dict'):
                params['msg_arg_list'] = self.msg_arg_list.to_alipay_dict()
            else:
                params['msg_arg_list'] = self.msg_arg_list
        if self.out_msg_id:
            if hasattr(self.out_msg_id, 'to_alipay_dict'):
                params['out_msg_id'] = self.out_msg_id.to_alipay_dict()
            else:
                params['out_msg_id'] = self.out_msg_id
        if self.patient:
            if hasattr(self.patient, 'to_alipay_dict'):
                params['patient'] = self.patient.to_alipay_dict()
            else:
                params['patient'] = self.patient
        if self.template_code:
            if hasattr(self.template_code, 'to_alipay_dict'):
                params['template_code'] = self.template_code.to_alipay_dict()
            else:
                params['template_code'] = self.template_code
        if self.user_card_no:
            if hasattr(self.user_card_no, 'to_alipay_dict'):
                params['user_card_no'] = self.user_card_no.to_alipay_dict()
            else:
                params['user_card_no'] = self.user_card_no
        if self.user_card_type:
            if hasattr(self.user_card_type, 'to_alipay_dict'):
                params['user_card_type'] = self.user_card_type.to_alipay_dict()
            else:
                params['user_card_type'] = self.user_card_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceMedicalAreaplatformMsgSendModel()
        if 'hospital' in d:
            o.hospital = d['hospital']
        if 'hospital_id_type' in d:
            o.hospital_id_type = d['hospital_id_type']
        if 'hospital_register_id' in d:
            o.hospital_register_id = d['hospital_register_id']
        if 'msg_arg_list' in d:
            o.msg_arg_list = d['msg_arg_list']
        if 'out_msg_id' in d:
            o.out_msg_id = d['out_msg_id']
        if 'patient' in d:
            o.patient = d['patient']
        if 'template_code' in d:
            o.template_code = d['template_code']
        if 'user_card_no' in d:
            o.user_card_no = d['user_card_no']
        if 'user_card_type' in d:
            o.user_card_type = d['user_card_type']
        return o


