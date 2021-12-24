#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.MassifBaseInfo import MassifBaseInfo


class MybankCreditLoanapplyBkruralindustryMassifQueryResponse(AlipayResponse):

    def __init__(self):
        super(MybankCreditLoanapplyBkruralindustryMassifQueryResponse, self).__init__()
        self._massif_info_list = None

    @property
    def massif_info_list(self):
        return self._massif_info_list

    @massif_info_list.setter
    def massif_info_list(self, value):
        if isinstance(value, list):
            self._massif_info_list = list()
            for i in value:
                if isinstance(i, MassifBaseInfo):
                    self._massif_info_list.append(i)
                else:
                    self._massif_info_list.append(MassifBaseInfo.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(MybankCreditLoanapplyBkruralindustryMassifQueryResponse, self).parse_response_content(response_content)
        if 'massif_info_list' in response:
            self.massif_info_list = response['massif_info_list']
