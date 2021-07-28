#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.LeadsOrderInfo import LeadsOrderInfo


class KoubeiServindustryLeadsRecordBatchqueryResponse(AlipayResponse):

    def __init__(self):
        super(KoubeiServindustryLeadsRecordBatchqueryResponse, self).__init__()
        self._leads_order_info_list = None
        self._total_count = None

    @property
    def leads_order_info_list(self):
        return self._leads_order_info_list

    @leads_order_info_list.setter
    def leads_order_info_list(self, value):
        if isinstance(value, list):
            self._leads_order_info_list = list()
            for i in value:
                if isinstance(i, LeadsOrderInfo):
                    self._leads_order_info_list.append(i)
                else:
                    self._leads_order_info_list.append(LeadsOrderInfo.from_alipay_dict(i))
    @property
    def total_count(self):
        return self._total_count

    @total_count.setter
    def total_count(self, value):
        self._total_count = value

    def parse_response_content(self, response_content):
        response = super(KoubeiServindustryLeadsRecordBatchqueryResponse, self).parse_response_content(response_content)
        if 'leads_order_info_list' in response:
            self.leads_order_info_list = response['leads_order_info_list']
        if 'total_count' in response:
            self.total_count = response['total_count']
