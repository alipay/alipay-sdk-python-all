#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.TagUrlInfo import TagUrlInfo


class AlipayCommerceIotManufacturerSnQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceIotManufacturerSnQueryResponse, self).__init__()
        self._tag_url_info_list = None

    @property
    def tag_url_info_list(self):
        return self._tag_url_info_list

    @tag_url_info_list.setter
    def tag_url_info_list(self, value):
        if isinstance(value, list):
            self._tag_url_info_list = list()
            for i in value:
                if isinstance(i, TagUrlInfo):
                    self._tag_url_info_list.append(i)
                else:
                    self._tag_url_info_list.append(TagUrlInfo.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceIotManufacturerSnQueryResponse, self).parse_response_content(response_content)
        if 'tag_url_info_list' in response:
            self.tag_url_info_list = response['tag_url_info_list']
