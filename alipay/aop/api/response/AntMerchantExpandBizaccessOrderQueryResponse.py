#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.IsvBizOpenOrderFailReason import IsvBizOpenOrderFailReason


class AntMerchantExpandBizaccessOrderQueryResponse(AlipayResponse):

    def __init__(self):
        super(AntMerchantExpandBizaccessOrderQueryResponse, self).__init__()
        self._fail_reasons = None
        self._order_id = None
        self._order_status = None
        self._wait_process_task_url = None

    @property
    def fail_reasons(self):
        return self._fail_reasons

    @fail_reasons.setter
    def fail_reasons(self, value):
        if isinstance(value, list):
            self._fail_reasons = list()
            for i in value:
                if isinstance(i, IsvBizOpenOrderFailReason):
                    self._fail_reasons.append(i)
                else:
                    self._fail_reasons.append(IsvBizOpenOrderFailReason.from_alipay_dict(i))
    @property
    def order_id(self):
        return self._order_id

    @order_id.setter
    def order_id(self, value):
        self._order_id = value
    @property
    def order_status(self):
        return self._order_status

    @order_status.setter
    def order_status(self, value):
        self._order_status = value
    @property
    def wait_process_task_url(self):
        return self._wait_process_task_url

    @wait_process_task_url.setter
    def wait_process_task_url(self, value):
        self._wait_process_task_url = value

    def parse_response_content(self, response_content):
        response = super(AntMerchantExpandBizaccessOrderQueryResponse, self).parse_response_content(response_content)
        if 'fail_reasons' in response:
            self.fail_reasons = response['fail_reasons']
        if 'order_id' in response:
            self.order_id = response['order_id']
        if 'order_status' in response:
            self.order_status = response['order_status']
        if 'wait_process_task_url' in response:
            self.wait_process_task_url = response['wait_process_task_url']
