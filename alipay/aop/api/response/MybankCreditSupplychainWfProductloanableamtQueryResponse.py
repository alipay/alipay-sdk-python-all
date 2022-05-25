#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.McaStoreLoanableDetail import McaStoreLoanableDetail


class MybankCreditSupplychainWfProductloanableamtQueryResponse(AlipayResponse):

    def __init__(self):
        super(MybankCreditSupplychainWfProductloanableamtQueryResponse, self).__init__()
        self._storeloanablelist = None

    @property
    def storeloanablelist(self):
        return self._storeloanablelist

    @storeloanablelist.setter
    def storeloanablelist(self, value):
        if isinstance(value, list):
            self._storeloanablelist = list()
            for i in value:
                if isinstance(i, McaStoreLoanableDetail):
                    self._storeloanablelist.append(i)
                else:
                    self._storeloanablelist.append(McaStoreLoanableDetail.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(MybankCreditSupplychainWfProductloanableamtQueryResponse, self).parse_response_content(response_content)
        if 'storeloanablelist' in response:
            self.storeloanablelist = response['storeloanablelist']
