#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class BankLogOpenApiDTO(object):

    def __init__(self):
        self._account_name = None
        self._account_no = None
        self._account_type = None
        self._balance = None
        self._biz_type = None
        self._ccy = None
        self._cent_factor = None
        self._credit_amount = None
        self._cust_name = None
        self._debit_amount = None
        self._distinguish_memo = None
        self._distinguish_result = None
        self._distinguish_result_msg = None
        self._distinguish_type = None
        self._erecon_collect_receipt_no = None
        self._erecon_inner_account_no = None
        self._fin_biz_code = None
        self._fin_biz_name = None
        self._fundlog_source = None
        self._his_sta = None
        self._id = None
        self._inst_id = None
        self._inst_name = None
        self._inst_serial_no = None
        self._is_fev_fc_ou = None
        self._link_no = None
        self._link_status = None
        self._memo = None
        self._op_cust_name = None
        self._origin_biz_memo = None
        self._other_account_name = None
        self._other_account_no = None
        self._other_account_type = None
        self._other_inst_name = None
        self._rel_voucher_id = None
        self._status = None
        self._sub_account_no = None
        self._target = None
        self._target_account_no = None
        self._top_1_predict_type = None
        self._top_2_predict_type = None
        self._top_3_predict_type = None
        self._trans_amount = None
        self._trans_direction = None
        self._trans_dt = None
        self._voucher_type = None

    @property
    def account_name(self):
        return self._account_name

    @account_name.setter
    def account_name(self, value):
        self._account_name = value
    @property
    def account_no(self):
        return self._account_no

    @account_no.setter
    def account_no(self, value):
        self._account_no = value
    @property
    def account_type(self):
        return self._account_type

    @account_type.setter
    def account_type(self, value):
        self._account_type = value
    @property
    def balance(self):
        return self._balance

    @balance.setter
    def balance(self, value):
        self._balance = value
    @property
    def biz_type(self):
        return self._biz_type

    @biz_type.setter
    def biz_type(self, value):
        self._biz_type = value
    @property
    def ccy(self):
        return self._ccy

    @ccy.setter
    def ccy(self, value):
        self._ccy = value
    @property
    def cent_factor(self):
        return self._cent_factor

    @cent_factor.setter
    def cent_factor(self, value):
        self._cent_factor = value
    @property
    def credit_amount(self):
        return self._credit_amount

    @credit_amount.setter
    def credit_amount(self, value):
        self._credit_amount = value
    @property
    def cust_name(self):
        return self._cust_name

    @cust_name.setter
    def cust_name(self, value):
        self._cust_name = value
    @property
    def debit_amount(self):
        return self._debit_amount

    @debit_amount.setter
    def debit_amount(self, value):
        self._debit_amount = value
    @property
    def distinguish_memo(self):
        return self._distinguish_memo

    @distinguish_memo.setter
    def distinguish_memo(self, value):
        self._distinguish_memo = value
    @property
    def distinguish_result(self):
        return self._distinguish_result

    @distinguish_result.setter
    def distinguish_result(self, value):
        self._distinguish_result = value
    @property
    def distinguish_result_msg(self):
        return self._distinguish_result_msg

    @distinguish_result_msg.setter
    def distinguish_result_msg(self, value):
        self._distinguish_result_msg = value
    @property
    def distinguish_type(self):
        return self._distinguish_type

    @distinguish_type.setter
    def distinguish_type(self, value):
        self._distinguish_type = value
    @property
    def erecon_collect_receipt_no(self):
        return self._erecon_collect_receipt_no

    @erecon_collect_receipt_no.setter
    def erecon_collect_receipt_no(self, value):
        self._erecon_collect_receipt_no = value
    @property
    def erecon_inner_account_no(self):
        return self._erecon_inner_account_no

    @erecon_inner_account_no.setter
    def erecon_inner_account_no(self, value):
        self._erecon_inner_account_no = value
    @property
    def fin_biz_code(self):
        return self._fin_biz_code

    @fin_biz_code.setter
    def fin_biz_code(self, value):
        self._fin_biz_code = value
    @property
    def fin_biz_name(self):
        return self._fin_biz_name

    @fin_biz_name.setter
    def fin_biz_name(self, value):
        self._fin_biz_name = value
    @property
    def fundlog_source(self):
        return self._fundlog_source

    @fundlog_source.setter
    def fundlog_source(self, value):
        self._fundlog_source = value
    @property
    def his_sta(self):
        return self._his_sta

    @his_sta.setter
    def his_sta(self, value):
        self._his_sta = value
    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        self._id = value
    @property
    def inst_id(self):
        return self._inst_id

    @inst_id.setter
    def inst_id(self, value):
        self._inst_id = value
    @property
    def inst_name(self):
        return self._inst_name

    @inst_name.setter
    def inst_name(self, value):
        self._inst_name = value
    @property
    def inst_serial_no(self):
        return self._inst_serial_no

    @inst_serial_no.setter
    def inst_serial_no(self, value):
        self._inst_serial_no = value
    @property
    def is_fev_fc_ou(self):
        return self._is_fev_fc_ou

    @is_fev_fc_ou.setter
    def is_fev_fc_ou(self, value):
        self._is_fev_fc_ou = value
    @property
    def link_no(self):
        return self._link_no

    @link_no.setter
    def link_no(self, value):
        self._link_no = value
    @property
    def link_status(self):
        return self._link_status

    @link_status.setter
    def link_status(self, value):
        self._link_status = value
    @property
    def memo(self):
        return self._memo

    @memo.setter
    def memo(self, value):
        self._memo = value
    @property
    def op_cust_name(self):
        return self._op_cust_name

    @op_cust_name.setter
    def op_cust_name(self, value):
        self._op_cust_name = value
    @property
    def origin_biz_memo(self):
        return self._origin_biz_memo

    @origin_biz_memo.setter
    def origin_biz_memo(self, value):
        self._origin_biz_memo = value
    @property
    def other_account_name(self):
        return self._other_account_name

    @other_account_name.setter
    def other_account_name(self, value):
        self._other_account_name = value
    @property
    def other_account_no(self):
        return self._other_account_no

    @other_account_no.setter
    def other_account_no(self, value):
        self._other_account_no = value
    @property
    def other_account_type(self):
        return self._other_account_type

    @other_account_type.setter
    def other_account_type(self, value):
        self._other_account_type = value
    @property
    def other_inst_name(self):
        return self._other_inst_name

    @other_inst_name.setter
    def other_inst_name(self, value):
        self._other_inst_name = value
    @property
    def rel_voucher_id(self):
        return self._rel_voucher_id

    @rel_voucher_id.setter
    def rel_voucher_id(self, value):
        self._rel_voucher_id = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value
    @property
    def sub_account_no(self):
        return self._sub_account_no

    @sub_account_no.setter
    def sub_account_no(self, value):
        self._sub_account_no = value
    @property
    def target(self):
        return self._target

    @target.setter
    def target(self, value):
        self._target = value
    @property
    def target_account_no(self):
        return self._target_account_no

    @target_account_no.setter
    def target_account_no(self, value):
        self._target_account_no = value
    @property
    def top_1_predict_type(self):
        return self._top_1_predict_type

    @top_1_predict_type.setter
    def top_1_predict_type(self, value):
        self._top_1_predict_type = value
    @property
    def top_2_predict_type(self):
        return self._top_2_predict_type

    @top_2_predict_type.setter
    def top_2_predict_type(self, value):
        self._top_2_predict_type = value
    @property
    def top_3_predict_type(self):
        return self._top_3_predict_type

    @top_3_predict_type.setter
    def top_3_predict_type(self, value):
        self._top_3_predict_type = value
    @property
    def trans_amount(self):
        return self._trans_amount

    @trans_amount.setter
    def trans_amount(self, value):
        self._trans_amount = value
    @property
    def trans_direction(self):
        return self._trans_direction

    @trans_direction.setter
    def trans_direction(self, value):
        self._trans_direction = value
    @property
    def trans_dt(self):
        return self._trans_dt

    @trans_dt.setter
    def trans_dt(self, value):
        self._trans_dt = value
    @property
    def voucher_type(self):
        return self._voucher_type

    @voucher_type.setter
    def voucher_type(self, value):
        self._voucher_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.account_name:
            if hasattr(self.account_name, 'to_alipay_dict'):
                params['account_name'] = self.account_name.to_alipay_dict()
            else:
                params['account_name'] = self.account_name
        if self.account_no:
            if hasattr(self.account_no, 'to_alipay_dict'):
                params['account_no'] = self.account_no.to_alipay_dict()
            else:
                params['account_no'] = self.account_no
        if self.account_type:
            if hasattr(self.account_type, 'to_alipay_dict'):
                params['account_type'] = self.account_type.to_alipay_dict()
            else:
                params['account_type'] = self.account_type
        if self.balance:
            if hasattr(self.balance, 'to_alipay_dict'):
                params['balance'] = self.balance.to_alipay_dict()
            else:
                params['balance'] = self.balance
        if self.biz_type:
            if hasattr(self.biz_type, 'to_alipay_dict'):
                params['biz_type'] = self.biz_type.to_alipay_dict()
            else:
                params['biz_type'] = self.biz_type
        if self.ccy:
            if hasattr(self.ccy, 'to_alipay_dict'):
                params['ccy'] = self.ccy.to_alipay_dict()
            else:
                params['ccy'] = self.ccy
        if self.cent_factor:
            if hasattr(self.cent_factor, 'to_alipay_dict'):
                params['cent_factor'] = self.cent_factor.to_alipay_dict()
            else:
                params['cent_factor'] = self.cent_factor
        if self.credit_amount:
            if hasattr(self.credit_amount, 'to_alipay_dict'):
                params['credit_amount'] = self.credit_amount.to_alipay_dict()
            else:
                params['credit_amount'] = self.credit_amount
        if self.cust_name:
            if hasattr(self.cust_name, 'to_alipay_dict'):
                params['cust_name'] = self.cust_name.to_alipay_dict()
            else:
                params['cust_name'] = self.cust_name
        if self.debit_amount:
            if hasattr(self.debit_amount, 'to_alipay_dict'):
                params['debit_amount'] = self.debit_amount.to_alipay_dict()
            else:
                params['debit_amount'] = self.debit_amount
        if self.distinguish_memo:
            if hasattr(self.distinguish_memo, 'to_alipay_dict'):
                params['distinguish_memo'] = self.distinguish_memo.to_alipay_dict()
            else:
                params['distinguish_memo'] = self.distinguish_memo
        if self.distinguish_result:
            if hasattr(self.distinguish_result, 'to_alipay_dict'):
                params['distinguish_result'] = self.distinguish_result.to_alipay_dict()
            else:
                params['distinguish_result'] = self.distinguish_result
        if self.distinguish_result_msg:
            if hasattr(self.distinguish_result_msg, 'to_alipay_dict'):
                params['distinguish_result_msg'] = self.distinguish_result_msg.to_alipay_dict()
            else:
                params['distinguish_result_msg'] = self.distinguish_result_msg
        if self.distinguish_type:
            if hasattr(self.distinguish_type, 'to_alipay_dict'):
                params['distinguish_type'] = self.distinguish_type.to_alipay_dict()
            else:
                params['distinguish_type'] = self.distinguish_type
        if self.erecon_collect_receipt_no:
            if hasattr(self.erecon_collect_receipt_no, 'to_alipay_dict'):
                params['erecon_collect_receipt_no'] = self.erecon_collect_receipt_no.to_alipay_dict()
            else:
                params['erecon_collect_receipt_no'] = self.erecon_collect_receipt_no
        if self.erecon_inner_account_no:
            if hasattr(self.erecon_inner_account_no, 'to_alipay_dict'):
                params['erecon_inner_account_no'] = self.erecon_inner_account_no.to_alipay_dict()
            else:
                params['erecon_inner_account_no'] = self.erecon_inner_account_no
        if self.fin_biz_code:
            if hasattr(self.fin_biz_code, 'to_alipay_dict'):
                params['fin_biz_code'] = self.fin_biz_code.to_alipay_dict()
            else:
                params['fin_biz_code'] = self.fin_biz_code
        if self.fin_biz_name:
            if hasattr(self.fin_biz_name, 'to_alipay_dict'):
                params['fin_biz_name'] = self.fin_biz_name.to_alipay_dict()
            else:
                params['fin_biz_name'] = self.fin_biz_name
        if self.fundlog_source:
            if hasattr(self.fundlog_source, 'to_alipay_dict'):
                params['fundlog_source'] = self.fundlog_source.to_alipay_dict()
            else:
                params['fundlog_source'] = self.fundlog_source
        if self.his_sta:
            if hasattr(self.his_sta, 'to_alipay_dict'):
                params['his_sta'] = self.his_sta.to_alipay_dict()
            else:
                params['his_sta'] = self.his_sta
        if self.id:
            if hasattr(self.id, 'to_alipay_dict'):
                params['id'] = self.id.to_alipay_dict()
            else:
                params['id'] = self.id
        if self.inst_id:
            if hasattr(self.inst_id, 'to_alipay_dict'):
                params['inst_id'] = self.inst_id.to_alipay_dict()
            else:
                params['inst_id'] = self.inst_id
        if self.inst_name:
            if hasattr(self.inst_name, 'to_alipay_dict'):
                params['inst_name'] = self.inst_name.to_alipay_dict()
            else:
                params['inst_name'] = self.inst_name
        if self.inst_serial_no:
            if hasattr(self.inst_serial_no, 'to_alipay_dict'):
                params['inst_serial_no'] = self.inst_serial_no.to_alipay_dict()
            else:
                params['inst_serial_no'] = self.inst_serial_no
        if self.is_fev_fc_ou:
            if hasattr(self.is_fev_fc_ou, 'to_alipay_dict'):
                params['is_fev_fc_ou'] = self.is_fev_fc_ou.to_alipay_dict()
            else:
                params['is_fev_fc_ou'] = self.is_fev_fc_ou
        if self.link_no:
            if hasattr(self.link_no, 'to_alipay_dict'):
                params['link_no'] = self.link_no.to_alipay_dict()
            else:
                params['link_no'] = self.link_no
        if self.link_status:
            if hasattr(self.link_status, 'to_alipay_dict'):
                params['link_status'] = self.link_status.to_alipay_dict()
            else:
                params['link_status'] = self.link_status
        if self.memo:
            if hasattr(self.memo, 'to_alipay_dict'):
                params['memo'] = self.memo.to_alipay_dict()
            else:
                params['memo'] = self.memo
        if self.op_cust_name:
            if hasattr(self.op_cust_name, 'to_alipay_dict'):
                params['op_cust_name'] = self.op_cust_name.to_alipay_dict()
            else:
                params['op_cust_name'] = self.op_cust_name
        if self.origin_biz_memo:
            if hasattr(self.origin_biz_memo, 'to_alipay_dict'):
                params['origin_biz_memo'] = self.origin_biz_memo.to_alipay_dict()
            else:
                params['origin_biz_memo'] = self.origin_biz_memo
        if self.other_account_name:
            if hasattr(self.other_account_name, 'to_alipay_dict'):
                params['other_account_name'] = self.other_account_name.to_alipay_dict()
            else:
                params['other_account_name'] = self.other_account_name
        if self.other_account_no:
            if hasattr(self.other_account_no, 'to_alipay_dict'):
                params['other_account_no'] = self.other_account_no.to_alipay_dict()
            else:
                params['other_account_no'] = self.other_account_no
        if self.other_account_type:
            if hasattr(self.other_account_type, 'to_alipay_dict'):
                params['other_account_type'] = self.other_account_type.to_alipay_dict()
            else:
                params['other_account_type'] = self.other_account_type
        if self.other_inst_name:
            if hasattr(self.other_inst_name, 'to_alipay_dict'):
                params['other_inst_name'] = self.other_inst_name.to_alipay_dict()
            else:
                params['other_inst_name'] = self.other_inst_name
        if self.rel_voucher_id:
            if hasattr(self.rel_voucher_id, 'to_alipay_dict'):
                params['rel_voucher_id'] = self.rel_voucher_id.to_alipay_dict()
            else:
                params['rel_voucher_id'] = self.rel_voucher_id
        if self.status:
            if hasattr(self.status, 'to_alipay_dict'):
                params['status'] = self.status.to_alipay_dict()
            else:
                params['status'] = self.status
        if self.sub_account_no:
            if hasattr(self.sub_account_no, 'to_alipay_dict'):
                params['sub_account_no'] = self.sub_account_no.to_alipay_dict()
            else:
                params['sub_account_no'] = self.sub_account_no
        if self.target:
            if hasattr(self.target, 'to_alipay_dict'):
                params['target'] = self.target.to_alipay_dict()
            else:
                params['target'] = self.target
        if self.target_account_no:
            if hasattr(self.target_account_no, 'to_alipay_dict'):
                params['target_account_no'] = self.target_account_no.to_alipay_dict()
            else:
                params['target_account_no'] = self.target_account_no
        if self.top_1_predict_type:
            if hasattr(self.top_1_predict_type, 'to_alipay_dict'):
                params['top_1_predict_type'] = self.top_1_predict_type.to_alipay_dict()
            else:
                params['top_1_predict_type'] = self.top_1_predict_type
        if self.top_2_predict_type:
            if hasattr(self.top_2_predict_type, 'to_alipay_dict'):
                params['top_2_predict_type'] = self.top_2_predict_type.to_alipay_dict()
            else:
                params['top_2_predict_type'] = self.top_2_predict_type
        if self.top_3_predict_type:
            if hasattr(self.top_3_predict_type, 'to_alipay_dict'):
                params['top_3_predict_type'] = self.top_3_predict_type.to_alipay_dict()
            else:
                params['top_3_predict_type'] = self.top_3_predict_type
        if self.trans_amount:
            if hasattr(self.trans_amount, 'to_alipay_dict'):
                params['trans_amount'] = self.trans_amount.to_alipay_dict()
            else:
                params['trans_amount'] = self.trans_amount
        if self.trans_direction:
            if hasattr(self.trans_direction, 'to_alipay_dict'):
                params['trans_direction'] = self.trans_direction.to_alipay_dict()
            else:
                params['trans_direction'] = self.trans_direction
        if self.trans_dt:
            if hasattr(self.trans_dt, 'to_alipay_dict'):
                params['trans_dt'] = self.trans_dt.to_alipay_dict()
            else:
                params['trans_dt'] = self.trans_dt
        if self.voucher_type:
            if hasattr(self.voucher_type, 'to_alipay_dict'):
                params['voucher_type'] = self.voucher_type.to_alipay_dict()
            else:
                params['voucher_type'] = self.voucher_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = BankLogOpenApiDTO()
        if 'account_name' in d:
            o.account_name = d['account_name']
        if 'account_no' in d:
            o.account_no = d['account_no']
        if 'account_type' in d:
            o.account_type = d['account_type']
        if 'balance' in d:
            o.balance = d['balance']
        if 'biz_type' in d:
            o.biz_type = d['biz_type']
        if 'ccy' in d:
            o.ccy = d['ccy']
        if 'cent_factor' in d:
            o.cent_factor = d['cent_factor']
        if 'credit_amount' in d:
            o.credit_amount = d['credit_amount']
        if 'cust_name' in d:
            o.cust_name = d['cust_name']
        if 'debit_amount' in d:
            o.debit_amount = d['debit_amount']
        if 'distinguish_memo' in d:
            o.distinguish_memo = d['distinguish_memo']
        if 'distinguish_result' in d:
            o.distinguish_result = d['distinguish_result']
        if 'distinguish_result_msg' in d:
            o.distinguish_result_msg = d['distinguish_result_msg']
        if 'distinguish_type' in d:
            o.distinguish_type = d['distinguish_type']
        if 'erecon_collect_receipt_no' in d:
            o.erecon_collect_receipt_no = d['erecon_collect_receipt_no']
        if 'erecon_inner_account_no' in d:
            o.erecon_inner_account_no = d['erecon_inner_account_no']
        if 'fin_biz_code' in d:
            o.fin_biz_code = d['fin_biz_code']
        if 'fin_biz_name' in d:
            o.fin_biz_name = d['fin_biz_name']
        if 'fundlog_source' in d:
            o.fundlog_source = d['fundlog_source']
        if 'his_sta' in d:
            o.his_sta = d['his_sta']
        if 'id' in d:
            o.id = d['id']
        if 'inst_id' in d:
            o.inst_id = d['inst_id']
        if 'inst_name' in d:
            o.inst_name = d['inst_name']
        if 'inst_serial_no' in d:
            o.inst_serial_no = d['inst_serial_no']
        if 'is_fev_fc_ou' in d:
            o.is_fev_fc_ou = d['is_fev_fc_ou']
        if 'link_no' in d:
            o.link_no = d['link_no']
        if 'link_status' in d:
            o.link_status = d['link_status']
        if 'memo' in d:
            o.memo = d['memo']
        if 'op_cust_name' in d:
            o.op_cust_name = d['op_cust_name']
        if 'origin_biz_memo' in d:
            o.origin_biz_memo = d['origin_biz_memo']
        if 'other_account_name' in d:
            o.other_account_name = d['other_account_name']
        if 'other_account_no' in d:
            o.other_account_no = d['other_account_no']
        if 'other_account_type' in d:
            o.other_account_type = d['other_account_type']
        if 'other_inst_name' in d:
            o.other_inst_name = d['other_inst_name']
        if 'rel_voucher_id' in d:
            o.rel_voucher_id = d['rel_voucher_id']
        if 'status' in d:
            o.status = d['status']
        if 'sub_account_no' in d:
            o.sub_account_no = d['sub_account_no']
        if 'target' in d:
            o.target = d['target']
        if 'target_account_no' in d:
            o.target_account_no = d['target_account_no']
        if 'top_1_predict_type' in d:
            o.top_1_predict_type = d['top_1_predict_type']
        if 'top_2_predict_type' in d:
            o.top_2_predict_type = d['top_2_predict_type']
        if 'top_3_predict_type' in d:
            o.top_3_predict_type = d['top_3_predict_type']
        if 'trans_amount' in d:
            o.trans_amount = d['trans_amount']
        if 'trans_direction' in d:
            o.trans_direction = d['trans_direction']
        if 'trans_dt' in d:
            o.trans_dt = d['trans_dt']
        if 'voucher_type' in d:
            o.voucher_type = d['voucher_type']
        return o


