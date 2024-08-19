#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.ServiceAssistantRecordVO import ServiceAssistantRecordVO


class AlipayMerchantGroupAssistantServiceBatchqueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayMerchantGroupAssistantServiceBatchqueryResponse, self).__init__()
        self._assistant_record_list = None
        self._total_count = None

    @property
    def assistant_record_list(self):
        return self._assistant_record_list

    @assistant_record_list.setter
    def assistant_record_list(self, value):
        if isinstance(value, list):
            self._assistant_record_list = list()
            for i in value:
                if isinstance(i, ServiceAssistantRecordVO):
                    self._assistant_record_list.append(i)
                else:
                    self._assistant_record_list.append(ServiceAssistantRecordVO.from_alipay_dict(i))
    @property
    def total_count(self):
        return self._total_count

    @total_count.setter
    def total_count(self, value):
        self._total_count = value

    def parse_response_content(self, response_content):
        response = super(AlipayMerchantGroupAssistantServiceBatchqueryResponse, self).parse_response_content(response_content)
        if 'assistant_record_list' in response:
            self.assistant_record_list = response['assistant_record_list']
        if 'total_count' in response:
            self.total_count = response['total_count']
