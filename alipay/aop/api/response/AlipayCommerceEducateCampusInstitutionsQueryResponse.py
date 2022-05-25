#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.SchoolSimpleInfo import SchoolSimpleInfo
from alipay.aop.api.domain.SchoolBaseInfo import SchoolBaseInfo


class AlipayCommerceEducateCampusInstitutionsQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceEducateCampusInstitutionsQueryResponse, self).__init__()
        self._school_info = None
        self._school_info_list = None

    @property
    def school_info(self):
        return self._school_info

    @school_info.setter
    def school_info(self, value):
        if isinstance(value, SchoolSimpleInfo):
            self._school_info = value
        else:
            self._school_info = SchoolSimpleInfo.from_alipay_dict(value)
    @property
    def school_info_list(self):
        return self._school_info_list

    @school_info_list.setter
    def school_info_list(self, value):
        if isinstance(value, list):
            self._school_info_list = list()
            for i in value:
                if isinstance(i, SchoolBaseInfo):
                    self._school_info_list.append(i)
                else:
                    self._school_info_list.append(SchoolBaseInfo.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceEducateCampusInstitutionsQueryResponse, self).parse_response_content(response_content)
        if 'school_info' in response:
            self.school_info = response['school_info']
        if 'school_info_list' in response:
            self.school_info_list = response['school_info_list']
