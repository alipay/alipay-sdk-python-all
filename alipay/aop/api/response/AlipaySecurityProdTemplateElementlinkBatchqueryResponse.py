#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.TemplateElementLinkDTO import TemplateElementLinkDTO


class AlipaySecurityProdTemplateElementlinkBatchqueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipaySecurityProdTemplateElementlinkBatchqueryResponse, self).__init__()
        self._element_link_dto_list = None

    @property
    def element_link_dto_list(self):
        return self._element_link_dto_list

    @element_link_dto_list.setter
    def element_link_dto_list(self, value):
        if isinstance(value, list):
            self._element_link_dto_list = list()
            for i in value:
                if isinstance(i, TemplateElementLinkDTO):
                    self._element_link_dto_list.append(i)
                else:
                    self._element_link_dto_list.append(TemplateElementLinkDTO.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AlipaySecurityProdTemplateElementlinkBatchqueryResponse, self).parse_response_content(response_content)
        if 'element_link_dto_list' in response:
            self.element_link_dto_list = response['element_link_dto_list']
