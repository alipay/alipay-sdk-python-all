#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.SchoolInfo import SchoolInfo


class AlipayCommerceEducateCampusSchoolQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceEducateCampusSchoolQueryResponse, self).__init__()
        self._school_info = None

    @property
    def school_info(self):
        return self._school_info

    @school_info.setter
    def school_info(self, value):
        if isinstance(value, list):
            self._school_info = list()
            for i in value:
                if isinstance(i, SchoolInfo):
                    self._school_info.append(i)
                else:
                    self._school_info.append(SchoolInfo.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceEducateCampusSchoolQueryResponse, self).parse_response_content(response_content)
        if 'school_info' in response:
            self.school_info = response['school_info']
