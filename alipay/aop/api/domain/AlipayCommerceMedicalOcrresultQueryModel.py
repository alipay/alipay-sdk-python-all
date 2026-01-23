#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.OcrAttachment import OcrAttachment


class AlipayCommerceMedicalOcrresultQueryModel(object):

    def __init__(self):
        self._attachment_list = None
        self._business_id = None
        self._business_type = None
        self._patient_id = None

    @property
    def attachment_list(self):
        return self._attachment_list

    @attachment_list.setter
    def attachment_list(self, value):
        if isinstance(value, list):
            self._attachment_list = list()
            for i in value:
                if isinstance(i, OcrAttachment):
                    self._attachment_list.append(i)
                else:
                    self._attachment_list.append(OcrAttachment.from_alipay_dict(i))
    @property
    def business_id(self):
        return self._business_id

    @business_id.setter
    def business_id(self, value):
        self._business_id = value
    @property
    def business_type(self):
        return self._business_type

    @business_type.setter
    def business_type(self, value):
        self._business_type = value
    @property
    def patient_id(self):
        return self._patient_id

    @patient_id.setter
    def patient_id(self, value):
        self._patient_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.attachment_list:
            if isinstance(self.attachment_list, list):
                for i in range(0, len(self.attachment_list)):
                    element = self.attachment_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.attachment_list[i] = element.to_alipay_dict()
            if hasattr(self.attachment_list, 'to_alipay_dict'):
                params['attachment_list'] = self.attachment_list.to_alipay_dict()
            else:
                params['attachment_list'] = self.attachment_list
        if self.business_id:
            if hasattr(self.business_id, 'to_alipay_dict'):
                params['business_id'] = self.business_id.to_alipay_dict()
            else:
                params['business_id'] = self.business_id
        if self.business_type:
            if hasattr(self.business_type, 'to_alipay_dict'):
                params['business_type'] = self.business_type.to_alipay_dict()
            else:
                params['business_type'] = self.business_type
        if self.patient_id:
            if hasattr(self.patient_id, 'to_alipay_dict'):
                params['patient_id'] = self.patient_id.to_alipay_dict()
            else:
                params['patient_id'] = self.patient_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceMedicalOcrresultQueryModel()
        if 'attachment_list' in d:
            o.attachment_list = d['attachment_list']
        if 'business_id' in d:
            o.business_id = d['business_id']
        if 'business_type' in d:
            o.business_type = d['business_type']
        if 'patient_id' in d:
            o.patient_id = d['patient_id']
        return o


