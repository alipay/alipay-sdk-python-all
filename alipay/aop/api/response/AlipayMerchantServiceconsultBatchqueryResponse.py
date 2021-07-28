#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.ServiceConsultQueryResponse import ServiceConsultQueryResponse


class AlipayMerchantServiceconsultBatchqueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayMerchantServiceconsultBatchqueryResponse, self).__init__()
        self._consult_infos = None
        self._page_num = None
        self._page_size = None
        self._total_num = None
        self._total_page_num = None

    @property
    def consult_infos(self):
        return self._consult_infos

    @consult_infos.setter
    def consult_infos(self, value):
        if isinstance(value, list):
            self._consult_infos = list()
            for i in value:
                if isinstance(i, ServiceConsultQueryResponse):
                    self._consult_infos.append(i)
                else:
                    self._consult_infos.append(ServiceConsultQueryResponse.from_alipay_dict(i))
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

    def parse_response_content(self, response_content):
        response = super(AlipayMerchantServiceconsultBatchqueryResponse, self).parse_response_content(response_content)
        if 'consult_infos' in response:
            self.consult_infos = response['consult_infos']
        if 'page_num' in response:
            self.page_num = response['page_num']
        if 'page_size' in response:
            self.page_size = response['page_size']
        if 'total_num' in response:
            self.total_num = response['total_num']
        if 'total_page_num' in response:
            self.total_page_num = response['total_page_num']
