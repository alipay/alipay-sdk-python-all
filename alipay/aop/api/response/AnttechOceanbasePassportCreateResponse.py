#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AnttechOceanbasePassportCreateResponse(AlipayResponse):

    def __init__(self):
        super(AnttechOceanbasePassportCreateResponse, self).__init__()
        self._entity_role_id = None
        self._passport_id = None

    @property
    def entity_role_id(self):
        return self._entity_role_id

    @entity_role_id.setter
    def entity_role_id(self, value):
        self._entity_role_id = value
    @property
    def passport_id(self):
        return self._passport_id

    @passport_id.setter
    def passport_id(self, value):
        self._passport_id = value

    def parse_response_content(self, response_content):
        response = super(AnttechOceanbasePassportCreateResponse, self).parse_response_content(response_content)
        if 'entity_role_id' in response:
            self.entity_role_id = response['entity_role_id']
        if 'passport_id' in response:
            self.passport_id = response['passport_id']
