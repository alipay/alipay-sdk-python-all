#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceTransportExpresswayTripCreateandpayModel(object):

    def __init__(self):
        self._biz_agreement_no = None
        self._end_station_name = None
        self._end_station_name_code = None
        self._end_time = None
        self._isv_id = None
        self._memo = None
        self._open_id = None
        self._out_trip_id = None
        self._plate_color = None
        self._plate_no = None
        self._replenish_deduct = None
        self._seller_id = None
        self._start_station_name = None
        self._start_station_name_code = None
        self._start_time = None
        self._subject = None
        self._total_amount = None
        self._user_id = None

    @property
    def biz_agreement_no(self):
        return self._biz_agreement_no

    @biz_agreement_no.setter
    def biz_agreement_no(self, value):
        self._biz_agreement_no = value
    @property
    def end_station_name(self):
        return self._end_station_name

    @end_station_name.setter
    def end_station_name(self, value):
        self._end_station_name = value
    @property
    def end_station_name_code(self):
        return self._end_station_name_code

    @end_station_name_code.setter
    def end_station_name_code(self, value):
        self._end_station_name_code = value
    @property
    def end_time(self):
        return self._end_time

    @end_time.setter
    def end_time(self, value):
        self._end_time = value
    @property
    def isv_id(self):
        return self._isv_id

    @isv_id.setter
    def isv_id(self, value):
        self._isv_id = value
    @property
    def memo(self):
        return self._memo

    @memo.setter
    def memo(self, value):
        self._memo = value
    @property
    def open_id(self):
        return self._open_id

    @open_id.setter
    def open_id(self, value):
        self._open_id = value
    @property
    def out_trip_id(self):
        return self._out_trip_id

    @out_trip_id.setter
    def out_trip_id(self, value):
        self._out_trip_id = value
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
    @property
    def replenish_deduct(self):
        return self._replenish_deduct

    @replenish_deduct.setter
    def replenish_deduct(self, value):
        self._replenish_deduct = value
    @property
    def seller_id(self):
        return self._seller_id

    @seller_id.setter
    def seller_id(self, value):
        self._seller_id = value
    @property
    def start_station_name(self):
        return self._start_station_name

    @start_station_name.setter
    def start_station_name(self, value):
        self._start_station_name = value
    @property
    def start_station_name_code(self):
        return self._start_station_name_code

    @start_station_name_code.setter
    def start_station_name_code(self, value):
        self._start_station_name_code = value
    @property
    def start_time(self):
        return self._start_time

    @start_time.setter
    def start_time(self, value):
        self._start_time = value
    @property
    def subject(self):
        return self._subject

    @subject.setter
    def subject(self, value):
        self._subject = value
    @property
    def total_amount(self):
        return self._total_amount

    @total_amount.setter
    def total_amount(self, value):
        self._total_amount = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.biz_agreement_no:
            if hasattr(self.biz_agreement_no, 'to_alipay_dict'):
                params['biz_agreement_no'] = self.biz_agreement_no.to_alipay_dict()
            else:
                params['biz_agreement_no'] = self.biz_agreement_no
        if self.end_station_name:
            if hasattr(self.end_station_name, 'to_alipay_dict'):
                params['end_station_name'] = self.end_station_name.to_alipay_dict()
            else:
                params['end_station_name'] = self.end_station_name
        if self.end_station_name_code:
            if hasattr(self.end_station_name_code, 'to_alipay_dict'):
                params['end_station_name_code'] = self.end_station_name_code.to_alipay_dict()
            else:
                params['end_station_name_code'] = self.end_station_name_code
        if self.end_time:
            if hasattr(self.end_time, 'to_alipay_dict'):
                params['end_time'] = self.end_time.to_alipay_dict()
            else:
                params['end_time'] = self.end_time
        if self.isv_id:
            if hasattr(self.isv_id, 'to_alipay_dict'):
                params['isv_id'] = self.isv_id.to_alipay_dict()
            else:
                params['isv_id'] = self.isv_id
        if self.memo:
            if hasattr(self.memo, 'to_alipay_dict'):
                params['memo'] = self.memo.to_alipay_dict()
            else:
                params['memo'] = self.memo
        if self.open_id:
            if hasattr(self.open_id, 'to_alipay_dict'):
                params['open_id'] = self.open_id.to_alipay_dict()
            else:
                params['open_id'] = self.open_id
        if self.out_trip_id:
            if hasattr(self.out_trip_id, 'to_alipay_dict'):
                params['out_trip_id'] = self.out_trip_id.to_alipay_dict()
            else:
                params['out_trip_id'] = self.out_trip_id
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
        if self.replenish_deduct:
            if hasattr(self.replenish_deduct, 'to_alipay_dict'):
                params['replenish_deduct'] = self.replenish_deduct.to_alipay_dict()
            else:
                params['replenish_deduct'] = self.replenish_deduct
        if self.seller_id:
            if hasattr(self.seller_id, 'to_alipay_dict'):
                params['seller_id'] = self.seller_id.to_alipay_dict()
            else:
                params['seller_id'] = self.seller_id
        if self.start_station_name:
            if hasattr(self.start_station_name, 'to_alipay_dict'):
                params['start_station_name'] = self.start_station_name.to_alipay_dict()
            else:
                params['start_station_name'] = self.start_station_name
        if self.start_station_name_code:
            if hasattr(self.start_station_name_code, 'to_alipay_dict'):
                params['start_station_name_code'] = self.start_station_name_code.to_alipay_dict()
            else:
                params['start_station_name_code'] = self.start_station_name_code
        if self.start_time:
            if hasattr(self.start_time, 'to_alipay_dict'):
                params['start_time'] = self.start_time.to_alipay_dict()
            else:
                params['start_time'] = self.start_time
        if self.subject:
            if hasattr(self.subject, 'to_alipay_dict'):
                params['subject'] = self.subject.to_alipay_dict()
            else:
                params['subject'] = self.subject
        if self.total_amount:
            if hasattr(self.total_amount, 'to_alipay_dict'):
                params['total_amount'] = self.total_amount.to_alipay_dict()
            else:
                params['total_amount'] = self.total_amount
        if self.user_id:
            if hasattr(self.user_id, 'to_alipay_dict'):
                params['user_id'] = self.user_id.to_alipay_dict()
            else:
                params['user_id'] = self.user_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceTransportExpresswayTripCreateandpayModel()
        if 'biz_agreement_no' in d:
            o.biz_agreement_no = d['biz_agreement_no']
        if 'end_station_name' in d:
            o.end_station_name = d['end_station_name']
        if 'end_station_name_code' in d:
            o.end_station_name_code = d['end_station_name_code']
        if 'end_time' in d:
            o.end_time = d['end_time']
        if 'isv_id' in d:
            o.isv_id = d['isv_id']
        if 'memo' in d:
            o.memo = d['memo']
        if 'open_id' in d:
            o.open_id = d['open_id']
        if 'out_trip_id' in d:
            o.out_trip_id = d['out_trip_id']
        if 'plate_color' in d:
            o.plate_color = d['plate_color']
        if 'plate_no' in d:
            o.plate_no = d['plate_no']
        if 'replenish_deduct' in d:
            o.replenish_deduct = d['replenish_deduct']
        if 'seller_id' in d:
            o.seller_id = d['seller_id']
        if 'start_station_name' in d:
            o.start_station_name = d['start_station_name']
        if 'start_station_name_code' in d:
            o.start_station_name_code = d['start_station_name_code']
        if 'start_time' in d:
            o.start_time = d['start_time']
        if 'subject' in d:
            o.subject = d['subject']
        if 'total_amount' in d:
            o.total_amount = d['total_amount']
        if 'user_id' in d:
            o.user_id = d['user_id']
        return o


