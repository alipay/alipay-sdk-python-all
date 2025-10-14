#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.ExtAttributeInfo import ExtAttributeInfo
from alipay.aop.api.domain.LogisticsFacadeResponse import LogisticsFacadeResponse


class SaleOrderOpenApiRes(object):

    def __init__(self):
        self._actual_delivery_time = None
        self._combine_number = None
        self._delivery_address = None
        self._delivery_finish_time = None
        self._delivery_materials_count = None
        self._ext_attr_list = None
        self._gmt_modified = None
        self._logistics_facade_responses = None
        self._materials_total = None
        self._order_id = None
        self._point_name = None
        self._produce_finish_time = None
        self._production_materials_count = None
        self._receiver_name = None
        self._receiver_phone = None

    @property
    def actual_delivery_time(self):
        return self._actual_delivery_time

    @actual_delivery_time.setter
    def actual_delivery_time(self, value):
        self._actual_delivery_time = value
    @property
    def combine_number(self):
        return self._combine_number

    @combine_number.setter
    def combine_number(self, value):
        self._combine_number = value
    @property
    def delivery_address(self):
        return self._delivery_address

    @delivery_address.setter
    def delivery_address(self, value):
        self._delivery_address = value
    @property
    def delivery_finish_time(self):
        return self._delivery_finish_time

    @delivery_finish_time.setter
    def delivery_finish_time(self, value):
        self._delivery_finish_time = value
    @property
    def delivery_materials_count(self):
        return self._delivery_materials_count

    @delivery_materials_count.setter
    def delivery_materials_count(self, value):
        self._delivery_materials_count = value
    @property
    def ext_attr_list(self):
        return self._ext_attr_list

    @ext_attr_list.setter
    def ext_attr_list(self, value):
        if isinstance(value, list):
            self._ext_attr_list = list()
            for i in value:
                if isinstance(i, ExtAttributeInfo):
                    self._ext_attr_list.append(i)
                else:
                    self._ext_attr_list.append(ExtAttributeInfo.from_alipay_dict(i))
    @property
    def gmt_modified(self):
        return self._gmt_modified

    @gmt_modified.setter
    def gmt_modified(self, value):
        self._gmt_modified = value
    @property
    def logistics_facade_responses(self):
        return self._logistics_facade_responses

    @logistics_facade_responses.setter
    def logistics_facade_responses(self, value):
        if isinstance(value, list):
            self._logistics_facade_responses = list()
            for i in value:
                if isinstance(i, LogisticsFacadeResponse):
                    self._logistics_facade_responses.append(i)
                else:
                    self._logistics_facade_responses.append(LogisticsFacadeResponse.from_alipay_dict(i))
    @property
    def materials_total(self):
        return self._materials_total

    @materials_total.setter
    def materials_total(self, value):
        self._materials_total = value
    @property
    def order_id(self):
        return self._order_id

    @order_id.setter
    def order_id(self, value):
        self._order_id = value
    @property
    def point_name(self):
        return self._point_name

    @point_name.setter
    def point_name(self, value):
        self._point_name = value
    @property
    def produce_finish_time(self):
        return self._produce_finish_time

    @produce_finish_time.setter
    def produce_finish_time(self, value):
        self._produce_finish_time = value
    @property
    def production_materials_count(self):
        return self._production_materials_count

    @production_materials_count.setter
    def production_materials_count(self, value):
        self._production_materials_count = value
    @property
    def receiver_name(self):
        return self._receiver_name

    @receiver_name.setter
    def receiver_name(self, value):
        self._receiver_name = value
    @property
    def receiver_phone(self):
        return self._receiver_phone

    @receiver_phone.setter
    def receiver_phone(self, value):
        self._receiver_phone = value


    def to_alipay_dict(self):
        params = dict()
        if self.actual_delivery_time:
            if hasattr(self.actual_delivery_time, 'to_alipay_dict'):
                params['actual_delivery_time'] = self.actual_delivery_time.to_alipay_dict()
            else:
                params['actual_delivery_time'] = self.actual_delivery_time
        if self.combine_number:
            if hasattr(self.combine_number, 'to_alipay_dict'):
                params['combine_number'] = self.combine_number.to_alipay_dict()
            else:
                params['combine_number'] = self.combine_number
        if self.delivery_address:
            if hasattr(self.delivery_address, 'to_alipay_dict'):
                params['delivery_address'] = self.delivery_address.to_alipay_dict()
            else:
                params['delivery_address'] = self.delivery_address
        if self.delivery_finish_time:
            if hasattr(self.delivery_finish_time, 'to_alipay_dict'):
                params['delivery_finish_time'] = self.delivery_finish_time.to_alipay_dict()
            else:
                params['delivery_finish_time'] = self.delivery_finish_time
        if self.delivery_materials_count:
            if hasattr(self.delivery_materials_count, 'to_alipay_dict'):
                params['delivery_materials_count'] = self.delivery_materials_count.to_alipay_dict()
            else:
                params['delivery_materials_count'] = self.delivery_materials_count
        if self.ext_attr_list:
            if isinstance(self.ext_attr_list, list):
                for i in range(0, len(self.ext_attr_list)):
                    element = self.ext_attr_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.ext_attr_list[i] = element.to_alipay_dict()
            if hasattr(self.ext_attr_list, 'to_alipay_dict'):
                params['ext_attr_list'] = self.ext_attr_list.to_alipay_dict()
            else:
                params['ext_attr_list'] = self.ext_attr_list
        if self.gmt_modified:
            if hasattr(self.gmt_modified, 'to_alipay_dict'):
                params['gmt_modified'] = self.gmt_modified.to_alipay_dict()
            else:
                params['gmt_modified'] = self.gmt_modified
        if self.logistics_facade_responses:
            if isinstance(self.logistics_facade_responses, list):
                for i in range(0, len(self.logistics_facade_responses)):
                    element = self.logistics_facade_responses[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.logistics_facade_responses[i] = element.to_alipay_dict()
            if hasattr(self.logistics_facade_responses, 'to_alipay_dict'):
                params['logistics_facade_responses'] = self.logistics_facade_responses.to_alipay_dict()
            else:
                params['logistics_facade_responses'] = self.logistics_facade_responses
        if self.materials_total:
            if hasattr(self.materials_total, 'to_alipay_dict'):
                params['materials_total'] = self.materials_total.to_alipay_dict()
            else:
                params['materials_total'] = self.materials_total
        if self.order_id:
            if hasattr(self.order_id, 'to_alipay_dict'):
                params['order_id'] = self.order_id.to_alipay_dict()
            else:
                params['order_id'] = self.order_id
        if self.point_name:
            if hasattr(self.point_name, 'to_alipay_dict'):
                params['point_name'] = self.point_name.to_alipay_dict()
            else:
                params['point_name'] = self.point_name
        if self.produce_finish_time:
            if hasattr(self.produce_finish_time, 'to_alipay_dict'):
                params['produce_finish_time'] = self.produce_finish_time.to_alipay_dict()
            else:
                params['produce_finish_time'] = self.produce_finish_time
        if self.production_materials_count:
            if hasattr(self.production_materials_count, 'to_alipay_dict'):
                params['production_materials_count'] = self.production_materials_count.to_alipay_dict()
            else:
                params['production_materials_count'] = self.production_materials_count
        if self.receiver_name:
            if hasattr(self.receiver_name, 'to_alipay_dict'):
                params['receiver_name'] = self.receiver_name.to_alipay_dict()
            else:
                params['receiver_name'] = self.receiver_name
        if self.receiver_phone:
            if hasattr(self.receiver_phone, 'to_alipay_dict'):
                params['receiver_phone'] = self.receiver_phone.to_alipay_dict()
            else:
                params['receiver_phone'] = self.receiver_phone
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = SaleOrderOpenApiRes()
        if 'actual_delivery_time' in d:
            o.actual_delivery_time = d['actual_delivery_time']
        if 'combine_number' in d:
            o.combine_number = d['combine_number']
        if 'delivery_address' in d:
            o.delivery_address = d['delivery_address']
        if 'delivery_finish_time' in d:
            o.delivery_finish_time = d['delivery_finish_time']
        if 'delivery_materials_count' in d:
            o.delivery_materials_count = d['delivery_materials_count']
        if 'ext_attr_list' in d:
            o.ext_attr_list = d['ext_attr_list']
        if 'gmt_modified' in d:
            o.gmt_modified = d['gmt_modified']
        if 'logistics_facade_responses' in d:
            o.logistics_facade_responses = d['logistics_facade_responses']
        if 'materials_total' in d:
            o.materials_total = d['materials_total']
        if 'order_id' in d:
            o.order_id = d['order_id']
        if 'point_name' in d:
            o.point_name = d['point_name']
        if 'produce_finish_time' in d:
            o.produce_finish_time = d['produce_finish_time']
        if 'production_materials_count' in d:
            o.production_materials_count = d['production_materials_count']
        if 'receiver_name' in d:
            o.receiver_name = d['receiver_name']
        if 'receiver_phone' in d:
            o.receiver_phone = d['receiver_phone']
        return o


