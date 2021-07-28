#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.FinanceBankAccountInfo import FinanceBankAccountInfo


class FinanceReceivableResultInfo(object):

    def __init__(self):
        self._accept_tx_hash = None
        self._asset_id = None
        self._factoring_account_info = None
        self._issue_date = None
        self._out_asset_id = None
        self._review_tx_hash = None
        self._submit_tx_hash = None

    @property
    def accept_tx_hash(self):
        return self._accept_tx_hash

    @accept_tx_hash.setter
    def accept_tx_hash(self, value):
        self._accept_tx_hash = value
    @property
    def asset_id(self):
        return self._asset_id

    @asset_id.setter
    def asset_id(self, value):
        self._asset_id = value
    @property
    def factoring_account_info(self):
        return self._factoring_account_info

    @factoring_account_info.setter
    def factoring_account_info(self, value):
        if isinstance(value, FinanceBankAccountInfo):
            self._factoring_account_info = value
        else:
            self._factoring_account_info = FinanceBankAccountInfo.from_alipay_dict(value)
    @property
    def issue_date(self):
        return self._issue_date

    @issue_date.setter
    def issue_date(self, value):
        self._issue_date = value
    @property
    def out_asset_id(self):
        return self._out_asset_id

    @out_asset_id.setter
    def out_asset_id(self, value):
        self._out_asset_id = value
    @property
    def review_tx_hash(self):
        return self._review_tx_hash

    @review_tx_hash.setter
    def review_tx_hash(self, value):
        self._review_tx_hash = value
    @property
    def submit_tx_hash(self):
        return self._submit_tx_hash

    @submit_tx_hash.setter
    def submit_tx_hash(self, value):
        self._submit_tx_hash = value


    def to_alipay_dict(self):
        params = dict()
        if self.accept_tx_hash:
            if hasattr(self.accept_tx_hash, 'to_alipay_dict'):
                params['accept_tx_hash'] = self.accept_tx_hash.to_alipay_dict()
            else:
                params['accept_tx_hash'] = self.accept_tx_hash
        if self.asset_id:
            if hasattr(self.asset_id, 'to_alipay_dict'):
                params['asset_id'] = self.asset_id.to_alipay_dict()
            else:
                params['asset_id'] = self.asset_id
        if self.factoring_account_info:
            if hasattr(self.factoring_account_info, 'to_alipay_dict'):
                params['factoring_account_info'] = self.factoring_account_info.to_alipay_dict()
            else:
                params['factoring_account_info'] = self.factoring_account_info
        if self.issue_date:
            if hasattr(self.issue_date, 'to_alipay_dict'):
                params['issue_date'] = self.issue_date.to_alipay_dict()
            else:
                params['issue_date'] = self.issue_date
        if self.out_asset_id:
            if hasattr(self.out_asset_id, 'to_alipay_dict'):
                params['out_asset_id'] = self.out_asset_id.to_alipay_dict()
            else:
                params['out_asset_id'] = self.out_asset_id
        if self.review_tx_hash:
            if hasattr(self.review_tx_hash, 'to_alipay_dict'):
                params['review_tx_hash'] = self.review_tx_hash.to_alipay_dict()
            else:
                params['review_tx_hash'] = self.review_tx_hash
        if self.submit_tx_hash:
            if hasattr(self.submit_tx_hash, 'to_alipay_dict'):
                params['submit_tx_hash'] = self.submit_tx_hash.to_alipay_dict()
            else:
                params['submit_tx_hash'] = self.submit_tx_hash
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = FinanceReceivableResultInfo()
        if 'accept_tx_hash' in d:
            o.accept_tx_hash = d['accept_tx_hash']
        if 'asset_id' in d:
            o.asset_id = d['asset_id']
        if 'factoring_account_info' in d:
            o.factoring_account_info = d['factoring_account_info']
        if 'issue_date' in d:
            o.issue_date = d['issue_date']
        if 'out_asset_id' in d:
            o.out_asset_id = d['out_asset_id']
        if 'review_tx_hash' in d:
            o.review_tx_hash = d['review_tx_hash']
        if 'submit_tx_hash' in d:
            o.submit_tx_hash = d['submit_tx_hash']
        return o


