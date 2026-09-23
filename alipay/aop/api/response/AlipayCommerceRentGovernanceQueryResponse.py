#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.RentGovernanceInfoVO import RentGovernanceInfoVO


class AlipayCommerceRentGovernanceQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceRentGovernanceQueryResponse, self).__init__()
        self._governance_infos = None

    @property
    def governance_infos(self):
        return self._governance_infos

    @governance_infos.setter
    def governance_infos(self, value):
        if isinstance(value, list):
            self._governance_infos = list()
            for i in value:
                if isinstance(i, RentGovernanceInfoVO):
                    self._governance_infos.append(i)
                else:
                    self._governance_infos.append(RentGovernanceInfoVO.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceRentGovernanceQueryResponse, self).parse_response_content(response_content)
        if 'governance_infos' in response:
            self.governance_infos = response['governance_infos']
