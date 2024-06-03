#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.LocalSettleBillItem import LocalSettleBillItem


class AlipayOpenMiniOrderbillLocalsettleBatchqueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOpenMiniOrderbillLocalsettleBatchqueryResponse, self).__init__()
        self._bill_list = None
        self._page_size = None
        self._page_token = None

    @property
    def bill_list(self):
        return self._bill_list

    @bill_list.setter
    def bill_list(self, value):
        if isinstance(value, list):
            self._bill_list = list()
            for i in value:
                if isinstance(i, LocalSettleBillItem):
                    self._bill_list.append(i)
                else:
                    self._bill_list.append(LocalSettleBillItem.from_alipay_dict(i))
    @property
    def page_size(self):
        return self._page_size

    @page_size.setter
    def page_size(self, value):
        self._page_size = value
    @property
    def page_token(self):
        return self._page_token

    @page_token.setter
    def page_token(self, value):
        self._page_token = value

    def parse_response_content(self, response_content):
        response = super(AlipayOpenMiniOrderbillLocalsettleBatchqueryResponse, self).parse_response_content(response_content)
        if 'bill_list' in response:
            self.bill_list = response['bill_list']
        if 'page_size' in response:
            self.page_size = response['page_size']
        if 'page_token' in response:
            self.page_token = response['page_token']
