#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.GroupActivityDetailVO import GroupActivityDetailVO


class AlipayMerchantGroupActivityQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayMerchantGroupActivityQueryResponse, self).__init__()
        self._activity_detail = None

    @property
    def activity_detail(self):
        return self._activity_detail

    @activity_detail.setter
    def activity_detail(self, value):
        if isinstance(value, GroupActivityDetailVO):
            self._activity_detail = value
        else:
            self._activity_detail = GroupActivityDetailVO.from_alipay_dict(value)

    def parse_response_content(self, response_content):
        response = super(AlipayMerchantGroupActivityQueryResponse, self).parse_response_content(response_content)
        if 'activity_detail' in response:
            self.activity_detail = response['activity_detail']
