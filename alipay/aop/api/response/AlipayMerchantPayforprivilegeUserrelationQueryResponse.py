#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.PayForPrivilegeUserRelation import PayForPrivilegeUserRelation


class AlipayMerchantPayforprivilegeUserrelationQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayMerchantPayforprivilegeUserrelationQueryResponse, self).__init__()
        self._member_info = None

    @property
    def member_info(self):
        return self._member_info

    @member_info.setter
    def member_info(self, value):
        if isinstance(value, PayForPrivilegeUserRelation):
            self._member_info = value
        else:
            self._member_info = PayForPrivilegeUserRelation.from_alipay_dict(value)

    def parse_response_content(self, response_content):
        response = super(AlipayMerchantPayforprivilegeUserrelationQueryResponse, self).parse_response_content(response_content)
        if 'member_info' in response:
            self.member_info = response['member_info']
