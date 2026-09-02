#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class PsychologicalFulfillmentDetailData(object):

    def __init__(self):
        self._book_time = None
        self._cancel_time = None
        self._confirm_time = None
        self._counseling_avatar = None
        self._counseling_name = None
        self._counseling_professional = None
        self._counseling_type = None
        self._create_time = None
        self._fulfillment_no = None
        self._fulfillment_status = None
        self._out_order_no = None
        self._remark = None
        self._type = None

    @property
    def book_time(self):
        return self._book_time

    @book_time.setter
    def book_time(self, value):
        self._book_time = value
    @property
    def cancel_time(self):
        return self._cancel_time

    @cancel_time.setter
    def cancel_time(self, value):
        self._cancel_time = value
    @property
    def confirm_time(self):
        return self._confirm_time

    @confirm_time.setter
    def confirm_time(self, value):
        self._confirm_time = value
    @property
    def counseling_avatar(self):
        return self._counseling_avatar

    @counseling_avatar.setter
    def counseling_avatar(self, value):
        self._counseling_avatar = value
    @property
    def counseling_name(self):
        return self._counseling_name

    @counseling_name.setter
    def counseling_name(self, value):
        self._counseling_name = value
    @property
    def counseling_professional(self):
        return self._counseling_professional

    @counseling_professional.setter
    def counseling_professional(self, value):
        self._counseling_professional = value
    @property
    def counseling_type(self):
        return self._counseling_type

    @counseling_type.setter
    def counseling_type(self, value):
        self._counseling_type = value
    @property
    def create_time(self):
        return self._create_time

    @create_time.setter
    def create_time(self, value):
        self._create_time = value
    @property
    def fulfillment_no(self):
        return self._fulfillment_no

    @fulfillment_no.setter
    def fulfillment_no(self, value):
        self._fulfillment_no = value
    @property
    def fulfillment_status(self):
        return self._fulfillment_status

    @fulfillment_status.setter
    def fulfillment_status(self, value):
        self._fulfillment_status = value
    @property
    def out_order_no(self):
        return self._out_order_no

    @out_order_no.setter
    def out_order_no(self, value):
        self._out_order_no = value
    @property
    def remark(self):
        return self._remark

    @remark.setter
    def remark(self, value):
        self._remark = value
    @property
    def type(self):
        return self._type

    @type.setter
    def type(self, value):
        self._type = value


    def to_alipay_dict(self):
        params = dict()
        if self.book_time:
            if hasattr(self.book_time, 'to_alipay_dict'):
                params['book_time'] = self.book_time.to_alipay_dict()
            else:
                params['book_time'] = self.book_time
        if self.cancel_time:
            if hasattr(self.cancel_time, 'to_alipay_dict'):
                params['cancel_time'] = self.cancel_time.to_alipay_dict()
            else:
                params['cancel_time'] = self.cancel_time
        if self.confirm_time:
            if hasattr(self.confirm_time, 'to_alipay_dict'):
                params['confirm_time'] = self.confirm_time.to_alipay_dict()
            else:
                params['confirm_time'] = self.confirm_time
        if self.counseling_avatar:
            if hasattr(self.counseling_avatar, 'to_alipay_dict'):
                params['counseling_avatar'] = self.counseling_avatar.to_alipay_dict()
            else:
                params['counseling_avatar'] = self.counseling_avatar
        if self.counseling_name:
            if hasattr(self.counseling_name, 'to_alipay_dict'):
                params['counseling_name'] = self.counseling_name.to_alipay_dict()
            else:
                params['counseling_name'] = self.counseling_name
        if self.counseling_professional:
            if hasattr(self.counseling_professional, 'to_alipay_dict'):
                params['counseling_professional'] = self.counseling_professional.to_alipay_dict()
            else:
                params['counseling_professional'] = self.counseling_professional
        if self.counseling_type:
            if hasattr(self.counseling_type, 'to_alipay_dict'):
                params['counseling_type'] = self.counseling_type.to_alipay_dict()
            else:
                params['counseling_type'] = self.counseling_type
        if self.create_time:
            if hasattr(self.create_time, 'to_alipay_dict'):
                params['create_time'] = self.create_time.to_alipay_dict()
            else:
                params['create_time'] = self.create_time
        if self.fulfillment_no:
            if hasattr(self.fulfillment_no, 'to_alipay_dict'):
                params['fulfillment_no'] = self.fulfillment_no.to_alipay_dict()
            else:
                params['fulfillment_no'] = self.fulfillment_no
        if self.fulfillment_status:
            if hasattr(self.fulfillment_status, 'to_alipay_dict'):
                params['fulfillment_status'] = self.fulfillment_status.to_alipay_dict()
            else:
                params['fulfillment_status'] = self.fulfillment_status
        if self.out_order_no:
            if hasattr(self.out_order_no, 'to_alipay_dict'):
                params['out_order_no'] = self.out_order_no.to_alipay_dict()
            else:
                params['out_order_no'] = self.out_order_no
        if self.remark:
            if hasattr(self.remark, 'to_alipay_dict'):
                params['remark'] = self.remark.to_alipay_dict()
            else:
                params['remark'] = self.remark
        if self.type:
            if hasattr(self.type, 'to_alipay_dict'):
                params['type'] = self.type.to_alipay_dict()
            else:
                params['type'] = self.type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = PsychologicalFulfillmentDetailData()
        if 'book_time' in d:
            o.book_time = d['book_time']
        if 'cancel_time' in d:
            o.cancel_time = d['cancel_time']
        if 'confirm_time' in d:
            o.confirm_time = d['confirm_time']
        if 'counseling_avatar' in d:
            o.counseling_avatar = d['counseling_avatar']
        if 'counseling_name' in d:
            o.counseling_name = d['counseling_name']
        if 'counseling_professional' in d:
            o.counseling_professional = d['counseling_professional']
        if 'counseling_type' in d:
            o.counseling_type = d['counseling_type']
        if 'create_time' in d:
            o.create_time = d['create_time']
        if 'fulfillment_no' in d:
            o.fulfillment_no = d['fulfillment_no']
        if 'fulfillment_status' in d:
            o.fulfillment_status = d['fulfillment_status']
        if 'out_order_no' in d:
            o.out_order_no = d['out_order_no']
        if 'remark' in d:
            o.remark = d['remark']
        if 'type' in d:
            o.type = d['type']
        return o


