#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayUserAlipaypointSendModel(object):

    def __init__(self):
        self._budget_code = None
        self._memo = None
        self._partner_biz_no = None
        self._point_amount = None
        self._user_account = None
        self._user_id = None

    @property
    def budget_code(self):
        return self._budget_code

    @budget_code.setter
    def budget_code(self, value):
        self._budget_code = value
    @property
    def memo(self):
        return self._memo

    @memo.setter
    def memo(self, value):
        self._memo = value
    @property
    def partner_biz_no(self):
        return self._partner_biz_no

    @partner_biz_no.setter
    def partner_biz_no(self, value):
        self._partner_biz_no = value
    @property
    def point_amount(self):
        return self._point_amount

    @point_amount.setter
    def point_amount(self, value):
        self._point_amount = value
    @property
    def user_account(self):
        return self._user_account

    @user_account.setter
    def user_account(self, value):
        self._user_account = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.budget_code:
            if hasattr(self.budget_code, 'to_alipay_dict'):
                params['budget_code'] = self.budget_code.to_alipay_dict()
            else:
                params['budget_code'] = self.budget_code
        if self.memo:
            if hasattr(self.memo, 'to_alipay_dict'):
                params['memo'] = self.memo.to_alipay_dict()
            else:
                params['memo'] = self.memo
        if self.partner_biz_no:
            if hasattr(self.partner_biz_no, 'to_alipay_dict'):
                params['partner_biz_no'] = self.partner_biz_no.to_alipay_dict()
            else:
                params['partner_biz_no'] = self.partner_biz_no
        if self.point_amount:
            if hasattr(self.point_amount, 'to_alipay_dict'):
                params['point_amount'] = self.point_amount.to_alipay_dict()
            else:
                params['point_amount'] = self.point_amount
        if self.user_account:
            if hasattr(self.user_account, 'to_alipay_dict'):
                params['user_account'] = self.user_account.to_alipay_dict()
            else:
                params['user_account'] = self.user_account
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
        o = AlipayUserAlipaypointSendModel()
        if 'budget_code' in d:
            o.budget_code = d['budget_code']
        if 'memo' in d:
            o.memo = d['memo']
        if 'partner_biz_no' in d:
            o.partner_biz_no = d['partner_biz_no']
        if 'point_amount' in d:
            o.point_amount = d['point_amount']
        if 'user_account' in d:
            o.user_account = d['user_account']
        if 'user_id' in d:
            o.user_id = d['user_id']
        return o


