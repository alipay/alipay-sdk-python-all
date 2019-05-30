#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.RoyaltyEntity import RoyaltyEntity


class AlipayTradeRoyaltyRelationBatchqueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayTradeRoyaltyRelationBatchqueryResponse, self).__init__()
        self._current_page_num = None
        self._current_page_size = None
        self._receiver_list = None
        self._result_code = None
        self._total_page_num = None
        self._total_record_num = None

    @property
    def current_page_num(self):
        return self._current_page_num

    @current_page_num.setter
    def current_page_num(self, value):
        self._current_page_num = value
    @property
    def current_page_size(self):
        return self._current_page_size

    @current_page_size.setter
    def current_page_size(self, value):
        self._current_page_size = value
    @property
    def receiver_list(self):
        return self._receiver_list

    @receiver_list.setter
    def receiver_list(self, value):
        if isinstance(value, list):
            self._receiver_list = list()
            for i in value:
                if isinstance(i, RoyaltyEntity):
                    self._receiver_list.append(i)
                else:
                    self._receiver_list.append(RoyaltyEntity.from_alipay_dict(i))
    @property
    def result_code(self):
        return self._result_code

    @result_code.setter
    def result_code(self, value):
        self._result_code = value
    @property
    def total_page_num(self):
        return self._total_page_num

    @total_page_num.setter
    def total_page_num(self, value):
        self._total_page_num = value
    @property
    def total_record_num(self):
        return self._total_record_num

    @total_record_num.setter
    def total_record_num(self, value):
        self._total_record_num = value

    def parse_response_content(self, response_content):
        response = super(AlipayTradeRoyaltyRelationBatchqueryResponse, self).parse_response_content(response_content)
        if 'current_page_num' in response:
            self.current_page_num = response['current_page_num']
        if 'current_page_size' in response:
            self.current_page_size = response['current_page_size']
        if 'receiver_list' in response:
            self.receiver_list = response['receiver_list']
        if 'result_code' in response:
            self.result_code = response['result_code']
        if 'total_page_num' in response:
            self.total_page_num = response['total_page_num']
        if 'total_record_num' in response:
            self.total_record_num = response['total_record_num']
