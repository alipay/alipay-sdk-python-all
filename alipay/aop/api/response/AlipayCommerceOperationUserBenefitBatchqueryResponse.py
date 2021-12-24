#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.UserBenefitInfo import UserBenefitInfo


class AlipayCommerceOperationUserBenefitBatchqueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceOperationUserBenefitBatchqueryResponse, self).__init__()
        self._page_num = None
        self._page_size = None
        self._total_size = None
        self._user_benefit_info_list = None

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
    def total_size(self):
        return self._total_size

    @total_size.setter
    def total_size(self, value):
        self._total_size = value
    @property
    def user_benefit_info_list(self):
        return self._user_benefit_info_list

    @user_benefit_info_list.setter
    def user_benefit_info_list(self, value):
        if isinstance(value, UserBenefitInfo):
            self._user_benefit_info_list = value
        else:
            self._user_benefit_info_list = UserBenefitInfo.from_alipay_dict(value)

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceOperationUserBenefitBatchqueryResponse, self).parse_response_content(response_content)
        if 'page_num' in response:
            self.page_num = response['page_num']
        if 'page_size' in response:
            self.page_size = response['page_size']
        if 'total_size' in response:
            self.total_size = response['total_size']
        if 'user_benefit_info_list' in response:
            self.user_benefit_info_list = response['user_benefit_info_list']
