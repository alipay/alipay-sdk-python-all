#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.EtcTripAdvanceDetail import EtcTripAdvanceDetail


class AlipayCommerceTransportEtcAdvanceQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceTransportEtcAdvanceQueryResponse, self).__init__()
        self._trip_advance_list = None

    @property
    def trip_advance_list(self):
        return self._trip_advance_list

    @trip_advance_list.setter
    def trip_advance_list(self, value):
        if isinstance(value, list):
            self._trip_advance_list = list()
            for i in value:
                if isinstance(i, EtcTripAdvanceDetail):
                    self._trip_advance_list.append(i)
                else:
                    self._trip_advance_list.append(EtcTripAdvanceDetail.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceTransportEtcAdvanceQueryResponse, self).parse_response_content(response_content)
        if 'trip_advance_list' in response:
            self.trip_advance_list = response['trip_advance_list']
