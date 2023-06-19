#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.ContactRecord import ContactRecord
from alipay.aop.api.domain.OrderChangeInfoExtIstd import OrderChangeInfoExtIstd


class AlipayCommerceLogisticsWaybillIstdstatusSyncModel(object):

    def __init__(self):
        self._action_time = None
        self._contact_records = None
        self._desc = None
        self._logistics_code = None
        self._order_ext_istd = None
        self._order_no = None
        self._out_order_no = None
        self._reach_duration = None
        self._rider_mobile_no = None
        self._rider_name = None
        self._shop_no = None
        self._status = None
        self._waybill_no = None

    @property
    def action_time(self):
        return self._action_time

    @action_time.setter
    def action_time(self, value):
        self._action_time = value
    @property
    def contact_records(self):
        return self._contact_records

    @contact_records.setter
    def contact_records(self, value):
        if isinstance(value, list):
            self._contact_records = list()
            for i in value:
                if isinstance(i, ContactRecord):
                    self._contact_records.append(i)
                else:
                    self._contact_records.append(ContactRecord.from_alipay_dict(i))
    @property
    def desc(self):
        return self._desc

    @desc.setter
    def desc(self, value):
        self._desc = value
    @property
    def logistics_code(self):
        return self._logistics_code

    @logistics_code.setter
    def logistics_code(self, value):
        self._logistics_code = value
    @property
    def order_ext_istd(self):
        return self._order_ext_istd

    @order_ext_istd.setter
    def order_ext_istd(self, value):
        if isinstance(value, OrderChangeInfoExtIstd):
            self._order_ext_istd = value
        else:
            self._order_ext_istd = OrderChangeInfoExtIstd.from_alipay_dict(value)
    @property
    def order_no(self):
        return self._order_no

    @order_no.setter
    def order_no(self, value):
        self._order_no = value
    @property
    def out_order_no(self):
        return self._out_order_no

    @out_order_no.setter
    def out_order_no(self, value):
        self._out_order_no = value
    @property
    def reach_duration(self):
        return self._reach_duration

    @reach_duration.setter
    def reach_duration(self, value):
        self._reach_duration = value
    @property
    def rider_mobile_no(self):
        return self._rider_mobile_no

    @rider_mobile_no.setter
    def rider_mobile_no(self, value):
        self._rider_mobile_no = value
    @property
    def rider_name(self):
        return self._rider_name

    @rider_name.setter
    def rider_name(self, value):
        self._rider_name = value
    @property
    def shop_no(self):
        return self._shop_no

    @shop_no.setter
    def shop_no(self, value):
        self._shop_no = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value
    @property
    def waybill_no(self):
        return self._waybill_no

    @waybill_no.setter
    def waybill_no(self, value):
        self._waybill_no = value


    def to_alipay_dict(self):
        params = dict()
        if self.action_time:
            if hasattr(self.action_time, 'to_alipay_dict'):
                params['action_time'] = self.action_time.to_alipay_dict()
            else:
                params['action_time'] = self.action_time
        if self.contact_records:
            if isinstance(self.contact_records, list):
                for i in range(0, len(self.contact_records)):
                    element = self.contact_records[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.contact_records[i] = element.to_alipay_dict()
            if hasattr(self.contact_records, 'to_alipay_dict'):
                params['contact_records'] = self.contact_records.to_alipay_dict()
            else:
                params['contact_records'] = self.contact_records
        if self.desc:
            if hasattr(self.desc, 'to_alipay_dict'):
                params['desc'] = self.desc.to_alipay_dict()
            else:
                params['desc'] = self.desc
        if self.logistics_code:
            if hasattr(self.logistics_code, 'to_alipay_dict'):
                params['logistics_code'] = self.logistics_code.to_alipay_dict()
            else:
                params['logistics_code'] = self.logistics_code
        if self.order_ext_istd:
            if hasattr(self.order_ext_istd, 'to_alipay_dict'):
                params['order_ext_istd'] = self.order_ext_istd.to_alipay_dict()
            else:
                params['order_ext_istd'] = self.order_ext_istd
        if self.order_no:
            if hasattr(self.order_no, 'to_alipay_dict'):
                params['order_no'] = self.order_no.to_alipay_dict()
            else:
                params['order_no'] = self.order_no
        if self.out_order_no:
            if hasattr(self.out_order_no, 'to_alipay_dict'):
                params['out_order_no'] = self.out_order_no.to_alipay_dict()
            else:
                params['out_order_no'] = self.out_order_no
        if self.reach_duration:
            if hasattr(self.reach_duration, 'to_alipay_dict'):
                params['reach_duration'] = self.reach_duration.to_alipay_dict()
            else:
                params['reach_duration'] = self.reach_duration
        if self.rider_mobile_no:
            if hasattr(self.rider_mobile_no, 'to_alipay_dict'):
                params['rider_mobile_no'] = self.rider_mobile_no.to_alipay_dict()
            else:
                params['rider_mobile_no'] = self.rider_mobile_no
        if self.rider_name:
            if hasattr(self.rider_name, 'to_alipay_dict'):
                params['rider_name'] = self.rider_name.to_alipay_dict()
            else:
                params['rider_name'] = self.rider_name
        if self.shop_no:
            if hasattr(self.shop_no, 'to_alipay_dict'):
                params['shop_no'] = self.shop_no.to_alipay_dict()
            else:
                params['shop_no'] = self.shop_no
        if self.status:
            if hasattr(self.status, 'to_alipay_dict'):
                params['status'] = self.status.to_alipay_dict()
            else:
                params['status'] = self.status
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
        o = AlipayCommerceLogisticsWaybillIstdstatusSyncModel()
        if 'action_time' in d:
            o.action_time = d['action_time']
        if 'contact_records' in d:
            o.contact_records = d['contact_records']
        if 'desc' in d:
            o.desc = d['desc']
        if 'logistics_code' in d:
            o.logistics_code = d['logistics_code']
        if 'order_ext_istd' in d:
            o.order_ext_istd = d['order_ext_istd']
        if 'order_no' in d:
            o.order_no = d['order_no']
        if 'out_order_no' in d:
            o.out_order_no = d['out_order_no']
        if 'reach_duration' in d:
            o.reach_duration = d['reach_duration']
        if 'rider_mobile_no' in d:
            o.rider_mobile_no = d['rider_mobile_no']
        if 'rider_name' in d:
            o.rider_name = d['rider_name']
        if 'shop_no' in d:
            o.shop_no = d['shop_no']
        if 'status' in d:
            o.status = d['status']
        if 'waybill_no' in d:
            o.waybill_no = d['waybill_no']
        return o


