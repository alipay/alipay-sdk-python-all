#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.BatchRoyaltyDetail import BatchRoyaltyDetail


class AlipayTradeBatchTransferQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayTradeBatchTransferQueryResponse, self).__init__()
        self._out_request_no = None
        self._royalty_detail = None
        self._settle_no = None

    @property
    def out_request_no(self):
        return self._out_request_no

    @out_request_no.setter
    def out_request_no(self, value):
        self._out_request_no = value
    @property
    def royalty_detail(self):
        return self._royalty_detail

    @royalty_detail.setter
    def royalty_detail(self, value):
        if isinstance(value, list):
            self._royalty_detail = list()
            for i in value:
                if isinstance(i, BatchRoyaltyDetail):
                    self._royalty_detail.append(i)
                else:
                    self._royalty_detail.append(BatchRoyaltyDetail.from_alipay_dict(i))
    @property
    def settle_no(self):
        return self._settle_no

    @settle_no.setter
    def settle_no(self, value):
        self._settle_no = value

    def parse_response_content(self, response_content):
        response = super(AlipayTradeBatchTransferQueryResponse, self).parse_response_content(response_content)
        if 'out_request_no' in response:
            self.out_request_no = response['out_request_no']
        if 'royalty_detail' in response:
            self.royalty_detail = response['royalty_detail']
        if 'settle_no' in response:
            self.settle_no = response['settle_no']
