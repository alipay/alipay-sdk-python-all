#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayInsScenePetprofilePlatformprofileCreateResponse(AlipayResponse):

    def __init__(self):
        super(AlipayInsScenePetprofilePlatformprofileCreateResponse, self).__init__()
        self._pet_id = None

    @property
    def pet_id(self):
        return self._pet_id

    @pet_id.setter
    def pet_id(self, value):
        self._pet_id = value

    def parse_response_content(self, response_content):
        response = super(AlipayInsScenePetprofilePlatformprofileCreateResponse, self).parse_response_content(response_content)
        if 'pet_id' in response:
            self.pet_id = response['pet_id']
