#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.SubCloudUserInfo import SubCloudUserInfo


class KoubeiMerchantKbcloudSubuserinfoQueryResponse(AlipayResponse):

    def __init__(self):
        super(KoubeiMerchantKbcloudSubuserinfoQueryResponse, self).__init__()
        self._sub_cloud_user_list = None

    @property
    def sub_cloud_user_list(self):
        return self._sub_cloud_user_list

    @sub_cloud_user_list.setter
    def sub_cloud_user_list(self, value):
        if isinstance(value, list):
            self._sub_cloud_user_list = list()
            for i in value:
                if isinstance(i, SubCloudUserInfo):
                    self._sub_cloud_user_list.append(i)
                else:
                    self._sub_cloud_user_list.append(SubCloudUserInfo.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(KoubeiMerchantKbcloudSubuserinfoQueryResponse, self).parse_response_content(response_content)
        if 'sub_cloud_user_list' in response:
            self.sub_cloud_user_list = response['sub_cloud_user_list']
