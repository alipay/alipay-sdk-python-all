#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.OneCategoryDTO import OneCategoryDTO


class DatadigitalFincloudFinsaasTagListBatchqueryResponse(AlipayResponse):

    def __init__(self):
        super(DatadigitalFincloudFinsaasTagListBatchqueryResponse, self).__init__()
        self._category_list = None

    @property
    def category_list(self):
        return self._category_list

    @category_list.setter
    def category_list(self, value):
        if isinstance(value, list):
            self._category_list = list()
            for i in value:
                if isinstance(i, OneCategoryDTO):
                    self._category_list.append(i)
                else:
                    self._category_list.append(OneCategoryDTO.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(DatadigitalFincloudFinsaasTagListBatchqueryResponse, self).parse_response_content(response_content)
        if 'category_list' in response:
            self.category_list = response['category_list']
