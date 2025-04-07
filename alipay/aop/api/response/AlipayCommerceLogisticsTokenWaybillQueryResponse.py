#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.WaybillMatchInfoObj import WaybillMatchInfoObj


class AlipayCommerceLogisticsTokenWaybillQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceLogisticsTokenWaybillQueryResponse, self).__init__()
        self._match_waybill_list = None

    @property
    def match_waybill_list(self):
        return self._match_waybill_list

    @match_waybill_list.setter
    def match_waybill_list(self, value):
        if isinstance(value, list):
            self._match_waybill_list = list()
            for i in value:
                if isinstance(i, WaybillMatchInfoObj):
                    self._match_waybill_list.append(i)
                else:
                    self._match_waybill_list.append(WaybillMatchInfoObj.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceLogisticsTokenWaybillQueryResponse, self).parse_response_content(response_content)
        if 'match_waybill_list' in response:
            self.match_waybill_list = response['match_waybill_list']
