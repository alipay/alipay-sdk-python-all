#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.IoTDeliveryPlan import IoTDeliveryPlan


class AlipayMarketingActivityIotdeliveryQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayMarketingActivityIotdeliveryQueryResponse, self).__init__()
        self._plan_detail = None

    @property
    def plan_detail(self):
        return self._plan_detail

    @plan_detail.setter
    def plan_detail(self, value):
        if isinstance(value, IoTDeliveryPlan):
            self._plan_detail = value
        else:
            self._plan_detail = IoTDeliveryPlan.from_alipay_dict(value)

    def parse_response_content(self, response_content):
        response = super(AlipayMarketingActivityIotdeliveryQueryResponse, self).parse_response_content(response_content)
        if 'plan_detail' in response:
            self.plan_detail = response['plan_detail']
