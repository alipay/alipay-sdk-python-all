#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.DoctorHospitalScheduleInfoDTO import DoctorHospitalScheduleInfoDTO
from alipay.aop.api.domain.InquiryServiceInfo import InquiryServiceInfo


class AlipayCommerceMedicalLargermodelDoctorscheduleQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceMedicalLargermodelDoctorscheduleQueryResponse, self).__init__()
        self._chat_id = None
        self._department_name = None
        self._detail_url = None
        self._doctor_gender = None
        self._doctor_id = None
        self._doctor_inner_id = None
        self._doctor_logo = None
        self._doctor_name = None
        self._education_title = None
        self._hospital_dep_feature_tags = None
        self._hospital_level = None
        self._hospital_name = None
        self._hospital_register_info_list = None
        self._hospital_uinq_code = None
        self._page_key = None
        self._platform_code = None
        self._register_page_url = None
        self._schedule_desc = None
        self._second_page_key = None
        self._service_info_list = None
        self._title = None

    @property
    def chat_id(self):
        return self._chat_id

    @chat_id.setter
    def chat_id(self, value):
        self._chat_id = value
    @property
    def department_name(self):
        return self._department_name

    @department_name.setter
    def department_name(self, value):
        self._department_name = value
    @property
    def detail_url(self):
        return self._detail_url

    @detail_url.setter
    def detail_url(self, value):
        self._detail_url = value
    @property
    def doctor_gender(self):
        return self._doctor_gender

    @doctor_gender.setter
    def doctor_gender(self, value):
        self._doctor_gender = value
    @property
    def doctor_id(self):
        return self._doctor_id

    @doctor_id.setter
    def doctor_id(self, value):
        self._doctor_id = value
    @property
    def doctor_inner_id(self):
        return self._doctor_inner_id

    @doctor_inner_id.setter
    def doctor_inner_id(self, value):
        self._doctor_inner_id = value
    @property
    def doctor_logo(self):
        return self._doctor_logo

    @doctor_logo.setter
    def doctor_logo(self, value):
        self._doctor_logo = value
    @property
    def doctor_name(self):
        return self._doctor_name

    @doctor_name.setter
    def doctor_name(self, value):
        self._doctor_name = value
    @property
    def education_title(self):
        return self._education_title

    @education_title.setter
    def education_title(self, value):
        self._education_title = value
    @property
    def hospital_dep_feature_tags(self):
        return self._hospital_dep_feature_tags

    @hospital_dep_feature_tags.setter
    def hospital_dep_feature_tags(self, value):
        if isinstance(value, list):
            self._hospital_dep_feature_tags = list()
            for i in value:
                self._hospital_dep_feature_tags.append(i)
    @property
    def hospital_level(self):
        return self._hospital_level

    @hospital_level.setter
    def hospital_level(self, value):
        self._hospital_level = value
    @property
    def hospital_name(self):
        return self._hospital_name

    @hospital_name.setter
    def hospital_name(self, value):
        self._hospital_name = value
    @property
    def hospital_register_info_list(self):
        return self._hospital_register_info_list

    @hospital_register_info_list.setter
    def hospital_register_info_list(self, value):
        if isinstance(value, list):
            self._hospital_register_info_list = list()
            for i in value:
                if isinstance(i, DoctorHospitalScheduleInfoDTO):
                    self._hospital_register_info_list.append(i)
                else:
                    self._hospital_register_info_list.append(DoctorHospitalScheduleInfoDTO.from_alipay_dict(i))
    @property
    def hospital_uinq_code(self):
        return self._hospital_uinq_code

    @hospital_uinq_code.setter
    def hospital_uinq_code(self, value):
        self._hospital_uinq_code = value
    @property
    def page_key(self):
        return self._page_key

    @page_key.setter
    def page_key(self, value):
        self._page_key = value
    @property
    def platform_code(self):
        return self._platform_code

    @platform_code.setter
    def platform_code(self, value):
        self._platform_code = value
    @property
    def register_page_url(self):
        return self._register_page_url

    @register_page_url.setter
    def register_page_url(self, value):
        self._register_page_url = value
    @property
    def schedule_desc(self):
        return self._schedule_desc

    @schedule_desc.setter
    def schedule_desc(self, value):
        self._schedule_desc = value
    @property
    def second_page_key(self):
        return self._second_page_key

    @second_page_key.setter
    def second_page_key(self, value):
        self._second_page_key = value
    @property
    def service_info_list(self):
        return self._service_info_list

    @service_info_list.setter
    def service_info_list(self, value):
        if isinstance(value, list):
            self._service_info_list = list()
            for i in value:
                if isinstance(i, InquiryServiceInfo):
                    self._service_info_list.append(i)
                else:
                    self._service_info_list.append(InquiryServiceInfo.from_alipay_dict(i))
    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        self._title = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceMedicalLargermodelDoctorscheduleQueryResponse, self).parse_response_content(response_content)
        if 'chat_id' in response:
            self.chat_id = response['chat_id']
        if 'department_name' in response:
            self.department_name = response['department_name']
        if 'detail_url' in response:
            self.detail_url = response['detail_url']
        if 'doctor_gender' in response:
            self.doctor_gender = response['doctor_gender']
        if 'doctor_id' in response:
            self.doctor_id = response['doctor_id']
        if 'doctor_inner_id' in response:
            self.doctor_inner_id = response['doctor_inner_id']
        if 'doctor_logo' in response:
            self.doctor_logo = response['doctor_logo']
        if 'doctor_name' in response:
            self.doctor_name = response['doctor_name']
        if 'education_title' in response:
            self.education_title = response['education_title']
        if 'hospital_dep_feature_tags' in response:
            self.hospital_dep_feature_tags = response['hospital_dep_feature_tags']
        if 'hospital_level' in response:
            self.hospital_level = response['hospital_level']
        if 'hospital_name' in response:
            self.hospital_name = response['hospital_name']
        if 'hospital_register_info_list' in response:
            self.hospital_register_info_list = response['hospital_register_info_list']
        if 'hospital_uinq_code' in response:
            self.hospital_uinq_code = response['hospital_uinq_code']
        if 'page_key' in response:
            self.page_key = response['page_key']
        if 'platform_code' in response:
            self.platform_code = response['platform_code']
        if 'register_page_url' in response:
            self.register_page_url = response['register_page_url']
        if 'schedule_desc' in response:
            self.schedule_desc = response['schedule_desc']
        if 'second_page_key' in response:
            self.second_page_key = response['second_page_key']
        if 'service_info_list' in response:
            self.service_info_list = response['service_info_list']
        if 'title' in response:
            self.title = response['title']
