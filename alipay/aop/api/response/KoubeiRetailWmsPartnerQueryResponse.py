#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.PartnerVO import PartnerVO


class KoubeiRetailWmsPartnerQueryResponse(AlipayResponse):

    def __init__(self):
        super(KoubeiRetailWmsPartnerQueryResponse, self).__init__()
        self._partners = None
        self._total_count = None

    @property
    def partners(self):
        return self._partners

    @partners.setter
    def partners(self, value):
        if isinstance(value, list):
            self._partners = list()
            for i in value:
                if isinstance(i, PartnerVO):
                    self._partners.append(i)
                else:
                    self._partners.append(PartnerVO.from_alipay_dict(i))
    @property
    def total_count(self):
        return self._total_count

    @total_count.setter
    def total_count(self, value):
        self._total_count = value

    def parse_response_content(self, response_content):
        response = super(KoubeiRetailWmsPartnerQueryResponse, self).parse_response_content(response_content)
        if 'partners' in response:
            self.partners = response['partners']
        if 'total_count' in response:
            self.total_count = response['total_count']
