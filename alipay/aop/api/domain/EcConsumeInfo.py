#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class EcConsumeInfo(object):

    def __init__(self):
        self._account_id = None
        self._agreement_peer_payer_id = None
        self._benefit_amount = None
        self._biz_out_no = None
        self._category_name = None
        self._consume_amount = None
        self._consume_biz_type = None
        self._consume_category = None
        self._consume_fee_with_discount = None
        self._consume_memo = None
        self._consume_type = None
        self._employee_id = None
        self._enterprise_id = None
        self._expense_rule_group_id = None
        self._expense_scene_code = None
        self._expense_type = None
        self._expense_type_sub_category = None
        self._ext_infos = None
        self._fund_biz_type = None
        self._gmt_biz_create = None
        self._gmt_receive_pay = None
        self._invoice_open_mode = None
        self._merchant_id = None
        self._merchant_name = None
        self._open_id = None
        self._opposite_full_name = None
        self._order_complete_label = None
        self._order_complete_time = None
        self._pay_no = None
        self._payer_card_no = None
        self._payer_logon_id = None
        self._payer_name = None
        self._peer_pay_amount = None
        self._peer_payer_card_no = None
        self._peer_refund_amount = None
        self._peer_refund_status = None
        self._related_pay_no = None
        self._scene_code = None
        self._seller_id = None
        self._shop_id = None
        self._store_id = None
        self._summary_apply_id = None
        self._user_id = None

    @property
    def account_id(self):
        return self._account_id

    @account_id.setter
    def account_id(self, value):
        self._account_id = value
    @property
    def agreement_peer_payer_id(self):
        return self._agreement_peer_payer_id

    @agreement_peer_payer_id.setter
    def agreement_peer_payer_id(self, value):
        self._agreement_peer_payer_id = value
    @property
    def benefit_amount(self):
        return self._benefit_amount

    @benefit_amount.setter
    def benefit_amount(self, value):
        self._benefit_amount = value
    @property
    def biz_out_no(self):
        return self._biz_out_no

    @biz_out_no.setter
    def biz_out_no(self, value):
        self._biz_out_no = value
    @property
    def category_name(self):
        return self._category_name

    @category_name.setter
    def category_name(self, value):
        self._category_name = value
    @property
    def consume_amount(self):
        return self._consume_amount

    @consume_amount.setter
    def consume_amount(self, value):
        self._consume_amount = value
    @property
    def consume_biz_type(self):
        return self._consume_biz_type

    @consume_biz_type.setter
    def consume_biz_type(self, value):
        self._consume_biz_type = value
    @property
    def consume_category(self):
        return self._consume_category

    @consume_category.setter
    def consume_category(self, value):
        self._consume_category = value
    @property
    def consume_fee_with_discount(self):
        return self._consume_fee_with_discount

    @consume_fee_with_discount.setter
    def consume_fee_with_discount(self, value):
        self._consume_fee_with_discount = value
    @property
    def consume_memo(self):
        return self._consume_memo

    @consume_memo.setter
    def consume_memo(self, value):
        self._consume_memo = value
    @property
    def consume_type(self):
        return self._consume_type

    @consume_type.setter
    def consume_type(self, value):
        self._consume_type = value
    @property
    def employee_id(self):
        return self._employee_id

    @employee_id.setter
    def employee_id(self, value):
        self._employee_id = value
    @property
    def enterprise_id(self):
        return self._enterprise_id

    @enterprise_id.setter
    def enterprise_id(self, value):
        self._enterprise_id = value
    @property
    def expense_rule_group_id(self):
        return self._expense_rule_group_id

    @expense_rule_group_id.setter
    def expense_rule_group_id(self, value):
        self._expense_rule_group_id = value
    @property
    def expense_scene_code(self):
        return self._expense_scene_code

    @expense_scene_code.setter
    def expense_scene_code(self, value):
        self._expense_scene_code = value
    @property
    def expense_type(self):
        return self._expense_type

    @expense_type.setter
    def expense_type(self, value):
        self._expense_type = value
    @property
    def expense_type_sub_category(self):
        return self._expense_type_sub_category

    @expense_type_sub_category.setter
    def expense_type_sub_category(self, value):
        self._expense_type_sub_category = value
    @property
    def ext_infos(self):
        return self._ext_infos

    @ext_infos.setter
    def ext_infos(self, value):
        self._ext_infos = value
    @property
    def fund_biz_type(self):
        return self._fund_biz_type

    @fund_biz_type.setter
    def fund_biz_type(self, value):
        self._fund_biz_type = value
    @property
    def gmt_biz_create(self):
        return self._gmt_biz_create

    @gmt_biz_create.setter
    def gmt_biz_create(self, value):
        self._gmt_biz_create = value
    @property
    def gmt_receive_pay(self):
        return self._gmt_receive_pay

    @gmt_receive_pay.setter
    def gmt_receive_pay(self, value):
        self._gmt_receive_pay = value
    @property
    def invoice_open_mode(self):
        return self._invoice_open_mode

    @invoice_open_mode.setter
    def invoice_open_mode(self, value):
        self._invoice_open_mode = value
    @property
    def merchant_id(self):
        return self._merchant_id

    @merchant_id.setter
    def merchant_id(self, value):
        self._merchant_id = value
    @property
    def merchant_name(self):
        return self._merchant_name

    @merchant_name.setter
    def merchant_name(self, value):
        self._merchant_name = value
    @property
    def open_id(self):
        return self._open_id

    @open_id.setter
    def open_id(self, value):
        self._open_id = value
    @property
    def opposite_full_name(self):
        return self._opposite_full_name

    @opposite_full_name.setter
    def opposite_full_name(self, value):
        self._opposite_full_name = value
    @property
    def order_complete_label(self):
        return self._order_complete_label

    @order_complete_label.setter
    def order_complete_label(self, value):
        self._order_complete_label = value
    @property
    def order_complete_time(self):
        return self._order_complete_time

    @order_complete_time.setter
    def order_complete_time(self, value):
        self._order_complete_time = value
    @property
    def pay_no(self):
        return self._pay_no

    @pay_no.setter
    def pay_no(self, value):
        self._pay_no = value
    @property
    def payer_card_no(self):
        return self._payer_card_no

    @payer_card_no.setter
    def payer_card_no(self, value):
        self._payer_card_no = value
    @property
    def payer_logon_id(self):
        return self._payer_logon_id

    @payer_logon_id.setter
    def payer_logon_id(self, value):
        self._payer_logon_id = value
    @property
    def payer_name(self):
        return self._payer_name

    @payer_name.setter
    def payer_name(self, value):
        self._payer_name = value
    @property
    def peer_pay_amount(self):
        return self._peer_pay_amount

    @peer_pay_amount.setter
    def peer_pay_amount(self, value):
        self._peer_pay_amount = value
    @property
    def peer_payer_card_no(self):
        return self._peer_payer_card_no

    @peer_payer_card_no.setter
    def peer_payer_card_no(self, value):
        self._peer_payer_card_no = value
    @property
    def peer_refund_amount(self):
        return self._peer_refund_amount

    @peer_refund_amount.setter
    def peer_refund_amount(self, value):
        self._peer_refund_amount = value
    @property
    def peer_refund_status(self):
        return self._peer_refund_status

    @peer_refund_status.setter
    def peer_refund_status(self, value):
        self._peer_refund_status = value
    @property
    def related_pay_no(self):
        return self._related_pay_no

    @related_pay_no.setter
    def related_pay_no(self, value):
        self._related_pay_no = value
    @property
    def scene_code(self):
        return self._scene_code

    @scene_code.setter
    def scene_code(self, value):
        self._scene_code = value
    @property
    def seller_id(self):
        return self._seller_id

    @seller_id.setter
    def seller_id(self, value):
        self._seller_id = value
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
    def summary_apply_id(self):
        return self._summary_apply_id

    @summary_apply_id.setter
    def summary_apply_id(self, value):
        self._summary_apply_id = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.account_id:
            if hasattr(self.account_id, 'to_alipay_dict'):
                params['account_id'] = self.account_id.to_alipay_dict()
            else:
                params['account_id'] = self.account_id
        if self.agreement_peer_payer_id:
            if hasattr(self.agreement_peer_payer_id, 'to_alipay_dict'):
                params['agreement_peer_payer_id'] = self.agreement_peer_payer_id.to_alipay_dict()
            else:
                params['agreement_peer_payer_id'] = self.agreement_peer_payer_id
        if self.benefit_amount:
            if hasattr(self.benefit_amount, 'to_alipay_dict'):
                params['benefit_amount'] = self.benefit_amount.to_alipay_dict()
            else:
                params['benefit_amount'] = self.benefit_amount
        if self.biz_out_no:
            if hasattr(self.biz_out_no, 'to_alipay_dict'):
                params['biz_out_no'] = self.biz_out_no.to_alipay_dict()
            else:
                params['biz_out_no'] = self.biz_out_no
        if self.category_name:
            if hasattr(self.category_name, 'to_alipay_dict'):
                params['category_name'] = self.category_name.to_alipay_dict()
            else:
                params['category_name'] = self.category_name
        if self.consume_amount:
            if hasattr(self.consume_amount, 'to_alipay_dict'):
                params['consume_amount'] = self.consume_amount.to_alipay_dict()
            else:
                params['consume_amount'] = self.consume_amount
        if self.consume_biz_type:
            if hasattr(self.consume_biz_type, 'to_alipay_dict'):
                params['consume_biz_type'] = self.consume_biz_type.to_alipay_dict()
            else:
                params['consume_biz_type'] = self.consume_biz_type
        if self.consume_category:
            if hasattr(self.consume_category, 'to_alipay_dict'):
                params['consume_category'] = self.consume_category.to_alipay_dict()
            else:
                params['consume_category'] = self.consume_category
        if self.consume_fee_with_discount:
            if hasattr(self.consume_fee_with_discount, 'to_alipay_dict'):
                params['consume_fee_with_discount'] = self.consume_fee_with_discount.to_alipay_dict()
            else:
                params['consume_fee_with_discount'] = self.consume_fee_with_discount
        if self.consume_memo:
            if hasattr(self.consume_memo, 'to_alipay_dict'):
                params['consume_memo'] = self.consume_memo.to_alipay_dict()
            else:
                params['consume_memo'] = self.consume_memo
        if self.consume_type:
            if hasattr(self.consume_type, 'to_alipay_dict'):
                params['consume_type'] = self.consume_type.to_alipay_dict()
            else:
                params['consume_type'] = self.consume_type
        if self.employee_id:
            if hasattr(self.employee_id, 'to_alipay_dict'):
                params['employee_id'] = self.employee_id.to_alipay_dict()
            else:
                params['employee_id'] = self.employee_id
        if self.enterprise_id:
            if hasattr(self.enterprise_id, 'to_alipay_dict'):
                params['enterprise_id'] = self.enterprise_id.to_alipay_dict()
            else:
                params['enterprise_id'] = self.enterprise_id
        if self.expense_rule_group_id:
            if hasattr(self.expense_rule_group_id, 'to_alipay_dict'):
                params['expense_rule_group_id'] = self.expense_rule_group_id.to_alipay_dict()
            else:
                params['expense_rule_group_id'] = self.expense_rule_group_id
        if self.expense_scene_code:
            if hasattr(self.expense_scene_code, 'to_alipay_dict'):
                params['expense_scene_code'] = self.expense_scene_code.to_alipay_dict()
            else:
                params['expense_scene_code'] = self.expense_scene_code
        if self.expense_type:
            if hasattr(self.expense_type, 'to_alipay_dict'):
                params['expense_type'] = self.expense_type.to_alipay_dict()
            else:
                params['expense_type'] = self.expense_type
        if self.expense_type_sub_category:
            if hasattr(self.expense_type_sub_category, 'to_alipay_dict'):
                params['expense_type_sub_category'] = self.expense_type_sub_category.to_alipay_dict()
            else:
                params['expense_type_sub_category'] = self.expense_type_sub_category
        if self.ext_infos:
            if hasattr(self.ext_infos, 'to_alipay_dict'):
                params['ext_infos'] = self.ext_infos.to_alipay_dict()
            else:
                params['ext_infos'] = self.ext_infos
        if self.fund_biz_type:
            if hasattr(self.fund_biz_type, 'to_alipay_dict'):
                params['fund_biz_type'] = self.fund_biz_type.to_alipay_dict()
            else:
                params['fund_biz_type'] = self.fund_biz_type
        if self.gmt_biz_create:
            if hasattr(self.gmt_biz_create, 'to_alipay_dict'):
                params['gmt_biz_create'] = self.gmt_biz_create.to_alipay_dict()
            else:
                params['gmt_biz_create'] = self.gmt_biz_create
        if self.gmt_receive_pay:
            if hasattr(self.gmt_receive_pay, 'to_alipay_dict'):
                params['gmt_receive_pay'] = self.gmt_receive_pay.to_alipay_dict()
            else:
                params['gmt_receive_pay'] = self.gmt_receive_pay
        if self.invoice_open_mode:
            if hasattr(self.invoice_open_mode, 'to_alipay_dict'):
                params['invoice_open_mode'] = self.invoice_open_mode.to_alipay_dict()
            else:
                params['invoice_open_mode'] = self.invoice_open_mode
        if self.merchant_id:
            if hasattr(self.merchant_id, 'to_alipay_dict'):
                params['merchant_id'] = self.merchant_id.to_alipay_dict()
            else:
                params['merchant_id'] = self.merchant_id
        if self.merchant_name:
            if hasattr(self.merchant_name, 'to_alipay_dict'):
                params['merchant_name'] = self.merchant_name.to_alipay_dict()
            else:
                params['merchant_name'] = self.merchant_name
        if self.open_id:
            if hasattr(self.open_id, 'to_alipay_dict'):
                params['open_id'] = self.open_id.to_alipay_dict()
            else:
                params['open_id'] = self.open_id
        if self.opposite_full_name:
            if hasattr(self.opposite_full_name, 'to_alipay_dict'):
                params['opposite_full_name'] = self.opposite_full_name.to_alipay_dict()
            else:
                params['opposite_full_name'] = self.opposite_full_name
        if self.order_complete_label:
            if hasattr(self.order_complete_label, 'to_alipay_dict'):
                params['order_complete_label'] = self.order_complete_label.to_alipay_dict()
            else:
                params['order_complete_label'] = self.order_complete_label
        if self.order_complete_time:
            if hasattr(self.order_complete_time, 'to_alipay_dict'):
                params['order_complete_time'] = self.order_complete_time.to_alipay_dict()
            else:
                params['order_complete_time'] = self.order_complete_time
        if self.pay_no:
            if hasattr(self.pay_no, 'to_alipay_dict'):
                params['pay_no'] = self.pay_no.to_alipay_dict()
            else:
                params['pay_no'] = self.pay_no
        if self.payer_card_no:
            if hasattr(self.payer_card_no, 'to_alipay_dict'):
                params['payer_card_no'] = self.payer_card_no.to_alipay_dict()
            else:
                params['payer_card_no'] = self.payer_card_no
        if self.payer_logon_id:
            if hasattr(self.payer_logon_id, 'to_alipay_dict'):
                params['payer_logon_id'] = self.payer_logon_id.to_alipay_dict()
            else:
                params['payer_logon_id'] = self.payer_logon_id
        if self.payer_name:
            if hasattr(self.payer_name, 'to_alipay_dict'):
                params['payer_name'] = self.payer_name.to_alipay_dict()
            else:
                params['payer_name'] = self.payer_name
        if self.peer_pay_amount:
            if hasattr(self.peer_pay_amount, 'to_alipay_dict'):
                params['peer_pay_amount'] = self.peer_pay_amount.to_alipay_dict()
            else:
                params['peer_pay_amount'] = self.peer_pay_amount
        if self.peer_payer_card_no:
            if hasattr(self.peer_payer_card_no, 'to_alipay_dict'):
                params['peer_payer_card_no'] = self.peer_payer_card_no.to_alipay_dict()
            else:
                params['peer_payer_card_no'] = self.peer_payer_card_no
        if self.peer_refund_amount:
            if hasattr(self.peer_refund_amount, 'to_alipay_dict'):
                params['peer_refund_amount'] = self.peer_refund_amount.to_alipay_dict()
            else:
                params['peer_refund_amount'] = self.peer_refund_amount
        if self.peer_refund_status:
            if hasattr(self.peer_refund_status, 'to_alipay_dict'):
                params['peer_refund_status'] = self.peer_refund_status.to_alipay_dict()
            else:
                params['peer_refund_status'] = self.peer_refund_status
        if self.related_pay_no:
            if hasattr(self.related_pay_no, 'to_alipay_dict'):
                params['related_pay_no'] = self.related_pay_no.to_alipay_dict()
            else:
                params['related_pay_no'] = self.related_pay_no
        if self.scene_code:
            if hasattr(self.scene_code, 'to_alipay_dict'):
                params['scene_code'] = self.scene_code.to_alipay_dict()
            else:
                params['scene_code'] = self.scene_code
        if self.seller_id:
            if hasattr(self.seller_id, 'to_alipay_dict'):
                params['seller_id'] = self.seller_id.to_alipay_dict()
            else:
                params['seller_id'] = self.seller_id
        if self.shop_id:
            if hasattr(self.shop_id, 'to_alipay_dict'):
                params['shop_id'] = self.shop_id.to_alipay_dict()
            else:
                params['shop_id'] = self.shop_id
        if self.store_id:
            if hasattr(self.store_id, 'to_alipay_dict'):
                params['store_id'] = self.store_id.to_alipay_dict()
            else:
                params['store_id'] = self.store_id
        if self.summary_apply_id:
            if hasattr(self.summary_apply_id, 'to_alipay_dict'):
                params['summary_apply_id'] = self.summary_apply_id.to_alipay_dict()
            else:
                params['summary_apply_id'] = self.summary_apply_id
        if self.user_id:
            if hasattr(self.user_id, 'to_alipay_dict'):
                params['user_id'] = self.user_id.to_alipay_dict()
            else:
                params['user_id'] = self.user_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = EcConsumeInfo()
        if 'account_id' in d:
            o.account_id = d['account_id']
        if 'agreement_peer_payer_id' in d:
            o.agreement_peer_payer_id = d['agreement_peer_payer_id']
        if 'benefit_amount' in d:
            o.benefit_amount = d['benefit_amount']
        if 'biz_out_no' in d:
            o.biz_out_no = d['biz_out_no']
        if 'category_name' in d:
            o.category_name = d['category_name']
        if 'consume_amount' in d:
            o.consume_amount = d['consume_amount']
        if 'consume_biz_type' in d:
            o.consume_biz_type = d['consume_biz_type']
        if 'consume_category' in d:
            o.consume_category = d['consume_category']
        if 'consume_fee_with_discount' in d:
            o.consume_fee_with_discount = d['consume_fee_with_discount']
        if 'consume_memo' in d:
            o.consume_memo = d['consume_memo']
        if 'consume_type' in d:
            o.consume_type = d['consume_type']
        if 'employee_id' in d:
            o.employee_id = d['employee_id']
        if 'enterprise_id' in d:
            o.enterprise_id = d['enterprise_id']
        if 'expense_rule_group_id' in d:
            o.expense_rule_group_id = d['expense_rule_group_id']
        if 'expense_scene_code' in d:
            o.expense_scene_code = d['expense_scene_code']
        if 'expense_type' in d:
            o.expense_type = d['expense_type']
        if 'expense_type_sub_category' in d:
            o.expense_type_sub_category = d['expense_type_sub_category']
        if 'ext_infos' in d:
            o.ext_infos = d['ext_infos']
        if 'fund_biz_type' in d:
            o.fund_biz_type = d['fund_biz_type']
        if 'gmt_biz_create' in d:
            o.gmt_biz_create = d['gmt_biz_create']
        if 'gmt_receive_pay' in d:
            o.gmt_receive_pay = d['gmt_receive_pay']
        if 'invoice_open_mode' in d:
            o.invoice_open_mode = d['invoice_open_mode']
        if 'merchant_id' in d:
            o.merchant_id = d['merchant_id']
        if 'merchant_name' in d:
            o.merchant_name = d['merchant_name']
        if 'open_id' in d:
            o.open_id = d['open_id']
        if 'opposite_full_name' in d:
            o.opposite_full_name = d['opposite_full_name']
        if 'order_complete_label' in d:
            o.order_complete_label = d['order_complete_label']
        if 'order_complete_time' in d:
            o.order_complete_time = d['order_complete_time']
        if 'pay_no' in d:
            o.pay_no = d['pay_no']
        if 'payer_card_no' in d:
            o.payer_card_no = d['payer_card_no']
        if 'payer_logon_id' in d:
            o.payer_logon_id = d['payer_logon_id']
        if 'payer_name' in d:
            o.payer_name = d['payer_name']
        if 'peer_pay_amount' in d:
            o.peer_pay_amount = d['peer_pay_amount']
        if 'peer_payer_card_no' in d:
            o.peer_payer_card_no = d['peer_payer_card_no']
        if 'peer_refund_amount' in d:
            o.peer_refund_amount = d['peer_refund_amount']
        if 'peer_refund_status' in d:
            o.peer_refund_status = d['peer_refund_status']
        if 'related_pay_no' in d:
            o.related_pay_no = d['related_pay_no']
        if 'scene_code' in d:
            o.scene_code = d['scene_code']
        if 'seller_id' in d:
            o.seller_id = d['seller_id']
        if 'shop_id' in d:
            o.shop_id = d['shop_id']
        if 'store_id' in d:
            o.store_id = d['store_id']
        if 'summary_apply_id' in d:
            o.summary_apply_id = d['summary_apply_id']
        if 'user_id' in d:
            o.user_id = d['user_id']
        return o


