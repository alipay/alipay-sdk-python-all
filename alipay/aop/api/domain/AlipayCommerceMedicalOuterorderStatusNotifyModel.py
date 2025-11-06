#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceMedicalOuterorderStatusNotifyModel(object):

    def __init__(self):
        self._consult_business = None
        self._consult_summary_url = None
        self._consult_time = None
        self._doctor_avatar_url = None
        self._doctor_name = None
        self._doctor_title = None
        self._fulfillment_order_id = None
        self._order_status = None
        self._partner_order_id = None
        self._prescription_url = None
        self._price = None

    @property
    def consult_business(self):
        return self._consult_business

    @consult_business.setter
    def consult_business(self, value):
        self._consult_business = value
    @property
    def consult_summary_url(self):
        return self._consult_summary_url

    @consult_summary_url.setter
    def consult_summary_url(self, value):
        self._consult_summary_url = value
    @property
    def consult_time(self):
        return self._consult_time

    @consult_time.setter
    def consult_time(self, value):
        self._consult_time = value
    @property
    def doctor_avatar_url(self):
        return self._doctor_avatar_url

    @doctor_avatar_url.setter
    def doctor_avatar_url(self, value):
        self._doctor_avatar_url = value
    @property
    def doctor_name(self):
        return self._doctor_name

    @doctor_name.setter
    def doctor_name(self, value):
        self._doctor_name = value
    @property
    def doctor_title(self):
        return self._doctor_title

    @doctor_title.setter
    def doctor_title(self, value):
        self._doctor_title = value
    @property
    def fulfillment_order_id(self):
        return self._fulfillment_order_id

    @fulfillment_order_id.setter
    def fulfillment_order_id(self, value):
        self._fulfillment_order_id = value
    @property
    def order_status(self):
        return self._order_status

    @order_status.setter
    def order_status(self, value):
        self._order_status = value
    @property
    def partner_order_id(self):
        return self._partner_order_id

    @partner_order_id.setter
    def partner_order_id(self, value):
        self._partner_order_id = value
    @property
    def prescription_url(self):
        return self._prescription_url

    @prescription_url.setter
    def prescription_url(self, value):
        self._prescription_url = value
    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        self._price = value


    def to_alipay_dict(self):
        params = dict()
        if self.consult_business:
            if hasattr(self.consult_business, 'to_alipay_dict'):
                params['consult_business'] = self.consult_business.to_alipay_dict()
            else:
                params['consult_business'] = self.consult_business
        if self.consult_summary_url:
            if hasattr(self.consult_summary_url, 'to_alipay_dict'):
                params['consult_summary_url'] = self.consult_summary_url.to_alipay_dict()
            else:
                params['consult_summary_url'] = self.consult_summary_url
        if self.consult_time:
            if hasattr(self.consult_time, 'to_alipay_dict'):
                params['consult_time'] = self.consult_time.to_alipay_dict()
            else:
                params['consult_time'] = self.consult_time
        if self.doctor_avatar_url:
            if hasattr(self.doctor_avatar_url, 'to_alipay_dict'):
                params['doctor_avatar_url'] = self.doctor_avatar_url.to_alipay_dict()
            else:
                params['doctor_avatar_url'] = self.doctor_avatar_url
        if self.doctor_name:
            if hasattr(self.doctor_name, 'to_alipay_dict'):
                params['doctor_name'] = self.doctor_name.to_alipay_dict()
            else:
                params['doctor_name'] = self.doctor_name
        if self.doctor_title:
            if hasattr(self.doctor_title, 'to_alipay_dict'):
                params['doctor_title'] = self.doctor_title.to_alipay_dict()
            else:
                params['doctor_title'] = self.doctor_title
        if self.fulfillment_order_id:
            if hasattr(self.fulfillment_order_id, 'to_alipay_dict'):
                params['fulfillment_order_id'] = self.fulfillment_order_id.to_alipay_dict()
            else:
                params['fulfillment_order_id'] = self.fulfillment_order_id
        if self.order_status:
            if hasattr(self.order_status, 'to_alipay_dict'):
                params['order_status'] = self.order_status.to_alipay_dict()
            else:
                params['order_status'] = self.order_status
        if self.partner_order_id:
            if hasattr(self.partner_order_id, 'to_alipay_dict'):
                params['partner_order_id'] = self.partner_order_id.to_alipay_dict()
            else:
                params['partner_order_id'] = self.partner_order_id
        if self.prescription_url:
            if hasattr(self.prescription_url, 'to_alipay_dict'):
                params['prescription_url'] = self.prescription_url.to_alipay_dict()
            else:
                params['prescription_url'] = self.prescription_url
        if self.price:
            if hasattr(self.price, 'to_alipay_dict'):
                params['price'] = self.price.to_alipay_dict()
            else:
                params['price'] = self.price
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceMedicalOuterorderStatusNotifyModel()
        if 'consult_business' in d:
            o.consult_business = d['consult_business']
        if 'consult_summary_url' in d:
            o.consult_summary_url = d['consult_summary_url']
        if 'consult_time' in d:
            o.consult_time = d['consult_time']
        if 'doctor_avatar_url' in d:
            o.doctor_avatar_url = d['doctor_avatar_url']
        if 'doctor_name' in d:
            o.doctor_name = d['doctor_name']
        if 'doctor_title' in d:
            o.doctor_title = d['doctor_title']
        if 'fulfillment_order_id' in d:
            o.fulfillment_order_id = d['fulfillment_order_id']
        if 'order_status' in d:
            o.order_status = d['order_status']
        if 'partner_order_id' in d:
            o.partner_order_id = d['partner_order_id']
        if 'prescription_url' in d:
            o.prescription_url = d['prescription_url']
        if 'price' in d:
            o.price = d['price']
        return o


