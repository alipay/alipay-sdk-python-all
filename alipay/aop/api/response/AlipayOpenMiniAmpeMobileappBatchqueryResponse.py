#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.MobileAppInfo import MobileAppInfo


class AlipayOpenMiniAmpeMobileappBatchqueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOpenMiniAmpeMobileappBatchqueryResponse, self).__init__()
        self._mobile_app_info_list = None

    @property
    def mobile_app_info_list(self):
        return self._mobile_app_info_list

    @mobile_app_info_list.setter
    def mobile_app_info_list(self, value):
        if isinstance(value, list):
            self._mobile_app_info_list = list()
            for i in value:
                if isinstance(i, MobileAppInfo):
                    self._mobile_app_info_list.append(i)
                else:
                    self._mobile_app_info_list.append(MobileAppInfo.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AlipayOpenMiniAmpeMobileappBatchqueryResponse, self).parse_response_content(response_content)
        if 'mobile_app_info_list' in response:
            self.mobile_app_info_list = response['mobile_app_info_list']
