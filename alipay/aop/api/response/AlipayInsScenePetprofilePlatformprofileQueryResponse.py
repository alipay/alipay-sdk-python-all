#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.PlatformPetProfile import PlatformPetProfile


class AlipayInsScenePetprofilePlatformprofileQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayInsScenePetprofilePlatformprofileQueryResponse, self).__init__()
        self._pet_profile = None

    @property
    def pet_profile(self):
        return self._pet_profile

    @pet_profile.setter
    def pet_profile(self, value):
        if isinstance(value, PlatformPetProfile):
            self._pet_profile = value
        else:
            self._pet_profile = PlatformPetProfile.from_alipay_dict(value)

    def parse_response_content(self, response_content):
        response = super(AlipayInsScenePetprofilePlatformprofileQueryResponse, self).parse_response_content(response_content)
        if 'pet_profile' in response:
            self.pet_profile = response['pet_profile']
