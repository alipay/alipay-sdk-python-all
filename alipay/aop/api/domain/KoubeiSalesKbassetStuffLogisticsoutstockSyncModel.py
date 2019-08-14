#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.OutStockStuffInfo import OutStockStuffInfo


class KoubeiSalesKbassetStuffLogisticsoutstockSyncModel(object):

    def __init__(self):
        self._actual_ship_date_time = None
        self._erp_order = None
        self._erp_order_type = None
        self._express_company_code = None
        self._express_company_name = None
        self._ext_info = None
        self._item_infos = None
        self._request_id = None
        self._return_tracking = None
        self._shipment_id = None
        self._way_bill_no = None

    @property
    def actual_ship_date_time(self):
        return self._actual_ship_date_time

    @actual_ship_date_time.setter
    def actual_ship_date_time(self, value):
        self._actual_ship_date_time = value
    @property
    def erp_order(self):
        return self._erp_order

    @erp_order.setter
    def erp_order(self, value):
        self._erp_order = value
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
    def express_company_name(self):
        return self._express_company_name

    @express_company_name.setter
    def express_company_name(self, value):
        self._express_company_name = value
    @property
    def ext_info(self):
        return self._ext_info

    @ext_info.setter
    def ext_info(self, value):
        self._ext_info = value
    @property
    def item_infos(self):
        return self._item_infos

    @item_infos.setter
    def item_infos(self, value):
        if isinstance(value, list):
            self._item_infos = list()
            for i in value:
                if isinstance(i, OutStockStuffInfo):
                    self._item_infos.append(i)
                else:
                    self._item_infos.append(OutStockStuffInfo.from_alipay_dict(i))
    @property
    def request_id(self):
        return self._request_id

    @request_id.setter
    def request_id(self, value):
        self._request_id = value
    @property
    def return_tracking(self):
        return self._return_tracking

    @return_tracking.setter
    def return_tracking(self, value):
        self._return_tracking = value
    @property
    def shipment_id(self):
        return self._shipment_id

    @shipment_id.setter
    def shipment_id(self, value):
        self._shipment_id = value
    @property
    def way_bill_no(self):
        return self._way_bill_no

    @way_bill_no.setter
    def way_bill_no(self, value):
        self._way_bill_no = value


    def to_alipay_dict(self):
        params = dict()
        if self.actual_ship_date_time:
            if hasattr(self.actual_ship_date_time, 'to_alipay_dict'):
                params['actual_ship_date_time'] = self.actual_ship_date_time.to_alipay_dict()
            else:
                params['actual_ship_date_time'] = self.actual_ship_date_time
        if self.erp_order:
            if hasattr(self.erp_order, 'to_alipay_dict'):
                params['erp_order'] = self.erp_order.to_alipay_dict()
            else:
                params['erp_order'] = self.erp_order
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
        if self.express_company_name:
            if hasattr(self.express_company_name, 'to_alipay_dict'):
                params['express_company_name'] = self.express_company_name.to_alipay_dict()
            else:
                params['express_company_name'] = self.express_company_name
        if self.ext_info:
            if hasattr(self.ext_info, 'to_alipay_dict'):
                params['ext_info'] = self.ext_info.to_alipay_dict()
            else:
                params['ext_info'] = self.ext_info
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
        if self.request_id:
            if hasattr(self.request_id, 'to_alipay_dict'):
                params['request_id'] = self.request_id.to_alipay_dict()
            else:
                params['request_id'] = self.request_id
        if self.return_tracking:
            if hasattr(self.return_tracking, 'to_alipay_dict'):
                params['return_tracking'] = self.return_tracking.to_alipay_dict()
            else:
                params['return_tracking'] = self.return_tracking
        if self.shipment_id:
            if hasattr(self.shipment_id, 'to_alipay_dict'):
                params['shipment_id'] = self.shipment_id.to_alipay_dict()
            else:
                params['shipment_id'] = self.shipment_id
        if self.way_bill_no:
            if hasattr(self.way_bill_no, 'to_alipay_dict'):
                params['way_bill_no'] = self.way_bill_no.to_alipay_dict()
            else:
                params['way_bill_no'] = self.way_bill_no
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = KoubeiSalesKbassetStuffLogisticsoutstockSyncModel()
        if 'actual_ship_date_time' in d:
            o.actual_ship_date_time = d['actual_ship_date_time']
        if 'erp_order' in d:
            o.erp_order = d['erp_order']
        if 'erp_order_type' in d:
            o.erp_order_type = d['erp_order_type']
        if 'express_company_code' in d:
            o.express_company_code = d['express_company_code']
        if 'express_company_name' in d:
            o.express_company_name = d['express_company_name']
        if 'ext_info' in d:
            o.ext_info = d['ext_info']
        if 'item_infos' in d:
            o.item_infos = d['item_infos']
        if 'request_id' in d:
            o.request_id = d['request_id']
        if 'return_tracking' in d:
            o.return_tracking = d['return_tracking']
        if 'shipment_id' in d:
            o.shipment_id = d['shipment_id']
        if 'way_bill_no' in d:
            o.way_bill_no = d['way_bill_no']
        return o


