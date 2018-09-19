#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class KoubeiAdvertCommissionMissionCreateResponse(AlipayResponse):

    def __init__(self):
        super(KoubeiAdvertCommissionMissionCreateResponse, self).__init__()
        self._mission_id = None

    @property
    def mission_id(self):
        return self._mission_id

    @mission_id.setter
    def mission_id(self, value):
        self._mission_id = value

    def parse_response_content(self, response_content):
        response = super(KoubeiAdvertCommissionMissionCreateResponse, self).parse_response_content(response_content)
        if 'mission_id' in response:
            self.mission_id = response['mission_id']
