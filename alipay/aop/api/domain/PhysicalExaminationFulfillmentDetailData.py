#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class PhysicalExaminationFulfillmentDetailData(object):

    def __init__(self):
        self._appointment_end_time = None
        self._appointment_start_time = None
        self._birth_date = None
        self._cancel_time = None
        self._cert_no = None
        self._cert_type = None
        self._create_time = None
        self._examinee_name = None
        self._finish_time = None
        self._gender = None
        self._marital_status = None
        self._package_name = None
        self._phone = None
        self._service_city = None
        self._service_institution = None
        self._update_time = None

    @property
    def appointment_end_time(self):
        return self._appointment_end_time

    @appointment_end_time.setter
    def appointment_end_time(self, value):
        self._appointment_end_time = value
    @property
    def appointment_start_time(self):
        return self._appointment_start_time

    @appointment_start_time.setter
    def appointment_start_time(self, value):
        self._appointment_start_time = value
    @property
    def birth_date(self):
        return self._birth_date

    @birth_date.setter
    def birth_date(self, value):
        self._birth_date = value
    @property
    def cancel_time(self):
        return self._cancel_time

    @cancel_time.setter
    def cancel_time(self, value):
        self._cancel_time = value
    @property
    def cert_no(self):
        return self._cert_no

    @cert_no.setter
    def cert_no(self, value):
        self._cert_no = value
    @property
    def cert_type(self):
        return self._cert_type

    @cert_type.setter
    def cert_type(self, value):
        self._cert_type = value
    @property
    def create_time(self):
        return self._create_time

    @create_time.setter
    def create_time(self, value):
        self._create_time = value
    @property
    def examinee_name(self):
        return self._examinee_name

    @examinee_name.setter
    def examinee_name(self, value):
        self._examinee_name = value
    @property
    def finish_time(self):
        return self._finish_time

    @finish_time.setter
    def finish_time(self, value):
        self._finish_time = value
    @property
    def gender(self):
        return self._gender

    @gender.setter
    def gender(self, value):
        self._gender = value
    @property
    def marital_status(self):
        return self._marital_status

    @marital_status.setter
    def marital_status(self, value):
        self._marital_status = value
    @property
    def package_name(self):
        return self._package_name

    @package_name.setter
    def package_name(self, value):
        self._package_name = value
    @property
    def phone(self):
        return self._phone

    @phone.setter
    def phone(self, value):
        self._phone = value
    @property
    def service_city(self):
        return self._service_city

    @service_city.setter
    def service_city(self, value):
        self._service_city = value
    @property
    def service_institution(self):
        return self._service_institution

    @service_institution.setter
    def service_institution(self, value):
        self._service_institution = value
    @property
    def update_time(self):
        return self._update_time

    @update_time.setter
    def update_time(self, value):
        self._update_time = value


    def to_alipay_dict(self):
        params = dict()
        if self.appointment_end_time:
            if hasattr(self.appointment_end_time, 'to_alipay_dict'):
                params['appointment_end_time'] = self.appointment_end_time.to_alipay_dict()
            else:
                params['appointment_end_time'] = self.appointment_end_time
        if self.appointment_start_time:
            if hasattr(self.appointment_start_time, 'to_alipay_dict'):
                params['appointment_start_time'] = self.appointment_start_time.to_alipay_dict()
            else:
                params['appointment_start_time'] = self.appointment_start_time
        if self.birth_date:
            if hasattr(self.birth_date, 'to_alipay_dict'):
                params['birth_date'] = self.birth_date.to_alipay_dict()
            else:
                params['birth_date'] = self.birth_date
        if self.cancel_time:
            if hasattr(self.cancel_time, 'to_alipay_dict'):
                params['cancel_time'] = self.cancel_time.to_alipay_dict()
            else:
                params['cancel_time'] = self.cancel_time
        if self.cert_no:
            if hasattr(self.cert_no, 'to_alipay_dict'):
                params['cert_no'] = self.cert_no.to_alipay_dict()
            else:
                params['cert_no'] = self.cert_no
        if self.cert_type:
            if hasattr(self.cert_type, 'to_alipay_dict'):
                params['cert_type'] = self.cert_type.to_alipay_dict()
            else:
                params['cert_type'] = self.cert_type
        if self.create_time:
            if hasattr(self.create_time, 'to_alipay_dict'):
                params['create_time'] = self.create_time.to_alipay_dict()
            else:
                params['create_time'] = self.create_time
        if self.examinee_name:
            if hasattr(self.examinee_name, 'to_alipay_dict'):
                params['examinee_name'] = self.examinee_name.to_alipay_dict()
            else:
                params['examinee_name'] = self.examinee_name
        if self.finish_time:
            if hasattr(self.finish_time, 'to_alipay_dict'):
                params['finish_time'] = self.finish_time.to_alipay_dict()
            else:
                params['finish_time'] = self.finish_time
        if self.gender:
            if hasattr(self.gender, 'to_alipay_dict'):
                params['gender'] = self.gender.to_alipay_dict()
            else:
                params['gender'] = self.gender
        if self.marital_status:
            if hasattr(self.marital_status, 'to_alipay_dict'):
                params['marital_status'] = self.marital_status.to_alipay_dict()
            else:
                params['marital_status'] = self.marital_status
        if self.package_name:
            if hasattr(self.package_name, 'to_alipay_dict'):
                params['package_name'] = self.package_name.to_alipay_dict()
            else:
                params['package_name'] = self.package_name
        if self.phone:
            if hasattr(self.phone, 'to_alipay_dict'):
                params['phone'] = self.phone.to_alipay_dict()
            else:
                params['phone'] = self.phone
        if self.service_city:
            if hasattr(self.service_city, 'to_alipay_dict'):
                params['service_city'] = self.service_city.to_alipay_dict()
            else:
                params['service_city'] = self.service_city
        if self.service_institution:
            if hasattr(self.service_institution, 'to_alipay_dict'):
                params['service_institution'] = self.service_institution.to_alipay_dict()
            else:
                params['service_institution'] = self.service_institution
        if self.update_time:
            if hasattr(self.update_time, 'to_alipay_dict'):
                params['update_time'] = self.update_time.to_alipay_dict()
            else:
                params['update_time'] = self.update_time
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = PhysicalExaminationFulfillmentDetailData()
        if 'appointment_end_time' in d:
            o.appointment_end_time = d['appointment_end_time']
        if 'appointment_start_time' in d:
            o.appointment_start_time = d['appointment_start_time']
        if 'birth_date' in d:
            o.birth_date = d['birth_date']
        if 'cancel_time' in d:
            o.cancel_time = d['cancel_time']
        if 'cert_no' in d:
            o.cert_no = d['cert_no']
        if 'cert_type' in d:
            o.cert_type = d['cert_type']
        if 'create_time' in d:
            o.create_time = d['create_time']
        if 'examinee_name' in d:
            o.examinee_name = d['examinee_name']
        if 'finish_time' in d:
            o.finish_time = d['finish_time']
        if 'gender' in d:
            o.gender = d['gender']
        if 'marital_status' in d:
            o.marital_status = d['marital_status']
        if 'package_name' in d:
            o.package_name = d['package_name']
        if 'phone' in d:
            o.phone = d['phone']
        if 'service_city' in d:
            o.service_city = d['service_city']
        if 'service_institution' in d:
            o.service_institution = d['service_institution']
        if 'update_time' in d:
            o.update_time = d['update_time']
        return o


