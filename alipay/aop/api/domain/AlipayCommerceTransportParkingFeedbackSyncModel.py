#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceTransportParkingFeedbackSyncModel(object):

    def __init__(self):
        self._feedback_result = None
        self._feedback_time = None
        self._feedback_type = None
        self._feedback_type_msg = None
        self._out_serial_no = None
        self._parking_id = None
        self._plate_color = None
        self._plate_no = None

    @property
    def feedback_result(self):
        return self._feedback_result

    @feedback_result.setter
    def feedback_result(self, value):
        self._feedback_result = value
    @property
    def feedback_time(self):
        return self._feedback_time

    @feedback_time.setter
    def feedback_time(self, value):
        self._feedback_time = value
    @property
    def feedback_type(self):
        return self._feedback_type

    @feedback_type.setter
    def feedback_type(self, value):
        self._feedback_type = value
    @property
    def feedback_type_msg(self):
        return self._feedback_type_msg

    @feedback_type_msg.setter
    def feedback_type_msg(self, value):
        self._feedback_type_msg = value
    @property
    def out_serial_no(self):
        return self._out_serial_no

    @out_serial_no.setter
    def out_serial_no(self, value):
        self._out_serial_no = value
    @property
    def parking_id(self):
        return self._parking_id

    @parking_id.setter
    def parking_id(self, value):
        self._parking_id = value
    @property
    def plate_color(self):
        return self._plate_color

    @plate_color.setter
    def plate_color(self, value):
        self._plate_color = value
    @property
    def plate_no(self):
        return self._plate_no

    @plate_no.setter
    def plate_no(self, value):
        self._plate_no = value


    def to_alipay_dict(self):
        params = dict()
        if self.feedback_result:
            if hasattr(self.feedback_result, 'to_alipay_dict'):
                params['feedback_result'] = self.feedback_result.to_alipay_dict()
            else:
                params['feedback_result'] = self.feedback_result
        if self.feedback_time:
            if hasattr(self.feedback_time, 'to_alipay_dict'):
                params['feedback_time'] = self.feedback_time.to_alipay_dict()
            else:
                params['feedback_time'] = self.feedback_time
        if self.feedback_type:
            if hasattr(self.feedback_type, 'to_alipay_dict'):
                params['feedback_type'] = self.feedback_type.to_alipay_dict()
            else:
                params['feedback_type'] = self.feedback_type
        if self.feedback_type_msg:
            if hasattr(self.feedback_type_msg, 'to_alipay_dict'):
                params['feedback_type_msg'] = self.feedback_type_msg.to_alipay_dict()
            else:
                params['feedback_type_msg'] = self.feedback_type_msg
        if self.out_serial_no:
            if hasattr(self.out_serial_no, 'to_alipay_dict'):
                params['out_serial_no'] = self.out_serial_no.to_alipay_dict()
            else:
                params['out_serial_no'] = self.out_serial_no
        if self.parking_id:
            if hasattr(self.parking_id, 'to_alipay_dict'):
                params['parking_id'] = self.parking_id.to_alipay_dict()
            else:
                params['parking_id'] = self.parking_id
        if self.plate_color:
            if hasattr(self.plate_color, 'to_alipay_dict'):
                params['plate_color'] = self.plate_color.to_alipay_dict()
            else:
                params['plate_color'] = self.plate_color
        if self.plate_no:
            if hasattr(self.plate_no, 'to_alipay_dict'):
                params['plate_no'] = self.plate_no.to_alipay_dict()
            else:
                params['plate_no'] = self.plate_no
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceTransportParkingFeedbackSyncModel()
        if 'feedback_result' in d:
            o.feedback_result = d['feedback_result']
        if 'feedback_time' in d:
            o.feedback_time = d['feedback_time']
        if 'feedback_type' in d:
            o.feedback_type = d['feedback_type']
        if 'feedback_type_msg' in d:
            o.feedback_type_msg = d['feedback_type_msg']
        if 'out_serial_no' in d:
            o.out_serial_no = d['out_serial_no']
        if 'parking_id' in d:
            o.parking_id = d['parking_id']
        if 'plate_color' in d:
            o.plate_color = d['plate_color']
        if 'plate_no' in d:
            o.plate_no = d['plate_no']
        return o


