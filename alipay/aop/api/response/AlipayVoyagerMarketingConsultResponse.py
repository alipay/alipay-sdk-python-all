#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.BenefitDisplayVO import BenefitDisplayVO
from alipay.aop.api.domain.BenefitDisplayVO import BenefitDisplayVO
from alipay.aop.api.domain.VoyagerPriceInfoDTO import VoyagerPriceInfoDTO
from alipay.aop.api.domain.ResultInfoDTO import ResultInfoDTO
from alipay.aop.api.domain.BenefitDisplayVO import BenefitDisplayVO


class AlipayVoyagerMarketingConsultResponse(AlipayResponse):

    def __init__(self):
        super(AlipayVoyagerMarketingConsultResponse, self).__init__()
        self._available_benefit_list = None
        self._best_benefit_list = None
        self._price_info_dto = None
        self._result = None
        self._selected_voucher_available = None
        self._un_available_benefit_list = None

    @property
    def available_benefit_list(self):
        return self._available_benefit_list

    @available_benefit_list.setter
    def available_benefit_list(self, value):
        if isinstance(value, list):
            self._available_benefit_list = list()
            for i in value:
                if isinstance(i, BenefitDisplayVO):
                    self._available_benefit_list.append(i)
                else:
                    self._available_benefit_list.append(BenefitDisplayVO.from_alipay_dict(i))
    @property
    def best_benefit_list(self):
        return self._best_benefit_list

    @best_benefit_list.setter
    def best_benefit_list(self, value):
        if isinstance(value, list):
            self._best_benefit_list = list()
            for i in value:
                if isinstance(i, BenefitDisplayVO):
                    self._best_benefit_list.append(i)
                else:
                    self._best_benefit_list.append(BenefitDisplayVO.from_alipay_dict(i))
    @property
    def price_info_dto(self):
        return self._price_info_dto

    @price_info_dto.setter
    def price_info_dto(self, value):
        if isinstance(value, VoyagerPriceInfoDTO):
            self._price_info_dto = value
        else:
            self._price_info_dto = VoyagerPriceInfoDTO.from_alipay_dict(value)
    @property
    def result(self):
        return self._result

    @result.setter
    def result(self, value):
        if isinstance(value, ResultInfoDTO):
            self._result = value
        else:
            self._result = ResultInfoDTO.from_alipay_dict(value)
    @property
    def selected_voucher_available(self):
        return self._selected_voucher_available

    @selected_voucher_available.setter
    def selected_voucher_available(self, value):
        self._selected_voucher_available = value
    @property
    def un_available_benefit_list(self):
        return self._un_available_benefit_list

    @un_available_benefit_list.setter
    def un_available_benefit_list(self, value):
        if isinstance(value, list):
            self._un_available_benefit_list = list()
            for i in value:
                if isinstance(i, BenefitDisplayVO):
                    self._un_available_benefit_list.append(i)
                else:
                    self._un_available_benefit_list.append(BenefitDisplayVO.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AlipayVoyagerMarketingConsultResponse, self).parse_response_content(response_content)
        if 'available_benefit_list' in response:
            self.available_benefit_list = response['available_benefit_list']
        if 'best_benefit_list' in response:
            self.best_benefit_list = response['best_benefit_list']
        if 'price_info_dto' in response:
            self.price_info_dto = response['price_info_dto']
        if 'result' in response:
            self.result = response['result']
        if 'selected_voucher_available' in response:
            self.selected_voucher_available = response['selected_voucher_available']
        if 'un_available_benefit_list' in response:
            self.un_available_benefit_list = response['un_available_benefit_list']
