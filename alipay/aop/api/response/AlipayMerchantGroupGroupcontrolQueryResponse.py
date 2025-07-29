#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.GroupControlVO import GroupControlVO


class AlipayMerchantGroupGroupcontrolQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayMerchantGroupGroupcontrolQueryResponse, self).__init__()
        self._group_control_detail = None

    @property
    def group_control_detail(self):
        return self._group_control_detail

    @group_control_detail.setter
    def group_control_detail(self, value):
        if isinstance(value, GroupControlVO):
            self._group_control_detail = value
        else:
            self._group_control_detail = GroupControlVO.from_alipay_dict(value)

    def parse_response_content(self, response_content):
        response = super(AlipayMerchantGroupGroupcontrolQueryResponse, self).parse_response_content(response_content)
        if 'group_control_detail' in response:
            self.group_control_detail = response['group_control_detail']
