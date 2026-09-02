#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayOpenSpSkillInfoModifyResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOpenSpSkillInfoModifyResponse, self).__init__()
        self._ability_code = None
        self._ability_version = None

    @property
    def ability_code(self):
        return self._ability_code

    @ability_code.setter
    def ability_code(self, value):
        self._ability_code = value
    @property
    def ability_version(self):
        return self._ability_version

    @ability_version.setter
    def ability_version(self, value):
        self._ability_version = value

    def parse_response_content(self, response_content):
        response = super(AlipayOpenSpSkillInfoModifyResponse, self).parse_response_content(response_content)
        if 'ability_code' in response:
            self.ability_code = response['ability_code']
        if 'ability_version' in response:
            self.ability_version = response['ability_version']
