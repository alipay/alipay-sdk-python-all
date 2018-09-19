#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class ZhimaCustomerCertificationQueryResponse(AlipayResponse):

    def __init__(self):
        super(ZhimaCustomerCertificationQueryResponse, self).__init__()
        self._attribute_info = None
        self._channel_statuses = None
        self._failed_reason = None
        self._identity_info = None
        self._passed = None

    @property
    def attribute_info(self):
        return self._attribute_info

    @attribute_info.setter
    def attribute_info(self, value):
        self._attribute_info = value
    @property
    def channel_statuses(self):
        return self._channel_statuses

    @channel_statuses.setter
    def channel_statuses(self, value):
        self._channel_statuses = value
    @property
    def failed_reason(self):
        return self._failed_reason

    @failed_reason.setter
    def failed_reason(self, value):
        self._failed_reason = value
    @property
    def identity_info(self):
        return self._identity_info

    @identity_info.setter
    def identity_info(self, value):
        self._identity_info = value
    @property
    def passed(self):
        return self._passed

    @passed.setter
    def passed(self, value):
        self._passed = value

    def parse_response_content(self, response_content):
        response = super(ZhimaCustomerCertificationQueryResponse, self).parse_response_content(response_content)
        if 'attribute_info' in response:
            self.attribute_info = response['attribute_info']
        if 'channel_statuses' in response:
            self.channel_statuses = response['channel_statuses']
        if 'failed_reason' in response:
            self.failed_reason = response['failed_reason']
        if 'identity_info' in response:
            self.identity_info = response['identity_info']
        if 'passed' in response:
            self.passed = response['passed']
