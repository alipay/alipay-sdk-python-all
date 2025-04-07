#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.DiseaseInfo import DiseaseInfo
from alipay.aop.api.domain.DrugInfo import DrugInfo
from alipay.aop.api.domain.PatientInfo import PatientInfo


class AlipayCommerceMedicalMedicinePrescriptionorderUploadModel(object):

    def __init__(self):
        self._depart_name = None
        self._disease_list = None
        self._doctor_name = None
        self._drug_info_list = None
        self._expire_time = None
        self._ext_doctor_id = None
        self._ext_prescription_code = None
        self._inquiry_id = None
        self._medical_picture_list = None
        self._note = None
        self._patient_info = None
        self._pharmacist_name = None
        self._platform_code = None
        self._prescription_pdf = None
        self._prescription_png = None
        self._prescription_status = None
        self._prescription_time = None
        self._prescription_type = None

    @property
    def depart_name(self):
        return self._depart_name

    @depart_name.setter
    def depart_name(self, value):
        self._depart_name = value
    @property
    def disease_list(self):
        return self._disease_list

    @disease_list.setter
    def disease_list(self, value):
        if isinstance(value, list):
            self._disease_list = list()
            for i in value:
                if isinstance(i, DiseaseInfo):
                    self._disease_list.append(i)
                else:
                    self._disease_list.append(DiseaseInfo.from_alipay_dict(i))
    @property
    def doctor_name(self):
        return self._doctor_name

    @doctor_name.setter
    def doctor_name(self, value):
        self._doctor_name = value
    @property
    def drug_info_list(self):
        return self._drug_info_list

    @drug_info_list.setter
    def drug_info_list(self, value):
        if isinstance(value, list):
            self._drug_info_list = list()
            for i in value:
                if isinstance(i, DrugInfo):
                    self._drug_info_list.append(i)
                else:
                    self._drug_info_list.append(DrugInfo.from_alipay_dict(i))
    @property
    def expire_time(self):
        return self._expire_time

    @expire_time.setter
    def expire_time(self, value):
        self._expire_time = value
    @property
    def ext_doctor_id(self):
        return self._ext_doctor_id

    @ext_doctor_id.setter
    def ext_doctor_id(self, value):
        self._ext_doctor_id = value
    @property
    def ext_prescription_code(self):
        return self._ext_prescription_code

    @ext_prescription_code.setter
    def ext_prescription_code(self, value):
        self._ext_prescription_code = value
    @property
    def inquiry_id(self):
        return self._inquiry_id

    @inquiry_id.setter
    def inquiry_id(self, value):
        self._inquiry_id = value
    @property
    def medical_picture_list(self):
        return self._medical_picture_list

    @medical_picture_list.setter
    def medical_picture_list(self, value):
        if isinstance(value, list):
            self._medical_picture_list = list()
            for i in value:
                self._medical_picture_list.append(i)
    @property
    def note(self):
        return self._note

    @note.setter
    def note(self, value):
        self._note = value
    @property
    def patient_info(self):
        return self._patient_info

    @patient_info.setter
    def patient_info(self, value):
        if isinstance(value, PatientInfo):
            self._patient_info = value
        else:
            self._patient_info = PatientInfo.from_alipay_dict(value)
    @property
    def pharmacist_name(self):
        return self._pharmacist_name

    @pharmacist_name.setter
    def pharmacist_name(self, value):
        self._pharmacist_name = value
    @property
    def platform_code(self):
        return self._platform_code

    @platform_code.setter
    def platform_code(self, value):
        self._platform_code = value
    @property
    def prescription_pdf(self):
        return self._prescription_pdf

    @prescription_pdf.setter
    def prescription_pdf(self, value):
        self._prescription_pdf = value
    @property
    def prescription_png(self):
        return self._prescription_png

    @prescription_png.setter
    def prescription_png(self, value):
        self._prescription_png = value
    @property
    def prescription_status(self):
        return self._prescription_status

    @prescription_status.setter
    def prescription_status(self, value):
        self._prescription_status = value
    @property
    def prescription_time(self):
        return self._prescription_time

    @prescription_time.setter
    def prescription_time(self, value):
        self._prescription_time = value
    @property
    def prescription_type(self):
        return self._prescription_type

    @prescription_type.setter
    def prescription_type(self, value):
        self._prescription_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.depart_name:
            if hasattr(self.depart_name, 'to_alipay_dict'):
                params['depart_name'] = self.depart_name.to_alipay_dict()
            else:
                params['depart_name'] = self.depart_name
        if self.disease_list:
            if isinstance(self.disease_list, list):
                for i in range(0, len(self.disease_list)):
                    element = self.disease_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.disease_list[i] = element.to_alipay_dict()
            if hasattr(self.disease_list, 'to_alipay_dict'):
                params['disease_list'] = self.disease_list.to_alipay_dict()
            else:
                params['disease_list'] = self.disease_list
        if self.doctor_name:
            if hasattr(self.doctor_name, 'to_alipay_dict'):
                params['doctor_name'] = self.doctor_name.to_alipay_dict()
            else:
                params['doctor_name'] = self.doctor_name
        if self.drug_info_list:
            if isinstance(self.drug_info_list, list):
                for i in range(0, len(self.drug_info_list)):
                    element = self.drug_info_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.drug_info_list[i] = element.to_alipay_dict()
            if hasattr(self.drug_info_list, 'to_alipay_dict'):
                params['drug_info_list'] = self.drug_info_list.to_alipay_dict()
            else:
                params['drug_info_list'] = self.drug_info_list
        if self.expire_time:
            if hasattr(self.expire_time, 'to_alipay_dict'):
                params['expire_time'] = self.expire_time.to_alipay_dict()
            else:
                params['expire_time'] = self.expire_time
        if self.ext_doctor_id:
            if hasattr(self.ext_doctor_id, 'to_alipay_dict'):
                params['ext_doctor_id'] = self.ext_doctor_id.to_alipay_dict()
            else:
                params['ext_doctor_id'] = self.ext_doctor_id
        if self.ext_prescription_code:
            if hasattr(self.ext_prescription_code, 'to_alipay_dict'):
                params['ext_prescription_code'] = self.ext_prescription_code.to_alipay_dict()
            else:
                params['ext_prescription_code'] = self.ext_prescription_code
        if self.inquiry_id:
            if hasattr(self.inquiry_id, 'to_alipay_dict'):
                params['inquiry_id'] = self.inquiry_id.to_alipay_dict()
            else:
                params['inquiry_id'] = self.inquiry_id
        if self.medical_picture_list:
            if isinstance(self.medical_picture_list, list):
                for i in range(0, len(self.medical_picture_list)):
                    element = self.medical_picture_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.medical_picture_list[i] = element.to_alipay_dict()
            if hasattr(self.medical_picture_list, 'to_alipay_dict'):
                params['medical_picture_list'] = self.medical_picture_list.to_alipay_dict()
            else:
                params['medical_picture_list'] = self.medical_picture_list
        if self.note:
            if hasattr(self.note, 'to_alipay_dict'):
                params['note'] = self.note.to_alipay_dict()
            else:
                params['note'] = self.note
        if self.patient_info:
            if hasattr(self.patient_info, 'to_alipay_dict'):
                params['patient_info'] = self.patient_info.to_alipay_dict()
            else:
                params['patient_info'] = self.patient_info
        if self.pharmacist_name:
            if hasattr(self.pharmacist_name, 'to_alipay_dict'):
                params['pharmacist_name'] = self.pharmacist_name.to_alipay_dict()
            else:
                params['pharmacist_name'] = self.pharmacist_name
        if self.platform_code:
            if hasattr(self.platform_code, 'to_alipay_dict'):
                params['platform_code'] = self.platform_code.to_alipay_dict()
            else:
                params['platform_code'] = self.platform_code
        if self.prescription_pdf:
            if hasattr(self.prescription_pdf, 'to_alipay_dict'):
                params['prescription_pdf'] = self.prescription_pdf.to_alipay_dict()
            else:
                params['prescription_pdf'] = self.prescription_pdf
        if self.prescription_png:
            if hasattr(self.prescription_png, 'to_alipay_dict'):
                params['prescription_png'] = self.prescription_png.to_alipay_dict()
            else:
                params['prescription_png'] = self.prescription_png
        if self.prescription_status:
            if hasattr(self.prescription_status, 'to_alipay_dict'):
                params['prescription_status'] = self.prescription_status.to_alipay_dict()
            else:
                params['prescription_status'] = self.prescription_status
        if self.prescription_time:
            if hasattr(self.prescription_time, 'to_alipay_dict'):
                params['prescription_time'] = self.prescription_time.to_alipay_dict()
            else:
                params['prescription_time'] = self.prescription_time
        if self.prescription_type:
            if hasattr(self.prescription_type, 'to_alipay_dict'):
                params['prescription_type'] = self.prescription_type.to_alipay_dict()
            else:
                params['prescription_type'] = self.prescription_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceMedicalMedicinePrescriptionorderUploadModel()
        if 'depart_name' in d:
            o.depart_name = d['depart_name']
        if 'disease_list' in d:
            o.disease_list = d['disease_list']
        if 'doctor_name' in d:
            o.doctor_name = d['doctor_name']
        if 'drug_info_list' in d:
            o.drug_info_list = d['drug_info_list']
        if 'expire_time' in d:
            o.expire_time = d['expire_time']
        if 'ext_doctor_id' in d:
            o.ext_doctor_id = d['ext_doctor_id']
        if 'ext_prescription_code' in d:
            o.ext_prescription_code = d['ext_prescription_code']
        if 'inquiry_id' in d:
            o.inquiry_id = d['inquiry_id']
        if 'medical_picture_list' in d:
            o.medical_picture_list = d['medical_picture_list']
        if 'note' in d:
            o.note = d['note']
        if 'patient_info' in d:
            o.patient_info = d['patient_info']
        if 'pharmacist_name' in d:
            o.pharmacist_name = d['pharmacist_name']
        if 'platform_code' in d:
            o.platform_code = d['platform_code']
        if 'prescription_pdf' in d:
            o.prescription_pdf = d['prescription_pdf']
        if 'prescription_png' in d:
            o.prescription_png = d['prescription_png']
        if 'prescription_status' in d:
            o.prescription_status = d['prescription_status']
        if 'prescription_time' in d:
            o.prescription_time = d['prescription_time']
        if 'prescription_type' in d:
            o.prescription_type = d['prescription_type']
        return o


