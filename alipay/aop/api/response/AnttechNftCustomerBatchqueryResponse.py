#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.UserAsset import UserAsset


class AnttechNftCustomerBatchqueryResponse(AlipayResponse):

    def __init__(self):
        super(AnttechNftCustomerBatchqueryResponse, self).__init__()
        self._asset_list = None
        self._page = None
        self._page_size = None
        self._req_msg_id = None
        self._total_count = None

    @property
    def asset_list(self):
        return self._asset_list

    @asset_list.setter
    def asset_list(self, value):
        if isinstance(value, list):
            self._asset_list = list()
            for i in value:
                if isinstance(i, UserAsset):
                    self._asset_list.append(i)
                else:
                    self._asset_list.append(UserAsset.from_alipay_dict(i))
    @property
    def page(self):
        return self._page

    @page.setter
    def page(self, value):
        self._page = value
    @property
    def page_size(self):
        return self._page_size

    @page_size.setter
    def page_size(self, value):
        self._page_size = value
    @property
    def req_msg_id(self):
        return self._req_msg_id

    @req_msg_id.setter
    def req_msg_id(self, value):
        self._req_msg_id = value
    @property
    def total_count(self):
        return self._total_count

    @total_count.setter
    def total_count(self, value):
        self._total_count = value

    def parse_response_content(self, response_content):
        response = super(AnttechNftCustomerBatchqueryResponse, self).parse_response_content(response_content)
        if 'asset_list' in response:
            self.asset_list = response['asset_list']
        if 'page' in response:
            self.page = response['page']
        if 'page_size' in response:
            self.page_size = response['page_size']
        if 'req_msg_id' in response:
            self.req_msg_id = response['req_msg_id']
        if 'total_count' in response:
            self.total_count = response['total_count']
