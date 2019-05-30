#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.MiniAppClientVersionInfo import MiniAppClientVersionInfo
from alipay.aop.api.domain.MiniAppClientVersionInfo import MiniAppClientVersionInfo


class AlipayOpenMiniInnerclientinfoDefaultversionQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOpenMiniInnerclientinfoDefaultversionQueryResponse, self).__init__()
        self._android_client_version_info = None
        self._ios_client_version_info = None

    @property
    def android_client_version_info(self):
        return self._android_client_version_info

    @android_client_version_info.setter
    def android_client_version_info(self, value):
        if isinstance(value, MiniAppClientVersionInfo):
            self._android_client_version_info = value
        else:
            self._android_client_version_info = MiniAppClientVersionInfo.from_alipay_dict(value)
    @property
    def ios_client_version_info(self):
        return self._ios_client_version_info

    @ios_client_version_info.setter
    def ios_client_version_info(self, value):
        if isinstance(value, MiniAppClientVersionInfo):
            self._ios_client_version_info = value
        else:
            self._ios_client_version_info = MiniAppClientVersionInfo.from_alipay_dict(value)

    def parse_response_content(self, response_content):
        response = super(AlipayOpenMiniInnerclientinfoDefaultversionQueryResponse, self).parse_response_content(response_content)
        if 'android_client_version_info' in response:
            self.android_client_version_info = response['android_client_version_info']
        if 'ios_client_version_info' in response:
            self.ios_client_version_info = response['ios_client_version_info']
