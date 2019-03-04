#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayEcoRenthouseReservationFeedbackSyncModel(object):

    def __init__(self):
        self._audit_comment = None
        self._final_look_time = None
        self._looker_name = None
        self._looker_phone = None
        self._out_biz_no = None
        self._reservation_no = None
        self._reserve_status = None
        self._room_code = None

    @property
    def audit_comment(self):
        return self._audit_comment

    @audit_comment.setter
    def audit_comment(self, value):
        self._audit_comment = value
    @property
    def final_look_time(self):
        return self._final_look_time

    @final_look_time.setter
    def final_look_time(self, value):
        self._final_look_time = value
    @property
    def looker_name(self):
        return self._looker_name

    @looker_name.setter
    def looker_name(self, value):
        self._looker_name = value
    @property
    def looker_phone(self):
        return self._looker_phone

    @looker_phone.setter
    def looker_phone(self, value):
        self._looker_phone = value
    @property
    def out_biz_no(self):
        return self._out_biz_no

    @out_biz_no.setter
    def out_biz_no(self, value):
        self._out_biz_no = value
    @property
    def reservation_no(self):
        return self._reservation_no

    @reservation_no.setter
    def reservation_no(self, value):
        self._reservation_no = value
    @property
    def reserve_status(self):
        return self._reserve_status

    @reserve_status.setter
    def reserve_status(self, value):
        self._reserve_status = value
    @property
    def room_code(self):
        return self._room_code

    @room_code.setter
    def room_code(self, value):
        self._room_code = value


    def to_alipay_dict(self):
        params = dict()
        if self.audit_comment:
            if hasattr(self.audit_comment, 'to_alipay_dict'):
                params['audit_comment'] = self.audit_comment.to_alipay_dict()
            else:
                params['audit_comment'] = self.audit_comment
        if self.final_look_time:
            if hasattr(self.final_look_time, 'to_alipay_dict'):
                params['final_look_time'] = self.final_look_time.to_alipay_dict()
            else:
                params['final_look_time'] = self.final_look_time
        if self.looker_name:
            if hasattr(self.looker_name, 'to_alipay_dict'):
                params['looker_name'] = self.looker_name.to_alipay_dict()
            else:
                params['looker_name'] = self.looker_name
        if self.looker_phone:
            if hasattr(self.looker_phone, 'to_alipay_dict'):
                params['looker_phone'] = self.looker_phone.to_alipay_dict()
            else:
                params['looker_phone'] = self.looker_phone
        if self.out_biz_no:
            if hasattr(self.out_biz_no, 'to_alipay_dict'):
                params['out_biz_no'] = self.out_biz_no.to_alipay_dict()
            else:
                params['out_biz_no'] = self.out_biz_no
        if self.reservation_no:
            if hasattr(self.reservation_no, 'to_alipay_dict'):
                params['reservation_no'] = self.reservation_no.to_alipay_dict()
            else:
                params['reservation_no'] = self.reservation_no
        if self.reserve_status:
            if hasattr(self.reserve_status, 'to_alipay_dict'):
                params['reserve_status'] = self.reserve_status.to_alipay_dict()
            else:
                params['reserve_status'] = self.reserve_status
        if self.room_code:
            if hasattr(self.room_code, 'to_alipay_dict'):
                params['room_code'] = self.room_code.to_alipay_dict()
            else:
                params['room_code'] = self.room_code
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayEcoRenthouseReservationFeedbackSyncModel()
        if 'audit_comment' in d:
            o.audit_comment = d['audit_comment']
        if 'final_look_time' in d:
            o.final_look_time = d['final_look_time']
        if 'looker_name' in d:
            o.looker_name = d['looker_name']
        if 'looker_phone' in d:
            o.looker_phone = d['looker_phone']
        if 'out_biz_no' in d:
            o.out_biz_no = d['out_biz_no']
        if 'reservation_no' in d:
            o.reservation_no = d['reservation_no']
        if 'reserve_status' in d:
            o.reserve_status = d['reserve_status']
        if 'room_code' in d:
            o.room_code = d['room_code']
        return o


