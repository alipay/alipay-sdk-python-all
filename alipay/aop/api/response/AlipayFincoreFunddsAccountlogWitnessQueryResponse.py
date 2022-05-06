#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.AccountingLogVO import AccountingLogVO


class AlipayFincoreFunddsAccountlogWitnessQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayFincoreFunddsAccountlogWitnessQueryResponse, self).__init__()
        self._accounting_log_list = None

    @property
    def accounting_log_list(self):
        return self._accounting_log_list

    @accounting_log_list.setter
    def accounting_log_list(self, value):
        if isinstance(value, list):
            self._accounting_log_list = list()
            for i in value:
                if isinstance(i, AccountingLogVO):
                    self._accounting_log_list.append(i)
                else:
                    self._accounting_log_list.append(AccountingLogVO.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AlipayFincoreFunddsAccountlogWitnessQueryResponse, self).parse_response_content(response_content)
        if 'accounting_log_list' in response:
            self.accounting_log_list = response['accounting_log_list']
