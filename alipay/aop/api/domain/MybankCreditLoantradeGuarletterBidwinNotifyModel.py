#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.BidDetailVO import BidDetailVO
from alipay.aop.api.domain.EnterpriseCustomerInfoVO import EnterpriseCustomerInfoVO


class MybankCreditLoantradeGuarletterBidwinNotifyModel(object):

    def __init__(self):
        self._bid_detail = None
        self._scheme_ar_no = None
        self._winer_user_info = None

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
    def scheme_ar_no(self):
        return self._scheme_ar_no

    @scheme_ar_no.setter
    def scheme_ar_no(self, value):
        self._scheme_ar_no = value
    @property
    def winer_user_info(self):
        return self._winer_user_info

    @winer_user_info.setter
    def winer_user_info(self, value):
        if isinstance(value, EnterpriseCustomerInfoVO):
            self._winer_user_info = value
        else:
            self._winer_user_info = EnterpriseCustomerInfoVO.from_alipay_dict(value)


    def to_alipay_dict(self):
        params = dict()
        if self.bid_detail:
            if hasattr(self.bid_detail, 'to_alipay_dict'):
                params['bid_detail'] = self.bid_detail.to_alipay_dict()
            else:
                params['bid_detail'] = self.bid_detail
        if self.scheme_ar_no:
            if hasattr(self.scheme_ar_no, 'to_alipay_dict'):
                params['scheme_ar_no'] = self.scheme_ar_no.to_alipay_dict()
            else:
                params['scheme_ar_no'] = self.scheme_ar_no
        if self.winer_user_info:
            if hasattr(self.winer_user_info, 'to_alipay_dict'):
                params['winer_user_info'] = self.winer_user_info.to_alipay_dict()
            else:
                params['winer_user_info'] = self.winer_user_info
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = MybankCreditLoantradeGuarletterBidwinNotifyModel()
        if 'bid_detail' in d:
            o.bid_detail = d['bid_detail']
        if 'scheme_ar_no' in d:
            o.scheme_ar_no = d['scheme_ar_no']
        if 'winer_user_info' in d:
            o.winer_user_info = d['winer_user_info']
        return o


