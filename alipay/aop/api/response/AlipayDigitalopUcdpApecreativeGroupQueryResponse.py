#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.CreativeGroup import CreativeGroup


class AlipayDigitalopUcdpApecreativeGroupQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayDigitalopUcdpApecreativeGroupQueryResponse, self).__init__()
        self._creative_group_list = None

    @property
    def creative_group_list(self):
        return self._creative_group_list

    @creative_group_list.setter
    def creative_group_list(self, value):
        if isinstance(value, CreativeGroup):
            self._creative_group_list = value
        else:
            self._creative_group_list = CreativeGroup.from_alipay_dict(value)

    def parse_response_content(self, response_content):
        response = super(AlipayDigitalopUcdpApecreativeGroupQueryResponse, self).parse_response_content(response_content)
        if 'creative_group_list' in response:
            self.creative_group_list = response['creative_group_list']
