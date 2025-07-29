#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.EduOrderCourseDetail import EduOrderCourseDetail
from alipay.aop.api.domain.EduOrderPaymentDetail import EduOrderPaymentDetail


class AlipayCommerceFhyeduOrderSyncModel(object):

    def __init__(self):
        self._course_detail_list = None
        self._create_time = None
        self._inst_id = None
        self._inst_name = None
        self._inst_phone = None
        self._last_payment_time = None
        self._order_id = None
        self._payment_list = None
        self._student_id = None
        self._student_name = None

    @property
    def course_detail_list(self):
        return self._course_detail_list

    @course_detail_list.setter
    def course_detail_list(self, value):
        if isinstance(value, list):
            self._course_detail_list = list()
            for i in value:
                if isinstance(i, EduOrderCourseDetail):
                    self._course_detail_list.append(i)
                else:
                    self._course_detail_list.append(EduOrderCourseDetail.from_alipay_dict(i))
    @property
    def create_time(self):
        return self._create_time

    @create_time.setter
    def create_time(self, value):
        self._create_time = value
    @property
    def inst_id(self):
        return self._inst_id

    @inst_id.setter
    def inst_id(self, value):
        self._inst_id = value
    @property
    def inst_name(self):
        return self._inst_name

    @inst_name.setter
    def inst_name(self, value):
        self._inst_name = value
    @property
    def inst_phone(self):
        return self._inst_phone

    @inst_phone.setter
    def inst_phone(self, value):
        self._inst_phone = value
    @property
    def last_payment_time(self):
        return self._last_payment_time

    @last_payment_time.setter
    def last_payment_time(self, value):
        self._last_payment_time = value
    @property
    def order_id(self):
        return self._order_id

    @order_id.setter
    def order_id(self, value):
        self._order_id = value
    @property
    def payment_list(self):
        return self._payment_list

    @payment_list.setter
    def payment_list(self, value):
        if isinstance(value, list):
            self._payment_list = list()
            for i in value:
                if isinstance(i, EduOrderPaymentDetail):
                    self._payment_list.append(i)
                else:
                    self._payment_list.append(EduOrderPaymentDetail.from_alipay_dict(i))
    @property
    def student_id(self):
        return self._student_id

    @student_id.setter
    def student_id(self, value):
        self._student_id = value
    @property
    def student_name(self):
        return self._student_name

    @student_name.setter
    def student_name(self, value):
        self._student_name = value


    def to_alipay_dict(self):
        params = dict()
        if self.course_detail_list:
            if isinstance(self.course_detail_list, list):
                for i in range(0, len(self.course_detail_list)):
                    element = self.course_detail_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.course_detail_list[i] = element.to_alipay_dict()
            if hasattr(self.course_detail_list, 'to_alipay_dict'):
                params['course_detail_list'] = self.course_detail_list.to_alipay_dict()
            else:
                params['course_detail_list'] = self.course_detail_list
        if self.create_time:
            if hasattr(self.create_time, 'to_alipay_dict'):
                params['create_time'] = self.create_time.to_alipay_dict()
            else:
                params['create_time'] = self.create_time
        if self.inst_id:
            if hasattr(self.inst_id, 'to_alipay_dict'):
                params['inst_id'] = self.inst_id.to_alipay_dict()
            else:
                params['inst_id'] = self.inst_id
        if self.inst_name:
            if hasattr(self.inst_name, 'to_alipay_dict'):
                params['inst_name'] = self.inst_name.to_alipay_dict()
            else:
                params['inst_name'] = self.inst_name
        if self.inst_phone:
            if hasattr(self.inst_phone, 'to_alipay_dict'):
                params['inst_phone'] = self.inst_phone.to_alipay_dict()
            else:
                params['inst_phone'] = self.inst_phone
        if self.last_payment_time:
            if hasattr(self.last_payment_time, 'to_alipay_dict'):
                params['last_payment_time'] = self.last_payment_time.to_alipay_dict()
            else:
                params['last_payment_time'] = self.last_payment_time
        if self.order_id:
            if hasattr(self.order_id, 'to_alipay_dict'):
                params['order_id'] = self.order_id.to_alipay_dict()
            else:
                params['order_id'] = self.order_id
        if self.payment_list:
            if isinstance(self.payment_list, list):
                for i in range(0, len(self.payment_list)):
                    element = self.payment_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.payment_list[i] = element.to_alipay_dict()
            if hasattr(self.payment_list, 'to_alipay_dict'):
                params['payment_list'] = self.payment_list.to_alipay_dict()
            else:
                params['payment_list'] = self.payment_list
        if self.student_id:
            if hasattr(self.student_id, 'to_alipay_dict'):
                params['student_id'] = self.student_id.to_alipay_dict()
            else:
                params['student_id'] = self.student_id
        if self.student_name:
            if hasattr(self.student_name, 'to_alipay_dict'):
                params['student_name'] = self.student_name.to_alipay_dict()
            else:
                params['student_name'] = self.student_name
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceFhyeduOrderSyncModel()
        if 'course_detail_list' in d:
            o.course_detail_list = d['course_detail_list']
        if 'create_time' in d:
            o.create_time = d['create_time']
        if 'inst_id' in d:
            o.inst_id = d['inst_id']
        if 'inst_name' in d:
            o.inst_name = d['inst_name']
        if 'inst_phone' in d:
            o.inst_phone = d['inst_phone']
        if 'last_payment_time' in d:
            o.last_payment_time = d['last_payment_time']
        if 'order_id' in d:
            o.order_id = d['order_id']
        if 'payment_list' in d:
            o.payment_list = d['payment_list']
        if 'student_id' in d:
            o.student_id = d['student_id']
        if 'student_name' in d:
            o.student_name = d['student_name']
        return o


