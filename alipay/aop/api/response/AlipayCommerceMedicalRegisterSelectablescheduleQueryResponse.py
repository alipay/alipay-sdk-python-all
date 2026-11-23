#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.DoctorHospitalScheduleInfoDTO import DoctorHospitalScheduleInfoDTO
from alipay.aop.api.domain.ReigsterServiceInfo import ReigsterServiceInfo


class AlipayCommerceMedicalRegisterSelectablescheduleQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceMedicalRegisterSelectablescheduleQueryResponse, self).__init__()
        self._afu_download_match_crowd = None
        self._department_name = None
        self._detail_url = None
        self._doctor_desc = None
        self._doctor_gender = None
        self._doctor_id = None
        self._doctor_inner_id = None
        self._doctor_logo = None
        self._doctor_name = None
        self._education_title = None
        self._flow_to_aq_model = None
        self._has_available_source = None
        self._has_more = None
        self._hospital_dep_feature_tags = None
        self._hospital_level = None
        self._hospital_name = None
        self._hospital_register_info_list = None
        self._hospital_type = None
        self._hospital_uinq_code = None
        self._muti_isv = None
        self._page_key = None
        self._platform_code = None
        self._proficiency = None
        self._res_prop = None
        self._schedule_desc = None
        self._scm_info = None
        self._second_page_key = None
        self._service_info_list = None
        self._title = None
        self._total_count = None

    @property
    def afu_download_match_crowd(self):
        return self._afu_download_match_crowd

    @afu_download_match_crowd.setter
    def afu_download_match_crowd(self, value):
        self._afu_download_match_crowd = value
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
    def doctor_desc(self):
        return self._doctor_desc

    @doctor_desc.setter
    def doctor_desc(self, value):
        self._doctor_desc = value
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
    def flow_to_aq_model(self):
        return self._flow_to_aq_model

    @flow_to_aq_model.setter
    def flow_to_aq_model(self, value):
        self._flow_to_aq_model = value
    @property
    def has_available_source(self):
        return self._has_available_source

    @has_available_source.setter
    def has_available_source(self, value):
        self._has_available_source = value
    @property
    def has_more(self):
        return self._has_more

    @has_more.setter
    def has_more(self, value):
        self._has_more = value
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
    def hospital_type(self):
        return self._hospital_type

    @hospital_type.setter
    def hospital_type(self, value):
        self._hospital_type = value
    @property
    def hospital_uinq_code(self):
        return self._hospital_uinq_code

    @hospital_uinq_code.setter
    def hospital_uinq_code(self, value):
        self._hospital_uinq_code = value
    @property
    def muti_isv(self):
        return self._muti_isv

    @muti_isv.setter
    def muti_isv(self, value):
        self._muti_isv = value
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
    def proficiency(self):
        return self._proficiency

    @proficiency.setter
    def proficiency(self, value):
        self._proficiency = value
    @property
    def res_prop(self):
        return self._res_prop

    @res_prop.setter
    def res_prop(self, value):
        self._res_prop = value
    @property
    def schedule_desc(self):
        return self._schedule_desc

    @schedule_desc.setter
    def schedule_desc(self, value):
        self._schedule_desc = value
    @property
    def scm_info(self):
        return self._scm_info

    @scm_info.setter
    def scm_info(self, value):
        self._scm_info = value
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
                if isinstance(i, ReigsterServiceInfo):
                    self._service_info_list.append(i)
                else:
                    self._service_info_list.append(ReigsterServiceInfo.from_alipay_dict(i))
    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        self._title = value
    @property
    def total_count(self):
        return self._total_count

    @total_count.setter
    def total_count(self, value):
        self._total_count = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceMedicalRegisterSelectablescheduleQueryResponse, self).parse_response_content(response_content)
        if 'afu_download_match_crowd' in response:
            self.afu_download_match_crowd = response['afu_download_match_crowd']
        if 'department_name' in response:
            self.department_name = response['department_name']
        if 'detail_url' in response:
            self.detail_url = response['detail_url']
        if 'doctor_desc' in response:
            self.doctor_desc = response['doctor_desc']
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
        if 'flow_to_aq_model' in response:
            self.flow_to_aq_model = response['flow_to_aq_model']
        if 'has_available_source' in response:
            self.has_available_source = response['has_available_source']
        if 'has_more' in response:
            self.has_more = response['has_more']
        if 'hospital_dep_feature_tags' in response:
            self.hospital_dep_feature_tags = response['hospital_dep_feature_tags']
        if 'hospital_level' in response:
            self.hospital_level = response['hospital_level']
        if 'hospital_name' in response:
            self.hospital_name = response['hospital_name']
        if 'hospital_register_info_list' in response:
            self.hospital_register_info_list = response['hospital_register_info_list']
        if 'hospital_type' in response:
            self.hospital_type = response['hospital_type']
        if 'hospital_uinq_code' in response:
            self.hospital_uinq_code = response['hospital_uinq_code']
        if 'muti_isv' in response:
            self.muti_isv = response['muti_isv']
        if 'page_key' in response:
            self.page_key = response['page_key']
        if 'platform_code' in response:
            self.platform_code = response['platform_code']
        if 'proficiency' in response:
            self.proficiency = response['proficiency']
        if 'res_prop' in response:
            self.res_prop = response['res_prop']
        if 'schedule_desc' in response:
            self.schedule_desc = response['schedule_desc']
        if 'scm_info' in response:
            self.scm_info = response['scm_info']
        if 'second_page_key' in response:
            self.second_page_key = response['second_page_key']
        if 'service_info_list' in response:
            self.service_info_list = response['service_info_list']
        if 'title' in response:
            self.title = response['title']
        if 'total_count' in response:
            self.total_count = response['total_count']
