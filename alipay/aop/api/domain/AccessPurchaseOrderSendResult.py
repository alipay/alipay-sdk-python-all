#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AccessPurchaseOrderSendResult(object):

    def __init__(self):
        self._asset_item_id = None
        self._asset_order_id = None
        self._asset_purchase_id = None
        self._error_code = None
        self._error_desc = None
        self._out_biz_no = None
        self._success = None

    @property
    def asset_item_id(self):
        return self._asset_item_id

    @asset_item_id.setter
    def asset_item_id(self, value):
        self._asset_item_id = value
    @property
    def asset_order_id(self):
        return self._asset_order_id

    @asset_order_id.setter
    def asset_order_id(self, value):
        self._asset_order_id = value
    @property
    def asset_purchase_id(self):
        return self._asset_purchase_id

    @asset_purchase_id.setter
    def asset_purchase_id(self, value):
        self._asset_purchase_id = value
    @property
    def error_code(self):
        return self._error_code

    @error_code.setter
    def error_code(self, value):
        self._error_code = value
    @property
    def error_desc(self):
        return self._error_desc

    @error_desc.setter
    def error_desc(self, value):
        self._error_desc = value
    @property
    def out_biz_no(self):
        return self._out_biz_no

    @out_biz_no.setter
    def out_biz_no(self, value):
        self._out_biz_no = value
    @property
    def success(self):
        return self._success

    @success.setter
    def success(self, value):
        self._success = value


    def to_alipay_dict(self):
        params = dict()
        if self.asset_item_id:
            if hasattr(self.asset_item_id, 'to_alipay_dict'):
                params['asset_item_id'] = self.asset_item_id.to_alipay_dict()
            else:
                params['asset_item_id'] = self.asset_item_id
        if self.asset_order_id:
            if hasattr(self.asset_order_id, 'to_alipay_dict'):
                params['asset_order_id'] = self.asset_order_id.to_alipay_dict()
            else:
                params['asset_order_id'] = self.asset_order_id
        if self.asset_purchase_id:
            if hasattr(self.asset_purchase_id, 'to_alipay_dict'):
                params['asset_purchase_id'] = self.asset_purchase_id.to_alipay_dict()
            else:
                params['asset_purchase_id'] = self.asset_purchase_id
        if self.error_code:
            if hasattr(self.error_code, 'to_alipay_dict'):
                params['error_code'] = self.error_code.to_alipay_dict()
            else:
                params['error_code'] = self.error_code
        if self.error_desc:
            if hasattr(self.error_desc, 'to_alipay_dict'):
                params['error_desc'] = self.error_desc.to_alipay_dict()
            else:
                params['error_desc'] = self.error_desc
        if self.out_biz_no:
            if hasattr(self.out_biz_no, 'to_alipay_dict'):
                params['out_biz_no'] = self.out_biz_no.to_alipay_dict()
            else:
                params['out_biz_no'] = self.out_biz_no
        if self.success:
            if hasattr(self.success, 'to_alipay_dict'):
                params['success'] = self.success.to_alipay_dict()
            else:
                params['success'] = self.success
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AccessPurchaseOrderSendResult()
        if 'asset_item_id' in d:
            o.asset_item_id = d['asset_item_id']
        if 'asset_order_id' in d:
            o.asset_order_id = d['asset_order_id']
        if 'asset_purchase_id' in d:
            o.asset_purchase_id = d['asset_purchase_id']
        if 'error_code' in d:
            o.error_code = d['error_code']
        if 'error_desc' in d:
            o.error_desc = d['error_desc']
        if 'out_biz_no' in d:
            o.out_biz_no = d['out_biz_no']
        if 'success' in d:
            o.success = d['success']
        return o


