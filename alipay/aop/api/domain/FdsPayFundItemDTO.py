#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.PayUserInfoDTO import PayUserInfoDTO
from alipay.aop.api.domain.PayUserInfoDTO import PayUserInfoDTO


class FdsPayFundItemDTO(object):

    def __init__(self):
        self._amount = None
        self._fund_biz_info = None
        self._fund_item_id = None
        self._gmt_pay = None
        self._memo = None
        self._payee_user_info = None
        self._payer_user_info = None
        self._status = None

    @property
    def amount(self):
        return self._amount

    @amount.setter
    def amount(self, value):
        self._amount = value
    @property
    def fund_biz_info(self):
        return self._fund_biz_info

    @fund_biz_info.setter
    def fund_biz_info(self, value):
        self._fund_biz_info = value
    @property
    def fund_item_id(self):
        return self._fund_item_id

    @fund_item_id.setter
    def fund_item_id(self, value):
        self._fund_item_id = value
    @property
    def gmt_pay(self):
        return self._gmt_pay

    @gmt_pay.setter
    def gmt_pay(self, value):
        self._gmt_pay = value
    @property
    def memo(self):
        return self._memo

    @memo.setter
    def memo(self, value):
        self._memo = value
    @property
    def payee_user_info(self):
        return self._payee_user_info

    @payee_user_info.setter
    def payee_user_info(self, value):
        if isinstance(value, PayUserInfoDTO):
            self._payee_user_info = value
        else:
            self._payee_user_info = PayUserInfoDTO.from_alipay_dict(value)
    @property
    def payer_user_info(self):
        return self._payer_user_info

    @payer_user_info.setter
    def payer_user_info(self, value):
        if isinstance(value, PayUserInfoDTO):
            self._payer_user_info = value
        else:
            self._payer_user_info = PayUserInfoDTO.from_alipay_dict(value)
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value


    def to_alipay_dict(self):
        params = dict()
        if self.amount:
            if hasattr(self.amount, 'to_alipay_dict'):
                params['amount'] = self.amount.to_alipay_dict()
            else:
                params['amount'] = self.amount
        if self.fund_biz_info:
            if hasattr(self.fund_biz_info, 'to_alipay_dict'):
                params['fund_biz_info'] = self.fund_biz_info.to_alipay_dict()
            else:
                params['fund_biz_info'] = self.fund_biz_info
        if self.fund_item_id:
            if hasattr(self.fund_item_id, 'to_alipay_dict'):
                params['fund_item_id'] = self.fund_item_id.to_alipay_dict()
            else:
                params['fund_item_id'] = self.fund_item_id
        if self.gmt_pay:
            if hasattr(self.gmt_pay, 'to_alipay_dict'):
                params['gmt_pay'] = self.gmt_pay.to_alipay_dict()
            else:
                params['gmt_pay'] = self.gmt_pay
        if self.memo:
            if hasattr(self.memo, 'to_alipay_dict'):
                params['memo'] = self.memo.to_alipay_dict()
            else:
                params['memo'] = self.memo
        if self.payee_user_info:
            if hasattr(self.payee_user_info, 'to_alipay_dict'):
                params['payee_user_info'] = self.payee_user_info.to_alipay_dict()
            else:
                params['payee_user_info'] = self.payee_user_info
        if self.payer_user_info:
            if hasattr(self.payer_user_info, 'to_alipay_dict'):
                params['payer_user_info'] = self.payer_user_info.to_alipay_dict()
            else:
                params['payer_user_info'] = self.payer_user_info
        if self.status:
            if hasattr(self.status, 'to_alipay_dict'):
                params['status'] = self.status.to_alipay_dict()
            else:
                params['status'] = self.status
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = FdsPayFundItemDTO()
        if 'amount' in d:
            o.amount = d['amount']
        if 'fund_biz_info' in d:
            o.fund_biz_info = d['fund_biz_info']
        if 'fund_item_id' in d:
            o.fund_item_id = d['fund_item_id']
        if 'gmt_pay' in d:
            o.gmt_pay = d['gmt_pay']
        if 'memo' in d:
            o.memo = d['memo']
        if 'payee_user_info' in d:
            o.payee_user_info = d['payee_user_info']
        if 'payer_user_info' in d:
            o.payer_user_info = d['payer_user_info']
        if 'status' in d:
            o.status = d['status']
        return o


