#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.BenefitActionResponseComponents import BenefitActionResponseComponents


class AlipayCommerceTransportVehownerbaseBenefitTakeResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceTransportVehownerbaseBenefitTakeResponse, self).__init__()
        self._components = None
        self._current_date = None
        self._operation_param_identity = None

    @property
    def components(self):
        return self._components

    @components.setter
    def components(self, value):
        if isinstance(value, BenefitActionResponseComponents):
            self._components = value
        else:
            self._components = BenefitActionResponseComponents.from_alipay_dict(value)
    @property
    def current_date(self):
        return self._current_date

    @current_date.setter
    def current_date(self, value):
        self._current_date = value
    @property
    def operation_param_identity(self):
        return self._operation_param_identity

    @operation_param_identity.setter
    def operation_param_identity(self, value):
        self._operation_param_identity = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceTransportVehownerbaseBenefitTakeResponse, self).parse_response_content(response_content)
        if 'components' in response:
            self.components = response['components']
        if 'current_date' in response:
            self.current_date = response['current_date']
        if 'operation_param_identity' in response:
            self.operation_param_identity = response['operation_param_identity']
