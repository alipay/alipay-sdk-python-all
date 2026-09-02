#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceMedicalFulfillmentNurseSyncModel(object):

    def __init__(self):
        self._expected_report_end_time = None
        self._expected_report_start_time = None
        self._fulfillment_id = None
        self._gender = None
        self._nurse_id = None
        self._nurse_name = None
        self._nurse_status = None
        self._nurse_status_desc = None
        self._nurse_status_time = None
        self._out_biz_no = None
        self._trade_order_id = None
        self._type = None
        self._verify_code = None

    @property
    def expected_report_end_time(self):
        return self._expected_report_end_time

    @expected_report_end_time.setter
    def expected_report_end_time(self, value):
        self._expected_report_end_time = value
    @property
    def expected_report_start_time(self):
        return self._expected_report_start_time

    @expected_report_start_time.setter
    def expected_report_start_time(self, value):
        self._expected_report_start_time = value
    @property
    def fulfillment_id(self):
        return self._fulfillment_id

    @fulfillment_id.setter
    def fulfillment_id(self, value):
        self._fulfillment_id = value
    @property
    def gender(self):
        return self._gender

    @gender.setter
    def gender(self, value):
        self._gender = value
    @property
    def nurse_id(self):
        return self._nurse_id

    @nurse_id.setter
    def nurse_id(self, value):
        self._nurse_id = value
    @property
    def nurse_name(self):
        return self._nurse_name

    @nurse_name.setter
    def nurse_name(self, value):
        self._nurse_name = value
    @property
    def nurse_status(self):
        return self._nurse_status

    @nurse_status.setter
    def nurse_status(self, value):
        self._nurse_status = value
    @property
    def nurse_status_desc(self):
        return self._nurse_status_desc

    @nurse_status_desc.setter
    def nurse_status_desc(self, value):
        self._nurse_status_desc = value
    @property
    def nurse_status_time(self):
        return self._nurse_status_time

    @nurse_status_time.setter
    def nurse_status_time(self, value):
        self._nurse_status_time = value
    @property
    def out_biz_no(self):
        return self._out_biz_no

    @out_biz_no.setter
    def out_biz_no(self, value):
        self._out_biz_no = value
    @property
    def trade_order_id(self):
        return self._trade_order_id

    @trade_order_id.setter
    def trade_order_id(self, value):
        self._trade_order_id = value
    @property
    def type(self):
        return self._type

    @type.setter
    def type(self, value):
        self._type = value
    @property
    def verify_code(self):
        return self._verify_code

    @verify_code.setter
    def verify_code(self, value):
        self._verify_code = value


    def to_alipay_dict(self):
        params = dict()
        if self.expected_report_end_time:
            if hasattr(self.expected_report_end_time, 'to_alipay_dict'):
                params['expected_report_end_time'] = self.expected_report_end_time.to_alipay_dict()
            else:
                params['expected_report_end_time'] = self.expected_report_end_time
        if self.expected_report_start_time:
            if hasattr(self.expected_report_start_time, 'to_alipay_dict'):
                params['expected_report_start_time'] = self.expected_report_start_time.to_alipay_dict()
            else:
                params['expected_report_start_time'] = self.expected_report_start_time
        if self.fulfillment_id:
            if hasattr(self.fulfillment_id, 'to_alipay_dict'):
                params['fulfillment_id'] = self.fulfillment_id.to_alipay_dict()
            else:
                params['fulfillment_id'] = self.fulfillment_id
        if self.gender:
            if hasattr(self.gender, 'to_alipay_dict'):
                params['gender'] = self.gender.to_alipay_dict()
            else:
                params['gender'] = self.gender
        if self.nurse_id:
            if hasattr(self.nurse_id, 'to_alipay_dict'):
                params['nurse_id'] = self.nurse_id.to_alipay_dict()
            else:
                params['nurse_id'] = self.nurse_id
        if self.nurse_name:
            if hasattr(self.nurse_name, 'to_alipay_dict'):
                params['nurse_name'] = self.nurse_name.to_alipay_dict()
            else:
                params['nurse_name'] = self.nurse_name
        if self.nurse_status:
            if hasattr(self.nurse_status, 'to_alipay_dict'):
                params['nurse_status'] = self.nurse_status.to_alipay_dict()
            else:
                params['nurse_status'] = self.nurse_status
        if self.nurse_status_desc:
            if hasattr(self.nurse_status_desc, 'to_alipay_dict'):
                params['nurse_status_desc'] = self.nurse_status_desc.to_alipay_dict()
            else:
                params['nurse_status_desc'] = self.nurse_status_desc
        if self.nurse_status_time:
            if hasattr(self.nurse_status_time, 'to_alipay_dict'):
                params['nurse_status_time'] = self.nurse_status_time.to_alipay_dict()
            else:
                params['nurse_status_time'] = self.nurse_status_time
        if self.out_biz_no:
            if hasattr(self.out_biz_no, 'to_alipay_dict'):
                params['out_biz_no'] = self.out_biz_no.to_alipay_dict()
            else:
                params['out_biz_no'] = self.out_biz_no
        if self.trade_order_id:
            if hasattr(self.trade_order_id, 'to_alipay_dict'):
                params['trade_order_id'] = self.trade_order_id.to_alipay_dict()
            else:
                params['trade_order_id'] = self.trade_order_id
        if self.type:
            if hasattr(self.type, 'to_alipay_dict'):
                params['type'] = self.type.to_alipay_dict()
            else:
                params['type'] = self.type
        if self.verify_code:
            if hasattr(self.verify_code, 'to_alipay_dict'):
                params['verify_code'] = self.verify_code.to_alipay_dict()
            else:
                params['verify_code'] = self.verify_code
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceMedicalFulfillmentNurseSyncModel()
        if 'expected_report_end_time' in d:
            o.expected_report_end_time = d['expected_report_end_time']
        if 'expected_report_start_time' in d:
            o.expected_report_start_time = d['expected_report_start_time']
        if 'fulfillment_id' in d:
            o.fulfillment_id = d['fulfillment_id']
        if 'gender' in d:
            o.gender = d['gender']
        if 'nurse_id' in d:
            o.nurse_id = d['nurse_id']
        if 'nurse_name' in d:
            o.nurse_name = d['nurse_name']
        if 'nurse_status' in d:
            o.nurse_status = d['nurse_status']
        if 'nurse_status_desc' in d:
            o.nurse_status_desc = d['nurse_status_desc']
        if 'nurse_status_time' in d:
            o.nurse_status_time = d['nurse_status_time']
        if 'out_biz_no' in d:
            o.out_biz_no = d['out_biz_no']
        if 'trade_order_id' in d:
            o.trade_order_id = d['trade_order_id']
        if 'type' in d:
            o.type = d['type']
        if 'verify_code' in d:
            o.verify_code = d['verify_code']
        return o


