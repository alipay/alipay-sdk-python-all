#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.InStockStuffInfo import InStockStuffInfo


class KoubeiSalesKbassetStuffLogisticsinstockSyncModel(object):

    def __init__(self):
        self._close_date = None
        self._erp_code = None
        self._erp_order_type = None
        self._express_company_code = None
        self._express_no = None
        self._item_infos = None
        self._receipt_id = None
        self._request_id = None
        self._warehouse_code = None

    @property
    def close_date(self):
        return self._close_date

    @close_date.setter
    def close_date(self, value):
        self._close_date = value
    @property
    def erp_code(self):
        return self._erp_code

    @erp_code.setter
    def erp_code(self, value):
        self._erp_code = value
    @property
    def erp_order_type(self):
        return self._erp_order_type

    @erp_order_type.setter
    def erp_order_type(self, value):
        self._erp_order_type = value
    @property
    def express_company_code(self):
        return self._express_company_code

    @express_company_code.setter
    def express_company_code(self, value):
        self._express_company_code = value
    @property
    def express_no(self):
        return self._express_no

    @express_no.setter
    def express_no(self, value):
        self._express_no = value
    @property
    def item_infos(self):
        return self._item_infos

    @item_infos.setter
    def item_infos(self, value):
        if isinstance(value, list):
            self._item_infos = list()
            for i in value:
                if isinstance(i, InStockStuffInfo):
                    self._item_infos.append(i)
                else:
                    self._item_infos.append(InStockStuffInfo.from_alipay_dict(i))
    @property
    def receipt_id(self):
        return self._receipt_id

    @receipt_id.setter
    def receipt_id(self, value):
        self._receipt_id = value
    @property
    def request_id(self):
        return self._request_id

    @request_id.setter
    def request_id(self, value):
        self._request_id = value
    @property
    def warehouse_code(self):
        return self._warehouse_code

    @warehouse_code.setter
    def warehouse_code(self, value):
        self._warehouse_code = value


    def to_alipay_dict(self):
        params = dict()
        if self.close_date:
            if hasattr(self.close_date, 'to_alipay_dict'):
                params['close_date'] = self.close_date.to_alipay_dict()
            else:
                params['close_date'] = self.close_date
        if self.erp_code:
            if hasattr(self.erp_code, 'to_alipay_dict'):
                params['erp_code'] = self.erp_code.to_alipay_dict()
            else:
                params['erp_code'] = self.erp_code
        if self.erp_order_type:
            if hasattr(self.erp_order_type, 'to_alipay_dict'):
                params['erp_order_type'] = self.erp_order_type.to_alipay_dict()
            else:
                params['erp_order_type'] = self.erp_order_type
        if self.express_company_code:
            if hasattr(self.express_company_code, 'to_alipay_dict'):
                params['express_company_code'] = self.express_company_code.to_alipay_dict()
            else:
                params['express_company_code'] = self.express_company_code
        if self.express_no:
            if hasattr(self.express_no, 'to_alipay_dict'):
                params['express_no'] = self.express_no.to_alipay_dict()
            else:
                params['express_no'] = self.express_no
        if self.item_infos:
            if isinstance(self.item_infos, list):
                for i in range(0, len(self.item_infos)):
                    element = self.item_infos[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.item_infos[i] = element.to_alipay_dict()
            if hasattr(self.item_infos, 'to_alipay_dict'):
                params['item_infos'] = self.item_infos.to_alipay_dict()
            else:
                params['item_infos'] = self.item_infos
        if self.receipt_id:
            if hasattr(self.receipt_id, 'to_alipay_dict'):
                params['receipt_id'] = self.receipt_id.to_alipay_dict()
            else:
                params['receipt_id'] = self.receipt_id
        if self.request_id:
            if hasattr(self.request_id, 'to_alipay_dict'):
                params['request_id'] = self.request_id.to_alipay_dict()
            else:
                params['request_id'] = self.request_id
        if self.warehouse_code:
            if hasattr(self.warehouse_code, 'to_alipay_dict'):
                params['warehouse_code'] = self.warehouse_code.to_alipay_dict()
            else:
                params['warehouse_code'] = self.warehouse_code
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = KoubeiSalesKbassetStuffLogisticsinstockSyncModel()
        if 'close_date' in d:
            o.close_date = d['close_date']
        if 'erp_code' in d:
            o.erp_code = d['erp_code']
        if 'erp_order_type' in d:
            o.erp_order_type = d['erp_order_type']
        if 'express_company_code' in d:
            o.express_company_code = d['express_company_code']
        if 'express_no' in d:
            o.express_no = d['express_no']
        if 'item_infos' in d:
            o.item_infos = d['item_infos']
        if 'receipt_id' in d:
            o.receipt_id = d['receipt_id']
        if 'request_id' in d:
            o.request_id = d['request_id']
        if 'warehouse_code' in d:
            o.warehouse_code = d['warehouse_code']
        return o


