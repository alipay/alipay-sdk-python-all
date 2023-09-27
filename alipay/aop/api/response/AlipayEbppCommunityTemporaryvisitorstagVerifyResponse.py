#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.CertifyPlatformInfo import CertifyPlatformInfo


class AlipayEbppCommunityTemporaryvisitorstagVerifyResponse(AlipayResponse):

    def __init__(self):
        super(AlipayEbppCommunityTemporaryvisitorstagVerifyResponse, self).__init__()
        self._certify_platform_info_list = None
        self._result = None

    @property
    def certify_platform_info_list(self):
        return self._certify_platform_info_list

    @certify_platform_info_list.setter
    def certify_platform_info_list(self, value):
        if isinstance(value, list):
            self._certify_platform_info_list = list()
            for i in value:
                if isinstance(i, CertifyPlatformInfo):
                    self._certify_platform_info_list.append(i)
                else:
                    self._certify_platform_info_list.append(CertifyPlatformInfo.from_alipay_dict(i))
    @property
    def result(self):
        return self._result

    @result.setter
    def result(self, value):
        self._result = value

    def parse_response_content(self, response_content):
        response = super(AlipayEbppCommunityTemporaryvisitorstagVerifyResponse, self).parse_response_content(response_content)
        if 'certify_platform_info_list' in response:
            self.certify_platform_info_list = response['certify_platform_info_list']
        if 'result' in response:
            self.result = response['result']
