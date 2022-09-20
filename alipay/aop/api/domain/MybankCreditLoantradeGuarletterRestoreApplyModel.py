#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.EnterpriseCustomerInfoVO import EnterpriseCustomerInfoVO
from alipay.aop.api.domain.BidDetailVO import BidDetailVO


class MybankCreditLoantradeGuarletterRestoreApplyModel(object):

    def __init__(self):
        self._beneficiary_user_info = None
        self._bid_detail = None
        self._decrypt_key = None
        self._guar_letter_order_no = None
        self._request_id = None
        self._scheme_ar_no = None

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
    def decrypt_key(self):
        return self._decrypt_key

    @decrypt_key.setter
    def decrypt_key(self, value):
        self._decrypt_key = value
    @property
    def guar_letter_order_no(self):
        return self._guar_letter_order_no

    @guar_letter_order_no.setter
    def guar_letter_order_no(self, value):
        self._guar_letter_order_no = value
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
        if self.decrypt_key:
            if hasattr(self.decrypt_key, 'to_alipay_dict'):
                params['decrypt_key'] = self.decrypt_key.to_alipay_dict()
            else:
                params['decrypt_key'] = self.decrypt_key
        if self.guar_letter_order_no:
            if hasattr(self.guar_letter_order_no, 'to_alipay_dict'):
                params['guar_letter_order_no'] = self.guar_letter_order_no.to_alipay_dict()
            else:
                params['guar_letter_order_no'] = self.guar_letter_order_no
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
        o = MybankCreditLoantradeGuarletterRestoreApplyModel()
        if 'beneficiary_user_info' in d:
            o.beneficiary_user_info = d['beneficiary_user_info']
        if 'bid_detail' in d:
            o.bid_detail = d['bid_detail']
        if 'decrypt_key' in d:
            o.decrypt_key = d['decrypt_key']
        if 'guar_letter_order_no' in d:
            o.guar_letter_order_no = d['guar_letter_order_no']
        if 'request_id' in d:
            o.request_id = d['request_id']
        if 'scheme_ar_no' in d:
            o.scheme_ar_no = d['scheme_ar_no']
        return o


