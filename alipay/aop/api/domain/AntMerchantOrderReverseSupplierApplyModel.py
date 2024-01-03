#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.AssetReverseSupplierApplyDetail import AssetReverseSupplierApplyDetail


class AntMerchantOrderReverseSupplierApplyModel(object):

    def __init__(self):
        self._asset_reverse_supplier_apply_detail = None

    @property
    def asset_reverse_supplier_apply_detail(self):
        return self._asset_reverse_supplier_apply_detail

    @asset_reverse_supplier_apply_detail.setter
    def asset_reverse_supplier_apply_detail(self, value):
        if isinstance(value, AssetReverseSupplierApplyDetail):
            self._asset_reverse_supplier_apply_detail = value
        else:
            self._asset_reverse_supplier_apply_detail = AssetReverseSupplierApplyDetail.from_alipay_dict(value)


    def to_alipay_dict(self):
        params = dict()
        if self.asset_reverse_supplier_apply_detail:
            if hasattr(self.asset_reverse_supplier_apply_detail, 'to_alipay_dict'):
                params['asset_reverse_supplier_apply_detail'] = self.asset_reverse_supplier_apply_detail.to_alipay_dict()
            else:
                params['asset_reverse_supplier_apply_detail'] = self.asset_reverse_supplier_apply_detail
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AntMerchantOrderReverseSupplierApplyModel()
        if 'asset_reverse_supplier_apply_detail' in d:
            o.asset_reverse_supplier_apply_detail = d['asset_reverse_supplier_apply_detail']
        return o


