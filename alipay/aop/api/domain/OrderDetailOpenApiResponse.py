#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.DeliveryLogistics import DeliveryLogistics


class OrderDetailOpenApiResponse(object):

    def __init__(self):
        self._delivery_express_info = None
        self._estimated_delivery_earliest_time = None
        self._estimated_delivery_latest_time = None
        self._gmt_create = None
        self._open_id = None
        self._order_desc = None
        self._order_id = None
        self._out_biz_no = None
        self._pid = None
        self._quantity = None
        self._status = None
        self._template_code = None

    @property
    def delivery_express_info(self):
        return self._delivery_express_info

    @delivery_express_info.setter
    def delivery_express_info(self, value):
        if isinstance(value, list):
            self._delivery_express_info = list()
            for i in value:
                if isinstance(i, DeliveryLogistics):
                    self._delivery_express_info.append(i)
                else:
                    self._delivery_express_info.append(DeliveryLogistics.from_alipay_dict(i))
    @property
    def estimated_delivery_earliest_time(self):
        return self._estimated_delivery_earliest_time

    @estimated_delivery_earliest_time.setter
    def estimated_delivery_earliest_time(self, value):
        self._estimated_delivery_earliest_time = value
    @property
    def estimated_delivery_latest_time(self):
        return self._estimated_delivery_latest_time

    @estimated_delivery_latest_time.setter
    def estimated_delivery_latest_time(self, value):
        self._estimated_delivery_latest_time = value
    @property
    def gmt_create(self):
        return self._gmt_create

    @gmt_create.setter
    def gmt_create(self, value):
        self._gmt_create = value
    @property
    def open_id(self):
        return self._open_id

    @open_id.setter
    def open_id(self, value):
        self._open_id = value
    @property
    def order_desc(self):
        return self._order_desc

    @order_desc.setter
    def order_desc(self, value):
        self._order_desc = value
    @property
    def order_id(self):
        return self._order_id

    @order_id.setter
    def order_id(self, value):
        self._order_id = value
    @property
    def out_biz_no(self):
        return self._out_biz_no

    @out_biz_no.setter
    def out_biz_no(self, value):
        self._out_biz_no = value
    @property
    def pid(self):
        return self._pid

    @pid.setter
    def pid(self, value):
        self._pid = value
    @property
    def quantity(self):
        return self._quantity

    @quantity.setter
    def quantity(self, value):
        self._quantity = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value
    @property
    def template_code(self):
        return self._template_code

    @template_code.setter
    def template_code(self, value):
        self._template_code = value


    def to_alipay_dict(self):
        params = dict()
        if self.delivery_express_info:
            if isinstance(self.delivery_express_info, list):
                for i in range(0, len(self.delivery_express_info)):
                    element = self.delivery_express_info[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.delivery_express_info[i] = element.to_alipay_dict()
            if hasattr(self.delivery_express_info, 'to_alipay_dict'):
                params['delivery_express_info'] = self.delivery_express_info.to_alipay_dict()
            else:
                params['delivery_express_info'] = self.delivery_express_info
        if self.estimated_delivery_earliest_time:
            if hasattr(self.estimated_delivery_earliest_time, 'to_alipay_dict'):
                params['estimated_delivery_earliest_time'] = self.estimated_delivery_earliest_time.to_alipay_dict()
            else:
                params['estimated_delivery_earliest_time'] = self.estimated_delivery_earliest_time
        if self.estimated_delivery_latest_time:
            if hasattr(self.estimated_delivery_latest_time, 'to_alipay_dict'):
                params['estimated_delivery_latest_time'] = self.estimated_delivery_latest_time.to_alipay_dict()
            else:
                params['estimated_delivery_latest_time'] = self.estimated_delivery_latest_time
        if self.gmt_create:
            if hasattr(self.gmt_create, 'to_alipay_dict'):
                params['gmt_create'] = self.gmt_create.to_alipay_dict()
            else:
                params['gmt_create'] = self.gmt_create
        if self.open_id:
            if hasattr(self.open_id, 'to_alipay_dict'):
                params['open_id'] = self.open_id.to_alipay_dict()
            else:
                params['open_id'] = self.open_id
        if self.order_desc:
            if hasattr(self.order_desc, 'to_alipay_dict'):
                params['order_desc'] = self.order_desc.to_alipay_dict()
            else:
                params['order_desc'] = self.order_desc
        if self.order_id:
            if hasattr(self.order_id, 'to_alipay_dict'):
                params['order_id'] = self.order_id.to_alipay_dict()
            else:
                params['order_id'] = self.order_id
        if self.out_biz_no:
            if hasattr(self.out_biz_no, 'to_alipay_dict'):
                params['out_biz_no'] = self.out_biz_no.to_alipay_dict()
            else:
                params['out_biz_no'] = self.out_biz_no
        if self.pid:
            if hasattr(self.pid, 'to_alipay_dict'):
                params['pid'] = self.pid.to_alipay_dict()
            else:
                params['pid'] = self.pid
        if self.quantity:
            if hasattr(self.quantity, 'to_alipay_dict'):
                params['quantity'] = self.quantity.to_alipay_dict()
            else:
                params['quantity'] = self.quantity
        if self.status:
            if hasattr(self.status, 'to_alipay_dict'):
                params['status'] = self.status.to_alipay_dict()
            else:
                params['status'] = self.status
        if self.template_code:
            if hasattr(self.template_code, 'to_alipay_dict'):
                params['template_code'] = self.template_code.to_alipay_dict()
            else:
                params['template_code'] = self.template_code
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = OrderDetailOpenApiResponse()
        if 'delivery_express_info' in d:
            o.delivery_express_info = d['delivery_express_info']
        if 'estimated_delivery_earliest_time' in d:
            o.estimated_delivery_earliest_time = d['estimated_delivery_earliest_time']
        if 'estimated_delivery_latest_time' in d:
            o.estimated_delivery_latest_time = d['estimated_delivery_latest_time']
        if 'gmt_create' in d:
            o.gmt_create = d['gmt_create']
        if 'open_id' in d:
            o.open_id = d['open_id']
        if 'order_desc' in d:
            o.order_desc = d['order_desc']
        if 'order_id' in d:
            o.order_id = d['order_id']
        if 'out_biz_no' in d:
            o.out_biz_no = d['out_biz_no']
        if 'pid' in d:
            o.pid = d['pid']
        if 'quantity' in d:
            o.quantity = d['quantity']
        if 'status' in d:
            o.status = d['status']
        if 'template_code' in d:
            o.template_code = d['template_code']
        return o


