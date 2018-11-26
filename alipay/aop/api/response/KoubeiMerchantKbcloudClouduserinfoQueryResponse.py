#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.CloudUserInfo import CloudUserInfo


class KoubeiMerchantKbcloudClouduserinfoQueryResponse(AlipayResponse):

    def __init__(self):
        super(KoubeiMerchantKbcloudClouduserinfoQueryResponse, self).__init__()
        self._cloud_user_list = None

    @property
    def cloud_user_list(self):
        return self._cloud_user_list

    @cloud_user_list.setter
    def cloud_user_list(self, value):
        if isinstance(value, list):
            self._cloud_user_list = list()
            for i in value:
                if isinstance(i, CloudUserInfo):
                    self._cloud_user_list.append(i)
                else:
                    self._cloud_user_list.append(CloudUserInfo.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(KoubeiMerchantKbcloudClouduserinfoQueryResponse, self).parse_response_content(response_content)
        if 'cloud_user_list' in response:
            self.cloud_user_list = response['cloud_user_list']
