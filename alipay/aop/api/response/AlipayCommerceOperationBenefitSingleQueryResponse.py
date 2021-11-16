#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.ActivityBenefit import ActivityBenefit
from alipay.aop.api.domain.PrivilegeBenefit import PrivilegeBenefit


class AlipayCommerceOperationBenefitSingleQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceOperationBenefitSingleQueryResponse, self).__init__()
        self._activity_benefit = None
        self._privilege_benefit = None

    @property
    def activity_benefit(self):
        return self._activity_benefit

    @activity_benefit.setter
    def activity_benefit(self, value):
        if isinstance(value, ActivityBenefit):
            self._activity_benefit = value
        else:
            self._activity_benefit = ActivityBenefit.from_alipay_dict(value)
    @property
    def privilege_benefit(self):
        return self._privilege_benefit

    @privilege_benefit.setter
    def privilege_benefit(self, value):
        if isinstance(value, PrivilegeBenefit):
            self._privilege_benefit = value
        else:
            self._privilege_benefit = PrivilegeBenefit.from_alipay_dict(value)

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceOperationBenefitSingleQueryResponse, self).parse_response_content(response_content)
        if 'activity_benefit' in response:
            self.activity_benefit = response['activity_benefit']
        if 'privilege_benefit' in response:
            self.privilege_benefit = response['privilege_benefit']
