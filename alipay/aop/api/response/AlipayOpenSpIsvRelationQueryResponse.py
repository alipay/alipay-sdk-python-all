#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.PromotionRelationDTO import PromotionRelationDTO


class AlipayOpenSpIsvRelationQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOpenSpIsvRelationQueryResponse, self).__init__()
        self._current_page = None
        self._page_size = None
        self._promotion_relations = None
        self._total_size = None

    @property
    def current_page(self):
        return self._current_page

    @current_page.setter
    def current_page(self, value):
        self._current_page = value
    @property
    def page_size(self):
        return self._page_size

    @page_size.setter
    def page_size(self, value):
        self._page_size = value
    @property
    def promotion_relations(self):
        return self._promotion_relations

    @promotion_relations.setter
    def promotion_relations(self, value):
        if isinstance(value, list):
            self._promotion_relations = list()
            for i in value:
                if isinstance(i, PromotionRelationDTO):
                    self._promotion_relations.append(i)
                else:
                    self._promotion_relations.append(PromotionRelationDTO.from_alipay_dict(i))
    @property
    def total_size(self):
        return self._total_size

    @total_size.setter
    def total_size(self, value):
        self._total_size = value

    def parse_response_content(self, response_content):
        response = super(AlipayOpenSpIsvRelationQueryResponse, self).parse_response_content(response_content)
        if 'current_page' in response:
            self.current_page = response['current_page']
        if 'page_size' in response:
            self.page_size = response['page_size']
        if 'promotion_relations' in response:
            self.promotion_relations = response['promotion_relations']
        if 'total_size' in response:
            self.total_size = response['total_size']
