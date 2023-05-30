#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.OpenApiTenantInfo import OpenApiTenantInfo


class AlipayIserviceIsresourceTenantpagequeryQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayIserviceIsresourceTenantpagequeryQueryResponse, self).__init__()
        self._biz_data = None
        self._page_count = None
        self._page_no = None
        self._page_size = None
        self._total = None

    @property
    def biz_data(self):
        return self._biz_data

    @biz_data.setter
    def biz_data(self, value):
        if isinstance(value, list):
            self._biz_data = list()
            for i in value:
                if isinstance(i, OpenApiTenantInfo):
                    self._biz_data.append(i)
                else:
                    self._biz_data.append(OpenApiTenantInfo.from_alipay_dict(i))
    @property
    def page_count(self):
        return self._page_count

    @page_count.setter
    def page_count(self, value):
        self._page_count = value
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
    def total(self):
        return self._total

    @total.setter
    def total(self, value):
        self._total = value

    def parse_response_content(self, response_content):
        response = super(AlipayIserviceIsresourceTenantpagequeryQueryResponse, self).parse_response_content(response_content)
        if 'biz_data' in response:
            self.biz_data = response['biz_data']
        if 'page_count' in response:
            self.page_count = response['page_count']
        if 'page_no' in response:
            self.page_no = response['page_no']
        if 'page_size' in response:
            self.page_size = response['page_size']
        if 'total' in response:
            self.total = response['total']
