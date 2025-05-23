#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCommerceHousingNewhouseProjectSaveResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceHousingNewhouseProjectSaveResponse, self).__init__()
        self._estate_project_id = None

    @property
    def estate_project_id(self):
        return self._estate_project_id

    @estate_project_id.setter
    def estate_project_id(self, value):
        self._estate_project_id = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceHousingNewhouseProjectSaveResponse, self).parse_response_content(response_content)
        if 'estate_project_id' in response:
            self.estate_project_id = response['estate_project_id']
