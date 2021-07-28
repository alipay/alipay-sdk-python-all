#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.MerchantBrandListResult import MerchantBrandListResult
from alipay.aop.api.domain.MiniappBrandAuditResult import MiniappBrandAuditResult


class AlipayOpenMiniMiniappBrandQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOpenMiniMiniappBrandQueryResponse, self).__init__()
        self._merchant_brand_list_result = None
        self._miniapp_brand_audit_result = None

    @property
    def merchant_brand_list_result(self):
        return self._merchant_brand_list_result

    @merchant_brand_list_result.setter
    def merchant_brand_list_result(self, value):
        if isinstance(value, MerchantBrandListResult):
            self._merchant_brand_list_result = value
        else:
            self._merchant_brand_list_result = MerchantBrandListResult.from_alipay_dict(value)
    @property
    def miniapp_brand_audit_result(self):
        return self._miniapp_brand_audit_result

    @miniapp_brand_audit_result.setter
    def miniapp_brand_audit_result(self, value):
        if isinstance(value, MiniappBrandAuditResult):
            self._miniapp_brand_audit_result = value
        else:
            self._miniapp_brand_audit_result = MiniappBrandAuditResult.from_alipay_dict(value)

    def parse_response_content(self, response_content):
        response = super(AlipayOpenMiniMiniappBrandQueryResponse, self).parse_response_content(response_content)
        if 'merchant_brand_list_result' in response:
            self.merchant_brand_list_result = response['merchant_brand_list_result']
        if 'miniapp_brand_audit_result' in response:
            self.miniapp_brand_audit_result = response['miniapp_brand_audit_result']
