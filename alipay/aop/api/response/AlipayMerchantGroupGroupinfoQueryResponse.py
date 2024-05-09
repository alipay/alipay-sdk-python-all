#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.GroupDetailVO import GroupDetailVO


class AlipayMerchantGroupGroupinfoQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayMerchantGroupGroupinfoQueryResponse, self).__init__()
        self._group_detail = None

    @property
    def group_detail(self):
        return self._group_detail

    @group_detail.setter
    def group_detail(self, value):
        if isinstance(value, GroupDetailVO):
            self._group_detail = value
        else:
            self._group_detail = GroupDetailVO.from_alipay_dict(value)

    def parse_response_content(self, response_content):
        response = super(AlipayMerchantGroupGroupinfoQueryResponse, self).parse_response_content(response_content)
        if 'group_detail' in response:
            self.group_detail = response['group_detail']
