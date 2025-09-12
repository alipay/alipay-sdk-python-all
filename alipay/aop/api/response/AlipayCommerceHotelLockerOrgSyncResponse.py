#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCommerceHotelLockerOrgSyncResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceHotelLockerOrgSyncResponse, self).__init__()
        self._alipay_org_id = None

    @property
    def alipay_org_id(self):
        return self._alipay_org_id

    @alipay_org_id.setter
    def alipay_org_id(self, value):
        self._alipay_org_id = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceHotelLockerOrgSyncResponse, self).parse_response_content(response_content)
        if 'alipay_org_id' in response:
            self.alipay_org_id = response['alipay_org_id']
