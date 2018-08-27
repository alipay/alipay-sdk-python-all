#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ConsumeRecordAOPModel(object):

    def __init__(self):
        self._access_channel = None
        self._additional_status = None
        self._biz_actions = None
        self._biz_extra_no = None
        self._biz_in_no = None
        self._biz_memo = None
        self._biz_orig = None
        self._biz_out_no = None
        self._biz_state = None
        self._biz_sub_type = None
        self._biz_type = None
        self._category_id = None
        self._consume_fee = None
        self._consume_refund_status = None
        self._consume_site = None
        self._consume_status = None
        self._consume_title = None
        self._consume_type = None
        self._currency = None
        self._delete_over_time = None
        self._delete_time = None
        self._delete_type = None
        self._depositback_status = None
        self._flag_locked = None
        self._flag_refund = None
        self._gmt_biz_create = None
        self._gmt_biz_modified = None
        self._gmt_create = None
        self._gmt_modified = None
        self._gmt_receive_pay = None
        self._gmt_send_pay = None
        self._has_fund_item = None
        self._has_new_fund_item = None
        self._in_out = None
        self._opposite_card_no = None
        self._opposite_login_id = None
        self._opposite_name = None
        self._opposite_nick_name = None
        self._orig_consume_title = None
        self._owner_card_no = None
        self._owner_customer_id = None
        self._owner_login_id = None
        self._owner_name = None
        self._owner_nick = None
        self._partner_id = None
        self._pay_channel = None
        self._peerpayer_real_name = None
        self._product = None
        self._refund_fee = None
        self._service_fee = None
        self._total_refund_fee = None
        self._trade_from = None

    @property
    def access_channel(self):
        return self._access_channel

    @access_channel.setter
    def access_channel(self, value):
        self._access_channel = value
    @property
    def additional_status(self):
        return self._additional_status

    @additional_status.setter
    def additional_status(self, value):
        self._additional_status = value
    @property
    def biz_actions(self):
        return self._biz_actions

    @biz_actions.setter
    def biz_actions(self, value):
        if isinstance(value, list):
            self._biz_actions = list()
            for i in value:
                self._biz_actions.append(i)
    @property
    def biz_extra_no(self):
        return self._biz_extra_no

    @biz_extra_no.setter
    def biz_extra_no(self, value):
        self._biz_extra_no = value
    @property
    def biz_in_no(self):
        return self._biz_in_no

    @biz_in_no.setter
    def biz_in_no(self, value):
        self._biz_in_no = value
    @property
    def biz_memo(self):
        return self._biz_memo

    @biz_memo.setter
    def biz_memo(self, value):
        self._biz_memo = value
    @property
    def biz_orig(self):
        return self._biz_orig

    @biz_orig.setter
    def biz_orig(self, value):
        self._biz_orig = value
    @property
    def biz_out_no(self):
        return self._biz_out_no

    @biz_out_no.setter
    def biz_out_no(self, value):
        self._biz_out_no = value
    @property
    def biz_state(self):
        return self._biz_state

    @biz_state.setter
    def biz_state(self, value):
        self._biz_state = value
    @property
    def biz_sub_type(self):
        return self._biz_sub_type

    @biz_sub_type.setter
    def biz_sub_type(self, value):
        self._biz_sub_type = value
    @property
    def biz_type(self):
        return self._biz_type

    @biz_type.setter
    def biz_type(self, value):
        self._biz_type = value
    @property
    def category_id(self):
        return self._category_id

    @category_id.setter
    def category_id(self, value):
        self._category_id = value
    @property
    def consume_fee(self):
        return self._consume_fee

    @consume_fee.setter
    def consume_fee(self, value):
        self._consume_fee = value
    @property
    def consume_refund_status(self):
        return self._consume_refund_status

    @consume_refund_status.setter
    def consume_refund_status(self, value):
        self._consume_refund_status = value
    @property
    def consume_site(self):
        return self._consume_site

    @consume_site.setter
    def consume_site(self, value):
        self._consume_site = value
    @property
    def consume_status(self):
        return self._consume_status

    @consume_status.setter
    def consume_status(self, value):
        self._consume_status = value
    @property
    def consume_title(self):
        return self._consume_title

    @consume_title.setter
    def consume_title(self, value):
        self._consume_title = value
    @property
    def consume_type(self):
        return self._consume_type

    @consume_type.setter
    def consume_type(self, value):
        self._consume_type = value
    @property
    def currency(self):
        return self._currency

    @currency.setter
    def currency(self, value):
        self._currency = value
    @property
    def delete_over_time(self):
        return self._delete_over_time

    @delete_over_time.setter
    def delete_over_time(self, value):
        self._delete_over_time = value
    @property
    def delete_time(self):
        return self._delete_time

    @delete_time.setter
    def delete_time(self, value):
        self._delete_time = value
    @property
    def delete_type(self):
        return self._delete_type

    @delete_type.setter
    def delete_type(self, value):
        self._delete_type = value
    @property
    def depositback_status(self):
        return self._depositback_status

    @depositback_status.setter
    def depositback_status(self, value):
        self._depositback_status = value
    @property
    def flag_locked(self):
        return self._flag_locked

    @flag_locked.setter
    def flag_locked(self, value):
        self._flag_locked = value
    @property
    def flag_refund(self):
        return self._flag_refund

    @flag_refund.setter
    def flag_refund(self, value):
        self._flag_refund = value
    @property
    def gmt_biz_create(self):
        return self._gmt_biz_create

    @gmt_biz_create.setter
    def gmt_biz_create(self, value):
        self._gmt_biz_create = value
    @property
    def gmt_biz_modified(self):
        return self._gmt_biz_modified

    @gmt_biz_modified.setter
    def gmt_biz_modified(self, value):
        self._gmt_biz_modified = value
    @property
    def gmt_create(self):
        return self._gmt_create

    @gmt_create.setter
    def gmt_create(self, value):
        self._gmt_create = value
    @property
    def gmt_modified(self):
        return self._gmt_modified

    @gmt_modified.setter
    def gmt_modified(self, value):
        self._gmt_modified = value
    @property
    def gmt_receive_pay(self):
        return self._gmt_receive_pay

    @gmt_receive_pay.setter
    def gmt_receive_pay(self, value):
        self._gmt_receive_pay = value
    @property
    def gmt_send_pay(self):
        return self._gmt_send_pay

    @gmt_send_pay.setter
    def gmt_send_pay(self, value):
        self._gmt_send_pay = value
    @property
    def has_fund_item(self):
        return self._has_fund_item

    @has_fund_item.setter
    def has_fund_item(self, value):
        self._has_fund_item = value
    @property
    def has_new_fund_item(self):
        return self._has_new_fund_item

    @has_new_fund_item.setter
    def has_new_fund_item(self, value):
        self._has_new_fund_item = value
    @property
    def in_out(self):
        return self._in_out

    @in_out.setter
    def in_out(self, value):
        self._in_out = value
    @property
    def opposite_card_no(self):
        return self._opposite_card_no

    @opposite_card_no.setter
    def opposite_card_no(self, value):
        self._opposite_card_no = value
    @property
    def opposite_login_id(self):
        return self._opposite_login_id

    @opposite_login_id.setter
    def opposite_login_id(self, value):
        self._opposite_login_id = value
    @property
    def opposite_name(self):
        return self._opposite_name

    @opposite_name.setter
    def opposite_name(self, value):
        self._opposite_name = value
    @property
    def opposite_nick_name(self):
        return self._opposite_nick_name

    @opposite_nick_name.setter
    def opposite_nick_name(self, value):
        self._opposite_nick_name = value
    @property
    def orig_consume_title(self):
        return self._orig_consume_title

    @orig_consume_title.setter
    def orig_consume_title(self, value):
        self._orig_consume_title = value
    @property
    def owner_card_no(self):
        return self._owner_card_no

    @owner_card_no.setter
    def owner_card_no(self, value):
        self._owner_card_no = value
    @property
    def owner_customer_id(self):
        return self._owner_customer_id

    @owner_customer_id.setter
    def owner_customer_id(self, value):
        self._owner_customer_id = value
    @property
    def owner_login_id(self):
        return self._owner_login_id

    @owner_login_id.setter
    def owner_login_id(self, value):
        self._owner_login_id = value
    @property
    def owner_name(self):
        return self._owner_name

    @owner_name.setter
    def owner_name(self, value):
        self._owner_name = value
    @property
    def owner_nick(self):
        return self._owner_nick

    @owner_nick.setter
    def owner_nick(self, value):
        self._owner_nick = value
    @property
    def partner_id(self):
        return self._partner_id

    @partner_id.setter
    def partner_id(self, value):
        self._partner_id = value
    @property
    def pay_channel(self):
        return self._pay_channel

    @pay_channel.setter
    def pay_channel(self, value):
        self._pay_channel = value
    @property
    def peerpayer_real_name(self):
        return self._peerpayer_real_name

    @peerpayer_real_name.setter
    def peerpayer_real_name(self, value):
        self._peerpayer_real_name = value
    @property
    def product(self):
        return self._product

    @product.setter
    def product(self, value):
        self._product = value
    @property
    def refund_fee(self):
        return self._refund_fee

    @refund_fee.setter
    def refund_fee(self, value):
        self._refund_fee = value
    @property
    def service_fee(self):
        return self._service_fee

    @service_fee.setter
    def service_fee(self, value):
        self._service_fee = value
    @property
    def total_refund_fee(self):
        return self._total_refund_fee

    @total_refund_fee.setter
    def total_refund_fee(self, value):
        self._total_refund_fee = value
    @property
    def trade_from(self):
        return self._trade_from

    @trade_from.setter
    def trade_from(self, value):
        self._trade_from = value


    def to_alipay_dict(self):
        params = dict()
        if self.access_channel:
            if hasattr(self.access_channel, 'to_alipay_dict'):
                params['access_channel'] = self.access_channel.to_alipay_dict()
            else:
                params['access_channel'] = self.access_channel
        if self.additional_status:
            if hasattr(self.additional_status, 'to_alipay_dict'):
                params['additional_status'] = self.additional_status.to_alipay_dict()
            else:
                params['additional_status'] = self.additional_status
        if self.biz_actions:
            if isinstance(self.biz_actions, list):
                for i in range(0, len(self.biz_actions)):
                    element = self.biz_actions[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.biz_actions[i] = element.to_alipay_dict()
            if hasattr(self.biz_actions, 'to_alipay_dict'):
                params['biz_actions'] = self.biz_actions.to_alipay_dict()
            else:
                params['biz_actions'] = self.biz_actions
        if self.biz_extra_no:
            if hasattr(self.biz_extra_no, 'to_alipay_dict'):
                params['biz_extra_no'] = self.biz_extra_no.to_alipay_dict()
            else:
                params['biz_extra_no'] = self.biz_extra_no
        if self.biz_in_no:
            if hasattr(self.biz_in_no, 'to_alipay_dict'):
                params['biz_in_no'] = self.biz_in_no.to_alipay_dict()
            else:
                params['biz_in_no'] = self.biz_in_no
        if self.biz_memo:
            if hasattr(self.biz_memo, 'to_alipay_dict'):
                params['biz_memo'] = self.biz_memo.to_alipay_dict()
            else:
                params['biz_memo'] = self.biz_memo
        if self.biz_orig:
            if hasattr(self.biz_orig, 'to_alipay_dict'):
                params['biz_orig'] = self.biz_orig.to_alipay_dict()
            else:
                params['biz_orig'] = self.biz_orig
        if self.biz_out_no:
            if hasattr(self.biz_out_no, 'to_alipay_dict'):
                params['biz_out_no'] = self.biz_out_no.to_alipay_dict()
            else:
                params['biz_out_no'] = self.biz_out_no
        if self.biz_state:
            if hasattr(self.biz_state, 'to_alipay_dict'):
                params['biz_state'] = self.biz_state.to_alipay_dict()
            else:
                params['biz_state'] = self.biz_state
        if self.biz_sub_type:
            if hasattr(self.biz_sub_type, 'to_alipay_dict'):
                params['biz_sub_type'] = self.biz_sub_type.to_alipay_dict()
            else:
                params['biz_sub_type'] = self.biz_sub_type
        if self.biz_type:
            if hasattr(self.biz_type, 'to_alipay_dict'):
                params['biz_type'] = self.biz_type.to_alipay_dict()
            else:
                params['biz_type'] = self.biz_type
        if self.category_id:
            if hasattr(self.category_id, 'to_alipay_dict'):
                params['category_id'] = self.category_id.to_alipay_dict()
            else:
                params['category_id'] = self.category_id
        if self.consume_fee:
            if hasattr(self.consume_fee, 'to_alipay_dict'):
                params['consume_fee'] = self.consume_fee.to_alipay_dict()
            else:
                params['consume_fee'] = self.consume_fee
        if self.consume_refund_status:
            if hasattr(self.consume_refund_status, 'to_alipay_dict'):
                params['consume_refund_status'] = self.consume_refund_status.to_alipay_dict()
            else:
                params['consume_refund_status'] = self.consume_refund_status
        if self.consume_site:
            if hasattr(self.consume_site, 'to_alipay_dict'):
                params['consume_site'] = self.consume_site.to_alipay_dict()
            else:
                params['consume_site'] = self.consume_site
        if self.consume_status:
            if hasattr(self.consume_status, 'to_alipay_dict'):
                params['consume_status'] = self.consume_status.to_alipay_dict()
            else:
                params['consume_status'] = self.consume_status
        if self.consume_title:
            if hasattr(self.consume_title, 'to_alipay_dict'):
                params['consume_title'] = self.consume_title.to_alipay_dict()
            else:
                params['consume_title'] = self.consume_title
        if self.consume_type:
            if hasattr(self.consume_type, 'to_alipay_dict'):
                params['consume_type'] = self.consume_type.to_alipay_dict()
            else:
                params['consume_type'] = self.consume_type
        if self.currency:
            if hasattr(self.currency, 'to_alipay_dict'):
                params['currency'] = self.currency.to_alipay_dict()
            else:
                params['currency'] = self.currency
        if self.delete_over_time:
            if hasattr(self.delete_over_time, 'to_alipay_dict'):
                params['delete_over_time'] = self.delete_over_time.to_alipay_dict()
            else:
                params['delete_over_time'] = self.delete_over_time
        if self.delete_time:
            if hasattr(self.delete_time, 'to_alipay_dict'):
                params['delete_time'] = self.delete_time.to_alipay_dict()
            else:
                params['delete_time'] = self.delete_time
        if self.delete_type:
            if hasattr(self.delete_type, 'to_alipay_dict'):
                params['delete_type'] = self.delete_type.to_alipay_dict()
            else:
                params['delete_type'] = self.delete_type
        if self.depositback_status:
            if hasattr(self.depositback_status, 'to_alipay_dict'):
                params['depositback_status'] = self.depositback_status.to_alipay_dict()
            else:
                params['depositback_status'] = self.depositback_status
        if self.flag_locked:
            if hasattr(self.flag_locked, 'to_alipay_dict'):
                params['flag_locked'] = self.flag_locked.to_alipay_dict()
            else:
                params['flag_locked'] = self.flag_locked
        if self.flag_refund:
            if hasattr(self.flag_refund, 'to_alipay_dict'):
                params['flag_refund'] = self.flag_refund.to_alipay_dict()
            else:
                params['flag_refund'] = self.flag_refund
        if self.gmt_biz_create:
            if hasattr(self.gmt_biz_create, 'to_alipay_dict'):
                params['gmt_biz_create'] = self.gmt_biz_create.to_alipay_dict()
            else:
                params['gmt_biz_create'] = self.gmt_biz_create
        if self.gmt_biz_modified:
            if hasattr(self.gmt_biz_modified, 'to_alipay_dict'):
                params['gmt_biz_modified'] = self.gmt_biz_modified.to_alipay_dict()
            else:
                params['gmt_biz_modified'] = self.gmt_biz_modified
        if self.gmt_create:
            if hasattr(self.gmt_create, 'to_alipay_dict'):
                params['gmt_create'] = self.gmt_create.to_alipay_dict()
            else:
                params['gmt_create'] = self.gmt_create
        if self.gmt_modified:
            if hasattr(self.gmt_modified, 'to_alipay_dict'):
                params['gmt_modified'] = self.gmt_modified.to_alipay_dict()
            else:
                params['gmt_modified'] = self.gmt_modified
        if self.gmt_receive_pay:
            if hasattr(self.gmt_receive_pay, 'to_alipay_dict'):
                params['gmt_receive_pay'] = self.gmt_receive_pay.to_alipay_dict()
            else:
                params['gmt_receive_pay'] = self.gmt_receive_pay
        if self.gmt_send_pay:
            if hasattr(self.gmt_send_pay, 'to_alipay_dict'):
                params['gmt_send_pay'] = self.gmt_send_pay.to_alipay_dict()
            else:
                params['gmt_send_pay'] = self.gmt_send_pay
        if self.has_fund_item:
            if hasattr(self.has_fund_item, 'to_alipay_dict'):
                params['has_fund_item'] = self.has_fund_item.to_alipay_dict()
            else:
                params['has_fund_item'] = self.has_fund_item
        if self.has_new_fund_item:
            if hasattr(self.has_new_fund_item, 'to_alipay_dict'):
                params['has_new_fund_item'] = self.has_new_fund_item.to_alipay_dict()
            else:
                params['has_new_fund_item'] = self.has_new_fund_item
        if self.in_out:
            if hasattr(self.in_out, 'to_alipay_dict'):
                params['in_out'] = self.in_out.to_alipay_dict()
            else:
                params['in_out'] = self.in_out
        if self.opposite_card_no:
            if hasattr(self.opposite_card_no, 'to_alipay_dict'):
                params['opposite_card_no'] = self.opposite_card_no.to_alipay_dict()
            else:
                params['opposite_card_no'] = self.opposite_card_no
        if self.opposite_login_id:
            if hasattr(self.opposite_login_id, 'to_alipay_dict'):
                params['opposite_login_id'] = self.opposite_login_id.to_alipay_dict()
            else:
                params['opposite_login_id'] = self.opposite_login_id
        if self.opposite_name:
            if hasattr(self.opposite_name, 'to_alipay_dict'):
                params['opposite_name'] = self.opposite_name.to_alipay_dict()
            else:
                params['opposite_name'] = self.opposite_name
        if self.opposite_nick_name:
            if hasattr(self.opposite_nick_name, 'to_alipay_dict'):
                params['opposite_nick_name'] = self.opposite_nick_name.to_alipay_dict()
            else:
                params['opposite_nick_name'] = self.opposite_nick_name
        if self.orig_consume_title:
            if hasattr(self.orig_consume_title, 'to_alipay_dict'):
                params['orig_consume_title'] = self.orig_consume_title.to_alipay_dict()
            else:
                params['orig_consume_title'] = self.orig_consume_title
        if self.owner_card_no:
            if hasattr(self.owner_card_no, 'to_alipay_dict'):
                params['owner_card_no'] = self.owner_card_no.to_alipay_dict()
            else:
                params['owner_card_no'] = self.owner_card_no
        if self.owner_customer_id:
            if hasattr(self.owner_customer_id, 'to_alipay_dict'):
                params['owner_customer_id'] = self.owner_customer_id.to_alipay_dict()
            else:
                params['owner_customer_id'] = self.owner_customer_id
        if self.owner_login_id:
            if hasattr(self.owner_login_id, 'to_alipay_dict'):
                params['owner_login_id'] = self.owner_login_id.to_alipay_dict()
            else:
                params['owner_login_id'] = self.owner_login_id
        if self.owner_name:
            if hasattr(self.owner_name, 'to_alipay_dict'):
                params['owner_name'] = self.owner_name.to_alipay_dict()
            else:
                params['owner_name'] = self.owner_name
        if self.owner_nick:
            if hasattr(self.owner_nick, 'to_alipay_dict'):
                params['owner_nick'] = self.owner_nick.to_alipay_dict()
            else:
                params['owner_nick'] = self.owner_nick
        if self.partner_id:
            if hasattr(self.partner_id, 'to_alipay_dict'):
                params['partner_id'] = self.partner_id.to_alipay_dict()
            else:
                params['partner_id'] = self.partner_id
        if self.pay_channel:
            if hasattr(self.pay_channel, 'to_alipay_dict'):
                params['pay_channel'] = self.pay_channel.to_alipay_dict()
            else:
                params['pay_channel'] = self.pay_channel
        if self.peerpayer_real_name:
            if hasattr(self.peerpayer_real_name, 'to_alipay_dict'):
                params['peerpayer_real_name'] = self.peerpayer_real_name.to_alipay_dict()
            else:
                params['peerpayer_real_name'] = self.peerpayer_real_name
        if self.product:
            if hasattr(self.product, 'to_alipay_dict'):
                params['product'] = self.product.to_alipay_dict()
            else:
                params['product'] = self.product
        if self.refund_fee:
            if hasattr(self.refund_fee, 'to_alipay_dict'):
                params['refund_fee'] = self.refund_fee.to_alipay_dict()
            else:
                params['refund_fee'] = self.refund_fee
        if self.service_fee:
            if hasattr(self.service_fee, 'to_alipay_dict'):
                params['service_fee'] = self.service_fee.to_alipay_dict()
            else:
                params['service_fee'] = self.service_fee
        if self.total_refund_fee:
            if hasattr(self.total_refund_fee, 'to_alipay_dict'):
                params['total_refund_fee'] = self.total_refund_fee.to_alipay_dict()
            else:
                params['total_refund_fee'] = self.total_refund_fee
        if self.trade_from:
            if hasattr(self.trade_from, 'to_alipay_dict'):
                params['trade_from'] = self.trade_from.to_alipay_dict()
            else:
                params['trade_from'] = self.trade_from
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ConsumeRecordAOPModel()
        if 'access_channel' in d:
            o.access_channel = d['access_channel']
        if 'additional_status' in d:
            o.additional_status = d['additional_status']
        if 'biz_actions' in d:
            o.biz_actions = d['biz_actions']
        if 'biz_extra_no' in d:
            o.biz_extra_no = d['biz_extra_no']
        if 'biz_in_no' in d:
            o.biz_in_no = d['biz_in_no']
        if 'biz_memo' in d:
            o.biz_memo = d['biz_memo']
        if 'biz_orig' in d:
            o.biz_orig = d['biz_orig']
        if 'biz_out_no' in d:
            o.biz_out_no = d['biz_out_no']
        if 'biz_state' in d:
            o.biz_state = d['biz_state']
        if 'biz_sub_type' in d:
            o.biz_sub_type = d['biz_sub_type']
        if 'biz_type' in d:
            o.biz_type = d['biz_type']
        if 'category_id' in d:
            o.category_id = d['category_id']
        if 'consume_fee' in d:
            o.consume_fee = d['consume_fee']
        if 'consume_refund_status' in d:
            o.consume_refund_status = d['consume_refund_status']
        if 'consume_site' in d:
            o.consume_site = d['consume_site']
        if 'consume_status' in d:
            o.consume_status = d['consume_status']
        if 'consume_title' in d:
            o.consume_title = d['consume_title']
        if 'consume_type' in d:
            o.consume_type = d['consume_type']
        if 'currency' in d:
            o.currency = d['currency']
        if 'delete_over_time' in d:
            o.delete_over_time = d['delete_over_time']
        if 'delete_time' in d:
            o.delete_time = d['delete_time']
        if 'delete_type' in d:
            o.delete_type = d['delete_type']
        if 'depositback_status' in d:
            o.depositback_status = d['depositback_status']
        if 'flag_locked' in d:
            o.flag_locked = d['flag_locked']
        if 'flag_refund' in d:
            o.flag_refund = d['flag_refund']
        if 'gmt_biz_create' in d:
            o.gmt_biz_create = d['gmt_biz_create']
        if 'gmt_biz_modified' in d:
            o.gmt_biz_modified = d['gmt_biz_modified']
        if 'gmt_create' in d:
            o.gmt_create = d['gmt_create']
        if 'gmt_modified' in d:
            o.gmt_modified = d['gmt_modified']
        if 'gmt_receive_pay' in d:
            o.gmt_receive_pay = d['gmt_receive_pay']
        if 'gmt_send_pay' in d:
            o.gmt_send_pay = d['gmt_send_pay']
        if 'has_fund_item' in d:
            o.has_fund_item = d['has_fund_item']
        if 'has_new_fund_item' in d:
            o.has_new_fund_item = d['has_new_fund_item']
        if 'in_out' in d:
            o.in_out = d['in_out']
        if 'opposite_card_no' in d:
            o.opposite_card_no = d['opposite_card_no']
        if 'opposite_login_id' in d:
            o.opposite_login_id = d['opposite_login_id']
        if 'opposite_name' in d:
            o.opposite_name = d['opposite_name']
        if 'opposite_nick_name' in d:
            o.opposite_nick_name = d['opposite_nick_name']
        if 'orig_consume_title' in d:
            o.orig_consume_title = d['orig_consume_title']
        if 'owner_card_no' in d:
            o.owner_card_no = d['owner_card_no']
        if 'owner_customer_id' in d:
            o.owner_customer_id = d['owner_customer_id']
        if 'owner_login_id' in d:
            o.owner_login_id = d['owner_login_id']
        if 'owner_name' in d:
            o.owner_name = d['owner_name']
        if 'owner_nick' in d:
            o.owner_nick = d['owner_nick']
        if 'partner_id' in d:
            o.partner_id = d['partner_id']
        if 'pay_channel' in d:
            o.pay_channel = d['pay_channel']
        if 'peerpayer_real_name' in d:
            o.peerpayer_real_name = d['peerpayer_real_name']
        if 'product' in d:
            o.product = d['product']
        if 'refund_fee' in d:
            o.refund_fee = d['refund_fee']
        if 'service_fee' in d:
            o.service_fee = d['service_fee']
        if 'total_refund_fee' in d:
            o.total_refund_fee = d['total_refund_fee']
        if 'trade_from' in d:
            o.trade_from = d['trade_from']
        return o


