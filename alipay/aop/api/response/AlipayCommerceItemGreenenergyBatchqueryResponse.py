#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.GreenEnergyLogsDTO import GreenEnergyLogsDTO


class AlipayCommerceItemGreenenergyBatchqueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceItemGreenenergyBatchqueryResponse, self).__init__()
        self._green_energy_logs = None
        self._page_num = None
        self._page_size = None
        self._total_size = None

    @property
    def green_energy_logs(self):
        return self._green_energy_logs

    @green_energy_logs.setter
    def green_energy_logs(self, value):
        if isinstance(value, list):
            self._green_energy_logs = list()
            for i in value:
                if isinstance(i, GreenEnergyLogsDTO):
                    self._green_energy_logs.append(i)
                else:
                    self._green_energy_logs.append(GreenEnergyLogsDTO.from_alipay_dict(i))
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
    def total_size(self):
        return self._total_size

    @total_size.setter
    def total_size(self, value):
        self._total_size = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceItemGreenenergyBatchqueryResponse, self).parse_response_content(response_content)
        if 'green_energy_logs' in response:
            self.green_energy_logs = response['green_energy_logs']
        if 'page_num' in response:
            self.page_num = response['page_num']
        if 'page_size' in response:
            self.page_size = response['page_size']
        if 'total_size' in response:
            self.total_size = response['total_size']
