#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceMedicalInsuranceClaimSyncModel(object):

    def __init__(self):
        self._advance_apply_no = None
        self._ant_apply_no = None
        self._claim_amount = None
        self._claim_detail = None
        self._claim_no = None
        self._claim_status = None
        self._claim_status_desc = None
        self._company_type = None
        self._open_id = None
        self._pay_account = None
        self._pay_time = None
        self._source = None
        self._user_id = None

    @property
    def advance_apply_no(self):
        return self._advance_apply_no

    @advance_apply_no.setter
    def advance_apply_no(self, value):
        self._advance_apply_no = value
    @property
    def ant_apply_no(self):
        return self._ant_apply_no

    @ant_apply_no.setter
    def ant_apply_no(self, value):
        self._ant_apply_no = value
    @property
    def claim_amount(self):
        return self._claim_amount

    @claim_amount.setter
    def claim_amount(self, value):
        self._claim_amount = value
    @property
    def claim_detail(self):
        return self._claim_detail

    @claim_detail.setter
    def claim_detail(self, value):
        self._claim_detail = value
    @property
    def claim_no(self):
        return self._claim_no

    @claim_no.setter
    def claim_no(self, value):
        self._claim_no = value
    @property
    def claim_status(self):
        return self._claim_status

    @claim_status.setter
    def claim_status(self, value):
        self._claim_status = value
    @property
    def claim_status_desc(self):
        return self._claim_status_desc

    @claim_status_desc.setter
    def claim_status_desc(self, value):
        self._claim_status_desc = value
    @property
    def company_type(self):
        return self._company_type

    @company_type.setter
    def company_type(self, value):
        self._company_type = value
    @property
    def open_id(self):
        return self._open_id

    @open_id.setter
    def open_id(self, value):
        self._open_id = value
    @property
    def pay_account(self):
        return self._pay_account

    @pay_account.setter
    def pay_account(self, value):
        self._pay_account = value
    @property
    def pay_time(self):
        return self._pay_time

    @pay_time.setter
    def pay_time(self, value):
        self._pay_time = value
    @property
    def source(self):
        return self._source

    @source.setter
    def source(self, value):
        self._source = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.advance_apply_no:
            if hasattr(self.advance_apply_no, 'to_alipay_dict'):
                params['advance_apply_no'] = self.advance_apply_no.to_alipay_dict()
            else:
                params['advance_apply_no'] = self.advance_apply_no
        if self.ant_apply_no:
            if hasattr(self.ant_apply_no, 'to_alipay_dict'):
                params['ant_apply_no'] = self.ant_apply_no.to_alipay_dict()
            else:
                params['ant_apply_no'] = self.ant_apply_no
        if self.claim_amount:
            if hasattr(self.claim_amount, 'to_alipay_dict'):
                params['claim_amount'] = self.claim_amount.to_alipay_dict()
            else:
                params['claim_amount'] = self.claim_amount
        if self.claim_detail:
            if hasattr(self.claim_detail, 'to_alipay_dict'):
                params['claim_detail'] = self.claim_detail.to_alipay_dict()
            else:
                params['claim_detail'] = self.claim_detail
        if self.claim_no:
            if hasattr(self.claim_no, 'to_alipay_dict'):
                params['claim_no'] = self.claim_no.to_alipay_dict()
            else:
                params['claim_no'] = self.claim_no
        if self.claim_status:
            if hasattr(self.claim_status, 'to_alipay_dict'):
                params['claim_status'] = self.claim_status.to_alipay_dict()
            else:
                params['claim_status'] = self.claim_status
        if self.claim_status_desc:
            if hasattr(self.claim_status_desc, 'to_alipay_dict'):
                params['claim_status_desc'] = self.claim_status_desc.to_alipay_dict()
            else:
                params['claim_status_desc'] = self.claim_status_desc
        if self.company_type:
            if hasattr(self.company_type, 'to_alipay_dict'):
                params['company_type'] = self.company_type.to_alipay_dict()
            else:
                params['company_type'] = self.company_type
        if self.open_id:
            if hasattr(self.open_id, 'to_alipay_dict'):
                params['open_id'] = self.open_id.to_alipay_dict()
            else:
                params['open_id'] = self.open_id
        if self.pay_account:
            if hasattr(self.pay_account, 'to_alipay_dict'):
                params['pay_account'] = self.pay_account.to_alipay_dict()
            else:
                params['pay_account'] = self.pay_account
        if self.pay_time:
            if hasattr(self.pay_time, 'to_alipay_dict'):
                params['pay_time'] = self.pay_time.to_alipay_dict()
            else:
                params['pay_time'] = self.pay_time
        if self.source:
            if hasattr(self.source, 'to_alipay_dict'):
                params['source'] = self.source.to_alipay_dict()
            else:
                params['source'] = self.source
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
        o = AlipayCommerceMedicalInsuranceClaimSyncModel()
        if 'advance_apply_no' in d:
            o.advance_apply_no = d['advance_apply_no']
        if 'ant_apply_no' in d:
            o.ant_apply_no = d['ant_apply_no']
        if 'claim_amount' in d:
            o.claim_amount = d['claim_amount']
        if 'claim_detail' in d:
            o.claim_detail = d['claim_detail']
        if 'claim_no' in d:
            o.claim_no = d['claim_no']
        if 'claim_status' in d:
            o.claim_status = d['claim_status']
        if 'claim_status_desc' in d:
            o.claim_status_desc = d['claim_status_desc']
        if 'company_type' in d:
            o.company_type = d['company_type']
        if 'open_id' in d:
            o.open_id = d['open_id']
        if 'pay_account' in d:
            o.pay_account = d['pay_account']
        if 'pay_time' in d:
            o.pay_time = d['pay_time']
        if 'source' in d:
            o.source = d['source']
        if 'user_id' in d:
            o.user_id = d['user_id']
        return o


