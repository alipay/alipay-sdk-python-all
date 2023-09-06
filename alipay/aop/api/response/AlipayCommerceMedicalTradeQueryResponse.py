#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.SubsidyAmountParam import SubsidyAmountParam


class AlipayCommerceMedicalTradeQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceMedicalTradeQueryResponse, self).__init__()
        self._account_amount = None
        self._alipay_trade_no = None
        self._bank_id = None
        self._bank_name = None
        self._bank_order_id = None
        self._chrg_bch_no = None
        self._gmt_medical_paid = None
        self._gmt_out_create = None
        self._gmt_own_paid = None
        self._gmt_refund = None
        self._gov_amount = None
        self._med_org_ord = None
        self._medical_pay_msg = None
        self._medical_pay_status = None
        self._nathsa_direct_url = None
        self._order_type = None
        self._org_no = None
        self._other_amount = None
        self._out_trade_no = None
        self._own_pay_msg = None
        self._own_pay_status = None
        self._pay_order_id = None
        self._real_amount = None
        self._refund_amount = None
        self._rels_pay_flag = None
        self._rels_pay_user_name = None
        self._remark = None
        self._request_content = None
        self._response_content = None
        self._shop_id = None
        self._store_id = None
        self._subject = None
        self._subsidy_amount_params = None
        self._total_amount = None
        self._trade_no = None
        self._trade_status = None

    @property
    def account_amount(self):
        return self._account_amount

    @account_amount.setter
    def account_amount(self, value):
        self._account_amount = value
    @property
    def alipay_trade_no(self):
        return self._alipay_trade_no

    @alipay_trade_no.setter
    def alipay_trade_no(self, value):
        self._alipay_trade_no = value
    @property
    def bank_id(self):
        return self._bank_id

    @bank_id.setter
    def bank_id(self, value):
        self._bank_id = value
    @property
    def bank_name(self):
        return self._bank_name

    @bank_name.setter
    def bank_name(self, value):
        self._bank_name = value
    @property
    def bank_order_id(self):
        return self._bank_order_id

    @bank_order_id.setter
    def bank_order_id(self, value):
        self._bank_order_id = value
    @property
    def chrg_bch_no(self):
        return self._chrg_bch_no

    @chrg_bch_no.setter
    def chrg_bch_no(self, value):
        self._chrg_bch_no = value
    @property
    def gmt_medical_paid(self):
        return self._gmt_medical_paid

    @gmt_medical_paid.setter
    def gmt_medical_paid(self, value):
        self._gmt_medical_paid = value
    @property
    def gmt_out_create(self):
        return self._gmt_out_create

    @gmt_out_create.setter
    def gmt_out_create(self, value):
        self._gmt_out_create = value
    @property
    def gmt_own_paid(self):
        return self._gmt_own_paid

    @gmt_own_paid.setter
    def gmt_own_paid(self, value):
        self._gmt_own_paid = value
    @property
    def gmt_refund(self):
        return self._gmt_refund

    @gmt_refund.setter
    def gmt_refund(self, value):
        self._gmt_refund = value
    @property
    def gov_amount(self):
        return self._gov_amount

    @gov_amount.setter
    def gov_amount(self, value):
        self._gov_amount = value
    @property
    def med_org_ord(self):
        return self._med_org_ord

    @med_org_ord.setter
    def med_org_ord(self, value):
        self._med_org_ord = value
    @property
    def medical_pay_msg(self):
        return self._medical_pay_msg

    @medical_pay_msg.setter
    def medical_pay_msg(self, value):
        self._medical_pay_msg = value
    @property
    def medical_pay_status(self):
        return self._medical_pay_status

    @medical_pay_status.setter
    def medical_pay_status(self, value):
        self._medical_pay_status = value
    @property
    def nathsa_direct_url(self):
        return self._nathsa_direct_url

    @nathsa_direct_url.setter
    def nathsa_direct_url(self, value):
        self._nathsa_direct_url = value
    @property
    def order_type(self):
        return self._order_type

    @order_type.setter
    def order_type(self, value):
        self._order_type = value
    @property
    def org_no(self):
        return self._org_no

    @org_no.setter
    def org_no(self, value):
        self._org_no = value
    @property
    def other_amount(self):
        return self._other_amount

    @other_amount.setter
    def other_amount(self, value):
        self._other_amount = value
    @property
    def out_trade_no(self):
        return self._out_trade_no

    @out_trade_no.setter
    def out_trade_no(self, value):
        self._out_trade_no = value
    @property
    def own_pay_msg(self):
        return self._own_pay_msg

    @own_pay_msg.setter
    def own_pay_msg(self, value):
        self._own_pay_msg = value
    @property
    def own_pay_status(self):
        return self._own_pay_status

    @own_pay_status.setter
    def own_pay_status(self, value):
        self._own_pay_status = value
    @property
    def pay_order_id(self):
        return self._pay_order_id

    @pay_order_id.setter
    def pay_order_id(self, value):
        self._pay_order_id = value
    @property
    def real_amount(self):
        return self._real_amount

    @real_amount.setter
    def real_amount(self, value):
        self._real_amount = value
    @property
    def refund_amount(self):
        return self._refund_amount

    @refund_amount.setter
    def refund_amount(self, value):
        self._refund_amount = value
    @property
    def rels_pay_flag(self):
        return self._rels_pay_flag

    @rels_pay_flag.setter
    def rels_pay_flag(self, value):
        self._rels_pay_flag = value
    @property
    def rels_pay_user_name(self):
        return self._rels_pay_user_name

    @rels_pay_user_name.setter
    def rels_pay_user_name(self, value):
        self._rels_pay_user_name = value
    @property
    def remark(self):
        return self._remark

    @remark.setter
    def remark(self, value):
        self._remark = value
    @property
    def request_content(self):
        return self._request_content

    @request_content.setter
    def request_content(self, value):
        self._request_content = value
    @property
    def response_content(self):
        return self._response_content

    @response_content.setter
    def response_content(self, value):
        self._response_content = value
    @property
    def shop_id(self):
        return self._shop_id

    @shop_id.setter
    def shop_id(self, value):
        self._shop_id = value
    @property
    def store_id(self):
        return self._store_id

    @store_id.setter
    def store_id(self, value):
        self._store_id = value
    @property
    def subject(self):
        return self._subject

    @subject.setter
    def subject(self, value):
        self._subject = value
    @property
    def subsidy_amount_params(self):
        return self._subsidy_amount_params

    @subsidy_amount_params.setter
    def subsidy_amount_params(self, value):
        if isinstance(value, list):
            self._subsidy_amount_params = list()
            for i in value:
                if isinstance(i, SubsidyAmountParam):
                    self._subsidy_amount_params.append(i)
                else:
                    self._subsidy_amount_params.append(SubsidyAmountParam.from_alipay_dict(i))
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
        response = super(AlipayCommerceMedicalTradeQueryResponse, self).parse_response_content(response_content)
        if 'account_amount' in response:
            self.account_amount = response['account_amount']
        if 'alipay_trade_no' in response:
            self.alipay_trade_no = response['alipay_trade_no']
        if 'bank_id' in response:
            self.bank_id = response['bank_id']
        if 'bank_name' in response:
            self.bank_name = response['bank_name']
        if 'bank_order_id' in response:
            self.bank_order_id = response['bank_order_id']
        if 'chrg_bch_no' in response:
            self.chrg_bch_no = response['chrg_bch_no']
        if 'gmt_medical_paid' in response:
            self.gmt_medical_paid = response['gmt_medical_paid']
        if 'gmt_out_create' in response:
            self.gmt_out_create = response['gmt_out_create']
        if 'gmt_own_paid' in response:
            self.gmt_own_paid = response['gmt_own_paid']
        if 'gmt_refund' in response:
            self.gmt_refund = response['gmt_refund']
        if 'gov_amount' in response:
            self.gov_amount = response['gov_amount']
        if 'med_org_ord' in response:
            self.med_org_ord = response['med_org_ord']
        if 'medical_pay_msg' in response:
            self.medical_pay_msg = response['medical_pay_msg']
        if 'medical_pay_status' in response:
            self.medical_pay_status = response['medical_pay_status']
        if 'nathsa_direct_url' in response:
            self.nathsa_direct_url = response['nathsa_direct_url']
        if 'order_type' in response:
            self.order_type = response['order_type']
        if 'org_no' in response:
            self.org_no = response['org_no']
        if 'other_amount' in response:
            self.other_amount = response['other_amount']
        if 'out_trade_no' in response:
            self.out_trade_no = response['out_trade_no']
        if 'own_pay_msg' in response:
            self.own_pay_msg = response['own_pay_msg']
        if 'own_pay_status' in response:
            self.own_pay_status = response['own_pay_status']
        if 'pay_order_id' in response:
            self.pay_order_id = response['pay_order_id']
        if 'real_amount' in response:
            self.real_amount = response['real_amount']
        if 'refund_amount' in response:
            self.refund_amount = response['refund_amount']
        if 'rels_pay_flag' in response:
            self.rels_pay_flag = response['rels_pay_flag']
        if 'rels_pay_user_name' in response:
            self.rels_pay_user_name = response['rels_pay_user_name']
        if 'remark' in response:
            self.remark = response['remark']
        if 'request_content' in response:
            self.request_content = response['request_content']
        if 'response_content' in response:
            self.response_content = response['response_content']
        if 'shop_id' in response:
            self.shop_id = response['shop_id']
        if 'store_id' in response:
            self.store_id = response['store_id']
        if 'subject' in response:
            self.subject = response['subject']
        if 'subsidy_amount_params' in response:
            self.subsidy_amount_params = response['subsidy_amount_params']
        if 'total_amount' in response:
            self.total_amount = response['total_amount']
        if 'trade_no' in response:
            self.trade_no = response['trade_no']
        if 'trade_status' in response:
            self.trade_status = response['trade_status']
