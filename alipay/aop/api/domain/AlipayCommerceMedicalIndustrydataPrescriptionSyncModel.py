#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.PlatformPrescriptionDrugInfo import PlatformPrescriptionDrugInfo


class AlipayCommerceMedicalIndustrydataPrescriptionSyncModel(object):

    def __init__(self):
        self._alipay_open_id = None
        self._alipay_order_id = None
        self._alipay_user_id = None
        self._audit_pharmacist_name = None
        self._clinic_desc = None
        self._doctor_name = None
        self._drug_list = None
        self._group_no = None
        self._medical_institution_name = None
        self._merchant_doctor_id = None
        self._merchant_user_id = None
        self._out_audit_pharmacist_id = None
        self._out_order_id = None
        self._out_prescription_id = None
        self._out_prescription_url = None
        self._patient_age = None
        self._patient_idcard = None
        self._patient_name = None
        self._patient_phone = None
        self._patient_sex = None
        self._platform_code = None
        self._prescription_status = None
        self._prescription_time = None
        self._prescription_type = None
        self._syndrome_type = None

    @property
    def alipay_open_id(self):
        return self._alipay_open_id

    @alipay_open_id.setter
    def alipay_open_id(self, value):
        self._alipay_open_id = value
    @property
    def alipay_order_id(self):
        return self._alipay_order_id

    @alipay_order_id.setter
    def alipay_order_id(self, value):
        self._alipay_order_id = value
    @property
    def alipay_user_id(self):
        return self._alipay_user_id

    @alipay_user_id.setter
    def alipay_user_id(self, value):
        self._alipay_user_id = value
    @property
    def audit_pharmacist_name(self):
        return self._audit_pharmacist_name

    @audit_pharmacist_name.setter
    def audit_pharmacist_name(self, value):
        self._audit_pharmacist_name = value
    @property
    def clinic_desc(self):
        return self._clinic_desc

    @clinic_desc.setter
    def clinic_desc(self, value):
        self._clinic_desc = value
    @property
    def doctor_name(self):
        return self._doctor_name

    @doctor_name.setter
    def doctor_name(self, value):
        self._doctor_name = value
    @property
    def drug_list(self):
        return self._drug_list

    @drug_list.setter
    def drug_list(self, value):
        if isinstance(value, list):
            self._drug_list = list()
            for i in value:
                if isinstance(i, PlatformPrescriptionDrugInfo):
                    self._drug_list.append(i)
                else:
                    self._drug_list.append(PlatformPrescriptionDrugInfo.from_alipay_dict(i))
    @property
    def group_no(self):
        return self._group_no

    @group_no.setter
    def group_no(self, value):
        self._group_no = value
    @property
    def medical_institution_name(self):
        return self._medical_institution_name

    @medical_institution_name.setter
    def medical_institution_name(self, value):
        self._medical_institution_name = value
    @property
    def merchant_doctor_id(self):
        return self._merchant_doctor_id

    @merchant_doctor_id.setter
    def merchant_doctor_id(self, value):
        self._merchant_doctor_id = value
    @property
    def merchant_user_id(self):
        return self._merchant_user_id

    @merchant_user_id.setter
    def merchant_user_id(self, value):
        self._merchant_user_id = value
    @property
    def out_audit_pharmacist_id(self):
        return self._out_audit_pharmacist_id

    @out_audit_pharmacist_id.setter
    def out_audit_pharmacist_id(self, value):
        self._out_audit_pharmacist_id = value
    @property
    def out_order_id(self):
        return self._out_order_id

    @out_order_id.setter
    def out_order_id(self, value):
        self._out_order_id = value
    @property
    def out_prescription_id(self):
        return self._out_prescription_id

    @out_prescription_id.setter
    def out_prescription_id(self, value):
        self._out_prescription_id = value
    @property
    def out_prescription_url(self):
        return self._out_prescription_url

    @out_prescription_url.setter
    def out_prescription_url(self, value):
        self._out_prescription_url = value
    @property
    def patient_age(self):
        return self._patient_age

    @patient_age.setter
    def patient_age(self, value):
        self._patient_age = value
    @property
    def patient_idcard(self):
        return self._patient_idcard

    @patient_idcard.setter
    def patient_idcard(self, value):
        self._patient_idcard = value
    @property
    def patient_name(self):
        return self._patient_name

    @patient_name.setter
    def patient_name(self, value):
        self._patient_name = value
    @property
    def patient_phone(self):
        return self._patient_phone

    @patient_phone.setter
    def patient_phone(self, value):
        self._patient_phone = value
    @property
    def patient_sex(self):
        return self._patient_sex

    @patient_sex.setter
    def patient_sex(self, value):
        self._patient_sex = value
    @property
    def platform_code(self):
        return self._platform_code

    @platform_code.setter
    def platform_code(self, value):
        self._platform_code = value
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
    @property
    def syndrome_type(self):
        return self._syndrome_type

    @syndrome_type.setter
    def syndrome_type(self, value):
        self._syndrome_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.alipay_open_id:
            if hasattr(self.alipay_open_id, 'to_alipay_dict'):
                params['alipay_open_id'] = self.alipay_open_id.to_alipay_dict()
            else:
                params['alipay_open_id'] = self.alipay_open_id
        if self.alipay_order_id:
            if hasattr(self.alipay_order_id, 'to_alipay_dict'):
                params['alipay_order_id'] = self.alipay_order_id.to_alipay_dict()
            else:
                params['alipay_order_id'] = self.alipay_order_id
        if self.alipay_user_id:
            if hasattr(self.alipay_user_id, 'to_alipay_dict'):
                params['alipay_user_id'] = self.alipay_user_id.to_alipay_dict()
            else:
                params['alipay_user_id'] = self.alipay_user_id
        if self.audit_pharmacist_name:
            if hasattr(self.audit_pharmacist_name, 'to_alipay_dict'):
                params['audit_pharmacist_name'] = self.audit_pharmacist_name.to_alipay_dict()
            else:
                params['audit_pharmacist_name'] = self.audit_pharmacist_name
        if self.clinic_desc:
            if hasattr(self.clinic_desc, 'to_alipay_dict'):
                params['clinic_desc'] = self.clinic_desc.to_alipay_dict()
            else:
                params['clinic_desc'] = self.clinic_desc
        if self.doctor_name:
            if hasattr(self.doctor_name, 'to_alipay_dict'):
                params['doctor_name'] = self.doctor_name.to_alipay_dict()
            else:
                params['doctor_name'] = self.doctor_name
        if self.drug_list:
            if isinstance(self.drug_list, list):
                for i in range(0, len(self.drug_list)):
                    element = self.drug_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.drug_list[i] = element.to_alipay_dict()
            if hasattr(self.drug_list, 'to_alipay_dict'):
                params['drug_list'] = self.drug_list.to_alipay_dict()
            else:
                params['drug_list'] = self.drug_list
        if self.group_no:
            if hasattr(self.group_no, 'to_alipay_dict'):
                params['group_no'] = self.group_no.to_alipay_dict()
            else:
                params['group_no'] = self.group_no
        if self.medical_institution_name:
            if hasattr(self.medical_institution_name, 'to_alipay_dict'):
                params['medical_institution_name'] = self.medical_institution_name.to_alipay_dict()
            else:
                params['medical_institution_name'] = self.medical_institution_name
        if self.merchant_doctor_id:
            if hasattr(self.merchant_doctor_id, 'to_alipay_dict'):
                params['merchant_doctor_id'] = self.merchant_doctor_id.to_alipay_dict()
            else:
                params['merchant_doctor_id'] = self.merchant_doctor_id
        if self.merchant_user_id:
            if hasattr(self.merchant_user_id, 'to_alipay_dict'):
                params['merchant_user_id'] = self.merchant_user_id.to_alipay_dict()
            else:
                params['merchant_user_id'] = self.merchant_user_id
        if self.out_audit_pharmacist_id:
            if hasattr(self.out_audit_pharmacist_id, 'to_alipay_dict'):
                params['out_audit_pharmacist_id'] = self.out_audit_pharmacist_id.to_alipay_dict()
            else:
                params['out_audit_pharmacist_id'] = self.out_audit_pharmacist_id
        if self.out_order_id:
            if hasattr(self.out_order_id, 'to_alipay_dict'):
                params['out_order_id'] = self.out_order_id.to_alipay_dict()
            else:
                params['out_order_id'] = self.out_order_id
        if self.out_prescription_id:
            if hasattr(self.out_prescription_id, 'to_alipay_dict'):
                params['out_prescription_id'] = self.out_prescription_id.to_alipay_dict()
            else:
                params['out_prescription_id'] = self.out_prescription_id
        if self.out_prescription_url:
            if hasattr(self.out_prescription_url, 'to_alipay_dict'):
                params['out_prescription_url'] = self.out_prescription_url.to_alipay_dict()
            else:
                params['out_prescription_url'] = self.out_prescription_url
        if self.patient_age:
            if hasattr(self.patient_age, 'to_alipay_dict'):
                params['patient_age'] = self.patient_age.to_alipay_dict()
            else:
                params['patient_age'] = self.patient_age
        if self.patient_idcard:
            if hasattr(self.patient_idcard, 'to_alipay_dict'):
                params['patient_idcard'] = self.patient_idcard.to_alipay_dict()
            else:
                params['patient_idcard'] = self.patient_idcard
        if self.patient_name:
            if hasattr(self.patient_name, 'to_alipay_dict'):
                params['patient_name'] = self.patient_name.to_alipay_dict()
            else:
                params['patient_name'] = self.patient_name
        if self.patient_phone:
            if hasattr(self.patient_phone, 'to_alipay_dict'):
                params['patient_phone'] = self.patient_phone.to_alipay_dict()
            else:
                params['patient_phone'] = self.patient_phone
        if self.patient_sex:
            if hasattr(self.patient_sex, 'to_alipay_dict'):
                params['patient_sex'] = self.patient_sex.to_alipay_dict()
            else:
                params['patient_sex'] = self.patient_sex
        if self.platform_code:
            if hasattr(self.platform_code, 'to_alipay_dict'):
                params['platform_code'] = self.platform_code.to_alipay_dict()
            else:
                params['platform_code'] = self.platform_code
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
        if self.syndrome_type:
            if hasattr(self.syndrome_type, 'to_alipay_dict'):
                params['syndrome_type'] = self.syndrome_type.to_alipay_dict()
            else:
                params['syndrome_type'] = self.syndrome_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceMedicalIndustrydataPrescriptionSyncModel()
        if 'alipay_open_id' in d:
            o.alipay_open_id = d['alipay_open_id']
        if 'alipay_order_id' in d:
            o.alipay_order_id = d['alipay_order_id']
        if 'alipay_user_id' in d:
            o.alipay_user_id = d['alipay_user_id']
        if 'audit_pharmacist_name' in d:
            o.audit_pharmacist_name = d['audit_pharmacist_name']
        if 'clinic_desc' in d:
            o.clinic_desc = d['clinic_desc']
        if 'doctor_name' in d:
            o.doctor_name = d['doctor_name']
        if 'drug_list' in d:
            o.drug_list = d['drug_list']
        if 'group_no' in d:
            o.group_no = d['group_no']
        if 'medical_institution_name' in d:
            o.medical_institution_name = d['medical_institution_name']
        if 'merchant_doctor_id' in d:
            o.merchant_doctor_id = d['merchant_doctor_id']
        if 'merchant_user_id' in d:
            o.merchant_user_id = d['merchant_user_id']
        if 'out_audit_pharmacist_id' in d:
            o.out_audit_pharmacist_id = d['out_audit_pharmacist_id']
        if 'out_order_id' in d:
            o.out_order_id = d['out_order_id']
        if 'out_prescription_id' in d:
            o.out_prescription_id = d['out_prescription_id']
        if 'out_prescription_url' in d:
            o.out_prescription_url = d['out_prescription_url']
        if 'patient_age' in d:
            o.patient_age = d['patient_age']
        if 'patient_idcard' in d:
            o.patient_idcard = d['patient_idcard']
        if 'patient_name' in d:
            o.patient_name = d['patient_name']
        if 'patient_phone' in d:
            o.patient_phone = d['patient_phone']
        if 'patient_sex' in d:
            o.patient_sex = d['patient_sex']
        if 'platform_code' in d:
            o.platform_code = d['platform_code']
        if 'prescription_status' in d:
            o.prescription_status = d['prescription_status']
        if 'prescription_time' in d:
            o.prescription_time = d['prescription_time']
        if 'prescription_type' in d:
            o.prescription_type = d['prescription_type']
        if 'syndrome_type' in d:
            o.syndrome_type = d['syndrome_type']
        return o


