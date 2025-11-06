#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCommerceMedicalHzreferralformDetailGetResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceMedicalHzreferralformDetailGetResponse, self).__init__()
        self._age = None
        self._area = None
        self._cert_no = None
        self._doctor_phone_no = None
        self._doctor_remark = None
        self._expected_date = None
        self._expected_hospital = None
        self._gmt_create = None
        self._gmt_modify = None
        self._image_list = None
        self._pass_history = None
        self._phone_no = None
        self._referral_form_id = None
        self._remark = None
        self._scales = None
        self._sex = None
        self._status = None
        self._user_description = None
        self._user_name = None
        self._visit_department = None
        self._visit_doctor = None
        self._visit_hospital = None
        self._visit_time = None

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        self._age = value
    @property
    def area(self):
        return self._area

    @area.setter
    def area(self, value):
        self._area = value
    @property
    def cert_no(self):
        return self._cert_no

    @cert_no.setter
    def cert_no(self, value):
        self._cert_no = value
    @property
    def doctor_phone_no(self):
        return self._doctor_phone_no

    @doctor_phone_no.setter
    def doctor_phone_no(self, value):
        self._doctor_phone_no = value
    @property
    def doctor_remark(self):
        return self._doctor_remark

    @doctor_remark.setter
    def doctor_remark(self, value):
        self._doctor_remark = value
    @property
    def expected_date(self):
        return self._expected_date

    @expected_date.setter
    def expected_date(self, value):
        self._expected_date = value
    @property
    def expected_hospital(self):
        return self._expected_hospital

    @expected_hospital.setter
    def expected_hospital(self, value):
        self._expected_hospital = value
    @property
    def gmt_create(self):
        return self._gmt_create

    @gmt_create.setter
    def gmt_create(self, value):
        self._gmt_create = value
    @property
    def gmt_modify(self):
        return self._gmt_modify

    @gmt_modify.setter
    def gmt_modify(self, value):
        self._gmt_modify = value
    @property
    def image_list(self):
        return self._image_list

    @image_list.setter
    def image_list(self, value):
        if isinstance(value, list):
            self._image_list = list()
            for i in value:
                self._image_list.append(i)
    @property
    def pass_history(self):
        return self._pass_history

    @pass_history.setter
    def pass_history(self, value):
        self._pass_history = value
    @property
    def phone_no(self):
        return self._phone_no

    @phone_no.setter
    def phone_no(self, value):
        self._phone_no = value
    @property
    def referral_form_id(self):
        return self._referral_form_id

    @referral_form_id.setter
    def referral_form_id(self, value):
        self._referral_form_id = value
    @property
    def remark(self):
        return self._remark

    @remark.setter
    def remark(self, value):
        self._remark = value
    @property
    def scales(self):
        return self._scales

    @scales.setter
    def scales(self, value):
        self._scales = value
    @property
    def sex(self):
        return self._sex

    @sex.setter
    def sex(self, value):
        self._sex = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value
    @property
    def user_description(self):
        return self._user_description

    @user_description.setter
    def user_description(self, value):
        self._user_description = value
    @property
    def user_name(self):
        return self._user_name

    @user_name.setter
    def user_name(self, value):
        self._user_name = value
    @property
    def visit_department(self):
        return self._visit_department

    @visit_department.setter
    def visit_department(self, value):
        self._visit_department = value
    @property
    def visit_doctor(self):
        return self._visit_doctor

    @visit_doctor.setter
    def visit_doctor(self, value):
        self._visit_doctor = value
    @property
    def visit_hospital(self):
        return self._visit_hospital

    @visit_hospital.setter
    def visit_hospital(self, value):
        self._visit_hospital = value
    @property
    def visit_time(self):
        return self._visit_time

    @visit_time.setter
    def visit_time(self, value):
        self._visit_time = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceMedicalHzreferralformDetailGetResponse, self).parse_response_content(response_content)
        if 'age' in response:
            self.age = response['age']
        if 'area' in response:
            self.area = response['area']
        if 'cert_no' in response:
            self.cert_no = response['cert_no']
        if 'doctor_phone_no' in response:
            self.doctor_phone_no = response['doctor_phone_no']
        if 'doctor_remark' in response:
            self.doctor_remark = response['doctor_remark']
        if 'expected_date' in response:
            self.expected_date = response['expected_date']
        if 'expected_hospital' in response:
            self.expected_hospital = response['expected_hospital']
        if 'gmt_create' in response:
            self.gmt_create = response['gmt_create']
        if 'gmt_modify' in response:
            self.gmt_modify = response['gmt_modify']
        if 'image_list' in response:
            self.image_list = response['image_list']
        if 'pass_history' in response:
            self.pass_history = response['pass_history']
        if 'phone_no' in response:
            self.phone_no = response['phone_no']
        if 'referral_form_id' in response:
            self.referral_form_id = response['referral_form_id']
        if 'remark' in response:
            self.remark = response['remark']
        if 'scales' in response:
            self.scales = response['scales']
        if 'sex' in response:
            self.sex = response['sex']
        if 'status' in response:
            self.status = response['status']
        if 'user_description' in response:
            self.user_description = response['user_description']
        if 'user_name' in response:
            self.user_name = response['user_name']
        if 'visit_department' in response:
            self.visit_department = response['visit_department']
        if 'visit_doctor' in response:
            self.visit_doctor = response['visit_doctor']
        if 'visit_hospital' in response:
            self.visit_hospital = response['visit_hospital']
        if 'visit_time' in response:
            self.visit_time = response['visit_time']
