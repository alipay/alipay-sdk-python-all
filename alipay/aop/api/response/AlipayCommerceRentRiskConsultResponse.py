#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.RentRiskInfoVO import RentRiskInfoVO


class AlipayCommerceRentRiskConsultResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceRentRiskConsultResponse, self).__init__()
        self._risk_infos = None

    @property
    def risk_infos(self):
        return self._risk_infos

    @risk_infos.setter
    def risk_infos(self, value):
        if isinstance(value, list):
            self._risk_infos = list()
            for i in value:
                if isinstance(i, RentRiskInfoVO):
                    self._risk_infos.append(i)
                else:
                    self._risk_infos.append(RentRiskInfoVO.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceRentRiskConsultResponse, self).parse_response_content(response_content)
        if 'risk_infos' in response:
            self.risk_infos = response['risk_infos']
