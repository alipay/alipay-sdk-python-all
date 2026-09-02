#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.SubscriptionReimbursementVO import SubscriptionReimbursementVO


class AntLinkeCheckreimburseQueryResponse(AlipayResponse):

    def __init__(self):
        super(AntLinkeCheckreimburseQueryResponse, self).__init__()
        self._subscription_reimbursement_list = None

    @property
    def subscription_reimbursement_list(self):
        return self._subscription_reimbursement_list

    @subscription_reimbursement_list.setter
    def subscription_reimbursement_list(self, value):
        if isinstance(value, list):
            self._subscription_reimbursement_list = list()
            for i in value:
                if isinstance(i, SubscriptionReimbursementVO):
                    self._subscription_reimbursement_list.append(i)
                else:
                    self._subscription_reimbursement_list.append(SubscriptionReimbursementVO.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AntLinkeCheckreimburseQueryResponse, self).parse_response_content(response_content)
        if 'subscription_reimbursement_list' in response:
            self.subscription_reimbursement_list = response['subscription_reimbursement_list']
