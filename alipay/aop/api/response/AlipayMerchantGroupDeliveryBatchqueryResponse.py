#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.GroupDeliveryRecordVO import GroupDeliveryRecordVO


class AlipayMerchantGroupDeliveryBatchqueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayMerchantGroupDeliveryBatchqueryResponse, self).__init__()
        self._delivery_record_list = None
        self._total_count = None

    @property
    def delivery_record_list(self):
        return self._delivery_record_list

    @delivery_record_list.setter
    def delivery_record_list(self, value):
        if isinstance(value, list):
            self._delivery_record_list = list()
            for i in value:
                if isinstance(i, GroupDeliveryRecordVO):
                    self._delivery_record_list.append(i)
                else:
                    self._delivery_record_list.append(GroupDeliveryRecordVO.from_alipay_dict(i))
    @property
    def total_count(self):
        return self._total_count

    @total_count.setter
    def total_count(self, value):
        self._total_count = value

    def parse_response_content(self, response_content):
        response = super(AlipayMerchantGroupDeliveryBatchqueryResponse, self).parse_response_content(response_content)
        if 'delivery_record_list' in response:
            self.delivery_record_list = response['delivery_record_list']
        if 'total_count' in response:
            self.total_count = response['total_count']
