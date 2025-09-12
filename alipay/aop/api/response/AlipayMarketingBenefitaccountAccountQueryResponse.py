#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.BenefitAccountFsFundInfoDTO import BenefitAccountFsFundInfoDTO
from alipay.aop.api.domain.BenefitAccountFundPreAuthInfoDTO import BenefitAccountFundPreAuthInfoDTO
from alipay.aop.api.domain.FsFundRelationGroupDTO import FsFundRelationGroupDTO


class AlipayMarketingBenefitaccountAccountQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayMarketingBenefitaccountAccountQueryResponse, self).__init__()
        self._benefit_account_no = None
        self._biz_identity = None
        self._current_amount = None
        self._effective_time = None
        self._expired_time = None
        self._fund_infos = None
        self._fund_pre_auth_info = None
        self._fund_relation_groups = None
        self._name = None
        self._out_card_no = None
        self._status = None
        self._total_amount = None

    @property
    def benefit_account_no(self):
        return self._benefit_account_no

    @benefit_account_no.setter
    def benefit_account_no(self, value):
        self._benefit_account_no = value
    @property
    def biz_identity(self):
        return self._biz_identity

    @biz_identity.setter
    def biz_identity(self, value):
        self._biz_identity = value
    @property
    def current_amount(self):
        return self._current_amount

    @current_amount.setter
    def current_amount(self, value):
        self._current_amount = value
    @property
    def effective_time(self):
        return self._effective_time

    @effective_time.setter
    def effective_time(self, value):
        self._effective_time = value
    @property
    def expired_time(self):
        return self._expired_time

    @expired_time.setter
    def expired_time(self, value):
        self._expired_time = value
    @property
    def fund_infos(self):
        return self._fund_infos

    @fund_infos.setter
    def fund_infos(self, value):
        if isinstance(value, list):
            self._fund_infos = list()
            for i in value:
                if isinstance(i, BenefitAccountFsFundInfoDTO):
                    self._fund_infos.append(i)
                else:
                    self._fund_infos.append(BenefitAccountFsFundInfoDTO.from_alipay_dict(i))
    @property
    def fund_pre_auth_info(self):
        return self._fund_pre_auth_info

    @fund_pre_auth_info.setter
    def fund_pre_auth_info(self, value):
        if isinstance(value, BenefitAccountFundPreAuthInfoDTO):
            self._fund_pre_auth_info = value
        else:
            self._fund_pre_auth_info = BenefitAccountFundPreAuthInfoDTO.from_alipay_dict(value)
    @property
    def fund_relation_groups(self):
        return self._fund_relation_groups

    @fund_relation_groups.setter
    def fund_relation_groups(self, value):
        if isinstance(value, list):
            self._fund_relation_groups = list()
            for i in value:
                if isinstance(i, FsFundRelationGroupDTO):
                    self._fund_relation_groups.append(i)
                else:
                    self._fund_relation_groups.append(FsFundRelationGroupDTO.from_alipay_dict(i))
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value
    @property
    def out_card_no(self):
        return self._out_card_no

    @out_card_no.setter
    def out_card_no(self, value):
        self._out_card_no = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value
    @property
    def total_amount(self):
        return self._total_amount

    @total_amount.setter
    def total_amount(self, value):
        self._total_amount = value

    def parse_response_content(self, response_content):
        response = super(AlipayMarketingBenefitaccountAccountQueryResponse, self).parse_response_content(response_content)
        if 'benefit_account_no' in response:
            self.benefit_account_no = response['benefit_account_no']
        if 'biz_identity' in response:
            self.biz_identity = response['biz_identity']
        if 'current_amount' in response:
            self.current_amount = response['current_amount']
        if 'effective_time' in response:
            self.effective_time = response['effective_time']
        if 'expired_time' in response:
            self.expired_time = response['expired_time']
        if 'fund_infos' in response:
            self.fund_infos = response['fund_infos']
        if 'fund_pre_auth_info' in response:
            self.fund_pre_auth_info = response['fund_pre_auth_info']
        if 'fund_relation_groups' in response:
            self.fund_relation_groups = response['fund_relation_groups']
        if 'name' in response:
            self.name = response['name']
        if 'out_card_no' in response:
            self.out_card_no = response['out_card_no']
        if 'status' in response:
            self.status = response['status']
        if 'total_amount' in response:
            self.total_amount = response['total_amount']
