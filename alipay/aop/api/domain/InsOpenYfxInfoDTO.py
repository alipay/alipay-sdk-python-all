#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class InsOpenYfxInfoDTO(object):

    def __init__(self):
        self._auction_picture_url = None
        self._auction_title = None
        self._biz_order_id = None
        self._claim_apply_time = None
        self._claim_expect_time = None
        self._claim_fee = None
        self._claim_in_account = None
        self._claim_no = None
        self._claim_refuse_code = None
        self._claim_report_no = None
        self._claim_status = None
        self._first_claim_apply_time = None
        self._issue_time = None
        self._order_gmt_create = None
        self._pay_time = None
        self._policy_no = None
        self._policy_status = None
        self._premium = None
        self._refund_goods_type = None
        self._refund_id = None
        self._refund_mail_no = None
        self._refund_post_type = None
        self._refund_status = None
        self._sum_insured = None
        self._yfx_type = None

    @property
    def auction_picture_url(self):
        return self._auction_picture_url

    @auction_picture_url.setter
    def auction_picture_url(self, value):
        self._auction_picture_url = value
    @property
    def auction_title(self):
        return self._auction_title

    @auction_title.setter
    def auction_title(self, value):
        self._auction_title = value
    @property
    def biz_order_id(self):
        return self._biz_order_id

    @biz_order_id.setter
    def biz_order_id(self, value):
        self._biz_order_id = value
    @property
    def claim_apply_time(self):
        return self._claim_apply_time

    @claim_apply_time.setter
    def claim_apply_time(self, value):
        self._claim_apply_time = value
    @property
    def claim_expect_time(self):
        return self._claim_expect_time

    @claim_expect_time.setter
    def claim_expect_time(self, value):
        self._claim_expect_time = value
    @property
    def claim_fee(self):
        return self._claim_fee

    @claim_fee.setter
    def claim_fee(self, value):
        self._claim_fee = value
    @property
    def claim_in_account(self):
        return self._claim_in_account

    @claim_in_account.setter
    def claim_in_account(self, value):
        self._claim_in_account = value
    @property
    def claim_no(self):
        return self._claim_no

    @claim_no.setter
    def claim_no(self, value):
        self._claim_no = value
    @property
    def claim_refuse_code(self):
        return self._claim_refuse_code

    @claim_refuse_code.setter
    def claim_refuse_code(self, value):
        self._claim_refuse_code = value
    @property
    def claim_report_no(self):
        return self._claim_report_no

    @claim_report_no.setter
    def claim_report_no(self, value):
        self._claim_report_no = value
    @property
    def claim_status(self):
        return self._claim_status

    @claim_status.setter
    def claim_status(self, value):
        self._claim_status = value
    @property
    def first_claim_apply_time(self):
        return self._first_claim_apply_time

    @first_claim_apply_time.setter
    def first_claim_apply_time(self, value):
        self._first_claim_apply_time = value
    @property
    def issue_time(self):
        return self._issue_time

    @issue_time.setter
    def issue_time(self, value):
        self._issue_time = value
    @property
    def order_gmt_create(self):
        return self._order_gmt_create

    @order_gmt_create.setter
    def order_gmt_create(self, value):
        self._order_gmt_create = value
    @property
    def pay_time(self):
        return self._pay_time

    @pay_time.setter
    def pay_time(self, value):
        self._pay_time = value
    @property
    def policy_no(self):
        return self._policy_no

    @policy_no.setter
    def policy_no(self, value):
        self._policy_no = value
    @property
    def policy_status(self):
        return self._policy_status

    @policy_status.setter
    def policy_status(self, value):
        self._policy_status = value
    @property
    def premium(self):
        return self._premium

    @premium.setter
    def premium(self, value):
        self._premium = value
    @property
    def refund_goods_type(self):
        return self._refund_goods_type

    @refund_goods_type.setter
    def refund_goods_type(self, value):
        self._refund_goods_type = value
    @property
    def refund_id(self):
        return self._refund_id

    @refund_id.setter
    def refund_id(self, value):
        self._refund_id = value
    @property
    def refund_mail_no(self):
        return self._refund_mail_no

    @refund_mail_no.setter
    def refund_mail_no(self, value):
        self._refund_mail_no = value
    @property
    def refund_post_type(self):
        return self._refund_post_type

    @refund_post_type.setter
    def refund_post_type(self, value):
        self._refund_post_type = value
    @property
    def refund_status(self):
        return self._refund_status

    @refund_status.setter
    def refund_status(self, value):
        self._refund_status = value
    @property
    def sum_insured(self):
        return self._sum_insured

    @sum_insured.setter
    def sum_insured(self, value):
        self._sum_insured = value
    @property
    def yfx_type(self):
        return self._yfx_type

    @yfx_type.setter
    def yfx_type(self, value):
        self._yfx_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.auction_picture_url:
            if hasattr(self.auction_picture_url, 'to_alipay_dict'):
                params['auction_picture_url'] = self.auction_picture_url.to_alipay_dict()
            else:
                params['auction_picture_url'] = self.auction_picture_url
        if self.auction_title:
            if hasattr(self.auction_title, 'to_alipay_dict'):
                params['auction_title'] = self.auction_title.to_alipay_dict()
            else:
                params['auction_title'] = self.auction_title
        if self.biz_order_id:
            if hasattr(self.biz_order_id, 'to_alipay_dict'):
                params['biz_order_id'] = self.biz_order_id.to_alipay_dict()
            else:
                params['biz_order_id'] = self.biz_order_id
        if self.claim_apply_time:
            if hasattr(self.claim_apply_time, 'to_alipay_dict'):
                params['claim_apply_time'] = self.claim_apply_time.to_alipay_dict()
            else:
                params['claim_apply_time'] = self.claim_apply_time
        if self.claim_expect_time:
            if hasattr(self.claim_expect_time, 'to_alipay_dict'):
                params['claim_expect_time'] = self.claim_expect_time.to_alipay_dict()
            else:
                params['claim_expect_time'] = self.claim_expect_time
        if self.claim_fee:
            if hasattr(self.claim_fee, 'to_alipay_dict'):
                params['claim_fee'] = self.claim_fee.to_alipay_dict()
            else:
                params['claim_fee'] = self.claim_fee
        if self.claim_in_account:
            if hasattr(self.claim_in_account, 'to_alipay_dict'):
                params['claim_in_account'] = self.claim_in_account.to_alipay_dict()
            else:
                params['claim_in_account'] = self.claim_in_account
        if self.claim_no:
            if hasattr(self.claim_no, 'to_alipay_dict'):
                params['claim_no'] = self.claim_no.to_alipay_dict()
            else:
                params['claim_no'] = self.claim_no
        if self.claim_refuse_code:
            if hasattr(self.claim_refuse_code, 'to_alipay_dict'):
                params['claim_refuse_code'] = self.claim_refuse_code.to_alipay_dict()
            else:
                params['claim_refuse_code'] = self.claim_refuse_code
        if self.claim_report_no:
            if hasattr(self.claim_report_no, 'to_alipay_dict'):
                params['claim_report_no'] = self.claim_report_no.to_alipay_dict()
            else:
                params['claim_report_no'] = self.claim_report_no
        if self.claim_status:
            if hasattr(self.claim_status, 'to_alipay_dict'):
                params['claim_status'] = self.claim_status.to_alipay_dict()
            else:
                params['claim_status'] = self.claim_status
        if self.first_claim_apply_time:
            if hasattr(self.first_claim_apply_time, 'to_alipay_dict'):
                params['first_claim_apply_time'] = self.first_claim_apply_time.to_alipay_dict()
            else:
                params['first_claim_apply_time'] = self.first_claim_apply_time
        if self.issue_time:
            if hasattr(self.issue_time, 'to_alipay_dict'):
                params['issue_time'] = self.issue_time.to_alipay_dict()
            else:
                params['issue_time'] = self.issue_time
        if self.order_gmt_create:
            if hasattr(self.order_gmt_create, 'to_alipay_dict'):
                params['order_gmt_create'] = self.order_gmt_create.to_alipay_dict()
            else:
                params['order_gmt_create'] = self.order_gmt_create
        if self.pay_time:
            if hasattr(self.pay_time, 'to_alipay_dict'):
                params['pay_time'] = self.pay_time.to_alipay_dict()
            else:
                params['pay_time'] = self.pay_time
        if self.policy_no:
            if hasattr(self.policy_no, 'to_alipay_dict'):
                params['policy_no'] = self.policy_no.to_alipay_dict()
            else:
                params['policy_no'] = self.policy_no
        if self.policy_status:
            if hasattr(self.policy_status, 'to_alipay_dict'):
                params['policy_status'] = self.policy_status.to_alipay_dict()
            else:
                params['policy_status'] = self.policy_status
        if self.premium:
            if hasattr(self.premium, 'to_alipay_dict'):
                params['premium'] = self.premium.to_alipay_dict()
            else:
                params['premium'] = self.premium
        if self.refund_goods_type:
            if hasattr(self.refund_goods_type, 'to_alipay_dict'):
                params['refund_goods_type'] = self.refund_goods_type.to_alipay_dict()
            else:
                params['refund_goods_type'] = self.refund_goods_type
        if self.refund_id:
            if hasattr(self.refund_id, 'to_alipay_dict'):
                params['refund_id'] = self.refund_id.to_alipay_dict()
            else:
                params['refund_id'] = self.refund_id
        if self.refund_mail_no:
            if hasattr(self.refund_mail_no, 'to_alipay_dict'):
                params['refund_mail_no'] = self.refund_mail_no.to_alipay_dict()
            else:
                params['refund_mail_no'] = self.refund_mail_no
        if self.refund_post_type:
            if hasattr(self.refund_post_type, 'to_alipay_dict'):
                params['refund_post_type'] = self.refund_post_type.to_alipay_dict()
            else:
                params['refund_post_type'] = self.refund_post_type
        if self.refund_status:
            if hasattr(self.refund_status, 'to_alipay_dict'):
                params['refund_status'] = self.refund_status.to_alipay_dict()
            else:
                params['refund_status'] = self.refund_status
        if self.sum_insured:
            if hasattr(self.sum_insured, 'to_alipay_dict'):
                params['sum_insured'] = self.sum_insured.to_alipay_dict()
            else:
                params['sum_insured'] = self.sum_insured
        if self.yfx_type:
            if hasattr(self.yfx_type, 'to_alipay_dict'):
                params['yfx_type'] = self.yfx_type.to_alipay_dict()
            else:
                params['yfx_type'] = self.yfx_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = InsOpenYfxInfoDTO()
        if 'auction_picture_url' in d:
            o.auction_picture_url = d['auction_picture_url']
        if 'auction_title' in d:
            o.auction_title = d['auction_title']
        if 'biz_order_id' in d:
            o.biz_order_id = d['biz_order_id']
        if 'claim_apply_time' in d:
            o.claim_apply_time = d['claim_apply_time']
        if 'claim_expect_time' in d:
            o.claim_expect_time = d['claim_expect_time']
        if 'claim_fee' in d:
            o.claim_fee = d['claim_fee']
        if 'claim_in_account' in d:
            o.claim_in_account = d['claim_in_account']
        if 'claim_no' in d:
            o.claim_no = d['claim_no']
        if 'claim_refuse_code' in d:
            o.claim_refuse_code = d['claim_refuse_code']
        if 'claim_report_no' in d:
            o.claim_report_no = d['claim_report_no']
        if 'claim_status' in d:
            o.claim_status = d['claim_status']
        if 'first_claim_apply_time' in d:
            o.first_claim_apply_time = d['first_claim_apply_time']
        if 'issue_time' in d:
            o.issue_time = d['issue_time']
        if 'order_gmt_create' in d:
            o.order_gmt_create = d['order_gmt_create']
        if 'pay_time' in d:
            o.pay_time = d['pay_time']
        if 'policy_no' in d:
            o.policy_no = d['policy_no']
        if 'policy_status' in d:
            o.policy_status = d['policy_status']
        if 'premium' in d:
            o.premium = d['premium']
        if 'refund_goods_type' in d:
            o.refund_goods_type = d['refund_goods_type']
        if 'refund_id' in d:
            o.refund_id = d['refund_id']
        if 'refund_mail_no' in d:
            o.refund_mail_no = d['refund_mail_no']
        if 'refund_post_type' in d:
            o.refund_post_type = d['refund_post_type']
        if 'refund_status' in d:
            o.refund_status = d['refund_status']
        if 'sum_insured' in d:
            o.sum_insured = d['sum_insured']
        if 'yfx_type' in d:
            o.yfx_type = d['yfx_type']
        return o


