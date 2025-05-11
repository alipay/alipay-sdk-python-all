#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.HospitalCampusRegisterScheduleInfoDTO import HospitalCampusRegisterScheduleInfoDTO


class AlipayCommerceMedicalLargermodelDepartmentscheduleQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceMedicalLargermodelDepartmentscheduleQueryResponse, self).__init__()
        self._chat_id = None
        self._department_name = None
        self._has_more = None
        self._hospital_name = None
        self._hospital_uinq_code = None
        self._page_key = None
        self._register_info_list = None
        self._schedule_page_url = None
        self._second_page_key = None
        self._url = None

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
    def has_more(self):
        return self._has_more

    @has_more.setter
    def has_more(self, value):
        self._has_more = value
    @property
    def hospital_name(self):
        return self._hospital_name

    @hospital_name.setter
    def hospital_name(self, value):
        self._hospital_name = value
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
    def register_info_list(self):
        return self._register_info_list

    @register_info_list.setter
    def register_info_list(self, value):
        if isinstance(value, list):
            self._register_info_list = list()
            for i in value:
                if isinstance(i, HospitalCampusRegisterScheduleInfoDTO):
                    self._register_info_list.append(i)
                else:
                    self._register_info_list.append(HospitalCampusRegisterScheduleInfoDTO.from_alipay_dict(i))
    @property
    def schedule_page_url(self):
        return self._schedule_page_url

    @schedule_page_url.setter
    def schedule_page_url(self, value):
        self._schedule_page_url = value
    @property
    def second_page_key(self):
        return self._second_page_key

    @second_page_key.setter
    def second_page_key(self, value):
        self._second_page_key = value
    @property
    def url(self):
        return self._url

    @url.setter
    def url(self, value):
        self._url = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceMedicalLargermodelDepartmentscheduleQueryResponse, self).parse_response_content(response_content)
        if 'chat_id' in response:
            self.chat_id = response['chat_id']
        if 'department_name' in response:
            self.department_name = response['department_name']
        if 'has_more' in response:
            self.has_more = response['has_more']
        if 'hospital_name' in response:
            self.hospital_name = response['hospital_name']
        if 'hospital_uinq_code' in response:
            self.hospital_uinq_code = response['hospital_uinq_code']
        if 'page_key' in response:
            self.page_key = response['page_key']
        if 'register_info_list' in response:
            self.register_info_list = response['register_info_list']
        if 'schedule_page_url' in response:
            self.schedule_page_url = response['schedule_page_url']
        if 'second_page_key' in response:
            self.second_page_key = response['second_page_key']
        if 'url' in response:
            self.url = response['url']
