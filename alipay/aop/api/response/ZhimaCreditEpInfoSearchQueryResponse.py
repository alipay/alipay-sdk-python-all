#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.EpSearchBasicInfo import EpSearchBasicInfo


class ZhimaCreditEpInfoSearchQueryResponse(AlipayResponse):

    def __init__(self):
        super(ZhimaCreditEpInfoSearchQueryResponse, self).__init__()
        self._basic_info_models = None
        self._has_next = None
        self._page_index = None
        self._page_total = None
        self._total = None

    @property
    def basic_info_models(self):
        return self._basic_info_models

    @basic_info_models.setter
    def basic_info_models(self, value):
        if isinstance(value, list):
            self._basic_info_models = list()
            for i in value:
                if isinstance(i, EpSearchBasicInfo):
                    self._basic_info_models.append(i)
                else:
                    self._basic_info_models.append(EpSearchBasicInfo.from_alipay_dict(i))
    @property
    def has_next(self):
        return self._has_next

    @has_next.setter
    def has_next(self, value):
        self._has_next = value
    @property
    def page_index(self):
        return self._page_index

    @page_index.setter
    def page_index(self, value):
        self._page_index = value
    @property
    def page_total(self):
        return self._page_total

    @page_total.setter
    def page_total(self, value):
        self._page_total = value
    @property
    def total(self):
        return self._total

    @total.setter
    def total(self, value):
        self._total = value

    def parse_response_content(self, response_content):
        response = super(ZhimaCreditEpInfoSearchQueryResponse, self).parse_response_content(response_content)
        if 'basic_info_models' in response:
            self.basic_info_models = response['basic_info_models']
        if 'has_next' in response:
            self.has_next = response['has_next']
        if 'page_index' in response:
            self.page_index = response['page_index']
        if 'page_total' in response:
            self.page_total = response['page_total']
        if 'total' in response:
            self.total = response['total']
