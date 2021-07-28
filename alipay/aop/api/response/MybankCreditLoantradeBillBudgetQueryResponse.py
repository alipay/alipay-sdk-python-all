#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.BillRepayBudgetVO import BillRepayBudgetVO
from alipay.aop.api.domain.RefuseVo import RefuseVo


class MybankCreditLoantradeBillBudgetQueryResponse(AlipayResponse):

    def __init__(self):
        super(MybankCreditLoantradeBillBudgetQueryResponse, self).__init__()
        self._bill_repay_budget = None
        self._refuse_msg = None
        self._success = None

    @property
    def bill_repay_budget(self):
        return self._bill_repay_budget

    @bill_repay_budget.setter
    def bill_repay_budget(self, value):
        if isinstance(value, BillRepayBudgetVO):
            self._bill_repay_budget = value
        else:
            self._bill_repay_budget = BillRepayBudgetVO.from_alipay_dict(value)
    @property
    def refuse_msg(self):
        return self._refuse_msg

    @refuse_msg.setter
    def refuse_msg(self, value):
        if isinstance(value, RefuseVo):
            self._refuse_msg = value
        else:
            self._refuse_msg = RefuseVo.from_alipay_dict(value)
    @property
    def success(self):
        return self._success

    @success.setter
    def success(self, value):
        self._success = value

    def parse_response_content(self, response_content):
        response = super(MybankCreditLoantradeBillBudgetQueryResponse, self).parse_response_content(response_content)
        if 'bill_repay_budget' in response:
            self.bill_repay_budget = response['bill_repay_budget']
        if 'refuse_msg' in response:
            self.refuse_msg = response['refuse_msg']
        if 'success' in response:
            self.success = response['success']
