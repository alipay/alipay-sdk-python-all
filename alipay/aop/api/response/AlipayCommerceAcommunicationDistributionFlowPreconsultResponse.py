#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCommerceAcommunicationDistributionFlowPreconsultResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceAcommunicationDistributionFlowPreconsultResponse, self).__init__()
        self._mobile_mapping_multi_user = None

    @property
    def mobile_mapping_multi_user(self):
        return self._mobile_mapping_multi_user

    @mobile_mapping_multi_user.setter
    def mobile_mapping_multi_user(self, value):
        self._mobile_mapping_multi_user = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceAcommunicationDistributionFlowPreconsultResponse, self).parse_response_content(response_content)
        if 'mobile_mapping_multi_user' in response:
            self.mobile_mapping_multi_user = response['mobile_mapping_multi_user']
