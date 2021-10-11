#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AnttechOceanbasePassinfoLogininfoQueryResponse(AlipayResponse):

    def __init__(self):
        super(AnttechOceanbasePassinfoLogininfoQueryResponse, self).__init__()
        self._entity_id = None
        self._passport_id = None
        self._role_type = None

    @property
    def entity_id(self):
        return self._entity_id

    @entity_id.setter
    def entity_id(self, value):
        self._entity_id = value
    @property
    def passport_id(self):
        return self._passport_id

    @passport_id.setter
    def passport_id(self, value):
        self._passport_id = value
    @property
    def role_type(self):
        return self._role_type

    @role_type.setter
    def role_type(self, value):
        self._role_type = value

    def parse_response_content(self, response_content):
        response = super(AnttechOceanbasePassinfoLogininfoQueryResponse, self).parse_response_content(response_content)
        if 'entity_id' in response:
            self.entity_id = response['entity_id']
        if 'passport_id' in response:
            self.passport_id = response['passport_id']
        if 'role_type' in response:
            self.role_type = response['role_type']
