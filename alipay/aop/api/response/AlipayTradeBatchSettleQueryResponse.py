#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.BatchSettleDetail import BatchSettleDetail


class AlipayTradeBatchSettleQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayTradeBatchSettleQueryResponse, self).__init__()
        self._out_request_no = None
        self._settle_detail = None
        self._settle_no = None

    @property
    def out_request_no(self):
        return self._out_request_no

    @out_request_no.setter
    def out_request_no(self, value):
        self._out_request_no = value
    @property
    def settle_detail(self):
        return self._settle_detail

    @settle_detail.setter
    def settle_detail(self, value):
        if isinstance(value, list):
            self._settle_detail = list()
            for i in value:
                if isinstance(i, BatchSettleDetail):
                    self._settle_detail.append(i)
                else:
                    self._settle_detail.append(BatchSettleDetail.from_alipay_dict(i))
    @property
    def settle_no(self):
        return self._settle_no

    @settle_no.setter
    def settle_no(self, value):
        self._settle_no = value

    def parse_response_content(self, response_content):
        response = super(AlipayTradeBatchSettleQueryResponse, self).parse_response_content(response_content)
        if 'out_request_no' in response:
            self.out_request_no = response['out_request_no']
        if 'settle_detail' in response:
            self.settle_detail = response['settle_detail']
        if 'settle_no' in response:
            self.settle_no = response['settle_no']
