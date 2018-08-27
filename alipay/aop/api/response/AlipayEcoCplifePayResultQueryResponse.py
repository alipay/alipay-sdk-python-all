#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.TradeAssocBillDetails import TradeAssocBillDetails
from alipay.aop.api.domain.FundBillListEco import FundBillListEco


class AlipayEcoCplifePayResultQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayEcoCplifePayResultQueryResponse, self).__init__()
        self._assoc_bill_details = None
        self._biz_entity_id = None
        self._biz_type = None
        self._buyer_logon_id = None
        self._buyer_user_id = None
        self._fund_bill_list = None
        self._gmt_payment = None
        self._seller_id = None
        self._total_amount = None
        self._trade_no = None
        self._trade_status = None

    @property
    def assoc_bill_details(self):
        return self._assoc_bill_details

    @assoc_bill_details.setter
    def assoc_bill_details(self, value):
        if isinstance(value, TradeAssocBillDetails):
            self._assoc_bill_details = value
        else:
            self._assoc_bill_details = TradeAssocBillDetails.from_alipay_dict(value)
    @property
    def biz_entity_id(self):
        return self._biz_entity_id

    @biz_entity_id.setter
    def biz_entity_id(self, value):
        self._biz_entity_id = value
    @property
    def biz_type(self):
        return self._biz_type

    @biz_type.setter
    def biz_type(self, value):
        self._biz_type = value
    @property
    def buyer_logon_id(self):
        return self._buyer_logon_id

    @buyer_logon_id.setter
    def buyer_logon_id(self, value):
        self._buyer_logon_id = value
    @property
    def buyer_user_id(self):
        return self._buyer_user_id

    @buyer_user_id.setter
    def buyer_user_id(self, value):
        self._buyer_user_id = value
    @property
    def fund_bill_list(self):
        return self._fund_bill_list

    @fund_bill_list.setter
    def fund_bill_list(self, value):
        if isinstance(value, FundBillListEco):
            self._fund_bill_list = value
        else:
            self._fund_bill_list = FundBillListEco.from_alipay_dict(value)
    @property
    def gmt_payment(self):
        return self._gmt_payment

    @gmt_payment.setter
    def gmt_payment(self, value):
        self._gmt_payment = value
    @property
    def seller_id(self):
        return self._seller_id

    @seller_id.setter
    def seller_id(self, value):
        self._seller_id = value
    @property
    def total_amount(self):
        return self._total_amount

    @total_amount.setter
    def total_amount(self, value):
        self._total_amount = value
    @property
    def trade_no(self):
        return self._trade_no

    @trade_no.setter
    def trade_no(self, value):
        self._trade_no = value
    @property
    def trade_status(self):
        return self._trade_status

    @trade_status.setter
    def trade_status(self, value):
        self._trade_status = value

    def parse_response_content(self, response_content):
        response = super(AlipayEcoCplifePayResultQueryResponse, self).parse_response_content(response_content)
        if 'assoc_bill_details' in response:
            self.assoc_bill_details = response['assoc_bill_details']
        if 'biz_entity_id' in response:
            self.biz_entity_id = response['biz_entity_id']
        if 'biz_type' in response:
            self.biz_type = response['biz_type']
        if 'buyer_logon_id' in response:
            self.buyer_logon_id = response['buyer_logon_id']
        if 'buyer_user_id' in response:
            self.buyer_user_id = response['buyer_user_id']
        if 'fund_bill_list' in response:
            self.fund_bill_list = response['fund_bill_list']
        if 'gmt_payment' in response:
            self.gmt_payment = response['gmt_payment']
        if 'seller_id' in response:
            self.seller_id = response['seller_id']
        if 'total_amount' in response:
            self.total_amount = response['total_amount']
        if 'trade_no' in response:
            self.trade_no = response['trade_no']
        if 'trade_status' in response:
            self.trade_status = response['trade_status']
