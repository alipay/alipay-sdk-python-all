#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.DeviceGroupMember import DeviceGroupMember


class AlipayCommerceIotGroupMemberBatchqueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceIotGroupMemberBatchqueryResponse, self).__init__()
        self._members = None
        self._total = None

    @property
    def members(self):
        return self._members

    @members.setter
    def members(self, value):
        if isinstance(value, list):
            self._members = list()
            for i in value:
                if isinstance(i, DeviceGroupMember):
                    self._members.append(i)
                else:
                    self._members.append(DeviceGroupMember.from_alipay_dict(i))
    @property
    def total(self):
        return self._total

    @total.setter
    def total(self, value):
        self._total = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceIotGroupMemberBatchqueryResponse, self).parse_response_content(response_content)
        if 'members' in response:
            self.members = response['members']
        if 'total' in response:
            self.total = response['total']
