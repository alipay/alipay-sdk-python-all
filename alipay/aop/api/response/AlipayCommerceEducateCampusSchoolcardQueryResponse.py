#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.SchoolCard import SchoolCard


class AlipayCommerceEducateCampusSchoolcardQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceEducateCampusSchoolcardQueryResponse, self).__init__()
        self._school_card_list = None

    @property
    def school_card_list(self):
        return self._school_card_list

    @school_card_list.setter
    def school_card_list(self, value):
        if isinstance(value, list):
            self._school_card_list = list()
            for i in value:
                if isinstance(i, SchoolCard):
                    self._school_card_list.append(i)
                else:
                    self._school_card_list.append(SchoolCard.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceEducateCampusSchoolcardQueryResponse, self).parse_response_content(response_content)
        if 'school_card_list' in response:
            self.school_card_list = response['school_card_list']
