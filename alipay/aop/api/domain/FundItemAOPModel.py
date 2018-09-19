#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class FundItemAOPModel(object):

    def __init__(self):
        self._acctrans_out_biz_no = None
        self._amount = None
        self._assert_type_code = None
        self._bank_card_pay_type = None
        self._bank_card_type = None
        self._biz_id = None
        self._biz_in_no = None
        self._biz_out_no = None
        self._biz_type = None
        self._currency = None
        self._dback_amount = None
        self._dback_gmt_create = None
        self._dback_gmt_est_bk_ack = None
        self._dback_gmt_est_bk_into = None
        self._dback_inst_account_name = None
        self._dback_inst_account_no = None
        self._dback_inst_id = None
        self._dback_inst_name = None
        self._fid = None
        self._fund_access_type = None
        self._fund_account_no = None
        self._fund_biz_type = None
        self._fund_create_time = None
        self._fund_finish_time = None
        self._fund_in_out = None
        self._fund_inst_id = None
        self._fund_modify_time = None
        self._fund_status = None
        self._fund_tool_belong_to_crowner = None
        self._fund_tool_owner_card_no = None
        self._fund_tool_type_for_crowner = None
        self._fund_tool_type_for_system = None
        self._fund_tool_type_name = None
        self._gmt_biz_create = None
        self._open_self_slip_type = None
        self._opposite_biz_card_alias = None
        self._opposite_biz_card_no = None
        self._opposite_fund_card_no = None
        self._out_request_no = None
        self._owner_card_no = None
        self._refund_bank_status = None
        self._slip_amount = None
        self._slip_id = None
        self._slip_status = None
        self._sub_prepaid_card_type = None
        self._uid = None

    @property
    def acctrans_out_biz_no(self):
        return self._acctrans_out_biz_no

    @acctrans_out_biz_no.setter
    def acctrans_out_biz_no(self, value):
        self._acctrans_out_biz_no = value
    @property
    def amount(self):
        return self._amount

    @amount.setter
    def amount(self, value):
        self._amount = value
    @property
    def assert_type_code(self):
        return self._assert_type_code

    @assert_type_code.setter
    def assert_type_code(self, value):
        self._assert_type_code = value
    @property
    def bank_card_pay_type(self):
        return self._bank_card_pay_type

    @bank_card_pay_type.setter
    def bank_card_pay_type(self, value):
        self._bank_card_pay_type = value
    @property
    def bank_card_type(self):
        return self._bank_card_type

    @bank_card_type.setter
    def bank_card_type(self, value):
        self._bank_card_type = value
    @property
    def biz_id(self):
        return self._biz_id

    @biz_id.setter
    def biz_id(self, value):
        self._biz_id = value
    @property
    def biz_in_no(self):
        return self._biz_in_no

    @biz_in_no.setter
    def biz_in_no(self, value):
        self._biz_in_no = value
    @property
    def biz_out_no(self):
        return self._biz_out_no

    @biz_out_no.setter
    def biz_out_no(self, value):
        self._biz_out_no = value
    @property
    def biz_type(self):
        return self._biz_type

    @biz_type.setter
    def biz_type(self, value):
        self._biz_type = value
    @property
    def currency(self):
        return self._currency

    @currency.setter
    def currency(self, value):
        self._currency = value
    @property
    def dback_amount(self):
        return self._dback_amount

    @dback_amount.setter
    def dback_amount(self, value):
        self._dback_amount = value
    @property
    def dback_gmt_create(self):
        return self._dback_gmt_create

    @dback_gmt_create.setter
    def dback_gmt_create(self, value):
        self._dback_gmt_create = value
    @property
    def dback_gmt_est_bk_ack(self):
        return self._dback_gmt_est_bk_ack

    @dback_gmt_est_bk_ack.setter
    def dback_gmt_est_bk_ack(self, value):
        self._dback_gmt_est_bk_ack = value
    @property
    def dback_gmt_est_bk_into(self):
        return self._dback_gmt_est_bk_into

    @dback_gmt_est_bk_into.setter
    def dback_gmt_est_bk_into(self, value):
        self._dback_gmt_est_bk_into = value
    @property
    def dback_inst_account_name(self):
        return self._dback_inst_account_name

    @dback_inst_account_name.setter
    def dback_inst_account_name(self, value):
        self._dback_inst_account_name = value
    @property
    def dback_inst_account_no(self):
        return self._dback_inst_account_no

    @dback_inst_account_no.setter
    def dback_inst_account_no(self, value):
        self._dback_inst_account_no = value
    @property
    def dback_inst_id(self):
        return self._dback_inst_id

    @dback_inst_id.setter
    def dback_inst_id(self, value):
        self._dback_inst_id = value
    @property
    def dback_inst_name(self):
        return self._dback_inst_name

    @dback_inst_name.setter
    def dback_inst_name(self, value):
        self._dback_inst_name = value
    @property
    def fid(self):
        return self._fid

    @fid.setter
    def fid(self, value):
        self._fid = value
    @property
    def fund_access_type(self):
        return self._fund_access_type

    @fund_access_type.setter
    def fund_access_type(self, value):
        self._fund_access_type = value
    @property
    def fund_account_no(self):
        return self._fund_account_no

    @fund_account_no.setter
    def fund_account_no(self, value):
        self._fund_account_no = value
    @property
    def fund_biz_type(self):
        return self._fund_biz_type

    @fund_biz_type.setter
    def fund_biz_type(self, value):
        self._fund_biz_type = value
    @property
    def fund_create_time(self):
        return self._fund_create_time

    @fund_create_time.setter
    def fund_create_time(self, value):
        self._fund_create_time = value
    @property
    def fund_finish_time(self):
        return self._fund_finish_time

    @fund_finish_time.setter
    def fund_finish_time(self, value):
        self._fund_finish_time = value
    @property
    def fund_in_out(self):
        return self._fund_in_out

    @fund_in_out.setter
    def fund_in_out(self, value):
        self._fund_in_out = value
    @property
    def fund_inst_id(self):
        return self._fund_inst_id

    @fund_inst_id.setter
    def fund_inst_id(self, value):
        self._fund_inst_id = value
    @property
    def fund_modify_time(self):
        return self._fund_modify_time

    @fund_modify_time.setter
    def fund_modify_time(self, value):
        self._fund_modify_time = value
    @property
    def fund_status(self):
        return self._fund_status

    @fund_status.setter
    def fund_status(self, value):
        self._fund_status = value
    @property
    def fund_tool_belong_to_crowner(self):
        return self._fund_tool_belong_to_crowner

    @fund_tool_belong_to_crowner.setter
    def fund_tool_belong_to_crowner(self, value):
        self._fund_tool_belong_to_crowner = value
    @property
    def fund_tool_owner_card_no(self):
        return self._fund_tool_owner_card_no

    @fund_tool_owner_card_no.setter
    def fund_tool_owner_card_no(self, value):
        self._fund_tool_owner_card_no = value
    @property
    def fund_tool_type_for_crowner(self):
        return self._fund_tool_type_for_crowner

    @fund_tool_type_for_crowner.setter
    def fund_tool_type_for_crowner(self, value):
        self._fund_tool_type_for_crowner = value
    @property
    def fund_tool_type_for_system(self):
        return self._fund_tool_type_for_system

    @fund_tool_type_for_system.setter
    def fund_tool_type_for_system(self, value):
        self._fund_tool_type_for_system = value
    @property
    def fund_tool_type_name(self):
        return self._fund_tool_type_name

    @fund_tool_type_name.setter
    def fund_tool_type_name(self, value):
        self._fund_tool_type_name = value
    @property
    def gmt_biz_create(self):
        return self._gmt_biz_create

    @gmt_biz_create.setter
    def gmt_biz_create(self, value):
        self._gmt_biz_create = value
    @property
    def open_self_slip_type(self):
        return self._open_self_slip_type

    @open_self_slip_type.setter
    def open_self_slip_type(self, value):
        self._open_self_slip_type = value
    @property
    def opposite_biz_card_alias(self):
        return self._opposite_biz_card_alias

    @opposite_biz_card_alias.setter
    def opposite_biz_card_alias(self, value):
        self._opposite_biz_card_alias = value
    @property
    def opposite_biz_card_no(self):
        return self._opposite_biz_card_no

    @opposite_biz_card_no.setter
    def opposite_biz_card_no(self, value):
        self._opposite_biz_card_no = value
    @property
    def opposite_fund_card_no(self):
        return self._opposite_fund_card_no

    @opposite_fund_card_no.setter
    def opposite_fund_card_no(self, value):
        self._opposite_fund_card_no = value
    @property
    def out_request_no(self):
        return self._out_request_no

    @out_request_no.setter
    def out_request_no(self, value):
        self._out_request_no = value
    @property
    def owner_card_no(self):
        return self._owner_card_no

    @owner_card_no.setter
    def owner_card_no(self, value):
        self._owner_card_no = value
    @property
    def refund_bank_status(self):
        return self._refund_bank_status

    @refund_bank_status.setter
    def refund_bank_status(self, value):
        self._refund_bank_status = value
    @property
    def slip_amount(self):
        return self._slip_amount

    @slip_amount.setter
    def slip_amount(self, value):
        self._slip_amount = value
    @property
    def slip_id(self):
        return self._slip_id

    @slip_id.setter
    def slip_id(self, value):
        self._slip_id = value
    @property
    def slip_status(self):
        return self._slip_status

    @slip_status.setter
    def slip_status(self, value):
        self._slip_status = value
    @property
    def sub_prepaid_card_type(self):
        return self._sub_prepaid_card_type

    @sub_prepaid_card_type.setter
    def sub_prepaid_card_type(self, value):
        self._sub_prepaid_card_type = value
    @property
    def uid(self):
        return self._uid

    @uid.setter
    def uid(self, value):
        self._uid = value


    def to_alipay_dict(self):
        params = dict()
        if self.acctrans_out_biz_no:
            if hasattr(self.acctrans_out_biz_no, 'to_alipay_dict'):
                params['acctrans_out_biz_no'] = self.acctrans_out_biz_no.to_alipay_dict()
            else:
                params['acctrans_out_biz_no'] = self.acctrans_out_biz_no
        if self.amount:
            if hasattr(self.amount, 'to_alipay_dict'):
                params['amount'] = self.amount.to_alipay_dict()
            else:
                params['amount'] = self.amount
        if self.assert_type_code:
            if hasattr(self.assert_type_code, 'to_alipay_dict'):
                params['assert_type_code'] = self.assert_type_code.to_alipay_dict()
            else:
                params['assert_type_code'] = self.assert_type_code
        if self.bank_card_pay_type:
            if hasattr(self.bank_card_pay_type, 'to_alipay_dict'):
                params['bank_card_pay_type'] = self.bank_card_pay_type.to_alipay_dict()
            else:
                params['bank_card_pay_type'] = self.bank_card_pay_type
        if self.bank_card_type:
            if hasattr(self.bank_card_type, 'to_alipay_dict'):
                params['bank_card_type'] = self.bank_card_type.to_alipay_dict()
            else:
                params['bank_card_type'] = self.bank_card_type
        if self.biz_id:
            if hasattr(self.biz_id, 'to_alipay_dict'):
                params['biz_id'] = self.biz_id.to_alipay_dict()
            else:
                params['biz_id'] = self.biz_id
        if self.biz_in_no:
            if hasattr(self.biz_in_no, 'to_alipay_dict'):
                params['biz_in_no'] = self.biz_in_no.to_alipay_dict()
            else:
                params['biz_in_no'] = self.biz_in_no
        if self.biz_out_no:
            if hasattr(self.biz_out_no, 'to_alipay_dict'):
                params['biz_out_no'] = self.biz_out_no.to_alipay_dict()
            else:
                params['biz_out_no'] = self.biz_out_no
        if self.biz_type:
            if hasattr(self.biz_type, 'to_alipay_dict'):
                params['biz_type'] = self.biz_type.to_alipay_dict()
            else:
                params['biz_type'] = self.biz_type
        if self.currency:
            if hasattr(self.currency, 'to_alipay_dict'):
                params['currency'] = self.currency.to_alipay_dict()
            else:
                params['currency'] = self.currency
        if self.dback_amount:
            if hasattr(self.dback_amount, 'to_alipay_dict'):
                params['dback_amount'] = self.dback_amount.to_alipay_dict()
            else:
                params['dback_amount'] = self.dback_amount
        if self.dback_gmt_create:
            if hasattr(self.dback_gmt_create, 'to_alipay_dict'):
                params['dback_gmt_create'] = self.dback_gmt_create.to_alipay_dict()
            else:
                params['dback_gmt_create'] = self.dback_gmt_create
        if self.dback_gmt_est_bk_ack:
            if hasattr(self.dback_gmt_est_bk_ack, 'to_alipay_dict'):
                params['dback_gmt_est_bk_ack'] = self.dback_gmt_est_bk_ack.to_alipay_dict()
            else:
                params['dback_gmt_est_bk_ack'] = self.dback_gmt_est_bk_ack
        if self.dback_gmt_est_bk_into:
            if hasattr(self.dback_gmt_est_bk_into, 'to_alipay_dict'):
                params['dback_gmt_est_bk_into'] = self.dback_gmt_est_bk_into.to_alipay_dict()
            else:
                params['dback_gmt_est_bk_into'] = self.dback_gmt_est_bk_into
        if self.dback_inst_account_name:
            if hasattr(self.dback_inst_account_name, 'to_alipay_dict'):
                params['dback_inst_account_name'] = self.dback_inst_account_name.to_alipay_dict()
            else:
                params['dback_inst_account_name'] = self.dback_inst_account_name
        if self.dback_inst_account_no:
            if hasattr(self.dback_inst_account_no, 'to_alipay_dict'):
                params['dback_inst_account_no'] = self.dback_inst_account_no.to_alipay_dict()
            else:
                params['dback_inst_account_no'] = self.dback_inst_account_no
        if self.dback_inst_id:
            if hasattr(self.dback_inst_id, 'to_alipay_dict'):
                params['dback_inst_id'] = self.dback_inst_id.to_alipay_dict()
            else:
                params['dback_inst_id'] = self.dback_inst_id
        if self.dback_inst_name:
            if hasattr(self.dback_inst_name, 'to_alipay_dict'):
                params['dback_inst_name'] = self.dback_inst_name.to_alipay_dict()
            else:
                params['dback_inst_name'] = self.dback_inst_name
        if self.fid:
            if hasattr(self.fid, 'to_alipay_dict'):
                params['fid'] = self.fid.to_alipay_dict()
            else:
                params['fid'] = self.fid
        if self.fund_access_type:
            if hasattr(self.fund_access_type, 'to_alipay_dict'):
                params['fund_access_type'] = self.fund_access_type.to_alipay_dict()
            else:
                params['fund_access_type'] = self.fund_access_type
        if self.fund_account_no:
            if hasattr(self.fund_account_no, 'to_alipay_dict'):
                params['fund_account_no'] = self.fund_account_no.to_alipay_dict()
            else:
                params['fund_account_no'] = self.fund_account_no
        if self.fund_biz_type:
            if hasattr(self.fund_biz_type, 'to_alipay_dict'):
                params['fund_biz_type'] = self.fund_biz_type.to_alipay_dict()
            else:
                params['fund_biz_type'] = self.fund_biz_type
        if self.fund_create_time:
            if hasattr(self.fund_create_time, 'to_alipay_dict'):
                params['fund_create_time'] = self.fund_create_time.to_alipay_dict()
            else:
                params['fund_create_time'] = self.fund_create_time
        if self.fund_finish_time:
            if hasattr(self.fund_finish_time, 'to_alipay_dict'):
                params['fund_finish_time'] = self.fund_finish_time.to_alipay_dict()
            else:
                params['fund_finish_time'] = self.fund_finish_time
        if self.fund_in_out:
            if hasattr(self.fund_in_out, 'to_alipay_dict'):
                params['fund_in_out'] = self.fund_in_out.to_alipay_dict()
            else:
                params['fund_in_out'] = self.fund_in_out
        if self.fund_inst_id:
            if hasattr(self.fund_inst_id, 'to_alipay_dict'):
                params['fund_inst_id'] = self.fund_inst_id.to_alipay_dict()
            else:
                params['fund_inst_id'] = self.fund_inst_id
        if self.fund_modify_time:
            if hasattr(self.fund_modify_time, 'to_alipay_dict'):
                params['fund_modify_time'] = self.fund_modify_time.to_alipay_dict()
            else:
                params['fund_modify_time'] = self.fund_modify_time
        if self.fund_status:
            if hasattr(self.fund_status, 'to_alipay_dict'):
                params['fund_status'] = self.fund_status.to_alipay_dict()
            else:
                params['fund_status'] = self.fund_status
        if self.fund_tool_belong_to_crowner:
            if hasattr(self.fund_tool_belong_to_crowner, 'to_alipay_dict'):
                params['fund_tool_belong_to_crowner'] = self.fund_tool_belong_to_crowner.to_alipay_dict()
            else:
                params['fund_tool_belong_to_crowner'] = self.fund_tool_belong_to_crowner
        if self.fund_tool_owner_card_no:
            if hasattr(self.fund_tool_owner_card_no, 'to_alipay_dict'):
                params['fund_tool_owner_card_no'] = self.fund_tool_owner_card_no.to_alipay_dict()
            else:
                params['fund_tool_owner_card_no'] = self.fund_tool_owner_card_no
        if self.fund_tool_type_for_crowner:
            if hasattr(self.fund_tool_type_for_crowner, 'to_alipay_dict'):
                params['fund_tool_type_for_crowner'] = self.fund_tool_type_for_crowner.to_alipay_dict()
            else:
                params['fund_tool_type_for_crowner'] = self.fund_tool_type_for_crowner
        if self.fund_tool_type_for_system:
            if hasattr(self.fund_tool_type_for_system, 'to_alipay_dict'):
                params['fund_tool_type_for_system'] = self.fund_tool_type_for_system.to_alipay_dict()
            else:
                params['fund_tool_type_for_system'] = self.fund_tool_type_for_system
        if self.fund_tool_type_name:
            if hasattr(self.fund_tool_type_name, 'to_alipay_dict'):
                params['fund_tool_type_name'] = self.fund_tool_type_name.to_alipay_dict()
            else:
                params['fund_tool_type_name'] = self.fund_tool_type_name
        if self.gmt_biz_create:
            if hasattr(self.gmt_biz_create, 'to_alipay_dict'):
                params['gmt_biz_create'] = self.gmt_biz_create.to_alipay_dict()
            else:
                params['gmt_biz_create'] = self.gmt_biz_create
        if self.open_self_slip_type:
            if hasattr(self.open_self_slip_type, 'to_alipay_dict'):
                params['open_self_slip_type'] = self.open_self_slip_type.to_alipay_dict()
            else:
                params['open_self_slip_type'] = self.open_self_slip_type
        if self.opposite_biz_card_alias:
            if hasattr(self.opposite_biz_card_alias, 'to_alipay_dict'):
                params['opposite_biz_card_alias'] = self.opposite_biz_card_alias.to_alipay_dict()
            else:
                params['opposite_biz_card_alias'] = self.opposite_biz_card_alias
        if self.opposite_biz_card_no:
            if hasattr(self.opposite_biz_card_no, 'to_alipay_dict'):
                params['opposite_biz_card_no'] = self.opposite_biz_card_no.to_alipay_dict()
            else:
                params['opposite_biz_card_no'] = self.opposite_biz_card_no
        if self.opposite_fund_card_no:
            if hasattr(self.opposite_fund_card_no, 'to_alipay_dict'):
                params['opposite_fund_card_no'] = self.opposite_fund_card_no.to_alipay_dict()
            else:
                params['opposite_fund_card_no'] = self.opposite_fund_card_no
        if self.out_request_no:
            if hasattr(self.out_request_no, 'to_alipay_dict'):
                params['out_request_no'] = self.out_request_no.to_alipay_dict()
            else:
                params['out_request_no'] = self.out_request_no
        if self.owner_card_no:
            if hasattr(self.owner_card_no, 'to_alipay_dict'):
                params['owner_card_no'] = self.owner_card_no.to_alipay_dict()
            else:
                params['owner_card_no'] = self.owner_card_no
        if self.refund_bank_status:
            if hasattr(self.refund_bank_status, 'to_alipay_dict'):
                params['refund_bank_status'] = self.refund_bank_status.to_alipay_dict()
            else:
                params['refund_bank_status'] = self.refund_bank_status
        if self.slip_amount:
            if hasattr(self.slip_amount, 'to_alipay_dict'):
                params['slip_amount'] = self.slip_amount.to_alipay_dict()
            else:
                params['slip_amount'] = self.slip_amount
        if self.slip_id:
            if hasattr(self.slip_id, 'to_alipay_dict'):
                params['slip_id'] = self.slip_id.to_alipay_dict()
            else:
                params['slip_id'] = self.slip_id
        if self.slip_status:
            if hasattr(self.slip_status, 'to_alipay_dict'):
                params['slip_status'] = self.slip_status.to_alipay_dict()
            else:
                params['slip_status'] = self.slip_status
        if self.sub_prepaid_card_type:
            if hasattr(self.sub_prepaid_card_type, 'to_alipay_dict'):
                params['sub_prepaid_card_type'] = self.sub_prepaid_card_type.to_alipay_dict()
            else:
                params['sub_prepaid_card_type'] = self.sub_prepaid_card_type
        if self.uid:
            if hasattr(self.uid, 'to_alipay_dict'):
                params['uid'] = self.uid.to_alipay_dict()
            else:
                params['uid'] = self.uid
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = FundItemAOPModel()
        if 'acctrans_out_biz_no' in d:
            o.acctrans_out_biz_no = d['acctrans_out_biz_no']
        if 'amount' in d:
            o.amount = d['amount']
        if 'assert_type_code' in d:
            o.assert_type_code = d['assert_type_code']
        if 'bank_card_pay_type' in d:
            o.bank_card_pay_type = d['bank_card_pay_type']
        if 'bank_card_type' in d:
            o.bank_card_type = d['bank_card_type']
        if 'biz_id' in d:
            o.biz_id = d['biz_id']
        if 'biz_in_no' in d:
            o.biz_in_no = d['biz_in_no']
        if 'biz_out_no' in d:
            o.biz_out_no = d['biz_out_no']
        if 'biz_type' in d:
            o.biz_type = d['biz_type']
        if 'currency' in d:
            o.currency = d['currency']
        if 'dback_amount' in d:
            o.dback_amount = d['dback_amount']
        if 'dback_gmt_create' in d:
            o.dback_gmt_create = d['dback_gmt_create']
        if 'dback_gmt_est_bk_ack' in d:
            o.dback_gmt_est_bk_ack = d['dback_gmt_est_bk_ack']
        if 'dback_gmt_est_bk_into' in d:
            o.dback_gmt_est_bk_into = d['dback_gmt_est_bk_into']
        if 'dback_inst_account_name' in d:
            o.dback_inst_account_name = d['dback_inst_account_name']
        if 'dback_inst_account_no' in d:
            o.dback_inst_account_no = d['dback_inst_account_no']
        if 'dback_inst_id' in d:
            o.dback_inst_id = d['dback_inst_id']
        if 'dback_inst_name' in d:
            o.dback_inst_name = d['dback_inst_name']
        if 'fid' in d:
            o.fid = d['fid']
        if 'fund_access_type' in d:
            o.fund_access_type = d['fund_access_type']
        if 'fund_account_no' in d:
            o.fund_account_no = d['fund_account_no']
        if 'fund_biz_type' in d:
            o.fund_biz_type = d['fund_biz_type']
        if 'fund_create_time' in d:
            o.fund_create_time = d['fund_create_time']
        if 'fund_finish_time' in d:
            o.fund_finish_time = d['fund_finish_time']
        if 'fund_in_out' in d:
            o.fund_in_out = d['fund_in_out']
        if 'fund_inst_id' in d:
            o.fund_inst_id = d['fund_inst_id']
        if 'fund_modify_time' in d:
            o.fund_modify_time = d['fund_modify_time']
        if 'fund_status' in d:
            o.fund_status = d['fund_status']
        if 'fund_tool_belong_to_crowner' in d:
            o.fund_tool_belong_to_crowner = d['fund_tool_belong_to_crowner']
        if 'fund_tool_owner_card_no' in d:
            o.fund_tool_owner_card_no = d['fund_tool_owner_card_no']
        if 'fund_tool_type_for_crowner' in d:
            o.fund_tool_type_for_crowner = d['fund_tool_type_for_crowner']
        if 'fund_tool_type_for_system' in d:
            o.fund_tool_type_for_system = d['fund_tool_type_for_system']
        if 'fund_tool_type_name' in d:
            o.fund_tool_type_name = d['fund_tool_type_name']
        if 'gmt_biz_create' in d:
            o.gmt_biz_create = d['gmt_biz_create']
        if 'open_self_slip_type' in d:
            o.open_self_slip_type = d['open_self_slip_type']
        if 'opposite_biz_card_alias' in d:
            o.opposite_biz_card_alias = d['opposite_biz_card_alias']
        if 'opposite_biz_card_no' in d:
            o.opposite_biz_card_no = d['opposite_biz_card_no']
        if 'opposite_fund_card_no' in d:
            o.opposite_fund_card_no = d['opposite_fund_card_no']
        if 'out_request_no' in d:
            o.out_request_no = d['out_request_no']
        if 'owner_card_no' in d:
            o.owner_card_no = d['owner_card_no']
        if 'refund_bank_status' in d:
            o.refund_bank_status = d['refund_bank_status']
        if 'slip_amount' in d:
            o.slip_amount = d['slip_amount']
        if 'slip_id' in d:
            o.slip_id = d['slip_id']
        if 'slip_status' in d:
            o.slip_status = d['slip_status']
        if 'sub_prepaid_card_type' in d:
            o.sub_prepaid_card_type = d['sub_prepaid_card_type']
        if 'uid' in d:
            o.uid = d['uid']
        return o


