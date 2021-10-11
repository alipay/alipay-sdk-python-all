#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class BizFundReportResult(object):

    def __init__(self):
        self._alipay_amount = None
        self._batch_type = None
        self._biz_type = None
        self._biz_type_desc = None
        self._charge_fee = None
        self._gmt_create = None
        self._instruction_id = None
        self._memo = None
        self._no_mbill_encrypt = None
        self._order_id = None
        self._pay_amount = None
        self._payee_card_no = None
        self._payee_full_name = None
        self._payee_fund_type = None
        self._payee_fund_type_desc = None
        self._payee_inst_name = None
        self._payee_login_email = None
        self._payee_name = None
        self._payer_fund_type = None
        self._payer_fund_type_desc = None
        self._refund_amount = None
        self._show_detail = None
        self._show_voucher = None
        self._source = None
        self._status = None
        self._status_desc = None
        self._sub_biz_type = None
        self._sub_biz_type_desc = None

    @property
    def alipay_amount(self):
        return self._alipay_amount

    @alipay_amount.setter
    def alipay_amount(self, value):
        self._alipay_amount = value
    @property
    def batch_type(self):
        return self._batch_type

    @batch_type.setter
    def batch_type(self, value):
        self._batch_type = value
    @property
    def biz_type(self):
        return self._biz_type

    @biz_type.setter
    def biz_type(self, value):
        self._biz_type = value
    @property
    def biz_type_desc(self):
        return self._biz_type_desc

    @biz_type_desc.setter
    def biz_type_desc(self, value):
        self._biz_type_desc = value
    @property
    def charge_fee(self):
        return self._charge_fee

    @charge_fee.setter
    def charge_fee(self, value):
        self._charge_fee = value
    @property
    def gmt_create(self):
        return self._gmt_create

    @gmt_create.setter
    def gmt_create(self, value):
        self._gmt_create = value
    @property
    def instruction_id(self):
        return self._instruction_id

    @instruction_id.setter
    def instruction_id(self, value):
        self._instruction_id = value
    @property
    def memo(self):
        return self._memo

    @memo.setter
    def memo(self, value):
        self._memo = value
    @property
    def no_mbill_encrypt(self):
        return self._no_mbill_encrypt

    @no_mbill_encrypt.setter
    def no_mbill_encrypt(self, value):
        self._no_mbill_encrypt = value
    @property
    def order_id(self):
        return self._order_id

    @order_id.setter
    def order_id(self, value):
        self._order_id = value
    @property
    def pay_amount(self):
        return self._pay_amount

    @pay_amount.setter
    def pay_amount(self, value):
        self._pay_amount = value
    @property
    def payee_card_no(self):
        return self._payee_card_no

    @payee_card_no.setter
    def payee_card_no(self, value):
        self._payee_card_no = value
    @property
    def payee_full_name(self):
        return self._payee_full_name

    @payee_full_name.setter
    def payee_full_name(self, value):
        self._payee_full_name = value
    @property
    def payee_fund_type(self):
        return self._payee_fund_type

    @payee_fund_type.setter
    def payee_fund_type(self, value):
        self._payee_fund_type = value
    @property
    def payee_fund_type_desc(self):
        return self._payee_fund_type_desc

    @payee_fund_type_desc.setter
    def payee_fund_type_desc(self, value):
        self._payee_fund_type_desc = value
    @property
    def payee_inst_name(self):
        return self._payee_inst_name

    @payee_inst_name.setter
    def payee_inst_name(self, value):
        self._payee_inst_name = value
    @property
    def payee_login_email(self):
        return self._payee_login_email

    @payee_login_email.setter
    def payee_login_email(self, value):
        self._payee_login_email = value
    @property
    def payee_name(self):
        return self._payee_name

    @payee_name.setter
    def payee_name(self, value):
        self._payee_name = value
    @property
    def payer_fund_type(self):
        return self._payer_fund_type

    @payer_fund_type.setter
    def payer_fund_type(self, value):
        self._payer_fund_type = value
    @property
    def payer_fund_type_desc(self):
        return self._payer_fund_type_desc

    @payer_fund_type_desc.setter
    def payer_fund_type_desc(self, value):
        self._payer_fund_type_desc = value
    @property
    def refund_amount(self):
        return self._refund_amount

    @refund_amount.setter
    def refund_amount(self, value):
        self._refund_amount = value
    @property
    def show_detail(self):
        return self._show_detail

    @show_detail.setter
    def show_detail(self, value):
        self._show_detail = value
    @property
    def show_voucher(self):
        return self._show_voucher

    @show_voucher.setter
    def show_voucher(self, value):
        self._show_voucher = value
    @property
    def source(self):
        return self._source

    @source.setter
    def source(self, value):
        self._source = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value
    @property
    def status_desc(self):
        return self._status_desc

    @status_desc.setter
    def status_desc(self, value):
        self._status_desc = value
    @property
    def sub_biz_type(self):
        return self._sub_biz_type

    @sub_biz_type.setter
    def sub_biz_type(self, value):
        self._sub_biz_type = value
    @property
    def sub_biz_type_desc(self):
        return self._sub_biz_type_desc

    @sub_biz_type_desc.setter
    def sub_biz_type_desc(self, value):
        self._sub_biz_type_desc = value


    def to_alipay_dict(self):
        params = dict()
        if self.alipay_amount:
            if hasattr(self.alipay_amount, 'to_alipay_dict'):
                params['alipay_amount'] = self.alipay_amount.to_alipay_dict()
            else:
                params['alipay_amount'] = self.alipay_amount
        if self.batch_type:
            if hasattr(self.batch_type, 'to_alipay_dict'):
                params['batch_type'] = self.batch_type.to_alipay_dict()
            else:
                params['batch_type'] = self.batch_type
        if self.biz_type:
            if hasattr(self.biz_type, 'to_alipay_dict'):
                params['biz_type'] = self.biz_type.to_alipay_dict()
            else:
                params['biz_type'] = self.biz_type
        if self.biz_type_desc:
            if hasattr(self.biz_type_desc, 'to_alipay_dict'):
                params['biz_type_desc'] = self.biz_type_desc.to_alipay_dict()
            else:
                params['biz_type_desc'] = self.biz_type_desc
        if self.charge_fee:
            if hasattr(self.charge_fee, 'to_alipay_dict'):
                params['charge_fee'] = self.charge_fee.to_alipay_dict()
            else:
                params['charge_fee'] = self.charge_fee
        if self.gmt_create:
            if hasattr(self.gmt_create, 'to_alipay_dict'):
                params['gmt_create'] = self.gmt_create.to_alipay_dict()
            else:
                params['gmt_create'] = self.gmt_create
        if self.instruction_id:
            if hasattr(self.instruction_id, 'to_alipay_dict'):
                params['instruction_id'] = self.instruction_id.to_alipay_dict()
            else:
                params['instruction_id'] = self.instruction_id
        if self.memo:
            if hasattr(self.memo, 'to_alipay_dict'):
                params['memo'] = self.memo.to_alipay_dict()
            else:
                params['memo'] = self.memo
        if self.no_mbill_encrypt:
            if hasattr(self.no_mbill_encrypt, 'to_alipay_dict'):
                params['no_mbill_encrypt'] = self.no_mbill_encrypt.to_alipay_dict()
            else:
                params['no_mbill_encrypt'] = self.no_mbill_encrypt
        if self.order_id:
            if hasattr(self.order_id, 'to_alipay_dict'):
                params['order_id'] = self.order_id.to_alipay_dict()
            else:
                params['order_id'] = self.order_id
        if self.pay_amount:
            if hasattr(self.pay_amount, 'to_alipay_dict'):
                params['pay_amount'] = self.pay_amount.to_alipay_dict()
            else:
                params['pay_amount'] = self.pay_amount
        if self.payee_card_no:
            if hasattr(self.payee_card_no, 'to_alipay_dict'):
                params['payee_card_no'] = self.payee_card_no.to_alipay_dict()
            else:
                params['payee_card_no'] = self.payee_card_no
        if self.payee_full_name:
            if hasattr(self.payee_full_name, 'to_alipay_dict'):
                params['payee_full_name'] = self.payee_full_name.to_alipay_dict()
            else:
                params['payee_full_name'] = self.payee_full_name
        if self.payee_fund_type:
            if hasattr(self.payee_fund_type, 'to_alipay_dict'):
                params['payee_fund_type'] = self.payee_fund_type.to_alipay_dict()
            else:
                params['payee_fund_type'] = self.payee_fund_type
        if self.payee_fund_type_desc:
            if hasattr(self.payee_fund_type_desc, 'to_alipay_dict'):
                params['payee_fund_type_desc'] = self.payee_fund_type_desc.to_alipay_dict()
            else:
                params['payee_fund_type_desc'] = self.payee_fund_type_desc
        if self.payee_inst_name:
            if hasattr(self.payee_inst_name, 'to_alipay_dict'):
                params['payee_inst_name'] = self.payee_inst_name.to_alipay_dict()
            else:
                params['payee_inst_name'] = self.payee_inst_name
        if self.payee_login_email:
            if hasattr(self.payee_login_email, 'to_alipay_dict'):
                params['payee_login_email'] = self.payee_login_email.to_alipay_dict()
            else:
                params['payee_login_email'] = self.payee_login_email
        if self.payee_name:
            if hasattr(self.payee_name, 'to_alipay_dict'):
                params['payee_name'] = self.payee_name.to_alipay_dict()
            else:
                params['payee_name'] = self.payee_name
        if self.payer_fund_type:
            if hasattr(self.payer_fund_type, 'to_alipay_dict'):
                params['payer_fund_type'] = self.payer_fund_type.to_alipay_dict()
            else:
                params['payer_fund_type'] = self.payer_fund_type
        if self.payer_fund_type_desc:
            if hasattr(self.payer_fund_type_desc, 'to_alipay_dict'):
                params['payer_fund_type_desc'] = self.payer_fund_type_desc.to_alipay_dict()
            else:
                params['payer_fund_type_desc'] = self.payer_fund_type_desc
        if self.refund_amount:
            if hasattr(self.refund_amount, 'to_alipay_dict'):
                params['refund_amount'] = self.refund_amount.to_alipay_dict()
            else:
                params['refund_amount'] = self.refund_amount
        if self.show_detail:
            if hasattr(self.show_detail, 'to_alipay_dict'):
                params['show_detail'] = self.show_detail.to_alipay_dict()
            else:
                params['show_detail'] = self.show_detail
        if self.show_voucher:
            if hasattr(self.show_voucher, 'to_alipay_dict'):
                params['show_voucher'] = self.show_voucher.to_alipay_dict()
            else:
                params['show_voucher'] = self.show_voucher
        if self.source:
            if hasattr(self.source, 'to_alipay_dict'):
                params['source'] = self.source.to_alipay_dict()
            else:
                params['source'] = self.source
        if self.status:
            if hasattr(self.status, 'to_alipay_dict'):
                params['status'] = self.status.to_alipay_dict()
            else:
                params['status'] = self.status
        if self.status_desc:
            if hasattr(self.status_desc, 'to_alipay_dict'):
                params['status_desc'] = self.status_desc.to_alipay_dict()
            else:
                params['status_desc'] = self.status_desc
        if self.sub_biz_type:
            if hasattr(self.sub_biz_type, 'to_alipay_dict'):
                params['sub_biz_type'] = self.sub_biz_type.to_alipay_dict()
            else:
                params['sub_biz_type'] = self.sub_biz_type
        if self.sub_biz_type_desc:
            if hasattr(self.sub_biz_type_desc, 'to_alipay_dict'):
                params['sub_biz_type_desc'] = self.sub_biz_type_desc.to_alipay_dict()
            else:
                params['sub_biz_type_desc'] = self.sub_biz_type_desc
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = BizFundReportResult()
        if 'alipay_amount' in d:
            o.alipay_amount = d['alipay_amount']
        if 'batch_type' in d:
            o.batch_type = d['batch_type']
        if 'biz_type' in d:
            o.biz_type = d['biz_type']
        if 'biz_type_desc' in d:
            o.biz_type_desc = d['biz_type_desc']
        if 'charge_fee' in d:
            o.charge_fee = d['charge_fee']
        if 'gmt_create' in d:
            o.gmt_create = d['gmt_create']
        if 'instruction_id' in d:
            o.instruction_id = d['instruction_id']
        if 'memo' in d:
            o.memo = d['memo']
        if 'no_mbill_encrypt' in d:
            o.no_mbill_encrypt = d['no_mbill_encrypt']
        if 'order_id' in d:
            o.order_id = d['order_id']
        if 'pay_amount' in d:
            o.pay_amount = d['pay_amount']
        if 'payee_card_no' in d:
            o.payee_card_no = d['payee_card_no']
        if 'payee_full_name' in d:
            o.payee_full_name = d['payee_full_name']
        if 'payee_fund_type' in d:
            o.payee_fund_type = d['payee_fund_type']
        if 'payee_fund_type_desc' in d:
            o.payee_fund_type_desc = d['payee_fund_type_desc']
        if 'payee_inst_name' in d:
            o.payee_inst_name = d['payee_inst_name']
        if 'payee_login_email' in d:
            o.payee_login_email = d['payee_login_email']
        if 'payee_name' in d:
            o.payee_name = d['payee_name']
        if 'payer_fund_type' in d:
            o.payer_fund_type = d['payer_fund_type']
        if 'payer_fund_type_desc' in d:
            o.payer_fund_type_desc = d['payer_fund_type_desc']
        if 'refund_amount' in d:
            o.refund_amount = d['refund_amount']
        if 'show_detail' in d:
            o.show_detail = d['show_detail']
        if 'show_voucher' in d:
            o.show_voucher = d['show_voucher']
        if 'source' in d:
            o.source = d['source']
        if 'status' in d:
            o.status = d['status']
        if 'status_desc' in d:
            o.status_desc = d['status_desc']
        if 'sub_biz_type' in d:
            o.sub_biz_type = d['sub_biz_type']
        if 'sub_biz_type_desc' in d:
            o.sub_biz_type_desc = d['sub_biz_type_desc']
        return o


