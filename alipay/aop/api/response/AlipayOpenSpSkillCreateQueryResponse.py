#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayOpenSpSkillCreateQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOpenSpSkillCreateQueryResponse, self).__init__()
        self._ability_code = None
        self._skill_chinese_name = None
        self._skill_english_name = None
        self._status = None

    @property
    def ability_code(self):
        return self._ability_code

    @ability_code.setter
    def ability_code(self, value):
        self._ability_code = value
    @property
    def skill_chinese_name(self):
        return self._skill_chinese_name

    @skill_chinese_name.setter
    def skill_chinese_name(self, value):
        self._skill_chinese_name = value
    @property
    def skill_english_name(self):
        return self._skill_english_name

    @skill_english_name.setter
    def skill_english_name(self, value):
        self._skill_english_name = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value

    def parse_response_content(self, response_content):
        response = super(AlipayOpenSpSkillCreateQueryResponse, self).parse_response_content(response_content)
        if 'ability_code' in response:
            self.ability_code = response['ability_code']
        if 'skill_chinese_name' in response:
            self.skill_chinese_name = response['skill_chinese_name']
        if 'skill_english_name' in response:
            self.skill_english_name = response['skill_english_name']
        if 'status' in response:
            self.status = response['status']
