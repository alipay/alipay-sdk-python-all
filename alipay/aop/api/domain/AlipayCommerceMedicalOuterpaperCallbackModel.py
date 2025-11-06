#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.HDFDoctorInfo import HDFDoctorInfo
from alipay.aop.api.domain.HDFMedicalContent import HDFMedicalContent
from alipay.aop.api.domain.HDFPatientInfo import HDFPatientInfo
from alipay.aop.api.domain.HDFPrescription import HDFPrescription


class AlipayCommerceMedicalOuterpaperCallbackModel(object):

    def __init__(self):
        self._doctor_info = None
        self._ext_info = None
        self._fulfillment_order_id = None
        self._medical_content_list = None
        self._partner_order_id = None
        self._patient_info = None
        self._prescription_info = None

    @property
    def doctor_info(self):
        return self._doctor_info

    @doctor_info.setter
    def doctor_info(self, value):
        if isinstance(value, HDFDoctorInfo):
            self._doctor_info = value
        else:
            self._doctor_info = HDFDoctorInfo.from_alipay_dict(value)
    @property
    def ext_info(self):
        return self._ext_info

    @ext_info.setter
    def ext_info(self, value):
        self._ext_info = value
    @property
    def fulfillment_order_id(self):
        return self._fulfillment_order_id

    @fulfillment_order_id.setter
    def fulfillment_order_id(self, value):
        self._fulfillment_order_id = value
    @property
    def medical_content_list(self):
        return self._medical_content_list

    @medical_content_list.setter
    def medical_content_list(self, value):
        if isinstance(value, list):
            self._medical_content_list = list()
            for i in value:
                if isinstance(i, HDFMedicalContent):
                    self._medical_content_list.append(i)
                else:
                    self._medical_content_list.append(HDFMedicalContent.from_alipay_dict(i))
    @property
    def partner_order_id(self):
        return self._partner_order_id

    @partner_order_id.setter
    def partner_order_id(self, value):
        self._partner_order_id = value
    @property
    def patient_info(self):
        return self._patient_info

    @patient_info.setter
    def patient_info(self, value):
        if isinstance(value, HDFPatientInfo):
            self._patient_info = value
        else:
            self._patient_info = HDFPatientInfo.from_alipay_dict(value)
    @property
    def prescription_info(self):
        return self._prescription_info

    @prescription_info.setter
    def prescription_info(self, value):
        if isinstance(value, HDFPrescription):
            self._prescription_info = value
        else:
            self._prescription_info = HDFPrescription.from_alipay_dict(value)


    def to_alipay_dict(self):
        params = dict()
        if self.doctor_info:
            if hasattr(self.doctor_info, 'to_alipay_dict'):
                params['doctor_info'] = self.doctor_info.to_alipay_dict()
            else:
                params['doctor_info'] = self.doctor_info
        if self.ext_info:
            if hasattr(self.ext_info, 'to_alipay_dict'):
                params['ext_info'] = self.ext_info.to_alipay_dict()
            else:
                params['ext_info'] = self.ext_info
        if self.fulfillment_order_id:
            if hasattr(self.fulfillment_order_id, 'to_alipay_dict'):
                params['fulfillment_order_id'] = self.fulfillment_order_id.to_alipay_dict()
            else:
                params['fulfillment_order_id'] = self.fulfillment_order_id
        if self.medical_content_list:
            if isinstance(self.medical_content_list, list):
                for i in range(0, len(self.medical_content_list)):
                    element = self.medical_content_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.medical_content_list[i] = element.to_alipay_dict()
            if hasattr(self.medical_content_list, 'to_alipay_dict'):
                params['medical_content_list'] = self.medical_content_list.to_alipay_dict()
            else:
                params['medical_content_list'] = self.medical_content_list
        if self.partner_order_id:
            if hasattr(self.partner_order_id, 'to_alipay_dict'):
                params['partner_order_id'] = self.partner_order_id.to_alipay_dict()
            else:
                params['partner_order_id'] = self.partner_order_id
        if self.patient_info:
            if hasattr(self.patient_info, 'to_alipay_dict'):
                params['patient_info'] = self.patient_info.to_alipay_dict()
            else:
                params['patient_info'] = self.patient_info
        if self.prescription_info:
            if hasattr(self.prescription_info, 'to_alipay_dict'):
                params['prescription_info'] = self.prescription_info.to_alipay_dict()
            else:
                params['prescription_info'] = self.prescription_info
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceMedicalOuterpaperCallbackModel()
        if 'doctor_info' in d:
            o.doctor_info = d['doctor_info']
        if 'ext_info' in d:
            o.ext_info = d['ext_info']
        if 'fulfillment_order_id' in d:
            o.fulfillment_order_id = d['fulfillment_order_id']
        if 'medical_content_list' in d:
            o.medical_content_list = d['medical_content_list']
        if 'partner_order_id' in d:
            o.partner_order_id = d['partner_order_id']
        if 'patient_info' in d:
            o.patient_info = d['patient_info']
        if 'prescription_info' in d:
            o.prescription_info = d['prescription_info']
        return o


