#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.BenefitRecordQueryResponseComponents import BenefitRecordQueryResponseComponents


class AlipayCommerceTransportVehownerbaseBenefitrecordQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceTransportVehownerbaseBenefitrecordQueryResponse, self).__init__()
        self._components = None
        self._current_date = None
        self._operation_param_identify = None

    @property
    def components(self):
        return self._components

    @components.setter
    def components(self, value):
        if isinstance(value, BenefitRecordQueryResponseComponents):
            self._components = value
        else:
            self._components = BenefitRecordQueryResponseComponents.from_alipay_dict(value)
    @property
    def current_date(self):
        return self._current_date

    @current_date.setter
    def current_date(self, value):
        self._current_date = value
    @property
    def operation_param_identify(self):
        return self._operation_param_identify

    @operation_param_identify.setter
    def operation_param_identify(self, value):
        self._operation_param_identify = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceTransportVehownerbaseBenefitrecordQueryResponse, self).parse_response_content(response_content)
        if 'components' in response:
            self.components = response['components']
        if 'current_date' in response:
            self.current_date = response['current_date']
        if 'operation_param_identify' in response:
            self.operation_param_identify = response['operation_param_identify']
