#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.FinanceReceivableInfo import FinanceReceivableInfo


class AnttechBlockchainFinanceAssetIssueApplyModel(object):

    def __init__(self):
        self._asset_type = None
        self._receivable_info = None

    @property
    def asset_type(self):
        return self._asset_type

    @asset_type.setter
    def asset_type(self, value):
        self._asset_type = value
    @property
    def receivable_info(self):
        return self._receivable_info

    @receivable_info.setter
    def receivable_info(self, value):
        if isinstance(value, FinanceReceivableInfo):
            self._receivable_info = value
        else:
            self._receivable_info = FinanceReceivableInfo.from_alipay_dict(value)


    def to_alipay_dict(self):
        params = dict()
        if self.asset_type:
            if hasattr(self.asset_type, 'to_alipay_dict'):
                params['asset_type'] = self.asset_type.to_alipay_dict()
            else:
                params['asset_type'] = self.asset_type
        if self.receivable_info:
            if hasattr(self.receivable_info, 'to_alipay_dict'):
                params['receivable_info'] = self.receivable_info.to_alipay_dict()
            else:
                params['receivable_info'] = self.receivable_info
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AnttechBlockchainFinanceAssetIssueApplyModel()
        if 'asset_type' in d:
            o.asset_type = d['asset_type']
        if 'receivable_info' in d:
            o.receivable_info = d['receivable_info']
        return o


