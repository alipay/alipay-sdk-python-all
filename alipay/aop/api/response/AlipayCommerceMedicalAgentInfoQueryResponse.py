#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.ServiceGroup import ServiceGroup


class AlipayCommerceMedicalAgentInfoQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceMedicalAgentInfoQueryResponse, self).__init__()
        self._agent_describe = None
        self._agent_id = None
        self._agent_logo = None
        self._agent_name = None
        self._agent_status = None
        self._agent_type = None
        self._city_code = None
        self._digital_human_pic = None
        self._digital_human_voice_id = None
        self._district_code = None
        self._org_id = None
        self._org_name = None
        self._parent_agent_id = None
        self._province_code = None
        self._recommend_question_list = None
        self._service_group_list = None
        self._standard_org_id = None
        self._uscc = None
        self._welcome_desc = None

    @property
    def agent_describe(self):
        return self._agent_describe

    @agent_describe.setter
    def agent_describe(self, value):
        self._agent_describe = value
    @property
    def agent_id(self):
        return self._agent_id

    @agent_id.setter
    def agent_id(self, value):
        self._agent_id = value
    @property
    def agent_logo(self):
        return self._agent_logo

    @agent_logo.setter
    def agent_logo(self, value):
        self._agent_logo = value
    @property
    def agent_name(self):
        return self._agent_name

    @agent_name.setter
    def agent_name(self, value):
        self._agent_name = value
    @property
    def agent_status(self):
        return self._agent_status

    @agent_status.setter
    def agent_status(self, value):
        self._agent_status = value
    @property
    def agent_type(self):
        return self._agent_type

    @agent_type.setter
    def agent_type(self, value):
        self._agent_type = value
    @property
    def city_code(self):
        return self._city_code

    @city_code.setter
    def city_code(self, value):
        self._city_code = value
    @property
    def digital_human_pic(self):
        return self._digital_human_pic

    @digital_human_pic.setter
    def digital_human_pic(self, value):
        self._digital_human_pic = value
    @property
    def digital_human_voice_id(self):
        return self._digital_human_voice_id

    @digital_human_voice_id.setter
    def digital_human_voice_id(self, value):
        self._digital_human_voice_id = value
    @property
    def district_code(self):
        return self._district_code

    @district_code.setter
    def district_code(self, value):
        self._district_code = value
    @property
    def org_id(self):
        return self._org_id

    @org_id.setter
    def org_id(self, value):
        self._org_id = value
    @property
    def org_name(self):
        return self._org_name

    @org_name.setter
    def org_name(self, value):
        self._org_name = value
    @property
    def parent_agent_id(self):
        return self._parent_agent_id

    @parent_agent_id.setter
    def parent_agent_id(self, value):
        self._parent_agent_id = value
    @property
    def province_code(self):
        return self._province_code

    @province_code.setter
    def province_code(self, value):
        self._province_code = value
    @property
    def recommend_question_list(self):
        return self._recommend_question_list

    @recommend_question_list.setter
    def recommend_question_list(self, value):
        if isinstance(value, list):
            self._recommend_question_list = list()
            for i in value:
                self._recommend_question_list.append(i)
    @property
    def service_group_list(self):
        return self._service_group_list

    @service_group_list.setter
    def service_group_list(self, value):
        if isinstance(value, list):
            self._service_group_list = list()
            for i in value:
                if isinstance(i, ServiceGroup):
                    self._service_group_list.append(i)
                else:
                    self._service_group_list.append(ServiceGroup.from_alipay_dict(i))
    @property
    def standard_org_id(self):
        return self._standard_org_id

    @standard_org_id.setter
    def standard_org_id(self, value):
        self._standard_org_id = value
    @property
    def uscc(self):
        return self._uscc

    @uscc.setter
    def uscc(self, value):
        self._uscc = value
    @property
    def welcome_desc(self):
        return self._welcome_desc

    @welcome_desc.setter
    def welcome_desc(self, value):
        self._welcome_desc = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceMedicalAgentInfoQueryResponse, self).parse_response_content(response_content)
        if 'agent_describe' in response:
            self.agent_describe = response['agent_describe']
        if 'agent_id' in response:
            self.agent_id = response['agent_id']
        if 'agent_logo' in response:
            self.agent_logo = response['agent_logo']
        if 'agent_name' in response:
            self.agent_name = response['agent_name']
        if 'agent_status' in response:
            self.agent_status = response['agent_status']
        if 'agent_type' in response:
            self.agent_type = response['agent_type']
        if 'city_code' in response:
            self.city_code = response['city_code']
        if 'digital_human_pic' in response:
            self.digital_human_pic = response['digital_human_pic']
        if 'digital_human_voice_id' in response:
            self.digital_human_voice_id = response['digital_human_voice_id']
        if 'district_code' in response:
            self.district_code = response['district_code']
        if 'org_id' in response:
            self.org_id = response['org_id']
        if 'org_name' in response:
            self.org_name = response['org_name']
        if 'parent_agent_id' in response:
            self.parent_agent_id = response['parent_agent_id']
        if 'province_code' in response:
            self.province_code = response['province_code']
        if 'recommend_question_list' in response:
            self.recommend_question_list = response['recommend_question_list']
        if 'service_group_list' in response:
            self.service_group_list = response['service_group_list']
        if 'standard_org_id' in response:
            self.standard_org_id = response['standard_org_id']
        if 'uscc' in response:
            self.uscc = response['uscc']
        if 'welcome_desc' in response:
            self.welcome_desc = response['welcome_desc']
