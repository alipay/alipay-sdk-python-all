#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.IncomeDistributionOrderTransInDetail import IncomeDistributionOrderTransInDetail


class AnttechBlockchainFinanceDistributionBillQueryResponse(AlipayResponse):

    def __init__(self):
        super(AnttechBlockchainFinanceDistributionBillQueryResponse, self).__init__()
        self._amount = None
        self._distribution_order_id = None
        self._distribution_rule_id = None
        self._statement_no = None
        self._status = None
        self._trade_id = None
        self._trans_in_detail_list = None
        self._trans_out_account_no = None
        self._trans_out_account_type = None
        self._trans_out_name = None
        self._write_off_biz_no = None

    @property
    def amount(self):
        return self._amount

    @amount.setter
    def amount(self, value):
        self._amount = value
    @property
    def distribution_order_id(self):
        return self._distribution_order_id

    @distribution_order_id.setter
    def distribution_order_id(self, value):
        self._distribution_order_id = value
    @property
    def distribution_rule_id(self):
        return self._distribution_rule_id

    @distribution_rule_id.setter
    def distribution_rule_id(self, value):
        self._distribution_rule_id = value
    @property
    def statement_no(self):
        return self._statement_no

    @statement_no.setter
    def statement_no(self, value):
        self._statement_no = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value
    @property
    def trade_id(self):
        return self._trade_id

    @trade_id.setter
    def trade_id(self, value):
        self._trade_id = value
    @property
    def trans_in_detail_list(self):
        return self._trans_in_detail_list

    @trans_in_detail_list.setter
    def trans_in_detail_list(self, value):
        if isinstance(value, list):
            self._trans_in_detail_list = list()
            for i in value:
                if isinstance(i, IncomeDistributionOrderTransInDetail):
                    self._trans_in_detail_list.append(i)
                else:
                    self._trans_in_detail_list.append(IncomeDistributionOrderTransInDetail.from_alipay_dict(i))
    @property
    def trans_out_account_no(self):
        return self._trans_out_account_no

    @trans_out_account_no.setter
    def trans_out_account_no(self, value):
        self._trans_out_account_no = value
    @property
    def trans_out_account_type(self):
        return self._trans_out_account_type

    @trans_out_account_type.setter
    def trans_out_account_type(self, value):
        self._trans_out_account_type = value
    @property
    def trans_out_name(self):
        return self._trans_out_name

    @trans_out_name.setter
    def trans_out_name(self, value):
        self._trans_out_name = value
    @property
    def write_off_biz_no(self):
        return self._write_off_biz_no

    @write_off_biz_no.setter
    def write_off_biz_no(self, value):
        self._write_off_biz_no = value

    def parse_response_content(self, response_content):
        response = super(AnttechBlockchainFinanceDistributionBillQueryResponse, self).parse_response_content(response_content)
        if 'amount' in response:
            self.amount = response['amount']
        if 'distribution_order_id' in response:
            self.distribution_order_id = response['distribution_order_id']
        if 'distribution_rule_id' in response:
            self.distribution_rule_id = response['distribution_rule_id']
        if 'statement_no' in response:
            self.statement_no = response['statement_no']
        if 'status' in response:
            self.status = response['status']
        if 'trade_id' in response:
            self.trade_id = response['trade_id']
        if 'trans_in_detail_list' in response:
            self.trans_in_detail_list = response['trans_in_detail_list']
        if 'trans_out_account_no' in response:
            self.trans_out_account_no = response['trans_out_account_no']
        if 'trans_out_account_type' in response:
            self.trans_out_account_type = response['trans_out_account_type']
        if 'trans_out_name' in response:
            self.trans_out_name = response['trans_out_name']
        if 'write_off_biz_no' in response:
            self.write_off_biz_no = response['write_off_biz_no']
