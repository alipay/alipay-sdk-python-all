#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.LinkTypeListResult import LinkTypeListResult


class AlipayDigitalmgmtLinktypeQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayDigitalmgmtLinktypeQueryResponse, self).__init__()
        self._link_type_list_result = None

    @property
    def link_type_list_result(self):
        return self._link_type_list_result

    @link_type_list_result.setter
    def link_type_list_result(self, value):
        if isinstance(value, LinkTypeListResult):
            self._link_type_list_result = value
        else:
            self._link_type_list_result = LinkTypeListResult.from_alipay_dict(value)

    def parse_response_content(self, response_content):
        response = super(AlipayDigitalmgmtLinktypeQueryResponse, self).parse_response_content(response_content)
        if 'link_type_list_result' in response:
            self.link_type_list_result = response['link_type_list_result']
