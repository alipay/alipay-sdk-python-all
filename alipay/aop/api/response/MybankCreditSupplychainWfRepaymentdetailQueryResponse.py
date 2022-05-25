#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.RepayRecordVO import RepayRecordVO


class MybankCreditSupplychainWfRepaymentdetailQueryResponse(AlipayResponse):

    def __init__(self):
        super(MybankCreditSupplychainWfRepaymentdetailQueryResponse, self).__init__()
        self._pageindex = None
        self._pagesize = None
        self._repayrecord = None
        self._totalnums = None

    @property
    def pageindex(self):
        return self._pageindex

    @pageindex.setter
    def pageindex(self, value):
        self._pageindex = value
    @property
    def pagesize(self):
        return self._pagesize

    @pagesize.setter
    def pagesize(self, value):
        self._pagesize = value
    @property
    def repayrecord(self):
        return self._repayrecord

    @repayrecord.setter
    def repayrecord(self, value):
        if isinstance(value, list):
            self._repayrecord = list()
            for i in value:
                if isinstance(i, RepayRecordVO):
                    self._repayrecord.append(i)
                else:
                    self._repayrecord.append(RepayRecordVO.from_alipay_dict(i))
    @property
    def totalnums(self):
        return self._totalnums

    @totalnums.setter
    def totalnums(self, value):
        self._totalnums = value

    def parse_response_content(self, response_content):
        response = super(MybankCreditSupplychainWfRepaymentdetailQueryResponse, self).parse_response_content(response_content)
        if 'pageindex' in response:
            self.pageindex = response['pageindex']
        if 'pagesize' in response:
            self.pagesize = response['pagesize']
        if 'repayrecord' in response:
            self.repayrecord = response['repayrecord']
        if 'totalnums' in response:
            self.totalnums = response['totalnums']
