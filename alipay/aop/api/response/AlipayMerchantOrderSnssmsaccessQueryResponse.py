#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.AccessSceneUrl import AccessSceneUrl


class AlipayMerchantOrderSnssmsaccessQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayMerchantOrderSnssmsaccessQueryResponse, self).__init__()
        self._access_scene_url_info = None
        self._valid_access_flag = None

    @property
    def access_scene_url_info(self):
        return self._access_scene_url_info

    @access_scene_url_info.setter
    def access_scene_url_info(self, value):
        if isinstance(value, list):
            self._access_scene_url_info = list()
            for i in value:
                if isinstance(i, AccessSceneUrl):
                    self._access_scene_url_info.append(i)
                else:
                    self._access_scene_url_info.append(AccessSceneUrl.from_alipay_dict(i))
    @property
    def valid_access_flag(self):
        return self._valid_access_flag

    @valid_access_flag.setter
    def valid_access_flag(self, value):
        self._valid_access_flag = value

    def parse_response_content(self, response_content):
        response = super(AlipayMerchantOrderSnssmsaccessQueryResponse, self).parse_response_content(response_content)
        if 'access_scene_url_info' in response:
            self.access_scene_url_info = response['access_scene_url_info']
        if 'valid_access_flag' in response:
            self.valid_access_flag = response['valid_access_flag']
