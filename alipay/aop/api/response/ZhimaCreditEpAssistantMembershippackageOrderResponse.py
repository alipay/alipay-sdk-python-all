#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.AssistantLicenseInfo import AssistantLicenseInfo


class ZhimaCreditEpAssistantMembershippackageOrderResponse(AlipayResponse):

    def __init__(self):
        super(ZhimaCreditEpAssistantMembershippackageOrderResponse, self).__init__()
        self._begin_time = None
        self._end_time = None
        self._license_detail_list = None
        self._package_id = None

    @property
    def begin_time(self):
        return self._begin_time

    @begin_time.setter
    def begin_time(self, value):
        self._begin_time = value
    @property
    def end_time(self):
        return self._end_time

    @end_time.setter
    def end_time(self, value):
        self._end_time = value
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
        response = super(ZhimaCreditEpAssistantMembershippackageOrderResponse, self).parse_response_content(response_content)
        if 'begin_time' in response:
            self.begin_time = response['begin_time']
        if 'end_time' in response:
            self.end_time = response['end_time']
        if 'license_detail_list' in response:
            self.license_detail_list = response['license_detail_list']
        if 'package_id' in response:
            self.package_id = response['package_id']
