#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.EtcTripInfo import EtcTripInfo


class AlipayCommerceTransportEtcenterpriseTripQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceTransportEtcenterpriseTripQueryResponse, self).__init__()
        self._biz_code = None
        self._biz_msg = None
        self._trip_list = None

    @property
    def biz_code(self):
        return self._biz_code

    @biz_code.setter
    def biz_code(self, value):
        self._biz_code = value
    @property
    def biz_msg(self):
        return self._biz_msg

    @biz_msg.setter
    def biz_msg(self, value):
        self._biz_msg = value
    @property
    def trip_list(self):
        return self._trip_list

    @trip_list.setter
    def trip_list(self, value):
        if isinstance(value, list):
            self._trip_list = list()
            for i in value:
                if isinstance(i, EtcTripInfo):
                    self._trip_list.append(i)
                else:
                    self._trip_list.append(EtcTripInfo.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceTransportEtcenterpriseTripQueryResponse, self).parse_response_content(response_content)
        if 'biz_code' in response:
            self.biz_code = response['biz_code']
        if 'biz_msg' in response:
            self.biz_msg = response['biz_msg']
        if 'trip_list' in response:
            self.trip_list = response['trip_list']
