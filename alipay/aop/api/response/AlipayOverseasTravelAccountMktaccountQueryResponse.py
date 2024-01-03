#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.OutMktAccount import OutMktAccount


class AlipayOverseasTravelAccountMktaccountQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOverseasTravelAccountMktaccountQueryResponse, self).__init__()
        self._need_retry = None
        self._out_mkt_accounts = None
        self._result_code = None
        self._result_message = None
        self._result_status = None

    @property
    def need_retry(self):
        return self._need_retry

    @need_retry.setter
    def need_retry(self, value):
        self._need_retry = value
    @property
    def out_mkt_accounts(self):
        return self._out_mkt_accounts

    @out_mkt_accounts.setter
    def out_mkt_accounts(self, value):
        if isinstance(value, list):
            self._out_mkt_accounts = list()
            for i in value:
                if isinstance(i, OutMktAccount):
                    self._out_mkt_accounts.append(i)
                else:
                    self._out_mkt_accounts.append(OutMktAccount.from_alipay_dict(i))
    @property
    def result_code(self):
        return self._result_code

    @result_code.setter
    def result_code(self, value):
        self._result_code = value
    @property
    def result_message(self):
        return self._result_message

    @result_message.setter
    def result_message(self, value):
        self._result_message = value
    @property
    def result_status(self):
        return self._result_status

    @result_status.setter
    def result_status(self, value):
        self._result_status = value

    def parse_response_content(self, response_content):
        response = super(AlipayOverseasTravelAccountMktaccountQueryResponse, self).parse_response_content(response_content)
        if 'need_retry' in response:
            self.need_retry = response['need_retry']
        if 'out_mkt_accounts' in response:
            self.out_mkt_accounts = response['out_mkt_accounts']
        if 'result_code' in response:
            self.result_code = response['result_code']
        if 'result_message' in response:
            self.result_message = response['result_message']
        if 'result_status' in response:
            self.result_status = response['result_status']
