#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.ExaminationCategoryInfo import ExaminationCategoryInfo


class AlipayCommerceMedicalExaminationCategorylistQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceMedicalExaminationCategorylistQueryResponse, self).__init__()
        self._category_info_list = None

    @property
    def category_info_list(self):
        return self._category_info_list

    @category_info_list.setter
    def category_info_list(self, value):
        if isinstance(value, list):
            self._category_info_list = list()
            for i in value:
                if isinstance(i, ExaminationCategoryInfo):
                    self._category_info_list.append(i)
                else:
                    self._category_info_list.append(ExaminationCategoryInfo.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceMedicalExaminationCategorylistQueryResponse, self).parse_response_content(response_content)
        if 'category_info_list' in response:
            self.category_info_list = response['category_info_list']
