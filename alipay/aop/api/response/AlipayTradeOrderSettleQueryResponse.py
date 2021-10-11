#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.RoyaltyDetail import RoyaltyDetail


class AlipayTradeOrderSettleQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayTradeOrderSettleQueryResponse, self).__init__()
        self._operation_dt = None
        self._out_request_no = None
        self._royalty_detail_list = None

    @property
    def operation_dt(self):
        return self._operation_dt

    @operation_dt.setter
    def operation_dt(self, value):
        self._operation_dt = value
    @property
    def out_request_no(self):
        return self._out_request_no

    @out_request_no.setter
    def out_request_no(self, value):
        self._out_request_no = value
    @property
    def royalty_detail_list(self):
        return self._royalty_detail_list

    @royalty_detail_list.setter
    def royalty_detail_list(self, value):
        if isinstance(value, list):
            self._royalty_detail_list = list()
            for i in value:
                if isinstance(i, RoyaltyDetail):
                    self._royalty_detail_list.append(i)
                else:
                    self._royalty_detail_list.append(RoyaltyDetail.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AlipayTradeOrderSettleQueryResponse, self).parse_response_content(response_content)
        if 'operation_dt' in response:
            self.operation_dt = response['operation_dt']
        if 'out_request_no' in response:
            self.out_request_no = response['out_request_no']
        if 'royalty_detail_list' in response:
            self.royalty_detail_list = response['royalty_detail_list']
