#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.TagDistDTO import TagDistDTO


class DatadigitalFincloudFinsaasTagDistQueryResponse(AlipayResponse):

    def __init__(self):
        super(DatadigitalFincloudFinsaasTagDistQueryResponse, self).__init__()
        self._tag_dist_dto_list = None

    @property
    def tag_dist_dto_list(self):
        return self._tag_dist_dto_list

    @tag_dist_dto_list.setter
    def tag_dist_dto_list(self, value):
        if isinstance(value, list):
            self._tag_dist_dto_list = list()
            for i in value:
                if isinstance(i, TagDistDTO):
                    self._tag_dist_dto_list.append(i)
                else:
                    self._tag_dist_dto_list.append(TagDistDTO.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(DatadigitalFincloudFinsaasTagDistQueryResponse, self).parse_response_content(response_content)
        if 'tag_dist_dto_list' in response:
            self.tag_dist_dto_list = response['tag_dist_dto_list']
