#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.OwnedSystemPrivacyField import OwnedSystemPrivacyField


class AlipayOpenMiniPrivacySystemfieldQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOpenMiniPrivacySystemfieldQueryResponse, self).__init__()
        self._system_privacy_fields = None

    @property
    def system_privacy_fields(self):
        return self._system_privacy_fields

    @system_privacy_fields.setter
    def system_privacy_fields(self, value):
        if isinstance(value, list):
            self._system_privacy_fields = list()
            for i in value:
                if isinstance(i, OwnedSystemPrivacyField):
                    self._system_privacy_fields.append(i)
                else:
                    self._system_privacy_fields.append(OwnedSystemPrivacyField.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AlipayOpenMiniPrivacySystemfieldQueryResponse, self).parse_response_content(response_content)
        if 'system_privacy_fields' in response:
            self.system_privacy_fields = response['system_privacy_fields']
