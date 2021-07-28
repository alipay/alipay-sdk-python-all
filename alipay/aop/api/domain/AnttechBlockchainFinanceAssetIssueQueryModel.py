#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.FinanceMemberInfo import FinanceMemberInfo


class AnttechBlockchainFinanceAssetIssueQueryModel(object):

    def __init__(self):
        self._asset_id = None
        self._core_business_info = None

    @property
    def asset_id(self):
        return self._asset_id

    @asset_id.setter
    def asset_id(self, value):
        self._asset_id = value
    @property
    def core_business_info(self):
        return self._core_business_info

    @core_business_info.setter
    def core_business_info(self, value):
        if isinstance(value, FinanceMemberInfo):
            self._core_business_info = value
        else:
            self._core_business_info = FinanceMemberInfo.from_alipay_dict(value)


    def to_alipay_dict(self):
        params = dict()
        if self.asset_id:
            if hasattr(self.asset_id, 'to_alipay_dict'):
                params['asset_id'] = self.asset_id.to_alipay_dict()
            else:
                params['asset_id'] = self.asset_id
        if self.core_business_info:
            if hasattr(self.core_business_info, 'to_alipay_dict'):
                params['core_business_info'] = self.core_business_info.to_alipay_dict()
            else:
                params['core_business_info'] = self.core_business_info
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AnttechBlockchainFinanceAssetIssueQueryModel()
        if 'asset_id' in d:
            o.asset_id = d['asset_id']
        if 'core_business_info' in d:
            o.core_business_info = d['core_business_info']
        return o


