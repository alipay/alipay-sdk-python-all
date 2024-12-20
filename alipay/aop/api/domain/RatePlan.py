#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.CancelRule import CancelRule
from alipay.aop.api.domain.HotelInvoice import HotelInvoice
from alipay.aop.api.domain.NightlyRate import NightlyRate
from alipay.aop.api.domain.RatePlanLabel import RatePlanLabel


class RatePlan(object):

    def __init__(self):
        self._booking_rule_ids = None
        self._cancel_rules = None
        self._confirm_minutes = None
        self._customer_type = None
        self._identification = None
        self._identification_type = None
        self._instant_confirmation = None
        self._invoice = None
        self._nightly_rates = None
        self._ota_url = None
        self._pay_type = None
        self._pkg_product_ids = None
        self._rate_plan_id = None
        self._rate_plan_labels = None
        self._rate_plan_name = None
        self._refund_rule_id = None
        self._refund_rule_ids = None
        self._room_id = None
        self._status = None
        self._supplier_source = None

    @property
    def booking_rule_ids(self):
        return self._booking_rule_ids

    @booking_rule_ids.setter
    def booking_rule_ids(self, value):
        if isinstance(value, list):
            self._booking_rule_ids = list()
            for i in value:
                self._booking_rule_ids.append(i)
    @property
    def cancel_rules(self):
        return self._cancel_rules

    @cancel_rules.setter
    def cancel_rules(self, value):
        if isinstance(value, list):
            self._cancel_rules = list()
            for i in value:
                if isinstance(i, CancelRule):
                    self._cancel_rules.append(i)
                else:
                    self._cancel_rules.append(CancelRule.from_alipay_dict(i))
    @property
    def confirm_minutes(self):
        return self._confirm_minutes

    @confirm_minutes.setter
    def confirm_minutes(self, value):
        self._confirm_minutes = value
    @property
    def customer_type(self):
        return self._customer_type

    @customer_type.setter
    def customer_type(self, value):
        self._customer_type = value
    @property
    def identification(self):
        return self._identification

    @identification.setter
    def identification(self, value):
        self._identification = value
    @property
    def identification_type(self):
        return self._identification_type

    @identification_type.setter
    def identification_type(self, value):
        if isinstance(value, list):
            self._identification_type = list()
            for i in value:
                self._identification_type.append(i)
    @property
    def instant_confirmation(self):
        return self._instant_confirmation

    @instant_confirmation.setter
    def instant_confirmation(self, value):
        self._instant_confirmation = value
    @property
    def invoice(self):
        return self._invoice

    @invoice.setter
    def invoice(self, value):
        if isinstance(value, HotelInvoice):
            self._invoice = value
        else:
            self._invoice = HotelInvoice.from_alipay_dict(value)
    @property
    def nightly_rates(self):
        return self._nightly_rates

    @nightly_rates.setter
    def nightly_rates(self, value):
        if isinstance(value, list):
            self._nightly_rates = list()
            for i in value:
                if isinstance(i, NightlyRate):
                    self._nightly_rates.append(i)
                else:
                    self._nightly_rates.append(NightlyRate.from_alipay_dict(i))
    @property
    def ota_url(self):
        return self._ota_url

    @ota_url.setter
    def ota_url(self, value):
        self._ota_url = value
    @property
    def pay_type(self):
        return self._pay_type

    @pay_type.setter
    def pay_type(self, value):
        self._pay_type = value
    @property
    def pkg_product_ids(self):
        return self._pkg_product_ids

    @pkg_product_ids.setter
    def pkg_product_ids(self, value):
        self._pkg_product_ids = value
    @property
    def rate_plan_id(self):
        return self._rate_plan_id

    @rate_plan_id.setter
    def rate_plan_id(self, value):
        self._rate_plan_id = value
    @property
    def rate_plan_labels(self):
        return self._rate_plan_labels

    @rate_plan_labels.setter
    def rate_plan_labels(self, value):
        if isinstance(value, list):
            self._rate_plan_labels = list()
            for i in value:
                if isinstance(i, RatePlanLabel):
                    self._rate_plan_labels.append(i)
                else:
                    self._rate_plan_labels.append(RatePlanLabel.from_alipay_dict(i))
    @property
    def rate_plan_name(self):
        return self._rate_plan_name

    @rate_plan_name.setter
    def rate_plan_name(self, value):
        self._rate_plan_name = value
    @property
    def refund_rule_id(self):
        return self._refund_rule_id

    @refund_rule_id.setter
    def refund_rule_id(self, value):
        self._refund_rule_id = value
    @property
    def refund_rule_ids(self):
        return self._refund_rule_ids

    @refund_rule_ids.setter
    def refund_rule_ids(self, value):
        if isinstance(value, list):
            self._refund_rule_ids = list()
            for i in value:
                self._refund_rule_ids.append(i)
    @property
    def room_id(self):
        return self._room_id

    @room_id.setter
    def room_id(self, value):
        self._room_id = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value
    @property
    def supplier_source(self):
        return self._supplier_source

    @supplier_source.setter
    def supplier_source(self, value):
        self._supplier_source = value


    def to_alipay_dict(self):
        params = dict()
        if self.booking_rule_ids:
            if isinstance(self.booking_rule_ids, list):
                for i in range(0, len(self.booking_rule_ids)):
                    element = self.booking_rule_ids[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.booking_rule_ids[i] = element.to_alipay_dict()
            if hasattr(self.booking_rule_ids, 'to_alipay_dict'):
                params['booking_rule_ids'] = self.booking_rule_ids.to_alipay_dict()
            else:
                params['booking_rule_ids'] = self.booking_rule_ids
        if self.cancel_rules:
            if isinstance(self.cancel_rules, list):
                for i in range(0, len(self.cancel_rules)):
                    element = self.cancel_rules[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.cancel_rules[i] = element.to_alipay_dict()
            if hasattr(self.cancel_rules, 'to_alipay_dict'):
                params['cancel_rules'] = self.cancel_rules.to_alipay_dict()
            else:
                params['cancel_rules'] = self.cancel_rules
        if self.confirm_minutes:
            if hasattr(self.confirm_minutes, 'to_alipay_dict'):
                params['confirm_minutes'] = self.confirm_minutes.to_alipay_dict()
            else:
                params['confirm_minutes'] = self.confirm_minutes
        if self.customer_type:
            if hasattr(self.customer_type, 'to_alipay_dict'):
                params['customer_type'] = self.customer_type.to_alipay_dict()
            else:
                params['customer_type'] = self.customer_type
        if self.identification:
            if hasattr(self.identification, 'to_alipay_dict'):
                params['identification'] = self.identification.to_alipay_dict()
            else:
                params['identification'] = self.identification
        if self.identification_type:
            if isinstance(self.identification_type, list):
                for i in range(0, len(self.identification_type)):
                    element = self.identification_type[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.identification_type[i] = element.to_alipay_dict()
            if hasattr(self.identification_type, 'to_alipay_dict'):
                params['identification_type'] = self.identification_type.to_alipay_dict()
            else:
                params['identification_type'] = self.identification_type
        if self.instant_confirmation:
            if hasattr(self.instant_confirmation, 'to_alipay_dict'):
                params['instant_confirmation'] = self.instant_confirmation.to_alipay_dict()
            else:
                params['instant_confirmation'] = self.instant_confirmation
        if self.invoice:
            if hasattr(self.invoice, 'to_alipay_dict'):
                params['invoice'] = self.invoice.to_alipay_dict()
            else:
                params['invoice'] = self.invoice
        if self.nightly_rates:
            if isinstance(self.nightly_rates, list):
                for i in range(0, len(self.nightly_rates)):
                    element = self.nightly_rates[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.nightly_rates[i] = element.to_alipay_dict()
            if hasattr(self.nightly_rates, 'to_alipay_dict'):
                params['nightly_rates'] = self.nightly_rates.to_alipay_dict()
            else:
                params['nightly_rates'] = self.nightly_rates
        if self.ota_url:
            if hasattr(self.ota_url, 'to_alipay_dict'):
                params['ota_url'] = self.ota_url.to_alipay_dict()
            else:
                params['ota_url'] = self.ota_url
        if self.pay_type:
            if hasattr(self.pay_type, 'to_alipay_dict'):
                params['pay_type'] = self.pay_type.to_alipay_dict()
            else:
                params['pay_type'] = self.pay_type
        if self.pkg_product_ids:
            if hasattr(self.pkg_product_ids, 'to_alipay_dict'):
                params['pkg_product_ids'] = self.pkg_product_ids.to_alipay_dict()
            else:
                params['pkg_product_ids'] = self.pkg_product_ids
        if self.rate_plan_id:
            if hasattr(self.rate_plan_id, 'to_alipay_dict'):
                params['rate_plan_id'] = self.rate_plan_id.to_alipay_dict()
            else:
                params['rate_plan_id'] = self.rate_plan_id
        if self.rate_plan_labels:
            if isinstance(self.rate_plan_labels, list):
                for i in range(0, len(self.rate_plan_labels)):
                    element = self.rate_plan_labels[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.rate_plan_labels[i] = element.to_alipay_dict()
            if hasattr(self.rate_plan_labels, 'to_alipay_dict'):
                params['rate_plan_labels'] = self.rate_plan_labels.to_alipay_dict()
            else:
                params['rate_plan_labels'] = self.rate_plan_labels
        if self.rate_plan_name:
            if hasattr(self.rate_plan_name, 'to_alipay_dict'):
                params['rate_plan_name'] = self.rate_plan_name.to_alipay_dict()
            else:
                params['rate_plan_name'] = self.rate_plan_name
        if self.refund_rule_id:
            if hasattr(self.refund_rule_id, 'to_alipay_dict'):
                params['refund_rule_id'] = self.refund_rule_id.to_alipay_dict()
            else:
                params['refund_rule_id'] = self.refund_rule_id
        if self.refund_rule_ids:
            if isinstance(self.refund_rule_ids, list):
                for i in range(0, len(self.refund_rule_ids)):
                    element = self.refund_rule_ids[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.refund_rule_ids[i] = element.to_alipay_dict()
            if hasattr(self.refund_rule_ids, 'to_alipay_dict'):
                params['refund_rule_ids'] = self.refund_rule_ids.to_alipay_dict()
            else:
                params['refund_rule_ids'] = self.refund_rule_ids
        if self.room_id:
            if hasattr(self.room_id, 'to_alipay_dict'):
                params['room_id'] = self.room_id.to_alipay_dict()
            else:
                params['room_id'] = self.room_id
        if self.status:
            if hasattr(self.status, 'to_alipay_dict'):
                params['status'] = self.status.to_alipay_dict()
            else:
                params['status'] = self.status
        if self.supplier_source:
            if hasattr(self.supplier_source, 'to_alipay_dict'):
                params['supplier_source'] = self.supplier_source.to_alipay_dict()
            else:
                params['supplier_source'] = self.supplier_source
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = RatePlan()
        if 'booking_rule_ids' in d:
            o.booking_rule_ids = d['booking_rule_ids']
        if 'cancel_rules' in d:
            o.cancel_rules = d['cancel_rules']
        if 'confirm_minutes' in d:
            o.confirm_minutes = d['confirm_minutes']
        if 'customer_type' in d:
            o.customer_type = d['customer_type']
        if 'identification' in d:
            o.identification = d['identification']
        if 'identification_type' in d:
            o.identification_type = d['identification_type']
        if 'instant_confirmation' in d:
            o.instant_confirmation = d['instant_confirmation']
        if 'invoice' in d:
            o.invoice = d['invoice']
        if 'nightly_rates' in d:
            o.nightly_rates = d['nightly_rates']
        if 'ota_url' in d:
            o.ota_url = d['ota_url']
        if 'pay_type' in d:
            o.pay_type = d['pay_type']
        if 'pkg_product_ids' in d:
            o.pkg_product_ids = d['pkg_product_ids']
        if 'rate_plan_id' in d:
            o.rate_plan_id = d['rate_plan_id']
        if 'rate_plan_labels' in d:
            o.rate_plan_labels = d['rate_plan_labels']
        if 'rate_plan_name' in d:
            o.rate_plan_name = d['rate_plan_name']
        if 'refund_rule_id' in d:
            o.refund_rule_id = d['refund_rule_id']
        if 'refund_rule_ids' in d:
            o.refund_rule_ids = d['refund_rule_ids']
        if 'room_id' in d:
            o.room_id = d['room_id']
        if 'status' in d:
            o.status = d['status']
        if 'supplier_source' in d:
            o.supplier_source = d['supplier_source']
        return o


