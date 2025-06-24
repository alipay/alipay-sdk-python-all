#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.MerchantSceneRoleFailInfo import MerchantSceneRoleFailInfo


class AntMerchantExpandSceneOrderQueryResponse(AlipayResponse):

    def __init__(self):
        super(AntMerchantExpandSceneOrderQueryResponse, self).__init__()
        self._fail_reasons = None
        self._order_id = None
        self._order_status = None
        self._partner_id = None

    @property
    def fail_reasons(self):
        return self._fail_reasons

    @fail_reasons.setter
    def fail_reasons(self, value):
        if isinstance(value, MerchantSceneRoleFailInfo):
            self._fail_reasons = value
        else:
            self._fail_reasons = MerchantSceneRoleFailInfo.from_alipay_dict(value)
    @property
    def order_id(self):
        return self._order_id

    @order_id.setter
    def order_id(self, value):
        self._order_id = value
    @property
    def order_status(self):
        return self._order_status

    @order_status.setter
    def order_status(self, value):
        self._order_status = value
    @property
    def partner_id(self):
        return self._partner_id

    @partner_id.setter
    def partner_id(self, value):
        self._partner_id = value

    def parse_response_content(self, response_content):
        response = super(AntMerchantExpandSceneOrderQueryResponse, self).parse_response_content(response_content)
        if 'fail_reasons' in response:
            self.fail_reasons = response['fail_reasons']
        if 'order_id' in response:
            self.order_id = response['order_id']
        if 'order_status' in response:
            self.order_status = response['order_status']
        if 'partner_id' in response:
            self.partner_id = response['partner_id']
