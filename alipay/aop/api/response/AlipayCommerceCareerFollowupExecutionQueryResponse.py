#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.FollowupExecution import FollowupExecution


class AlipayCommerceCareerFollowupExecutionQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceCareerFollowupExecutionQueryResponse, self).__init__()
        self._ended_type = None
        self._executions = None
        self._order_no = None
        self._out_biz_no = None
        self._status = None

    @property
    def ended_type(self):
        return self._ended_type

    @ended_type.setter
    def ended_type(self, value):
        self._ended_type = value
    @property
    def executions(self):
        return self._executions

    @executions.setter
    def executions(self, value):
        if isinstance(value, list):
            self._executions = list()
            for i in value:
                if isinstance(i, FollowupExecution):
                    self._executions.append(i)
                else:
                    self._executions.append(FollowupExecution.from_alipay_dict(i))
    @property
    def order_no(self):
        return self._order_no

    @order_no.setter
    def order_no(self, value):
        self._order_no = value
    @property
    def out_biz_no(self):
        return self._out_biz_no

    @out_biz_no.setter
    def out_biz_no(self, value):
        self._out_biz_no = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceCareerFollowupExecutionQueryResponse, self).parse_response_content(response_content)
        if 'ended_type' in response:
            self.ended_type = response['ended_type']
        if 'executions' in response:
            self.executions = response['executions']
        if 'order_no' in response:
            self.order_no = response['order_no']
        if 'out_biz_no' in response:
            self.out_biz_no = response['out_biz_no']
        if 'status' in response:
            self.status = response['status']
