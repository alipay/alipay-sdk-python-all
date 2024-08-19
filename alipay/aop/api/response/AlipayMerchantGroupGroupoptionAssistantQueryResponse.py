#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.GroupOptionVO import GroupOptionVO


class AlipayMerchantGroupGroupoptionAssistantQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayMerchantGroupGroupoptionAssistantQueryResponse, self).__init__()
        self._group_options = None

    @property
    def group_options(self):
        return self._group_options

    @group_options.setter
    def group_options(self, value):
        if isinstance(value, list):
            self._group_options = list()
            for i in value:
                if isinstance(i, GroupOptionVO):
                    self._group_options.append(i)
                else:
                    self._group_options.append(GroupOptionVO.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AlipayMerchantGroupGroupoptionAssistantQueryResponse, self).parse_response_content(response_content)
        if 'group_options' in response:
            self.group_options = response['group_options']
