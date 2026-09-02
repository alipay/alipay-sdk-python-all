#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayOpenSpSkillDetailQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOpenSpSkillDetailQueryResponse, self).__init__()
        self._ability_code = None
        self._ability_status = None
        self._ability_version = None
        self._skill_chinese_name = None
        self._skill_desc = None
        self._skill_download_url = None
        self._skill_english_name = None
        self._skill_logo_url = None
        self._support_account_type = None

    @property
    def ability_code(self):
        return self._ability_code

    @ability_code.setter
    def ability_code(self, value):
        self._ability_code = value
    @property
    def ability_status(self):
        return self._ability_status

    @ability_status.setter
    def ability_status(self, value):
        self._ability_status = value
    @property
    def ability_version(self):
        return self._ability_version

    @ability_version.setter
    def ability_version(self, value):
        self._ability_version = value
    @property
    def skill_chinese_name(self):
        return self._skill_chinese_name

    @skill_chinese_name.setter
    def skill_chinese_name(self, value):
        self._skill_chinese_name = value
    @property
    def skill_desc(self):
        return self._skill_desc

    @skill_desc.setter
    def skill_desc(self, value):
        self._skill_desc = value
    @property
    def skill_download_url(self):
        return self._skill_download_url

    @skill_download_url.setter
    def skill_download_url(self, value):
        self._skill_download_url = value
    @property
    def skill_english_name(self):
        return self._skill_english_name

    @skill_english_name.setter
    def skill_english_name(self, value):
        self._skill_english_name = value
    @property
    def skill_logo_url(self):
        return self._skill_logo_url

    @skill_logo_url.setter
    def skill_logo_url(self, value):
        self._skill_logo_url = value
    @property
    def support_account_type(self):
        return self._support_account_type

    @support_account_type.setter
    def support_account_type(self, value):
        if isinstance(value, list):
            self._support_account_type = list()
            for i in value:
                self._support_account_type.append(i)

    def parse_response_content(self, response_content):
        response = super(AlipayOpenSpSkillDetailQueryResponse, self).parse_response_content(response_content)
        if 'ability_code' in response:
            self.ability_code = response['ability_code']
        if 'ability_status' in response:
            self.ability_status = response['ability_status']
        if 'ability_version' in response:
            self.ability_version = response['ability_version']
        if 'skill_chinese_name' in response:
            self.skill_chinese_name = response['skill_chinese_name']
        if 'skill_desc' in response:
            self.skill_desc = response['skill_desc']
        if 'skill_download_url' in response:
            self.skill_download_url = response['skill_download_url']
        if 'skill_english_name' in response:
            self.skill_english_name = response['skill_english_name']
        if 'skill_logo_url' in response:
            self.skill_logo_url = response['skill_logo_url']
        if 'support_account_type' in response:
            self.support_account_type = response['support_account_type']
