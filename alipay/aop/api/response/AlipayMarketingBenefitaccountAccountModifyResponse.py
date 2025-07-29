#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.BenefitAccountFsFundInfoDTO import BenefitAccountFsFundInfoDTO
from alipay.aop.api.domain.FsFundRelationGroupDTO import FsFundRelationGroupDTO


class AlipayMarketingBenefitaccountAccountModifyResponse(AlipayResponse):

    def __init__(self):
        super(AlipayMarketingBenefitaccountAccountModifyResponse, self).__init__()
        self._benefit_account_no = None
        self._fund_infos = None
        self._fund_relation_groups = None

    @property
    def benefit_account_no(self):
        return self._benefit_account_no

    @benefit_account_no.setter
    def benefit_account_no(self, value):
        self._benefit_account_no = value
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
    def fund_relation_groups(self):
        return self._fund_relation_groups

    @fund_relation_groups.setter
    def fund_relation_groups(self, value):
        if isinstance(value, FsFundRelationGroupDTO):
            self._fund_relation_groups = value
        else:
            self._fund_relation_groups = FsFundRelationGroupDTO.from_alipay_dict(value)

    def parse_response_content(self, response_content):
        response = super(AlipayMarketingBenefitaccountAccountModifyResponse, self).parse_response_content(response_content)
        if 'benefit_account_no' in response:
            self.benefit_account_no = response['benefit_account_no']
        if 'fund_infos' in response:
            self.fund_infos = response['fund_infos']
        if 'fund_relation_groups' in response:
            self.fund_relation_groups = response['fund_relation_groups']
