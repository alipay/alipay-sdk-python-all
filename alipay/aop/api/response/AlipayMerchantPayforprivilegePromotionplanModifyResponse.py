#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.PayForPrivilegePromotionPlanInfo import PayForPrivilegePromotionPlanInfo


class AlipayMerchantPayforprivilegePromotionplanModifyResponse(AlipayResponse):

    def __init__(self):
        super(AlipayMerchantPayforprivilegePromotionplanModifyResponse, self).__init__()
        self._promotion_plan = None

    @property
    def promotion_plan(self):
        return self._promotion_plan

    @promotion_plan.setter
    def promotion_plan(self, value):
        if isinstance(value, PayForPrivilegePromotionPlanInfo):
            self._promotion_plan = value
        else:
            self._promotion_plan = PayForPrivilegePromotionPlanInfo.from_alipay_dict(value)

    def parse_response_content(self, response_content):
        response = super(AlipayMerchantPayforprivilegePromotionplanModifyResponse, self).parse_response_content(response_content)
        if 'promotion_plan' in response:
            self.promotion_plan = response['promotion_plan']
