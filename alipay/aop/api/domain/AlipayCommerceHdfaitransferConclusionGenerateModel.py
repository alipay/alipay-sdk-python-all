#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.ChatRecordInfo import ChatRecordInfo
from alipay.aop.api.domain.MedicalRecordInfo import MedicalRecordInfo


class AlipayCommerceHdfaitransferConclusionGenerateModel(object):

    def __init__(self):
        self._chat_record_info = None
        self._medical_record_info = None

    @property
    def chat_record_info(self):
        return self._chat_record_info

    @chat_record_info.setter
    def chat_record_info(self, value):
        if isinstance(value, list):
            self._chat_record_info = list()
            for i in value:
                if isinstance(i, ChatRecordInfo):
                    self._chat_record_info.append(i)
                else:
                    self._chat_record_info.append(ChatRecordInfo.from_alipay_dict(i))
    @property
    def medical_record_info(self):
        return self._medical_record_info

    @medical_record_info.setter
    def medical_record_info(self, value):
        if isinstance(value, MedicalRecordInfo):
            self._medical_record_info = value
        else:
            self._medical_record_info = MedicalRecordInfo.from_alipay_dict(value)


    def to_alipay_dict(self):
        params = dict()
        if self.chat_record_info:
            if isinstance(self.chat_record_info, list):
                for i in range(0, len(self.chat_record_info)):
                    element = self.chat_record_info[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.chat_record_info[i] = element.to_alipay_dict()
            if hasattr(self.chat_record_info, 'to_alipay_dict'):
                params['chat_record_info'] = self.chat_record_info.to_alipay_dict()
            else:
                params['chat_record_info'] = self.chat_record_info
        if self.medical_record_info:
            if hasattr(self.medical_record_info, 'to_alipay_dict'):
                params['medical_record_info'] = self.medical_record_info.to_alipay_dict()
            else:
                params['medical_record_info'] = self.medical_record_info
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceHdfaitransferConclusionGenerateModel()
        if 'chat_record_info' in d:
            o.chat_record_info = d['chat_record_info']
        if 'medical_record_info' in d:
            o.medical_record_info = d['medical_record_info']
        return o


