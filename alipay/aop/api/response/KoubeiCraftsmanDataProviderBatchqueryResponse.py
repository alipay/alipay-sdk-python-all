#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.CraftsmanOpenModel import CraftsmanOpenModel


class KoubeiCraftsmanDataProviderBatchqueryResponse(AlipayResponse):

    def __init__(self):
        super(KoubeiCraftsmanDataProviderBatchqueryResponse, self).__init__()
        self._craftsmans = None
        self._current_page_no = None
        self._page_size = None
        self._total_craftsmans = None
        self._total_page_no = None

    @property
    def craftsmans(self):
        return self._craftsmans

    @craftsmans.setter
    def craftsmans(self, value):
        if isinstance(value, list):
            self._craftsmans = list()
            for i in value:
                if isinstance(i, CraftsmanOpenModel):
                    self._craftsmans.append(i)
                else:
                    self._craftsmans.append(CraftsmanOpenModel.from_alipay_dict(i))
    @property
    def current_page_no(self):
        return self._current_page_no

    @current_page_no.setter
    def current_page_no(self, value):
        self._current_page_no = value
    @property
    def page_size(self):
        return self._page_size

    @page_size.setter
    def page_size(self, value):
        self._page_size = value
    @property
    def total_craftsmans(self):
        return self._total_craftsmans

    @total_craftsmans.setter
    def total_craftsmans(self, value):
        self._total_craftsmans = value
    @property
    def total_page_no(self):
        return self._total_page_no

    @total_page_no.setter
    def total_page_no(self, value):
        self._total_page_no = value

    def parse_response_content(self, response_content):
        response = super(KoubeiCraftsmanDataProviderBatchqueryResponse, self).parse_response_content(response_content)
        if 'craftsmans' in response:
            self.craftsmans = response['craftsmans']
        if 'current_page_no' in response:
            self.current_page_no = response['current_page_no']
        if 'page_size' in response:
            self.page_size = response['page_size']
        if 'total_craftsmans' in response:
            self.total_craftsmans = response['total_craftsmans']
        if 'total_page_no' in response:
            self.total_page_no = response['total_page_no']
