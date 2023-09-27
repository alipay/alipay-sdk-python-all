#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.BusinessRelationShopMemberDigest import BusinessRelationShopMemberDigest


class AlipayBusinessRelationShopmemberBatchqueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayBusinessRelationShopmemberBatchqueryResponse, self).__init__()
        self._members = None

    @property
    def members(self):
        return self._members

    @members.setter
    def members(self, value):
        if isinstance(value, list):
            self._members = list()
            for i in value:
                if isinstance(i, BusinessRelationShopMemberDigest):
                    self._members.append(i)
                else:
                    self._members.append(BusinessRelationShopMemberDigest.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AlipayBusinessRelationShopmemberBatchqueryResponse, self).parse_response_content(response_content)
        if 'members' in response:
            self.members = response['members']
