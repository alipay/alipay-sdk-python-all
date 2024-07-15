#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.AssistantMsgRecordVO import AssistantMsgRecordVO


class AlipayMerchantGroupAssistantMsgBatchqueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayMerchantGroupAssistantMsgBatchqueryResponse, self).__init__()
        self._msg_record_list = None
        self._total_count = None

    @property
    def msg_record_list(self):
        return self._msg_record_list

    @msg_record_list.setter
    def msg_record_list(self, value):
        if isinstance(value, list):
            self._msg_record_list = list()
            for i in value:
                if isinstance(i, AssistantMsgRecordVO):
                    self._msg_record_list.append(i)
                else:
                    self._msg_record_list.append(AssistantMsgRecordVO.from_alipay_dict(i))
    @property
    def total_count(self):
        return self._total_count

    @total_count.setter
    def total_count(self, value):
        self._total_count = value

    def parse_response_content(self, response_content):
        response = super(AlipayMerchantGroupAssistantMsgBatchqueryResponse, self).parse_response_content(response_content)
        if 'msg_record_list' in response:
            self.msg_record_list = response['msg_record_list']
        if 'total_count' in response:
            self.total_count = response['total_count']
