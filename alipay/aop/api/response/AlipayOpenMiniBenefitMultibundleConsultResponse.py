#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.OpBenefitDataVO import OpBenefitDataVO


class AlipayOpenMiniBenefitMultibundleConsultResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOpenMiniBenefitMultibundleConsultResponse, self).__init__()
        self._op_benefit_data_list = None
        self._page_num = None
        self._page_size = None
        self._total = None

    @property
    def op_benefit_data_list(self):
        return self._op_benefit_data_list

    @op_benefit_data_list.setter
    def op_benefit_data_list(self, value):
        if isinstance(value, list):
            self._op_benefit_data_list = list()
            for i in value:
                if isinstance(i, OpBenefitDataVO):
                    self._op_benefit_data_list.append(i)
                else:
                    self._op_benefit_data_list.append(OpBenefitDataVO.from_alipay_dict(i))
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
    def total(self):
        return self._total

    @total.setter
    def total(self, value):
        self._total = value

    def parse_response_content(self, response_content):
        response = super(AlipayOpenMiniBenefitMultibundleConsultResponse, self).parse_response_content(response_content)
        if 'op_benefit_data_list' in response:
            self.op_benefit_data_list = response['op_benefit_data_list']
        if 'page_num' in response:
            self.page_num = response['page_num']
        if 'page_size' in response:
            self.page_size = response['page_size']
        if 'total' in response:
            self.total = response['total']
