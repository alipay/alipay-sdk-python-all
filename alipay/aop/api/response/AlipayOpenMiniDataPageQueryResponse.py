#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.PageVisitDataResponse import PageVisitDataResponse


class AlipayOpenMiniDataPageQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOpenMiniDataPageQueryResponse, self).__init__()
        self._page_visit_data_list_response = None

    @property
    def page_visit_data_list_response(self):
        return self._page_visit_data_list_response

    @page_visit_data_list_response.setter
    def page_visit_data_list_response(self, value):
        if isinstance(value, list):
            self._page_visit_data_list_response = list()
            for i in value:
                if isinstance(i, PageVisitDataResponse):
                    self._page_visit_data_list_response.append(i)
                else:
                    self._page_visit_data_list_response.append(PageVisitDataResponse.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AlipayOpenMiniDataPageQueryResponse, self).parse_response_content(response_content)
        if 'page_visit_data_list_response' in response:
            self.page_visit_data_list_response = response['page_visit_data_list_response']
