#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class ZhimaCreditEpAssistantMembershippackageCreateResponse(AlipayResponse):

    def __init__(self):
        super(ZhimaCreditEpAssistantMembershippackageCreateResponse, self).__init__()
        self._licenses = None
        self._package_id = None

    @property
    def licenses(self):
        return self._licenses

    @licenses.setter
    def licenses(self, value):
        if isinstance(value, list):
            self._licenses = list()
            for i in value:
                self._licenses.append(i)
    @property
    def package_id(self):
        return self._package_id

    @package_id.setter
    def package_id(self, value):
        self._package_id = value

    def parse_response_content(self, response_content):
        response = super(ZhimaCreditEpAssistantMembershippackageCreateResponse, self).parse_response_content(response_content)
        if 'licenses' in response:
            self.licenses = response['licenses']
        if 'package_id' in response:
            self.package_id = response['package_id']
