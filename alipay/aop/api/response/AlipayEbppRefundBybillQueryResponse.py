#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.EbppRefundInfo import EbppRefundInfo


class AlipayEbppRefundBybillQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayEbppRefundBybillQueryResponse, self).__init__()
        self._bill_no = None
        self._refund_info_list = None

    @property
    def bill_no(self):
        return self._bill_no

    @bill_no.setter
    def bill_no(self, value):
        self._bill_no = value
    @property
    def refund_info_list(self):
        return self._refund_info_list

    @refund_info_list.setter
    def refund_info_list(self, value):
        if isinstance(value, list):
            self._refund_info_list = list()
            for i in value:
                if isinstance(i, EbppRefundInfo):
                    self._refund_info_list.append(i)
                else:
                    self._refund_info_list.append(EbppRefundInfo.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AlipayEbppRefundBybillQueryResponse, self).parse_response_content(response_content)
        if 'bill_no' in response:
            self.bill_no = response['bill_no']
        if 'refund_info_list' in response:
            self.refund_info_list = response['refund_info_list']
