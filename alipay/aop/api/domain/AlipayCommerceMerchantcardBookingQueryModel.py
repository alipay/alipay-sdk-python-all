#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceMerchantcardBookingQueryModel(object):

    def __init__(self):
        self._booking_end_date = None
        self._booking_ids = None
        self._booking_start_date = None
        self._page_no = None
        self._page_size = None
        self._phone = None
        self._shop_id = None
        self._status = None

    @property
    def booking_end_date(self):
        return self._booking_end_date

    @booking_end_date.setter
    def booking_end_date(self, value):
        self._booking_end_date = value
    @property
    def booking_ids(self):
        return self._booking_ids

    @booking_ids.setter
    def booking_ids(self, value):
        if isinstance(value, list):
            self._booking_ids = list()
            for i in value:
                self._booking_ids.append(i)
    @property
    def booking_start_date(self):
        return self._booking_start_date

    @booking_start_date.setter
    def booking_start_date(self, value):
        self._booking_start_date = value
    @property
    def page_no(self):
        return self._page_no

    @page_no.setter
    def page_no(self, value):
        self._page_no = value
    @property
    def page_size(self):
        return self._page_size

    @page_size.setter
    def page_size(self, value):
        self._page_size = value
    @property
    def phone(self):
        return self._phone

    @phone.setter
    def phone(self, value):
        self._phone = value
    @property
    def shop_id(self):
        return self._shop_id

    @shop_id.setter
    def shop_id(self, value):
        self._shop_id = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value


    def to_alipay_dict(self):
        params = dict()
        if self.booking_end_date:
            if hasattr(self.booking_end_date, 'to_alipay_dict'):
                params['booking_end_date'] = self.booking_end_date.to_alipay_dict()
            else:
                params['booking_end_date'] = self.booking_end_date
        if self.booking_ids:
            if isinstance(self.booking_ids, list):
                for i in range(0, len(self.booking_ids)):
                    element = self.booking_ids[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.booking_ids[i] = element.to_alipay_dict()
            if hasattr(self.booking_ids, 'to_alipay_dict'):
                params['booking_ids'] = self.booking_ids.to_alipay_dict()
            else:
                params['booking_ids'] = self.booking_ids
        if self.booking_start_date:
            if hasattr(self.booking_start_date, 'to_alipay_dict'):
                params['booking_start_date'] = self.booking_start_date.to_alipay_dict()
            else:
                params['booking_start_date'] = self.booking_start_date
        if self.page_no:
            if hasattr(self.page_no, 'to_alipay_dict'):
                params['page_no'] = self.page_no.to_alipay_dict()
            else:
                params['page_no'] = self.page_no
        if self.page_size:
            if hasattr(self.page_size, 'to_alipay_dict'):
                params['page_size'] = self.page_size.to_alipay_dict()
            else:
                params['page_size'] = self.page_size
        if self.phone:
            if hasattr(self.phone, 'to_alipay_dict'):
                params['phone'] = self.phone.to_alipay_dict()
            else:
                params['phone'] = self.phone
        if self.shop_id:
            if hasattr(self.shop_id, 'to_alipay_dict'):
                params['shop_id'] = self.shop_id.to_alipay_dict()
            else:
                params['shop_id'] = self.shop_id
        if self.status:
            if hasattr(self.status, 'to_alipay_dict'):
                params['status'] = self.status.to_alipay_dict()
            else:
                params['status'] = self.status
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceMerchantcardBookingQueryModel()
        if 'booking_end_date' in d:
            o.booking_end_date = d['booking_end_date']
        if 'booking_ids' in d:
            o.booking_ids = d['booking_ids']
        if 'booking_start_date' in d:
            o.booking_start_date = d['booking_start_date']
        if 'page_no' in d:
            o.page_no = d['page_no']
        if 'page_size' in d:
            o.page_size = d['page_size']
        if 'phone' in d:
            o.phone = d['phone']
        if 'shop_id' in d:
            o.shop_id = d['shop_id']
        if 'status' in d:
            o.status = d['status']
        return o


