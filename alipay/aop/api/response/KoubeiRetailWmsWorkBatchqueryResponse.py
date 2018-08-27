#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.WorkListVO import WorkListVO


class KoubeiRetailWmsWorkBatchqueryResponse(AlipayResponse):

    def __init__(self):
        super(KoubeiRetailWmsWorkBatchqueryResponse, self).__init__()
        self._page_no = None
        self._page_size = None
        self._total_count = None
        self._work_list = None

    @property
    def page_no(self):
        return self._page_no

    @page_no.setter
    def page_no(self, value):
        self._page_no = value
    @property
    def page_size(self):
        return self._page_size

    @page_size.setter
    def page_size(self, value):
        self._page_size = value
    @property
    def total_count(self):
        return self._total_count

    @total_count.setter
    def total_count(self, value):
        self._total_count = value
    @property
    def work_list(self):
        return self._work_list

    @work_list.setter
    def work_list(self, value):
        if isinstance(value, list):
            self._work_list = list()
            for i in value:
                if isinstance(i, WorkListVO):
                    self._work_list.append(i)
                else:
                    self._work_list.append(WorkListVO.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(KoubeiRetailWmsWorkBatchqueryResponse, self).parse_response_content(response_content)
        if 'page_no' in response:
            self.page_no = response['page_no']
        if 'page_size' in response:
            self.page_size = response['page_size']
        if 'total_count' in response:
            self.total_count = response['total_count']
        if 'work_list' in response:
            self.work_list = response['work_list']
