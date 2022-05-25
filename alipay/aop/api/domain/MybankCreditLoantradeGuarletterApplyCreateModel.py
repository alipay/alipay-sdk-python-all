#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.CreditPayMoneyVO import CreditPayMoneyVO
from alipay.aop.api.domain.ApplyAttatchmentVO import ApplyAttatchmentVO
from alipay.aop.api.domain.EnterpriseCustomerInfoVO import EnterpriseCustomerInfoVO
from alipay.aop.api.domain.EnterpriseCustomerInfoVO import EnterpriseCustomerInfoVO
from alipay.aop.api.domain.BidDetailVO import BidDetailVO
from alipay.aop.api.domain.IndividualCustomerInfoVO import IndividualCustomerInfoVO


class MybankCreditLoantradeGuarletterApplyCreateModel(object):

    def __init__(self):
        self._apply_amt = None
        self._apply_attatchments = None
        self._apply_time = None
        self._apply_user_info = None
        self._beneficiary_user_info = None
        self._bid_detail = None
        self._guar_end_date = None
        self._guar_start_date = None
        self._guar_valid_days = None
        self._operator_user_info = None
        self._request_id = None
        self._scheme_ar_no = None

    @property
    def apply_amt(self):
        return self._apply_amt

    @apply_amt.setter
    def apply_amt(self, value):
        if isinstance(value, CreditPayMoneyVO):
            self._apply_amt = value
        else:
            self._apply_amt = CreditPayMoneyVO.from_alipay_dict(value)
    @property
    def apply_attatchments(self):
        return self._apply_attatchments

    @apply_attatchments.setter
    def apply_attatchments(self, value):
        if isinstance(value, ApplyAttatchmentVO):
            self._apply_attatchments = value
        else:
            self._apply_attatchments = ApplyAttatchmentVO.from_alipay_dict(value)
    @property
    def apply_time(self):
        return self._apply_time

    @apply_time.setter
    def apply_time(self, value):
        self._apply_time = value
    @property
    def apply_user_info(self):
        return self._apply_user_info

    @apply_user_info.setter
    def apply_user_info(self, value):
        if isinstance(value, EnterpriseCustomerInfoVO):
            self._apply_user_info = value
        else:
            self._apply_user_info = EnterpriseCustomerInfoVO.from_alipay_dict(value)
    @property
    def beneficiary_user_info(self):
        return self._beneficiary_user_info

    @beneficiary_user_info.setter
    def beneficiary_user_info(self, value):
        if isinstance(value, EnterpriseCustomerInfoVO):
            self._beneficiary_user_info = value
        else:
            self._beneficiary_user_info = EnterpriseCustomerInfoVO.from_alipay_dict(value)
    @property
    def bid_detail(self):
        return self._bid_detail

    @bid_detail.setter
    def bid_detail(self, value):
        if isinstance(value, BidDetailVO):
            self._bid_detail = value
        else:
            self._bid_detail = BidDetailVO.from_alipay_dict(value)
    @property
    def guar_end_date(self):
        return self._guar_end_date

    @guar_end_date.setter
    def guar_end_date(self, value):
        self._guar_end_date = value
    @property
    def guar_start_date(self):
        return self._guar_start_date

    @guar_start_date.setter
    def guar_start_date(self, value):
        self._guar_start_date = value
    @property
    def guar_valid_days(self):
        return self._guar_valid_days

    @guar_valid_days.setter
    def guar_valid_days(self, value):
        self._guar_valid_days = value
    @property
    def operator_user_info(self):
        return self._operator_user_info

    @operator_user_info.setter
    def operator_user_info(self, value):
        if isinstance(value, IndividualCustomerInfoVO):
            self._operator_user_info = value
        else:
            self._operator_user_info = IndividualCustomerInfoVO.from_alipay_dict(value)
    @property
    def request_id(self):
        return self._request_id

    @request_id.setter
    def request_id(self, value):
        self._request_id = value
    @property
    def scheme_ar_no(self):
        return self._scheme_ar_no

    @scheme_ar_no.setter
    def scheme_ar_no(self, value):
        self._scheme_ar_no = value


    def to_alipay_dict(self):
        params = dict()
        if self.apply_amt:
            if hasattr(self.apply_amt, 'to_alipay_dict'):
                params['apply_amt'] = self.apply_amt.to_alipay_dict()
            else:
                params['apply_amt'] = self.apply_amt
        if self.apply_attatchments:
            if hasattr(self.apply_attatchments, 'to_alipay_dict'):
                params['apply_attatchments'] = self.apply_attatchments.to_alipay_dict()
            else:
                params['apply_attatchments'] = self.apply_attatchments
        if self.apply_time:
            if hasattr(self.apply_time, 'to_alipay_dict'):
                params['apply_time'] = self.apply_time.to_alipay_dict()
            else:
                params['apply_time'] = self.apply_time
        if self.apply_user_info:
            if hasattr(self.apply_user_info, 'to_alipay_dict'):
                params['apply_user_info'] = self.apply_user_info.to_alipay_dict()
            else:
                params['apply_user_info'] = self.apply_user_info
        if self.beneficiary_user_info:
            if hasattr(self.beneficiary_user_info, 'to_alipay_dict'):
                params['beneficiary_user_info'] = self.beneficiary_user_info.to_alipay_dict()
            else:
                params['beneficiary_user_info'] = self.beneficiary_user_info
        if self.bid_detail:
            if hasattr(self.bid_detail, 'to_alipay_dict'):
                params['bid_detail'] = self.bid_detail.to_alipay_dict()
            else:
                params['bid_detail'] = self.bid_detail
        if self.guar_end_date:
            if hasattr(self.guar_end_date, 'to_alipay_dict'):
                params['guar_end_date'] = self.guar_end_date.to_alipay_dict()
            else:
                params['guar_end_date'] = self.guar_end_date
        if self.guar_start_date:
            if hasattr(self.guar_start_date, 'to_alipay_dict'):
                params['guar_start_date'] = self.guar_start_date.to_alipay_dict()
            else:
                params['guar_start_date'] = self.guar_start_date
        if self.guar_valid_days:
            if hasattr(self.guar_valid_days, 'to_alipay_dict'):
                params['guar_valid_days'] = self.guar_valid_days.to_alipay_dict()
            else:
                params['guar_valid_days'] = self.guar_valid_days
        if self.operator_user_info:
            if hasattr(self.operator_user_info, 'to_alipay_dict'):
                params['operator_user_info'] = self.operator_user_info.to_alipay_dict()
            else:
                params['operator_user_info'] = self.operator_user_info
        if self.request_id:
            if hasattr(self.request_id, 'to_alipay_dict'):
                params['request_id'] = self.request_id.to_alipay_dict()
            else:
                params['request_id'] = self.request_id
        if self.scheme_ar_no:
            if hasattr(self.scheme_ar_no, 'to_alipay_dict'):
                params['scheme_ar_no'] = self.scheme_ar_no.to_alipay_dict()
            else:
                params['scheme_ar_no'] = self.scheme_ar_no
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = MybankCreditLoantradeGuarletterApplyCreateModel()
        if 'apply_amt' in d:
            o.apply_amt = d['apply_amt']
        if 'apply_attatchments' in d:
            o.apply_attatchments = d['apply_attatchments']
        if 'apply_time' in d:
            o.apply_time = d['apply_time']
        if 'apply_user_info' in d:
            o.apply_user_info = d['apply_user_info']
        if 'beneficiary_user_info' in d:
            o.beneficiary_user_info = d['beneficiary_user_info']
        if 'bid_detail' in d:
            o.bid_detail = d['bid_detail']
        if 'guar_end_date' in d:
            o.guar_end_date = d['guar_end_date']
        if 'guar_start_date' in d:
            o.guar_start_date = d['guar_start_date']
        if 'guar_valid_days' in d:
            o.guar_valid_days = d['guar_valid_days']
        if 'operator_user_info' in d:
            o.operator_user_info = d['operator_user_info']
        if 'request_id' in d:
            o.request_id = d['request_id']
        if 'scheme_ar_no' in d:
            o.scheme_ar_no = d['scheme_ar_no']
        return o


