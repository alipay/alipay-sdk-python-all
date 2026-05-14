#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.ServicepackagePatientInfo import ServicepackagePatientInfo
from alipay.aop.api.domain.ServicepackageRefundInfo import ServicepackageRefundInfo
from alipay.aop.api.domain.ServicePackageItem import ServicePackageItem


class OrderServicePackageVO(object):

    def __init__(self):
        self._amount_user = None
        self._can_refund = None
        self._doctor_team_id = None
        self._fulfillment_valid_days = None
        self._lead_doctor_id = None
        self._order_no = None
        self._order_status = None
        self._patient_info = None
        self._pay_time = None
        self._refund_info = None
        self._refund_status = None
        self._service_package_id = None
        self._service_package_items = None
        self._service_package_name = None
        self._service_package_price = None
        self._service_package_time = None

    @property
    def amount_user(self):
        return self._amount_user

    @amount_user.setter
    def amount_user(self, value):
        self._amount_user = value
    @property
    def can_refund(self):
        return self._can_refund

    @can_refund.setter
    def can_refund(self, value):
        self._can_refund = value
    @property
    def doctor_team_id(self):
        return self._doctor_team_id

    @doctor_team_id.setter
    def doctor_team_id(self, value):
        self._doctor_team_id = value
    @property
    def fulfillment_valid_days(self):
        return self._fulfillment_valid_days

    @fulfillment_valid_days.setter
    def fulfillment_valid_days(self, value):
        self._fulfillment_valid_days = value
    @property
    def lead_doctor_id(self):
        return self._lead_doctor_id

    @lead_doctor_id.setter
    def lead_doctor_id(self, value):
        self._lead_doctor_id = value
    @property
    def order_no(self):
        return self._order_no

    @order_no.setter
    def order_no(self, value):
        self._order_no = value
    @property
    def order_status(self):
        return self._order_status

    @order_status.setter
    def order_status(self, value):
        self._order_status = value
    @property
    def patient_info(self):
        return self._patient_info

    @patient_info.setter
    def patient_info(self, value):
        if isinstance(value, ServicepackagePatientInfo):
            self._patient_info = value
        else:
            self._patient_info = ServicepackagePatientInfo.from_alipay_dict(value)
    @property
    def pay_time(self):
        return self._pay_time

    @pay_time.setter
    def pay_time(self, value):
        self._pay_time = value
    @property
    def refund_info(self):
        return self._refund_info

    @refund_info.setter
    def refund_info(self, value):
        if isinstance(value, ServicepackageRefundInfo):
            self._refund_info = value
        else:
            self._refund_info = ServicepackageRefundInfo.from_alipay_dict(value)
    @property
    def refund_status(self):
        return self._refund_status

    @refund_status.setter
    def refund_status(self, value):
        self._refund_status = value
    @property
    def service_package_id(self):
        return self._service_package_id

    @service_package_id.setter
    def service_package_id(self, value):
        self._service_package_id = value
    @property
    def service_package_items(self):
        return self._service_package_items

    @service_package_items.setter
    def service_package_items(self, value):
        if isinstance(value, list):
            self._service_package_items = list()
            for i in value:
                if isinstance(i, ServicePackageItem):
                    self._service_package_items.append(i)
                else:
                    self._service_package_items.append(ServicePackageItem.from_alipay_dict(i))
    @property
    def service_package_name(self):
        return self._service_package_name

    @service_package_name.setter
    def service_package_name(self, value):
        self._service_package_name = value
    @property
    def service_package_price(self):
        return self._service_package_price

    @service_package_price.setter
    def service_package_price(self, value):
        self._service_package_price = value
    @property
    def service_package_time(self):
        return self._service_package_time

    @service_package_time.setter
    def service_package_time(self, value):
        self._service_package_time = value


    def to_alipay_dict(self):
        params = dict()
        if self.amount_user:
            if hasattr(self.amount_user, 'to_alipay_dict'):
                params['amount_user'] = self.amount_user.to_alipay_dict()
            else:
                params['amount_user'] = self.amount_user
        if self.can_refund:
            if hasattr(self.can_refund, 'to_alipay_dict'):
                params['can_refund'] = self.can_refund.to_alipay_dict()
            else:
                params['can_refund'] = self.can_refund
        if self.doctor_team_id:
            if hasattr(self.doctor_team_id, 'to_alipay_dict'):
                params['doctor_team_id'] = self.doctor_team_id.to_alipay_dict()
            else:
                params['doctor_team_id'] = self.doctor_team_id
        if self.fulfillment_valid_days:
            if hasattr(self.fulfillment_valid_days, 'to_alipay_dict'):
                params['fulfillment_valid_days'] = self.fulfillment_valid_days.to_alipay_dict()
            else:
                params['fulfillment_valid_days'] = self.fulfillment_valid_days
        if self.lead_doctor_id:
            if hasattr(self.lead_doctor_id, 'to_alipay_dict'):
                params['lead_doctor_id'] = self.lead_doctor_id.to_alipay_dict()
            else:
                params['lead_doctor_id'] = self.lead_doctor_id
        if self.order_no:
            if hasattr(self.order_no, 'to_alipay_dict'):
                params['order_no'] = self.order_no.to_alipay_dict()
            else:
                params['order_no'] = self.order_no
        if self.order_status:
            if hasattr(self.order_status, 'to_alipay_dict'):
                params['order_status'] = self.order_status.to_alipay_dict()
            else:
                params['order_status'] = self.order_status
        if self.patient_info:
            if hasattr(self.patient_info, 'to_alipay_dict'):
                params['patient_info'] = self.patient_info.to_alipay_dict()
            else:
                params['patient_info'] = self.patient_info
        if self.pay_time:
            if hasattr(self.pay_time, 'to_alipay_dict'):
                params['pay_time'] = self.pay_time.to_alipay_dict()
            else:
                params['pay_time'] = self.pay_time
        if self.refund_info:
            if hasattr(self.refund_info, 'to_alipay_dict'):
                params['refund_info'] = self.refund_info.to_alipay_dict()
            else:
                params['refund_info'] = self.refund_info
        if self.refund_status:
            if hasattr(self.refund_status, 'to_alipay_dict'):
                params['refund_status'] = self.refund_status.to_alipay_dict()
            else:
                params['refund_status'] = self.refund_status
        if self.service_package_id:
            if hasattr(self.service_package_id, 'to_alipay_dict'):
                params['service_package_id'] = self.service_package_id.to_alipay_dict()
            else:
                params['service_package_id'] = self.service_package_id
        if self.service_package_items:
            if isinstance(self.service_package_items, list):
                for i in range(0, len(self.service_package_items)):
                    element = self.service_package_items[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.service_package_items[i] = element.to_alipay_dict()
            if hasattr(self.service_package_items, 'to_alipay_dict'):
                params['service_package_items'] = self.service_package_items.to_alipay_dict()
            else:
                params['service_package_items'] = self.service_package_items
        if self.service_package_name:
            if hasattr(self.service_package_name, 'to_alipay_dict'):
                params['service_package_name'] = self.service_package_name.to_alipay_dict()
            else:
                params['service_package_name'] = self.service_package_name
        if self.service_package_price:
            if hasattr(self.service_package_price, 'to_alipay_dict'):
                params['service_package_price'] = self.service_package_price.to_alipay_dict()
            else:
                params['service_package_price'] = self.service_package_price
        if self.service_package_time:
            if hasattr(self.service_package_time, 'to_alipay_dict'):
                params['service_package_time'] = self.service_package_time.to_alipay_dict()
            else:
                params['service_package_time'] = self.service_package_time
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = OrderServicePackageVO()
        if 'amount_user' in d:
            o.amount_user = d['amount_user']
        if 'can_refund' in d:
            o.can_refund = d['can_refund']
        if 'doctor_team_id' in d:
            o.doctor_team_id = d['doctor_team_id']
        if 'fulfillment_valid_days' in d:
            o.fulfillment_valid_days = d['fulfillment_valid_days']
        if 'lead_doctor_id' in d:
            o.lead_doctor_id = d['lead_doctor_id']
        if 'order_no' in d:
            o.order_no = d['order_no']
        if 'order_status' in d:
            o.order_status = d['order_status']
        if 'patient_info' in d:
            o.patient_info = d['patient_info']
        if 'pay_time' in d:
            o.pay_time = d['pay_time']
        if 'refund_info' in d:
            o.refund_info = d['refund_info']
        if 'refund_status' in d:
            o.refund_status = d['refund_status']
        if 'service_package_id' in d:
            o.service_package_id = d['service_package_id']
        if 'service_package_items' in d:
            o.service_package_items = d['service_package_items']
        if 'service_package_name' in d:
            o.service_package_name = d['service_package_name']
        if 'service_package_price' in d:
            o.service_package_price = d['service_package_price']
        if 'service_package_time' in d:
            o.service_package_time = d['service_package_time']
        return o


