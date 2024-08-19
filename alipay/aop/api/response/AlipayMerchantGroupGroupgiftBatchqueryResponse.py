#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.MultiChannelJoinGiftRecordVO import MultiChannelJoinGiftRecordVO


class AlipayMerchantGroupGroupgiftBatchqueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayMerchantGroupGroupgiftBatchqueryResponse, self).__init__()
        self._join_gift_record_list = None
        self._total_count = None

    @property
    def join_gift_record_list(self):
        return self._join_gift_record_list

    @join_gift_record_list.setter
    def join_gift_record_list(self, value):
        if isinstance(value, list):
            self._join_gift_record_list = list()
            for i in value:
                if isinstance(i, MultiChannelJoinGiftRecordVO):
                    self._join_gift_record_list.append(i)
                else:
                    self._join_gift_record_list.append(MultiChannelJoinGiftRecordVO.from_alipay_dict(i))
    @property
    def total_count(self):
        return self._total_count

    @total_count.setter
    def total_count(self, value):
        self._total_count = value

    def parse_response_content(self, response_content):
        response = super(AlipayMerchantGroupGroupgiftBatchqueryResponse, self).parse_response_content(response_content)
        if 'join_gift_record_list' in response:
            self.join_gift_record_list = response['join_gift_record_list']
        if 'total_count' in response:
            self.total_count = response['total_count']
