#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.AssetReverseSupplierApplyExpressSnDetails import AssetReverseSupplierApplyExpressSnDetails


class AssetReverseSupplierApplyDetail(object):

    def __init__(self):
        self._express_sn_details = None
        self._supplier_id = None
        self._supplier_pid = None
        self._warehouse_id = None

    @property
    def express_sn_details(self):
        return self._express_sn_details

    @express_sn_details.setter
    def express_sn_details(self, value):
        if isinstance(value, list):
            self._express_sn_details = list()
            for i in value:
                if isinstance(i, AssetReverseSupplierApplyExpressSnDetails):
                    self._express_sn_details.append(i)
                else:
                    self._express_sn_details.append(AssetReverseSupplierApplyExpressSnDetails.from_alipay_dict(i))
    @property
    def supplier_id(self):
        return self._supplier_id

    @supplier_id.setter
    def supplier_id(self, value):
        self._supplier_id = value
    @property
    def supplier_pid(self):
        return self._supplier_pid

    @supplier_pid.setter
    def supplier_pid(self, value):
        self._supplier_pid = value
    @property
    def warehouse_id(self):
        return self._warehouse_id

    @warehouse_id.setter
    def warehouse_id(self, value):
        self._warehouse_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.express_sn_details:
            if isinstance(self.express_sn_details, list):
                for i in range(0, len(self.express_sn_details)):
                    element = self.express_sn_details[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.express_sn_details[i] = element.to_alipay_dict()
            if hasattr(self.express_sn_details, 'to_alipay_dict'):
                params['express_sn_details'] = self.express_sn_details.to_alipay_dict()
            else:
                params['express_sn_details'] = self.express_sn_details
        if self.supplier_id:
            if hasattr(self.supplier_id, 'to_alipay_dict'):
                params['supplier_id'] = self.supplier_id.to_alipay_dict()
            else:
                params['supplier_id'] = self.supplier_id
        if self.supplier_pid:
            if hasattr(self.supplier_pid, 'to_alipay_dict'):
                params['supplier_pid'] = self.supplier_pid.to_alipay_dict()
            else:
                params['supplier_pid'] = self.supplier_pid
        if self.warehouse_id:
            if hasattr(self.warehouse_id, 'to_alipay_dict'):
                params['warehouse_id'] = self.warehouse_id.to_alipay_dict()
            else:
                params['warehouse_id'] = self.warehouse_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AssetReverseSupplierApplyDetail()
        if 'express_sn_details' in d:
            o.express_sn_details = d['express_sn_details']
        if 'supplier_id' in d:
            o.supplier_id = d['supplier_id']
        if 'supplier_pid' in d:
            o.supplier_pid = d['supplier_pid']
        if 'warehouse_id' in d:
            o.warehouse_id = d['warehouse_id']
        return o


