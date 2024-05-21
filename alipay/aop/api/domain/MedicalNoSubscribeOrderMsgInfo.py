#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class MedicalNoSubscribeOrderMsgInfo(object):

    def __init__(self):
        self._check_item = None
        self._check_time = None
        self._check_time_slot = None
        self._current_num = None
        self._department = None
        self._dept_loc = None
        self._hospital = None
        self._medical_num = None
        self._merchant_order_link_page = None
        self._msg_popup_url = None
        self._patient = None
        self._pay_amount = None
        self._refund_amount = None
        self._scheduled_time = None
        self._scheduled_time_slot = None
        self._summary_tip = None
        self._wait_pay_amount = None

    @property
    def check_item(self):
        return self._check_item

    @check_item.setter
    def check_item(self, value):
        self._check_item = value
    @property
    def check_time(self):
        return self._check_time

    @check_time.setter
    def check_time(self, value):
        self._check_time = value
    @property
    def check_time_slot(self):
        return self._check_time_slot

    @check_time_slot.setter
    def check_time_slot(self, value):
        self._check_time_slot = value
    @property
    def current_num(self):
        return self._current_num

    @current_num.setter
    def current_num(self, value):
        self._current_num = value
    @property
    def department(self):
        return self._department

    @department.setter
    def department(self, value):
        self._department = value
    @property
    def dept_loc(self):
        return self._dept_loc

    @dept_loc.setter
    def dept_loc(self, value):
        self._dept_loc = value
    @property
    def hospital(self):
        return self._hospital

    @hospital.setter
    def hospital(self, value):
        self._hospital = value
    @property
    def medical_num(self):
        return self._medical_num

    @medical_num.setter
    def medical_num(self, value):
        self._medical_num = value
    @property
    def merchant_order_link_page(self):
        return self._merchant_order_link_page

    @merchant_order_link_page.setter
    def merchant_order_link_page(self, value):
        self._merchant_order_link_page = value
    @property
    def msg_popup_url(self):
        return self._msg_popup_url

    @msg_popup_url.setter
    def msg_popup_url(self, value):
        self._msg_popup_url = value
    @property
    def patient(self):
        return self._patient

    @patient.setter
    def patient(self, value):
        self._patient = value
    @property
    def pay_amount(self):
        return self._pay_amount

    @pay_amount.setter
    def pay_amount(self, value):
        self._pay_amount = value
    @property
    def refund_amount(self):
        return self._refund_amount

    @refund_amount.setter
    def refund_amount(self, value):
        self._refund_amount = value
    @property
    def scheduled_time(self):
        return self._scheduled_time

    @scheduled_time.setter
    def scheduled_time(self, value):
        self._scheduled_time = value
    @property
    def scheduled_time_slot(self):
        return self._scheduled_time_slot

    @scheduled_time_slot.setter
    def scheduled_time_slot(self, value):
        self._scheduled_time_slot = value
    @property
    def summary_tip(self):
        return self._summary_tip

    @summary_tip.setter
    def summary_tip(self, value):
        self._summary_tip = value
    @property
    def wait_pay_amount(self):
        return self._wait_pay_amount

    @wait_pay_amount.setter
    def wait_pay_amount(self, value):
        self._wait_pay_amount = value


    def to_alipay_dict(self):
        params = dict()
        if self.check_item:
            if hasattr(self.check_item, 'to_alipay_dict'):
                params['check_item'] = self.check_item.to_alipay_dict()
            else:
                params['check_item'] = self.check_item
        if self.check_time:
            if hasattr(self.check_time, 'to_alipay_dict'):
                params['check_time'] = self.check_time.to_alipay_dict()
            else:
                params['check_time'] = self.check_time
        if self.check_time_slot:
            if hasattr(self.check_time_slot, 'to_alipay_dict'):
                params['check_time_slot'] = self.check_time_slot.to_alipay_dict()
            else:
                params['check_time_slot'] = self.check_time_slot
        if self.current_num:
            if hasattr(self.current_num, 'to_alipay_dict'):
                params['current_num'] = self.current_num.to_alipay_dict()
            else:
                params['current_num'] = self.current_num
        if self.department:
            if hasattr(self.department, 'to_alipay_dict'):
                params['department'] = self.department.to_alipay_dict()
            else:
                params['department'] = self.department
        if self.dept_loc:
            if hasattr(self.dept_loc, 'to_alipay_dict'):
                params['dept_loc'] = self.dept_loc.to_alipay_dict()
            else:
                params['dept_loc'] = self.dept_loc
        if self.hospital:
            if hasattr(self.hospital, 'to_alipay_dict'):
                params['hospital'] = self.hospital.to_alipay_dict()
            else:
                params['hospital'] = self.hospital
        if self.medical_num:
            if hasattr(self.medical_num, 'to_alipay_dict'):
                params['medical_num'] = self.medical_num.to_alipay_dict()
            else:
                params['medical_num'] = self.medical_num
        if self.merchant_order_link_page:
            if hasattr(self.merchant_order_link_page, 'to_alipay_dict'):
                params['merchant_order_link_page'] = self.merchant_order_link_page.to_alipay_dict()
            else:
                params['merchant_order_link_page'] = self.merchant_order_link_page
        if self.msg_popup_url:
            if hasattr(self.msg_popup_url, 'to_alipay_dict'):
                params['msg_popup_url'] = self.msg_popup_url.to_alipay_dict()
            else:
                params['msg_popup_url'] = self.msg_popup_url
        if self.patient:
            if hasattr(self.patient, 'to_alipay_dict'):
                params['patient'] = self.patient.to_alipay_dict()
            else:
                params['patient'] = self.patient
        if self.pay_amount:
            if hasattr(self.pay_amount, 'to_alipay_dict'):
                params['pay_amount'] = self.pay_amount.to_alipay_dict()
            else:
                params['pay_amount'] = self.pay_amount
        if self.refund_amount:
            if hasattr(self.refund_amount, 'to_alipay_dict'):
                params['refund_amount'] = self.refund_amount.to_alipay_dict()
            else:
                params['refund_amount'] = self.refund_amount
        if self.scheduled_time:
            if hasattr(self.scheduled_time, 'to_alipay_dict'):
                params['scheduled_time'] = self.scheduled_time.to_alipay_dict()
            else:
                params['scheduled_time'] = self.scheduled_time
        if self.scheduled_time_slot:
            if hasattr(self.scheduled_time_slot, 'to_alipay_dict'):
                params['scheduled_time_slot'] = self.scheduled_time_slot.to_alipay_dict()
            else:
                params['scheduled_time_slot'] = self.scheduled_time_slot
        if self.summary_tip:
            if hasattr(self.summary_tip, 'to_alipay_dict'):
                params['summary_tip'] = self.summary_tip.to_alipay_dict()
            else:
                params['summary_tip'] = self.summary_tip
        if self.wait_pay_amount:
            if hasattr(self.wait_pay_amount, 'to_alipay_dict'):
                params['wait_pay_amount'] = self.wait_pay_amount.to_alipay_dict()
            else:
                params['wait_pay_amount'] = self.wait_pay_amount
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = MedicalNoSubscribeOrderMsgInfo()
        if 'check_item' in d:
            o.check_item = d['check_item']
        if 'check_time' in d:
            o.check_time = d['check_time']
        if 'check_time_slot' in d:
            o.check_time_slot = d['check_time_slot']
        if 'current_num' in d:
            o.current_num = d['current_num']
        if 'department' in d:
            o.department = d['department']
        if 'dept_loc' in d:
            o.dept_loc = d['dept_loc']
        if 'hospital' in d:
            o.hospital = d['hospital']
        if 'medical_num' in d:
            o.medical_num = d['medical_num']
        if 'merchant_order_link_page' in d:
            o.merchant_order_link_page = d['merchant_order_link_page']
        if 'msg_popup_url' in d:
            o.msg_popup_url = d['msg_popup_url']
        if 'patient' in d:
            o.patient = d['patient']
        if 'pay_amount' in d:
            o.pay_amount = d['pay_amount']
        if 'refund_amount' in d:
            o.refund_amount = d['refund_amount']
        if 'scheduled_time' in d:
            o.scheduled_time = d['scheduled_time']
        if 'scheduled_time_slot' in d:
            o.scheduled_time_slot = d['scheduled_time_slot']
        if 'summary_tip' in d:
            o.summary_tip = d['summary_tip']
        if 'wait_pay_amount' in d:
            o.wait_pay_amount = d['wait_pay_amount']
        return o


