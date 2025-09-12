#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.HonorOverdueInfoDTO import HonorOverdueInfoDTO
from alipay.aop.api.domain.HonorProductInfoDTO import HonorProductInfoDTO
from alipay.aop.api.domain.HonorRepayInfoDTO import HonorRepayInfoDTO
from alipay.aop.api.domain.HonorTempLimitInfoDTO import HonorTempLimitInfoDTO


class AlipayPcreditLoanHonorAmountConsultResponse(AlipayResponse):

    def __init__(self):
        super(AlipayPcreditLoanHonorAmountConsultResponse, self).__init__()
        self._can_credit_change = None
        self._cancel_status = None
        self._cp_user_name = None
        self._grey_expire_time = None
        self._limit_type = None
        self._limit_use_err_desc = None
        self._limit_use_err_status = None
        self._max_loan = None
        self._min_loan = None
        self._overdue_info = None
        self._product_infos = None
        self._repay_day = None
        self._repay_info = None
        self._status = None
        self._temp_limit_info = None
        self._total_available_limit = None
        self._total_credit_limit = None

    @property
    def can_credit_change(self):
        return self._can_credit_change

    @can_credit_change.setter
    def can_credit_change(self, value):
        self._can_credit_change = value
    @property
    def cancel_status(self):
        return self._cancel_status

    @cancel_status.setter
    def cancel_status(self, value):
        self._cancel_status = value
    @property
    def cp_user_name(self):
        return self._cp_user_name

    @cp_user_name.setter
    def cp_user_name(self, value):
        self._cp_user_name = value
    @property
    def grey_expire_time(self):
        return self._grey_expire_time

    @grey_expire_time.setter
    def grey_expire_time(self, value):
        self._grey_expire_time = value
    @property
    def limit_type(self):
        return self._limit_type

    @limit_type.setter
    def limit_type(self, value):
        self._limit_type = value
    @property
    def limit_use_err_desc(self):
        return self._limit_use_err_desc

    @limit_use_err_desc.setter
    def limit_use_err_desc(self, value):
        self._limit_use_err_desc = value
    @property
    def limit_use_err_status(self):
        return self._limit_use_err_status

    @limit_use_err_status.setter
    def limit_use_err_status(self, value):
        self._limit_use_err_status = value
    @property
    def max_loan(self):
        return self._max_loan

    @max_loan.setter
    def max_loan(self, value):
        self._max_loan = value
    @property
    def min_loan(self):
        return self._min_loan

    @min_loan.setter
    def min_loan(self, value):
        self._min_loan = value
    @property
    def overdue_info(self):
        return self._overdue_info

    @overdue_info.setter
    def overdue_info(self, value):
        if isinstance(value, HonorOverdueInfoDTO):
            self._overdue_info = value
        else:
            self._overdue_info = HonorOverdueInfoDTO.from_alipay_dict(value)
    @property
    def product_infos(self):
        return self._product_infos

    @product_infos.setter
    def product_infos(self, value):
        if isinstance(value, list):
            self._product_infos = list()
            for i in value:
                if isinstance(i, HonorProductInfoDTO):
                    self._product_infos.append(i)
                else:
                    self._product_infos.append(HonorProductInfoDTO.from_alipay_dict(i))
    @property
    def repay_day(self):
        return self._repay_day

    @repay_day.setter
    def repay_day(self, value):
        self._repay_day = value
    @property
    def repay_info(self):
        return self._repay_info

    @repay_info.setter
    def repay_info(self, value):
        if isinstance(value, HonorRepayInfoDTO):
            self._repay_info = value
        else:
            self._repay_info = HonorRepayInfoDTO.from_alipay_dict(value)
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value
    @property
    def temp_limit_info(self):
        return self._temp_limit_info

    @temp_limit_info.setter
    def temp_limit_info(self, value):
        if isinstance(value, HonorTempLimitInfoDTO):
            self._temp_limit_info = value
        else:
            self._temp_limit_info = HonorTempLimitInfoDTO.from_alipay_dict(value)
    @property
    def total_available_limit(self):
        return self._total_available_limit

    @total_available_limit.setter
    def total_available_limit(self, value):
        self._total_available_limit = value
    @property
    def total_credit_limit(self):
        return self._total_credit_limit

    @total_credit_limit.setter
    def total_credit_limit(self, value):
        self._total_credit_limit = value

    def parse_response_content(self, response_content):
        response = super(AlipayPcreditLoanHonorAmountConsultResponse, self).parse_response_content(response_content)
        if 'can_credit_change' in response:
            self.can_credit_change = response['can_credit_change']
        if 'cancel_status' in response:
            self.cancel_status = response['cancel_status']
        if 'cp_user_name' in response:
            self.cp_user_name = response['cp_user_name']
        if 'grey_expire_time' in response:
            self.grey_expire_time = response['grey_expire_time']
        if 'limit_type' in response:
            self.limit_type = response['limit_type']
        if 'limit_use_err_desc' in response:
            self.limit_use_err_desc = response['limit_use_err_desc']
        if 'limit_use_err_status' in response:
            self.limit_use_err_status = response['limit_use_err_status']
        if 'max_loan' in response:
            self.max_loan = response['max_loan']
        if 'min_loan' in response:
            self.min_loan = response['min_loan']
        if 'overdue_info' in response:
            self.overdue_info = response['overdue_info']
        if 'product_infos' in response:
            self.product_infos = response['product_infos']
        if 'repay_day' in response:
            self.repay_day = response['repay_day']
        if 'repay_info' in response:
            self.repay_info = response['repay_info']
        if 'status' in response:
            self.status = response['status']
        if 'temp_limit_info' in response:
            self.temp_limit_info = response['temp_limit_info']
        if 'total_available_limit' in response:
            self.total_available_limit = response['total_available_limit']
        if 'total_credit_limit' in response:
            self.total_credit_limit = response['total_credit_limit']
