#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.AssistantLicenseInfo import AssistantLicenseInfo


class ZhimaCreditEpAssistantMembershippackageAppendResponse(AlipayResponse):

    def __init__(self):
        super(ZhimaCreditEpAssistantMembershippackageAppendResponse, self).__init__()
        self._license_detail_list = None
        self._package_id = None

    @property
    def license_detail_list(self):
        return self._license_detail_list

    @license_detail_list.setter
    def license_detail_list(self, value):
        if isinstance(value, list):
            self._license_detail_list = list()
            for i in value:
                if isinstance(i, AssistantLicenseInfo):
                    self._license_detail_list.append(i)
                else:
                    self._license_detail_list.append(AssistantLicenseInfo.from_alipay_dict(i))
    @property
    def package_id(self):
        return self._package_id

    @package_id.setter
    def package_id(self, value):
        self._package_id = value

    def parse_response_content(self, response_content):
        response = super(ZhimaCreditEpAssistantMembershippackageAppendResponse, self).parse_response_content(response_content)
        if 'license_detail_list' in response:
            self.license_detail_list = response['license_detail_list']
        if 'package_id' in response:
            self.package_id = response['package_id']
