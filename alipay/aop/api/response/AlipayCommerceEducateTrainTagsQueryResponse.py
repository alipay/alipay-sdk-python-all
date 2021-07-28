#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.TagInfoVO import TagInfoVO


class AlipayCommerceEducateTrainTagsQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceEducateTrainTagsQueryResponse, self).__init__()
        self._tag_infos = None

    @property
    def tag_infos(self):
        return self._tag_infos

    @tag_infos.setter
    def tag_infos(self, value):
        if isinstance(value, list):
            self._tag_infos = list()
            for i in value:
                if isinstance(i, TagInfoVO):
                    self._tag_infos.append(i)
                else:
                    self._tag_infos.append(TagInfoVO.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceEducateTrainTagsQueryResponse, self).parse_response_content(response_content)
        if 'tag_infos' in response:
            self.tag_infos = response['tag_infos']
