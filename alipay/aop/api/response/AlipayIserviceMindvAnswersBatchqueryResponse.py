#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.UserSubmitModel import UserSubmitModel


class AlipayIserviceMindvAnswersBatchqueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayIserviceMindvAnswersBatchqueryResponse, self).__init__()
        self._current_page_num = None
        self._page_data = None
        self._per_page_size = None
        self._total_num = None

    @property
    def current_page_num(self):
        return self._current_page_num

    @current_page_num.setter
    def current_page_num(self, value):
        self._current_page_num = value
    @property
    def page_data(self):
        return self._page_data

    @page_data.setter
    def page_data(self, value):
        if isinstance(value, list):
            self._page_data = list()
            for i in value:
                if isinstance(i, UserSubmitModel):
                    self._page_data.append(i)
                else:
                    self._page_data.append(UserSubmitModel.from_alipay_dict(i))
    @property
    def per_page_size(self):
        return self._per_page_size

    @per_page_size.setter
    def per_page_size(self, value):
        self._per_page_size = value
    @property
    def total_num(self):
        return self._total_num

    @total_num.setter
    def total_num(self, value):
        self._total_num = value

    def parse_response_content(self, response_content):
        response = super(AlipayIserviceMindvAnswersBatchqueryResponse, self).parse_response_content(response_content)
        if 'current_page_num' in response:
            self.current_page_num = response['current_page_num']
        if 'page_data' in response:
            self.page_data = response['page_data']
        if 'per_page_size' in response:
            self.per_page_size = response['per_page_size']
        if 'total_num' in response:
            self.total_num = response['total_num']
