#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.TicketOrderDetailInfo import TicketOrderDetailInfo


class AlipayCloudCloudpromoTicketOrderSyncModel(object):

    def __init__(self):
        self._actual_amount = None
        self._contacter_cert_no = None
        self._contacter_cert_type = None
        self._contacter_mobile_no = None
        self._contacter_name = None
        self._discount_amount = None
        self._end_time = None
        self._entry_end_time = None
        self._entry_start_time = None
        self._good_desc = None
        self._good_id = None
        self._good_name = None
        self._invalid_dates = None
        self._invalid_day_in_week = None
        self._location_name = None
        self._num = None
        self._order_amount = None
        self._order_create_time = None
        self._order_details = None
        self._order_id = None
        self._order_modified_time = None
        self._start_time = None
        self._status = None
        self._type = None
        self._unit_price = None

    @property
    def actual_amount(self):
        return self._actual_amount

    @actual_amount.setter
    def actual_amount(self, value):
        self._actual_amount = value
    @property
    def contacter_cert_no(self):
        return self._contacter_cert_no

    @contacter_cert_no.setter
    def contacter_cert_no(self, value):
        self._contacter_cert_no = value
    @property
    def contacter_cert_type(self):
        return self._contacter_cert_type

    @contacter_cert_type.setter
    def contacter_cert_type(self, value):
        self._contacter_cert_type = value
    @property
    def contacter_mobile_no(self):
        return self._contacter_mobile_no

    @contacter_mobile_no.setter
    def contacter_mobile_no(self, value):
        self._contacter_mobile_no = value
    @property
    def contacter_name(self):
        return self._contacter_name

    @contacter_name.setter
    def contacter_name(self, value):
        self._contacter_name = value
    @property
    def discount_amount(self):
        return self._discount_amount

    @discount_amount.setter
    def discount_amount(self, value):
        self._discount_amount = value
    @property
    def end_time(self):
        return self._end_time

    @end_time.setter
    def end_time(self, value):
        self._end_time = value
    @property
    def entry_end_time(self):
        return self._entry_end_time

    @entry_end_time.setter
    def entry_end_time(self, value):
        self._entry_end_time = value
    @property
    def entry_start_time(self):
        return self._entry_start_time

    @entry_start_time.setter
    def entry_start_time(self, value):
        self._entry_start_time = value
    @property
    def good_desc(self):
        return self._good_desc

    @good_desc.setter
    def good_desc(self, value):
        self._good_desc = value
    @property
    def good_id(self):
        return self._good_id

    @good_id.setter
    def good_id(self, value):
        self._good_id = value
    @property
    def good_name(self):
        return self._good_name

    @good_name.setter
    def good_name(self, value):
        self._good_name = value
    @property
    def invalid_dates(self):
        return self._invalid_dates

    @invalid_dates.setter
    def invalid_dates(self, value):
        if isinstance(value, list):
            self._invalid_dates = list()
            for i in value:
                self._invalid_dates.append(i)
    @property
    def invalid_day_in_week(self):
        return self._invalid_day_in_week

    @invalid_day_in_week.setter
    def invalid_day_in_week(self, value):
        if isinstance(value, list):
            self._invalid_day_in_week = list()
            for i in value:
                self._invalid_day_in_week.append(i)
    @property
    def location_name(self):
        return self._location_name

    @location_name.setter
    def location_name(self, value):
        self._location_name = value
    @property
    def num(self):
        return self._num

    @num.setter
    def num(self, value):
        self._num = value
    @property
    def order_amount(self):
        return self._order_amount

    @order_amount.setter
    def order_amount(self, value):
        self._order_amount = value
    @property
    def order_create_time(self):
        return self._order_create_time

    @order_create_time.setter
    def order_create_time(self, value):
        self._order_create_time = value
    @property
    def order_details(self):
        return self._order_details

    @order_details.setter
    def order_details(self, value):
        if isinstance(value, list):
            self._order_details = list()
            for i in value:
                if isinstance(i, TicketOrderDetailInfo):
                    self._order_details.append(i)
                else:
                    self._order_details.append(TicketOrderDetailInfo.from_alipay_dict(i))
    @property
    def order_id(self):
        return self._order_id

    @order_id.setter
    def order_id(self, value):
        self._order_id = value
    @property
    def order_modified_time(self):
        return self._order_modified_time

    @order_modified_time.setter
    def order_modified_time(self, value):
        self._order_modified_time = value
    @property
    def start_time(self):
        return self._start_time

    @start_time.setter
    def start_time(self, value):
        self._start_time = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value
    @property
    def type(self):
        return self._type

    @type.setter
    def type(self, value):
        self._type = value
    @property
    def unit_price(self):
        return self._unit_price

    @unit_price.setter
    def unit_price(self, value):
        self._unit_price = value


    def to_alipay_dict(self):
        params = dict()
        if self.actual_amount:
            if hasattr(self.actual_amount, 'to_alipay_dict'):
                params['actual_amount'] = self.actual_amount.to_alipay_dict()
            else:
                params['actual_amount'] = self.actual_amount
        if self.contacter_cert_no:
            if hasattr(self.contacter_cert_no, 'to_alipay_dict'):
                params['contacter_cert_no'] = self.contacter_cert_no.to_alipay_dict()
            else:
                params['contacter_cert_no'] = self.contacter_cert_no
        if self.contacter_cert_type:
            if hasattr(self.contacter_cert_type, 'to_alipay_dict'):
                params['contacter_cert_type'] = self.contacter_cert_type.to_alipay_dict()
            else:
                params['contacter_cert_type'] = self.contacter_cert_type
        if self.contacter_mobile_no:
            if hasattr(self.contacter_mobile_no, 'to_alipay_dict'):
                params['contacter_mobile_no'] = self.contacter_mobile_no.to_alipay_dict()
            else:
                params['contacter_mobile_no'] = self.contacter_mobile_no
        if self.contacter_name:
            if hasattr(self.contacter_name, 'to_alipay_dict'):
                params['contacter_name'] = self.contacter_name.to_alipay_dict()
            else:
                params['contacter_name'] = self.contacter_name
        if self.discount_amount:
            if hasattr(self.discount_amount, 'to_alipay_dict'):
                params['discount_amount'] = self.discount_amount.to_alipay_dict()
            else:
                params['discount_amount'] = self.discount_amount
        if self.end_time:
            if hasattr(self.end_time, 'to_alipay_dict'):
                params['end_time'] = self.end_time.to_alipay_dict()
            else:
                params['end_time'] = self.end_time
        if self.entry_end_time:
            if hasattr(self.entry_end_time, 'to_alipay_dict'):
                params['entry_end_time'] = self.entry_end_time.to_alipay_dict()
            else:
                params['entry_end_time'] = self.entry_end_time
        if self.entry_start_time:
            if hasattr(self.entry_start_time, 'to_alipay_dict'):
                params['entry_start_time'] = self.entry_start_time.to_alipay_dict()
            else:
                params['entry_start_time'] = self.entry_start_time
        if self.good_desc:
            if hasattr(self.good_desc, 'to_alipay_dict'):
                params['good_desc'] = self.good_desc.to_alipay_dict()
            else:
                params['good_desc'] = self.good_desc
        if self.good_id:
            if hasattr(self.good_id, 'to_alipay_dict'):
                params['good_id'] = self.good_id.to_alipay_dict()
            else:
                params['good_id'] = self.good_id
        if self.good_name:
            if hasattr(self.good_name, 'to_alipay_dict'):
                params['good_name'] = self.good_name.to_alipay_dict()
            else:
                params['good_name'] = self.good_name
        if self.invalid_dates:
            if isinstance(self.invalid_dates, list):
                for i in range(0, len(self.invalid_dates)):
                    element = self.invalid_dates[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.invalid_dates[i] = element.to_alipay_dict()
            if hasattr(self.invalid_dates, 'to_alipay_dict'):
                params['invalid_dates'] = self.invalid_dates.to_alipay_dict()
            else:
                params['invalid_dates'] = self.invalid_dates
        if self.invalid_day_in_week:
            if isinstance(self.invalid_day_in_week, list):
                for i in range(0, len(self.invalid_day_in_week)):
                    element = self.invalid_day_in_week[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.invalid_day_in_week[i] = element.to_alipay_dict()
            if hasattr(self.invalid_day_in_week, 'to_alipay_dict'):
                params['invalid_day_in_week'] = self.invalid_day_in_week.to_alipay_dict()
            else:
                params['invalid_day_in_week'] = self.invalid_day_in_week
        if self.location_name:
            if hasattr(self.location_name, 'to_alipay_dict'):
                params['location_name'] = self.location_name.to_alipay_dict()
            else:
                params['location_name'] = self.location_name
        if self.num:
            if hasattr(self.num, 'to_alipay_dict'):
                params['num'] = self.num.to_alipay_dict()
            else:
                params['num'] = self.num
        if self.order_amount:
            if hasattr(self.order_amount, 'to_alipay_dict'):
                params['order_amount'] = self.order_amount.to_alipay_dict()
            else:
                params['order_amount'] = self.order_amount
        if self.order_create_time:
            if hasattr(self.order_create_time, 'to_alipay_dict'):
                params['order_create_time'] = self.order_create_time.to_alipay_dict()
            else:
                params['order_create_time'] = self.order_create_time
        if self.order_details:
            if isinstance(self.order_details, list):
                for i in range(0, len(self.order_details)):
                    element = self.order_details[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.order_details[i] = element.to_alipay_dict()
            if hasattr(self.order_details, 'to_alipay_dict'):
                params['order_details'] = self.order_details.to_alipay_dict()
            else:
                params['order_details'] = self.order_details
        if self.order_id:
            if hasattr(self.order_id, 'to_alipay_dict'):
                params['order_id'] = self.order_id.to_alipay_dict()
            else:
                params['order_id'] = self.order_id
        if self.order_modified_time:
            if hasattr(self.order_modified_time, 'to_alipay_dict'):
                params['order_modified_time'] = self.order_modified_time.to_alipay_dict()
            else:
                params['order_modified_time'] = self.order_modified_time
        if self.start_time:
            if hasattr(self.start_time, 'to_alipay_dict'):
                params['start_time'] = self.start_time.to_alipay_dict()
            else:
                params['start_time'] = self.start_time
        if self.status:
            if hasattr(self.status, 'to_alipay_dict'):
                params['status'] = self.status.to_alipay_dict()
            else:
                params['status'] = self.status
        if self.type:
            if hasattr(self.type, 'to_alipay_dict'):
                params['type'] = self.type.to_alipay_dict()
            else:
                params['type'] = self.type
        if self.unit_price:
            if hasattr(self.unit_price, 'to_alipay_dict'):
                params['unit_price'] = self.unit_price.to_alipay_dict()
            else:
                params['unit_price'] = self.unit_price
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCloudCloudpromoTicketOrderSyncModel()
        if 'actual_amount' in d:
            o.actual_amount = d['actual_amount']
        if 'contacter_cert_no' in d:
            o.contacter_cert_no = d['contacter_cert_no']
        if 'contacter_cert_type' in d:
            o.contacter_cert_type = d['contacter_cert_type']
        if 'contacter_mobile_no' in d:
            o.contacter_mobile_no = d['contacter_mobile_no']
        if 'contacter_name' in d:
            o.contacter_name = d['contacter_name']
        if 'discount_amount' in d:
            o.discount_amount = d['discount_amount']
        if 'end_time' in d:
            o.end_time = d['end_time']
        if 'entry_end_time' in d:
            o.entry_end_time = d['entry_end_time']
        if 'entry_start_time' in d:
            o.entry_start_time = d['entry_start_time']
        if 'good_desc' in d:
            o.good_desc = d['good_desc']
        if 'good_id' in d:
            o.good_id = d['good_id']
        if 'good_name' in d:
            o.good_name = d['good_name']
        if 'invalid_dates' in d:
            o.invalid_dates = d['invalid_dates']
        if 'invalid_day_in_week' in d:
            o.invalid_day_in_week = d['invalid_day_in_week']
        if 'location_name' in d:
            o.location_name = d['location_name']
        if 'num' in d:
            o.num = d['num']
        if 'order_amount' in d:
            o.order_amount = d['order_amount']
        if 'order_create_time' in d:
            o.order_create_time = d['order_create_time']
        if 'order_details' in d:
            o.order_details = d['order_details']
        if 'order_id' in d:
            o.order_id = d['order_id']
        if 'order_modified_time' in d:
            o.order_modified_time = d['order_modified_time']
        if 'start_time' in d:
            o.start_time = d['start_time']
        if 'status' in d:
            o.status = d['status']
        if 'type' in d:
            o.type = d['type']
        if 'unit_price' in d:
            o.unit_price = d['unit_price']
        return o


