#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.CraftsmanWorkOpenModel import CraftsmanWorkOpenModel


class KoubeiCraftsmanDataWorkBatchqueryResponse(AlipayResponse):

    def __init__(self):
        super(KoubeiCraftsmanDataWorkBatchqueryResponse, self).__init__()
        self._current_page_no = None
        self._page_size = None
        self._total_page_no = None
        self._total_works = None
        self._works = None

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
    def total_page_no(self):
        return self._total_page_no

    @total_page_no.setter
    def total_page_no(self, value):
        self._total_page_no = value
    @property
    def total_works(self):
        return self._total_works

    @total_works.setter
    def total_works(self, value):
        self._total_works = value
    @property
    def works(self):
        return self._works

    @works.setter
    def works(self, value):
        if isinstance(value, list):
            self._works = list()
            for i in value:
                if isinstance(i, CraftsmanWorkOpenModel):
                    self._works.append(i)
                else:
                    self._works.append(CraftsmanWorkOpenModel.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(KoubeiCraftsmanDataWorkBatchqueryResponse, self).parse_response_content(response_content)
        if 'current_page_no' in response:
            self.current_page_no = response['current_page_no']
        if 'page_size' in response:
            self.page_size = response['page_size']
        if 'total_page_no' in response:
            self.total_page_no = response['total_page_no']
        if 'total_works' in response:
            self.total_works = response['total_works']
        if 'works' in response:
            self.works = response['works']
