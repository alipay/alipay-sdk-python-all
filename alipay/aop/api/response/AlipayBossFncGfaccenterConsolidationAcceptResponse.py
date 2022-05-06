#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayBossFncGfaccenterConsolidationAcceptResponse(AlipayResponse):

    def __init__(self):
        super(AlipayBossFncGfaccenterConsolidationAcceptResponse, self).__init__()
        self._consolidation_success = None
        self._need_retry = None
        self._result_msg = None

    @property
    def consolidation_success(self):
        return self._consolidation_success

    @consolidation_success.setter
    def consolidation_success(self, value):
        self._consolidation_success = value
    @property
    def need_retry(self):
        return self._need_retry

    @need_retry.setter
    def need_retry(self, value):
        self._need_retry = value
    @property
    def result_msg(self):
        return self._result_msg

    @result_msg.setter
    def result_msg(self, value):
        self._result_msg = value

    def parse_response_content(self, response_content):
        response = super(AlipayBossFncGfaccenterConsolidationAcceptResponse, self).parse_response_content(response_content)
        if 'consolidation_success' in response:
            self.consolidation_success = response['consolidation_success']
        if 'need_retry' in response:
            self.need_retry = response['need_retry']
        if 'result_msg' in response:
            self.result_msg = response['result_msg']
