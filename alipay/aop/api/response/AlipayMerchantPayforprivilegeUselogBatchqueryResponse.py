#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.PayForPrivilegeRechargeCardUseLog import PayForPrivilegeRechargeCardUseLog


class AlipayMerchantPayforprivilegeUselogBatchqueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayMerchantPayforprivilegeUselogBatchqueryResponse, self).__init__()
        self._use_log_list = None

    @property
    def use_log_list(self):
        return self._use_log_list

    @use_log_list.setter
    def use_log_list(self, value):
        if isinstance(value, list):
            self._use_log_list = list()
            for i in value:
                if isinstance(i, PayForPrivilegeRechargeCardUseLog):
                    self._use_log_list.append(i)
                else:
                    self._use_log_list.append(PayForPrivilegeRechargeCardUseLog.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AlipayMerchantPayforprivilegeUselogBatchqueryResponse, self).parse_response_content(response_content)
        if 'use_log_list' in response:
            self.use_log_list = response['use_log_list']
