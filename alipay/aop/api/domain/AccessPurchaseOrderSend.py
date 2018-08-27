#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AccessPurchaseOrderSend(object):

    def __init__(self):
        self._asset_item_id = None
        self._asset_order_id = None
        self._asset_purchase_id = None
        self._express_code = None
        self._express_name = None
        self._express_no = None
        self._out_biz_no = None
        self._po_no = None
        self._return_qrcode_count = None
        self._ship_count = None

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
    def express_code(self):
        return self._express_code

    @express_code.setter
    def express_code(self, value):
        self._express_code = value
    @property
    def express_name(self):
        return self._express_name

    @express_name.setter
    def express_name(self, value):
        self._express_name = value
    @property
    def express_no(self):
        return self._express_no

    @express_no.setter
    def express_no(self, value):
        self._express_no = value
    @property
    def out_biz_no(self):
        return self._out_biz_no

    @out_biz_no.setter
    def out_biz_no(self, value):
        self._out_biz_no = value
    @property
    def po_no(self):
        return self._po_no

    @po_no.setter
    def po_no(self, value):
        self._po_no = value
    @property
    def return_qrcode_count(self):
        return self._return_qrcode_count

    @return_qrcode_count.setter
    def return_qrcode_count(self, value):
        self._return_qrcode_count = value
    @property
    def ship_count(self):
        return self._ship_count

    @ship_count.setter
    def ship_count(self, value):
        self._ship_count = value


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
        if self.express_code:
            if hasattr(self.express_code, 'to_alipay_dict'):
                params['express_code'] = self.express_code.to_alipay_dict()
            else:
                params['express_code'] = self.express_code
        if self.express_name:
            if hasattr(self.express_name, 'to_alipay_dict'):
                params['express_name'] = self.express_name.to_alipay_dict()
            else:
                params['express_name'] = self.express_name
        if self.express_no:
            if hasattr(self.express_no, 'to_alipay_dict'):
                params['express_no'] = self.express_no.to_alipay_dict()
            else:
                params['express_no'] = self.express_no
        if self.out_biz_no:
            if hasattr(self.out_biz_no, 'to_alipay_dict'):
                params['out_biz_no'] = self.out_biz_no.to_alipay_dict()
            else:
                params['out_biz_no'] = self.out_biz_no
        if self.po_no:
            if hasattr(self.po_no, 'to_alipay_dict'):
                params['po_no'] = self.po_no.to_alipay_dict()
            else:
                params['po_no'] = self.po_no
        if self.return_qrcode_count:
            if hasattr(self.return_qrcode_count, 'to_alipay_dict'):
                params['return_qrcode_count'] = self.return_qrcode_count.to_alipay_dict()
            else:
                params['return_qrcode_count'] = self.return_qrcode_count
        if self.ship_count:
            if hasattr(self.ship_count, 'to_alipay_dict'):
                params['ship_count'] = self.ship_count.to_alipay_dict()
            else:
                params['ship_count'] = self.ship_count
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AccessPurchaseOrderSend()
        if 'asset_item_id' in d:
            o.asset_item_id = d['asset_item_id']
        if 'asset_order_id' in d:
            o.asset_order_id = d['asset_order_id']
        if 'asset_purchase_id' in d:
            o.asset_purchase_id = d['asset_purchase_id']
        if 'express_code' in d:
            o.express_code = d['express_code']
        if 'express_name' in d:
            o.express_name = d['express_name']
        if 'express_no' in d:
            o.express_no = d['express_no']
        if 'out_biz_no' in d:
            o.out_biz_no = d['out_biz_no']
        if 'po_no' in d:
            o.po_no = d['po_no']
        if 'return_qrcode_count' in d:
            o.return_qrcode_count = d['return_qrcode_count']
        if 'ship_count' in d:
            o.ship_count = d['ship_count']
        return o


