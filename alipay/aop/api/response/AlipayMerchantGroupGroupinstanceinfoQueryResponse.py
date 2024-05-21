#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.GroupInstanceInfoVO import GroupInstanceInfoVO


class AlipayMerchantGroupGroupinstanceinfoQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayMerchantGroupGroupinstanceinfoQueryResponse, self).__init__()
        self._group_instance_info = None

    @property
    def group_instance_info(self):
        return self._group_instance_info

    @group_instance_info.setter
    def group_instance_info(self, value):
        if isinstance(value, GroupInstanceInfoVO):
            self._group_instance_info = value
        else:
            self._group_instance_info = GroupInstanceInfoVO.from_alipay_dict(value)

    def parse_response_content(self, response_content):
        response = super(AlipayMerchantGroupGroupinstanceinfoQueryResponse, self).parse_response_content(response_content)
        if 'group_instance_info' in response:
            self.group_instance_info = response['group_instance_info']
