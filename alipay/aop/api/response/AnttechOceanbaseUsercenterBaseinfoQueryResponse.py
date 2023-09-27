#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AnttechOceanbaseUsercenterBaseinfoQueryResponse(AlipayResponse):

    def __init__(self):
        super(AnttechOceanbaseUsercenterBaseinfoQueryResponse, self).__init__()
        self._entity_role_type_list = None
        self._passport_id = None

    @property
    def entity_role_type_list(self):
        return self._entity_role_type_list

    @entity_role_type_list.setter
    def entity_role_type_list(self, value):
        if isinstance(value, list):
            self._entity_role_type_list = list()
            for i in value:
                self._entity_role_type_list.append(i)
    @property
    def passport_id(self):
        return self._passport_id

    @passport_id.setter
    def passport_id(self, value):
        self._passport_id = value

    def parse_response_content(self, response_content):
        response = super(AnttechOceanbaseUsercenterBaseinfoQueryResponse, self).parse_response_content(response_content)
        if 'entity_role_type_list' in response:
            self.entity_role_type_list = response['entity_role_type_list']
        if 'passport_id' in response:
            self.passport_id = response['passport_id']
