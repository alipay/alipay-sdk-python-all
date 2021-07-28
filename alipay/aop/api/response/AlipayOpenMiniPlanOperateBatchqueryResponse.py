#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.PaymentSuccessPagePlanInfo import PaymentSuccessPagePlanInfo


class AlipayOpenMiniPlanOperateBatchqueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOpenMiniPlanOperateBatchqueryResponse, self).__init__()
        self._page_data = None
        self._page_num = None
        self._page_size = None
        self._total_number = None

    @property
    def page_data(self):
        return self._page_data

    @page_data.setter
    def page_data(self, value):
        if isinstance(value, list):
            self._page_data = list()
            for i in value:
                if isinstance(i, PaymentSuccessPagePlanInfo):
                    self._page_data.append(i)
                else:
                    self._page_data.append(PaymentSuccessPagePlanInfo.from_alipay_dict(i))
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
    def total_number(self):
        return self._total_number

    @total_number.setter
    def total_number(self, value):
        self._total_number = value

    def parse_response_content(self, response_content):
        response = super(AlipayOpenMiniPlanOperateBatchqueryResponse, self).parse_response_content(response_content)
        if 'page_data' in response:
            self.page_data = response['page_data']
        if 'page_num' in response:
            self.page_num = response['page_num']
        if 'page_size' in response:
            self.page_size = response['page_size']
        if 'total_number' in response:
            self.total_number = response['total_number']
