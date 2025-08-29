#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.EduSmActivityDTO import EduSmActivityDTO


class AlipayCommerceEducateSchooldeviceSmBatchqueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceEducateSchooldeviceSmBatchqueryResponse, self).__init__()
        self._edu_sm_activity_dto_list = None
        self._page_num = None
        self._page_size = None
        self._total_result_size = None

    @property
    def edu_sm_activity_dto_list(self):
        return self._edu_sm_activity_dto_list

    @edu_sm_activity_dto_list.setter
    def edu_sm_activity_dto_list(self, value):
        if isinstance(value, list):
            self._edu_sm_activity_dto_list = list()
            for i in value:
                if isinstance(i, EduSmActivityDTO):
                    self._edu_sm_activity_dto_list.append(i)
                else:
                    self._edu_sm_activity_dto_list.append(EduSmActivityDTO.from_alipay_dict(i))
    @property
    def page_num(self):
        return self._page_num

    @page_num.setter
    def page_num(self, value):
        self._page_num = value
    @property
    def page_size(self):
        return self._page_size

    @page_size.setter
    def page_size(self, value):
        self._page_size = value
    @property
    def total_result_size(self):
        return self._total_result_size

    @total_result_size.setter
    def total_result_size(self, value):
        self._total_result_size = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceEducateSchooldeviceSmBatchqueryResponse, self).parse_response_content(response_content)
        if 'edu_sm_activity_dto_list' in response:
            self.edu_sm_activity_dto_list = response['edu_sm_activity_dto_list']
        if 'page_num' in response:
            self.page_num = response['page_num']
        if 'page_size' in response:
            self.page_size = response['page_size']
        if 'total_result_size' in response:
            self.total_result_size = response['total_result_size']
