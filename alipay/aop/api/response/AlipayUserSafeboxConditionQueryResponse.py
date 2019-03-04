#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayUserSafeboxConditionQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayUserSafeboxConditionQueryResponse, self).__init__()
        self._emergency_offline = None
        self._has_agreement = None

    @property
    def emergency_offline(self):
        return self._emergency_offline

    @emergency_offline.setter
    def emergency_offline(self, value):
        self._emergency_offline = value
    @property
    def has_agreement(self):
        return self._has_agreement

    @has_agreement.setter
    def has_agreement(self, value):
        self._has_agreement = value

    def parse_response_content(self, response_content):
        response = super(AlipayUserSafeboxConditionQueryResponse, self).parse_response_content(response_content)
        if 'emergency_offline' in response:
            self.emergency_offline = response['emergency_offline']
        if 'has_agreement' in response:
            self.has_agreement = response['has_agreement']
