#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCommerceLogisticsLinkGetResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceLogisticsLinkGetResponse, self).__init__()
        self._logistics_biz_scene_action = None
        self._logistics_link_encryption = None
        self._logistics_link_url = None

    @property
    def logistics_biz_scene_action(self):
        return self._logistics_biz_scene_action

    @logistics_biz_scene_action.setter
    def logistics_biz_scene_action(self, value):
        self._logistics_biz_scene_action = value
    @property
    def logistics_link_encryption(self):
        return self._logistics_link_encryption

    @logistics_link_encryption.setter
    def logistics_link_encryption(self, value):
        self._logistics_link_encryption = value
    @property
    def logistics_link_url(self):
        return self._logistics_link_url

    @logistics_link_url.setter
    def logistics_link_url(self, value):
        self._logistics_link_url = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceLogisticsLinkGetResponse, self).parse_response_content(response_content)
        if 'logistics_biz_scene_action' in response:
            self.logistics_biz_scene_action = response['logistics_biz_scene_action']
        if 'logistics_link_encryption' in response:
            self.logistics_link_encryption = response['logistics_link_encryption']
        if 'logistics_link_url' in response:
            self.logistics_link_url = response['logistics_link_url']
