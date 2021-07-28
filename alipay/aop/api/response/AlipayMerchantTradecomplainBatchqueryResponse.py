#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.TradeComplainQueryResponse import TradeComplainQueryResponse


class AlipayMerchantTradecomplainBatchqueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayMerchantTradecomplainBatchqueryResponse, self).__init__()
        self._page_num = None
        self._page_size = None
        self._total_num = None
        self._total_page_num = None
        self._trade_complain_infos = None

    @property
    def page_num(self):
        return self._page_num

    @page_num.setter
    def page_num(self, value):
        self._page_num = value
    @property
    def page_size(self):
        return self._page_size

    @page_size.setter
    def page_size(self, value):
        self._page_size = value
    @property
    def total_num(self):
        return self._total_num

    @total_num.setter
    def total_num(self, value):
        self._total_num = value
    @property
    def total_page_num(self):
        return self._total_page_num

    @total_page_num.setter
    def total_page_num(self, value):
        self._total_page_num = value
    @property
    def trade_complain_infos(self):
        return self._trade_complain_infos

    @trade_complain_infos.setter
    def trade_complain_infos(self, value):
        if isinstance(value, list):
            self._trade_complain_infos = list()
            for i in value:
                if isinstance(i, TradeComplainQueryResponse):
                    self._trade_complain_infos.append(i)
                else:
                    self._trade_complain_infos.append(TradeComplainQueryResponse.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AlipayMerchantTradecomplainBatchqueryResponse, self).parse_response_content(response_content)
        if 'page_num' in response:
            self.page_num = response['page_num']
        if 'page_size' in response:
            self.page_size = response['page_size']
        if 'total_num' in response:
            self.total_num = response['total_num']
        if 'total_page_num' in response:
            self.total_page_num = response['total_page_num']
        if 'trade_complain_infos' in response:
            self.trade_complain_infos = response['trade_complain_infos']
