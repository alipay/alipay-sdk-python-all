#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.MiniappCloudDetailInfo import MiniappCloudDetailInfo


class AlipayOpenMiniCloudDetailQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOpenMiniCloudDetailQueryResponse, self).__init__()
        self._miniapp_cloud_detail_info_list = None
        self._partner_id = None

    @property
    def miniapp_cloud_detail_info_list(self):
        return self._miniapp_cloud_detail_info_list

    @miniapp_cloud_detail_info_list.setter
    def miniapp_cloud_detail_info_list(self, value):
        if isinstance(value, list):
            self._miniapp_cloud_detail_info_list = list()
            for i in value:
                if isinstance(i, MiniappCloudDetailInfo):
                    self._miniapp_cloud_detail_info_list.append(i)
                else:
                    self._miniapp_cloud_detail_info_list.append(MiniappCloudDetailInfo.from_alipay_dict(i))
    @property
    def partner_id(self):
        return self._partner_id

    @partner_id.setter
    def partner_id(self, value):
        self._partner_id = value

    def parse_response_content(self, response_content):
        response = super(AlipayOpenMiniCloudDetailQueryResponse, self).parse_response_content(response_content)
        if 'miniapp_cloud_detail_info_list' in response:
            self.miniapp_cloud_detail_info_list = response['miniapp_cloud_detail_info_list']
        if 'partner_id' in response:
            self.partner_id = response['partner_id']
