#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.BillDetailResult import BillDetailResult


class MybankCreditSupplychainWfBilldetailQueryResponse(AlipayResponse):

    def __init__(self):
        super(MybankCreditSupplychainWfBilldetailQueryResponse, self).__init__()
        self._billdetailresultlist = None
        self._pageindex = None
        self._pagesize = None
        self._totalnums = None

    @property
    def billdetailresultlist(self):
        return self._billdetailresultlist

    @billdetailresultlist.setter
    def billdetailresultlist(self, value):
        if isinstance(value, list):
            self._billdetailresultlist = list()
            for i in value:
                if isinstance(i, BillDetailResult):
                    self._billdetailresultlist.append(i)
                else:
                    self._billdetailresultlist.append(BillDetailResult.from_alipay_dict(i))
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
    def totalnums(self):
        return self._totalnums

    @totalnums.setter
    def totalnums(self, value):
        self._totalnums = value

    def parse_response_content(self, response_content):
        response = super(MybankCreditSupplychainWfBilldetailQueryResponse, self).parse_response_content(response_content)
        if 'billdetailresultlist' in response:
            self.billdetailresultlist = response['billdetailresultlist']
        if 'pageindex' in response:
            self.pageindex = response['pageindex']
        if 'pagesize' in response:
            self.pagesize = response['pagesize']
        if 'totalnums' in response:
            self.totalnums = response['totalnums']
