#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.UniqueBizInfo import UniqueBizInfo


class AlipayCommerceMedicalServicepackageGrantbyphonenoCreateResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceMedicalServicepackageGrantbyphonenoCreateResponse, self).__init__()
        self._sub_unique_biz_info_list = None
        self._unique_biz_no = None

    @property
    def sub_unique_biz_info_list(self):
        return self._sub_unique_biz_info_list

    @sub_unique_biz_info_list.setter
    def sub_unique_biz_info_list(self, value):
        if isinstance(value, list):
            self._sub_unique_biz_info_list = list()
            for i in value:
                if isinstance(i, UniqueBizInfo):
                    self._sub_unique_biz_info_list.append(i)
                else:
                    self._sub_unique_biz_info_list.append(UniqueBizInfo.from_alipay_dict(i))
    @property
    def unique_biz_no(self):
        return self._unique_biz_no

    @unique_biz_no.setter
    def unique_biz_no(self, value):
        self._unique_biz_no = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceMedicalServicepackageGrantbyphonenoCreateResponse, self).parse_response_content(response_content)
        if 'sub_unique_biz_info_list' in response:
            self.sub_unique_biz_info_list = response['sub_unique_biz_info_list']
        if 'unique_biz_no' in response:
            self.unique_biz_no = response['unique_biz_no']
