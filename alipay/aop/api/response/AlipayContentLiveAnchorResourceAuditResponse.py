#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.ResourceAuditResult import ResourceAuditResult


class AlipayContentLiveAnchorResourceAuditResponse(AlipayResponse):

    def __init__(self):
        super(AlipayContentLiveAnchorResourceAuditResponse, self).__init__()
        self._biz_trace_id = None
        self._reject_item_list = None

    @property
    def biz_trace_id(self):
        return self._biz_trace_id

    @biz_trace_id.setter
    def biz_trace_id(self, value):
        self._biz_trace_id = value
    @property
    def reject_item_list(self):
        return self._reject_item_list

    @reject_item_list.setter
    def reject_item_list(self, value):
        if isinstance(value, list):
            self._reject_item_list = list()
            for i in value:
                if isinstance(i, ResourceAuditResult):
                    self._reject_item_list.append(i)
                else:
                    self._reject_item_list.append(ResourceAuditResult.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AlipayContentLiveAnchorResourceAuditResponse, self).parse_response_content(response_content)
        if 'biz_trace_id' in response:
            self.biz_trace_id = response['biz_trace_id']
        if 'reject_item_list' in response:
            self.reject_item_list = response['reject_item_list']
