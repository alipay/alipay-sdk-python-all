#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceLogisticsIncentivecodeOperationSyncModel(object):

    def __init__(self):
        self._alipay_trade_no = None
        self._alipay_trade_status = None
        self._incentive_code = None
        self._logistics_code = None
        self._operation_dynamic_sales_type = None
        self._operation_latitude = None
        self._operation_longitude = None
        self._operation_open_id = None
        self._operation_source = None
        self._operation_time = None
        self._operation_user_id = None
        self._order_no = None
        self._pay_finish_url = None
        self._pay_url = None
        self._waybill_no = None

    @property
    def alipay_trade_no(self):
        return self._alipay_trade_no

    @alipay_trade_no.setter
    def alipay_trade_no(self, value):
        self._alipay_trade_no = value
    @property
    def alipay_trade_status(self):
        return self._alipay_trade_status

    @alipay_trade_status.setter
    def alipay_trade_status(self, value):
        self._alipay_trade_status = value
    @property
    def incentive_code(self):
        return self._incentive_code

    @incentive_code.setter
    def incentive_code(self, value):
        self._incentive_code = value
    @property
    def logistics_code(self):
        return self._logistics_code

    @logistics_code.setter
    def logistics_code(self, value):
        self._logistics_code = value
    @property
    def operation_dynamic_sales_type(self):
        return self._operation_dynamic_sales_type

    @operation_dynamic_sales_type.setter
    def operation_dynamic_sales_type(self, value):
        self._operation_dynamic_sales_type = value
    @property
    def operation_latitude(self):
        return self._operation_latitude

    @operation_latitude.setter
    def operation_latitude(self, value):
        self._operation_latitude = value
    @property
    def operation_longitude(self):
        return self._operation_longitude

    @operation_longitude.setter
    def operation_longitude(self, value):
        self._operation_longitude = value
    @property
    def operation_open_id(self):
        return self._operation_open_id

    @operation_open_id.setter
    def operation_open_id(self, value):
        self._operation_open_id = value
    @property
    def operation_source(self):
        return self._operation_source

    @operation_source.setter
    def operation_source(self, value):
        self._operation_source = value
    @property
    def operation_time(self):
        return self._operation_time

    @operation_time.setter
    def operation_time(self, value):
        self._operation_time = value
    @property
    def operation_user_id(self):
        return self._operation_user_id

    @operation_user_id.setter
    def operation_user_id(self, value):
        self._operation_user_id = value
    @property
    def order_no(self):
        return self._order_no

    @order_no.setter
    def order_no(self, value):
        self._order_no = value
    @property
    def pay_finish_url(self):
        return self._pay_finish_url

    @pay_finish_url.setter
    def pay_finish_url(self, value):
        self._pay_finish_url = value
    @property
    def pay_url(self):
        return self._pay_url

    @pay_url.setter
    def pay_url(self, value):
        self._pay_url = value
    @property
    def waybill_no(self):
        return self._waybill_no

    @waybill_no.setter
    def waybill_no(self, value):
        self._waybill_no = value


    def to_alipay_dict(self):
        params = dict()
        if self.alipay_trade_no:
            if hasattr(self.alipay_trade_no, 'to_alipay_dict'):
                params['alipay_trade_no'] = self.alipay_trade_no.to_alipay_dict()
            else:
                params['alipay_trade_no'] = self.alipay_trade_no
        if self.alipay_trade_status:
            if hasattr(self.alipay_trade_status, 'to_alipay_dict'):
                params['alipay_trade_status'] = self.alipay_trade_status.to_alipay_dict()
            else:
                params['alipay_trade_status'] = self.alipay_trade_status
        if self.incentive_code:
            if hasattr(self.incentive_code, 'to_alipay_dict'):
                params['incentive_code'] = self.incentive_code.to_alipay_dict()
            else:
                params['incentive_code'] = self.incentive_code
        if self.logistics_code:
            if hasattr(self.logistics_code, 'to_alipay_dict'):
                params['logistics_code'] = self.logistics_code.to_alipay_dict()
            else:
                params['logistics_code'] = self.logistics_code
        if self.operation_dynamic_sales_type:
            if hasattr(self.operation_dynamic_sales_type, 'to_alipay_dict'):
                params['operation_dynamic_sales_type'] = self.operation_dynamic_sales_type.to_alipay_dict()
            else:
                params['operation_dynamic_sales_type'] = self.operation_dynamic_sales_type
        if self.operation_latitude:
            if hasattr(self.operation_latitude, 'to_alipay_dict'):
                params['operation_latitude'] = self.operation_latitude.to_alipay_dict()
            else:
                params['operation_latitude'] = self.operation_latitude
        if self.operation_longitude:
            if hasattr(self.operation_longitude, 'to_alipay_dict'):
                params['operation_longitude'] = self.operation_longitude.to_alipay_dict()
            else:
                params['operation_longitude'] = self.operation_longitude
        if self.operation_open_id:
            if hasattr(self.operation_open_id, 'to_alipay_dict'):
                params['operation_open_id'] = self.operation_open_id.to_alipay_dict()
            else:
                params['operation_open_id'] = self.operation_open_id
        if self.operation_source:
            if hasattr(self.operation_source, 'to_alipay_dict'):
                params['operation_source'] = self.operation_source.to_alipay_dict()
            else:
                params['operation_source'] = self.operation_source
        if self.operation_time:
            if hasattr(self.operation_time, 'to_alipay_dict'):
                params['operation_time'] = self.operation_time.to_alipay_dict()
            else:
                params['operation_time'] = self.operation_time
        if self.operation_user_id:
            if hasattr(self.operation_user_id, 'to_alipay_dict'):
                params['operation_user_id'] = self.operation_user_id.to_alipay_dict()
            else:
                params['operation_user_id'] = self.operation_user_id
        if self.order_no:
            if hasattr(self.order_no, 'to_alipay_dict'):
                params['order_no'] = self.order_no.to_alipay_dict()
            else:
                params['order_no'] = self.order_no
        if self.pay_finish_url:
            if hasattr(self.pay_finish_url, 'to_alipay_dict'):
                params['pay_finish_url'] = self.pay_finish_url.to_alipay_dict()
            else:
                params['pay_finish_url'] = self.pay_finish_url
        if self.pay_url:
            if hasattr(self.pay_url, 'to_alipay_dict'):
                params['pay_url'] = self.pay_url.to_alipay_dict()
            else:
                params['pay_url'] = self.pay_url
        if self.waybill_no:
            if hasattr(self.waybill_no, 'to_alipay_dict'):
                params['waybill_no'] = self.waybill_no.to_alipay_dict()
            else:
                params['waybill_no'] = self.waybill_no
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceLogisticsIncentivecodeOperationSyncModel()
        if 'alipay_trade_no' in d:
            o.alipay_trade_no = d['alipay_trade_no']
        if 'alipay_trade_status' in d:
            o.alipay_trade_status = d['alipay_trade_status']
        if 'incentive_code' in d:
            o.incentive_code = d['incentive_code']
        if 'logistics_code' in d:
            o.logistics_code = d['logistics_code']
        if 'operation_dynamic_sales_type' in d:
            o.operation_dynamic_sales_type = d['operation_dynamic_sales_type']
        if 'operation_latitude' in d:
            o.operation_latitude = d['operation_latitude']
        if 'operation_longitude' in d:
            o.operation_longitude = d['operation_longitude']
        if 'operation_open_id' in d:
            o.operation_open_id = d['operation_open_id']
        if 'operation_source' in d:
            o.operation_source = d['operation_source']
        if 'operation_time' in d:
            o.operation_time = d['operation_time']
        if 'operation_user_id' in d:
            o.operation_user_id = d['operation_user_id']
        if 'order_no' in d:
            o.order_no = d['order_no']
        if 'pay_finish_url' in d:
            o.pay_finish_url = d['pay_finish_url']
        if 'pay_url' in d:
            o.pay_url = d['pay_url']
        if 'waybill_no' in d:
            o.waybill_no = d['waybill_no']
        return o


