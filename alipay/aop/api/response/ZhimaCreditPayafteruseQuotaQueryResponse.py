#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.CreditMoney import CreditMoney


class ZhimaCreditPayafteruseQuotaQueryResponse(AlipayResponse):

    def __init__(self):
        super(ZhimaCreditPayafteruseQuotaQueryResponse, self).__init__()
        self._total_quota = None

    @property
    def total_quota(self):
        return self._total_quota

    @total_quota.setter
    def total_quota(self, value):
        if isinstance(value, CreditMoney):
            self._total_quota = value
        else:
            self._total_quota = CreditMoney.from_alipay_dict(value)

    def parse_response_content(self, response_content):
        response = super(ZhimaCreditPayafteruseQuotaQueryResponse, self).parse_response_content(response_content)
        if 'total_quota' in response:
            self.total_quota = response['total_quota']
