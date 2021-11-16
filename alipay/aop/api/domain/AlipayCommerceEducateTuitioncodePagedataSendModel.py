#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.TuitionOrderExtendParam import TuitionOrderExtendParam


class AlipayCommerceEducateTuitioncodePagedataSendModel(object):

    def __init__(self):
        self._alias_name = None
        self._course_end_month = None
        self._course_name = None
        self._course_start_month = None
        self._ext_info = None
        self._ext_param = None
        self._logo = None
        self._out_biz_no = None
        self._out_order_no = None
        self._pay_amount = None
        self._period = None
        self._period_type = None
        self._remark = None
        self._smid = None
        self._user_display_name = None

    @property
    def alias_name(self):
        return self._alias_name

    @alias_name.setter
    def alias_name(self, value):
        self._alias_name = value
    @property
    def course_end_month(self):
        return self._course_end_month

    @course_end_month.setter
    def course_end_month(self, value):
        self._course_end_month = value
    @property
    def course_name(self):
        return self._course_name

    @course_name.setter
    def course_name(self, value):
        self._course_name = value
    @property
    def course_start_month(self):
        return self._course_start_month

    @course_start_month.setter
    def course_start_month(self, value):
        self._course_start_month = value
    @property
    def ext_info(self):
        return self._ext_info

    @ext_info.setter
    def ext_info(self, value):
        self._ext_info = value
    @property
    def ext_param(self):
        return self._ext_param

    @ext_param.setter
    def ext_param(self, value):
        if isinstance(value, TuitionOrderExtendParam):
            self._ext_param = value
        else:
            self._ext_param = TuitionOrderExtendParam.from_alipay_dict(value)
    @property
    def logo(self):
        return self._logo

    @logo.setter
    def logo(self, value):
        self._logo = value
    @property
    def out_biz_no(self):
        return self._out_biz_no

    @out_biz_no.setter
    def out_biz_no(self, value):
        self._out_biz_no = value
    @property
    def out_order_no(self):
        return self._out_order_no

    @out_order_no.setter
    def out_order_no(self, value):
        self._out_order_no = value
    @property
    def pay_amount(self):
        return self._pay_amount

    @pay_amount.setter
    def pay_amount(self, value):
        self._pay_amount = value
    @property
    def period(self):
        return self._period

    @period.setter
    def period(self, value):
        self._period = value
    @property
    def period_type(self):
        return self._period_type

    @period_type.setter
    def period_type(self, value):
        self._period_type = value
    @property
    def remark(self):
        return self._remark

    @remark.setter
    def remark(self, value):
        self._remark = value
    @property
    def smid(self):
        return self._smid

    @smid.setter
    def smid(self, value):
        self._smid = value
    @property
    def user_display_name(self):
        return self._user_display_name

    @user_display_name.setter
    def user_display_name(self, value):
        self._user_display_name = value


    def to_alipay_dict(self):
        params = dict()
        if self.alias_name:
            if hasattr(self.alias_name, 'to_alipay_dict'):
                params['alias_name'] = self.alias_name.to_alipay_dict()
            else:
                params['alias_name'] = self.alias_name
        if self.course_end_month:
            if hasattr(self.course_end_month, 'to_alipay_dict'):
                params['course_end_month'] = self.course_end_month.to_alipay_dict()
            else:
                params['course_end_month'] = self.course_end_month
        if self.course_name:
            if hasattr(self.course_name, 'to_alipay_dict'):
                params['course_name'] = self.course_name.to_alipay_dict()
            else:
                params['course_name'] = self.course_name
        if self.course_start_month:
            if hasattr(self.course_start_month, 'to_alipay_dict'):
                params['course_start_month'] = self.course_start_month.to_alipay_dict()
            else:
                params['course_start_month'] = self.course_start_month
        if self.ext_info:
            if hasattr(self.ext_info, 'to_alipay_dict'):
                params['ext_info'] = self.ext_info.to_alipay_dict()
            else:
                params['ext_info'] = self.ext_info
        if self.ext_param:
            if hasattr(self.ext_param, 'to_alipay_dict'):
                params['ext_param'] = self.ext_param.to_alipay_dict()
            else:
                params['ext_param'] = self.ext_param
        if self.logo:
            if hasattr(self.logo, 'to_alipay_dict'):
                params['logo'] = self.logo.to_alipay_dict()
            else:
                params['logo'] = self.logo
        if self.out_biz_no:
            if hasattr(self.out_biz_no, 'to_alipay_dict'):
                params['out_biz_no'] = self.out_biz_no.to_alipay_dict()
            else:
                params['out_biz_no'] = self.out_biz_no
        if self.out_order_no:
            if hasattr(self.out_order_no, 'to_alipay_dict'):
                params['out_order_no'] = self.out_order_no.to_alipay_dict()
            else:
                params['out_order_no'] = self.out_order_no
        if self.pay_amount:
            if hasattr(self.pay_amount, 'to_alipay_dict'):
                params['pay_amount'] = self.pay_amount.to_alipay_dict()
            else:
                params['pay_amount'] = self.pay_amount
        if self.period:
            if hasattr(self.period, 'to_alipay_dict'):
                params['period'] = self.period.to_alipay_dict()
            else:
                params['period'] = self.period
        if self.period_type:
            if hasattr(self.period_type, 'to_alipay_dict'):
                params['period_type'] = self.period_type.to_alipay_dict()
            else:
                params['period_type'] = self.period_type
        if self.remark:
            if hasattr(self.remark, 'to_alipay_dict'):
                params['remark'] = self.remark.to_alipay_dict()
            else:
                params['remark'] = self.remark
        if self.smid:
            if hasattr(self.smid, 'to_alipay_dict'):
                params['smid'] = self.smid.to_alipay_dict()
            else:
                params['smid'] = self.smid
        if self.user_display_name:
            if hasattr(self.user_display_name, 'to_alipay_dict'):
                params['user_display_name'] = self.user_display_name.to_alipay_dict()
            else:
                params['user_display_name'] = self.user_display_name
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceEducateTuitioncodePagedataSendModel()
        if 'alias_name' in d:
            o.alias_name = d['alias_name']
        if 'course_end_month' in d:
            o.course_end_month = d['course_end_month']
        if 'course_name' in d:
            o.course_name = d['course_name']
        if 'course_start_month' in d:
            o.course_start_month = d['course_start_month']
        if 'ext_info' in d:
            o.ext_info = d['ext_info']
        if 'ext_param' in d:
            o.ext_param = d['ext_param']
        if 'logo' in d:
            o.logo = d['logo']
        if 'out_biz_no' in d:
            o.out_biz_no = d['out_biz_no']
        if 'out_order_no' in d:
            o.out_order_no = d['out_order_no']
        if 'pay_amount' in d:
            o.pay_amount = d['pay_amount']
        if 'period' in d:
            o.period = d['period']
        if 'period_type' in d:
            o.period_type = d['period_type']
        if 'remark' in d:
            o.remark = d['remark']
        if 'smid' in d:
            o.smid = d['smid']
        if 'user_display_name' in d:
            o.user_display_name = d['user_display_name']
        return o


