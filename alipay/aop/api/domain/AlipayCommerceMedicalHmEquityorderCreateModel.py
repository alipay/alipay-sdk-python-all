#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.HmAppointInfo import HmAppointInfo
from alipay.aop.api.domain.HmPayInfo import HmPayInfo
from alipay.aop.api.domain.HmProductInfo import HmProductInfo
from alipay.aop.api.domain.HmRefundInfo import HmRefundInfo


class AlipayCommerceMedicalHmEquityorderCreateModel(object):

    def __init__(self):
        self._appoint_info_list = None
        self._benefit_code = None
        self._biz_serial_no = None
        self._biz_type = None
        self._certificate_no = None
        self._certificate_type = None
        self._equity_package_code = None
        self._hm_uid = None
        self._order_source = None
        self._order_time = None
        self._order_type = None
        self._out_uid = None
        self._pay_info_list = None
        self._product_info_list = None
        self._refund_info_list = None
        self._supplier_order_id = None
        self._total_amount = None
        self._uid = None
        self._uid_open_id = None
        self._user_name = None
        self._user_phone = None

    @property
    def appoint_info_list(self):
        return self._appoint_info_list

    @appoint_info_list.setter
    def appoint_info_list(self, value):
        if isinstance(value, list):
            self._appoint_info_list = list()
            for i in value:
                if isinstance(i, HmAppointInfo):
                    self._appoint_info_list.append(i)
                else:
                    self._appoint_info_list.append(HmAppointInfo.from_alipay_dict(i))
    @property
    def benefit_code(self):
        return self._benefit_code

    @benefit_code.setter
    def benefit_code(self, value):
        self._benefit_code = value
    @property
    def biz_serial_no(self):
        return self._biz_serial_no

    @biz_serial_no.setter
    def biz_serial_no(self, value):
        self._biz_serial_no = value
    @property
    def biz_type(self):
        return self._biz_type

    @biz_type.setter
    def biz_type(self, value):
        self._biz_type = value
    @property
    def certificate_no(self):
        return self._certificate_no

    @certificate_no.setter
    def certificate_no(self, value):
        self._certificate_no = value
    @property
    def certificate_type(self):
        return self._certificate_type

    @certificate_type.setter
    def certificate_type(self, value):
        self._certificate_type = value
    @property
    def equity_package_code(self):
        return self._equity_package_code

    @equity_package_code.setter
    def equity_package_code(self, value):
        self._equity_package_code = value
    @property
    def hm_uid(self):
        return self._hm_uid

    @hm_uid.setter
    def hm_uid(self, value):
        self._hm_uid = value
    @property
    def order_source(self):
        return self._order_source

    @order_source.setter
    def order_source(self, value):
        self._order_source = value
    @property
    def order_time(self):
        return self._order_time

    @order_time.setter
    def order_time(self, value):
        self._order_time = value
    @property
    def order_type(self):
        return self._order_type

    @order_type.setter
    def order_type(self, value):
        self._order_type = value
    @property
    def out_uid(self):
        return self._out_uid

    @out_uid.setter
    def out_uid(self, value):
        self._out_uid = value
    @property
    def pay_info_list(self):
        return self._pay_info_list

    @pay_info_list.setter
    def pay_info_list(self, value):
        if isinstance(value, list):
            self._pay_info_list = list()
            for i in value:
                if isinstance(i, HmPayInfo):
                    self._pay_info_list.append(i)
                else:
                    self._pay_info_list.append(HmPayInfo.from_alipay_dict(i))
    @property
    def product_info_list(self):
        return self._product_info_list

    @product_info_list.setter
    def product_info_list(self, value):
        if isinstance(value, list):
            self._product_info_list = list()
            for i in value:
                if isinstance(i, HmProductInfo):
                    self._product_info_list.append(i)
                else:
                    self._product_info_list.append(HmProductInfo.from_alipay_dict(i))
    @property
    def refund_info_list(self):
        return self._refund_info_list

    @refund_info_list.setter
    def refund_info_list(self, value):
        if isinstance(value, list):
            self._refund_info_list = list()
            for i in value:
                if isinstance(i, HmRefundInfo):
                    self._refund_info_list.append(i)
                else:
                    self._refund_info_list.append(HmRefundInfo.from_alipay_dict(i))
    @property
    def supplier_order_id(self):
        return self._supplier_order_id

    @supplier_order_id.setter
    def supplier_order_id(self, value):
        self._supplier_order_id = value
    @property
    def total_amount(self):
        return self._total_amount

    @total_amount.setter
    def total_amount(self, value):
        self._total_amount = value
    @property
    def uid(self):
        return self._uid

    @uid.setter
    def uid(self, value):
        self._uid = value
    @property
    def uid_open_id(self):
        return self._uid_open_id

    @uid_open_id.setter
    def uid_open_id(self, value):
        self._uid_open_id = value
    @property
    def user_name(self):
        return self._user_name

    @user_name.setter
    def user_name(self, value):
        self._user_name = value
    @property
    def user_phone(self):
        return self._user_phone

    @user_phone.setter
    def user_phone(self, value):
        self._user_phone = value


    def to_alipay_dict(self):
        params = dict()
        if self.appoint_info_list:
            if isinstance(self.appoint_info_list, list):
                for i in range(0, len(self.appoint_info_list)):
                    element = self.appoint_info_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.appoint_info_list[i] = element.to_alipay_dict()
            if hasattr(self.appoint_info_list, 'to_alipay_dict'):
                params['appoint_info_list'] = self.appoint_info_list.to_alipay_dict()
            else:
                params['appoint_info_list'] = self.appoint_info_list
        if self.benefit_code:
            if hasattr(self.benefit_code, 'to_alipay_dict'):
                params['benefit_code'] = self.benefit_code.to_alipay_dict()
            else:
                params['benefit_code'] = self.benefit_code
        if self.biz_serial_no:
            if hasattr(self.biz_serial_no, 'to_alipay_dict'):
                params['biz_serial_no'] = self.biz_serial_no.to_alipay_dict()
            else:
                params['biz_serial_no'] = self.biz_serial_no
        if self.biz_type:
            if hasattr(self.biz_type, 'to_alipay_dict'):
                params['biz_type'] = self.biz_type.to_alipay_dict()
            else:
                params['biz_type'] = self.biz_type
        if self.certificate_no:
            if hasattr(self.certificate_no, 'to_alipay_dict'):
                params['certificate_no'] = self.certificate_no.to_alipay_dict()
            else:
                params['certificate_no'] = self.certificate_no
        if self.certificate_type:
            if hasattr(self.certificate_type, 'to_alipay_dict'):
                params['certificate_type'] = self.certificate_type.to_alipay_dict()
            else:
                params['certificate_type'] = self.certificate_type
        if self.equity_package_code:
            if hasattr(self.equity_package_code, 'to_alipay_dict'):
                params['equity_package_code'] = self.equity_package_code.to_alipay_dict()
            else:
                params['equity_package_code'] = self.equity_package_code
        if self.hm_uid:
            if hasattr(self.hm_uid, 'to_alipay_dict'):
                params['hm_uid'] = self.hm_uid.to_alipay_dict()
            else:
                params['hm_uid'] = self.hm_uid
        if self.order_source:
            if hasattr(self.order_source, 'to_alipay_dict'):
                params['order_source'] = self.order_source.to_alipay_dict()
            else:
                params['order_source'] = self.order_source
        if self.order_time:
            if hasattr(self.order_time, 'to_alipay_dict'):
                params['order_time'] = self.order_time.to_alipay_dict()
            else:
                params['order_time'] = self.order_time
        if self.order_type:
            if hasattr(self.order_type, 'to_alipay_dict'):
                params['order_type'] = self.order_type.to_alipay_dict()
            else:
                params['order_type'] = self.order_type
        if self.out_uid:
            if hasattr(self.out_uid, 'to_alipay_dict'):
                params['out_uid'] = self.out_uid.to_alipay_dict()
            else:
                params['out_uid'] = self.out_uid
        if self.pay_info_list:
            if isinstance(self.pay_info_list, list):
                for i in range(0, len(self.pay_info_list)):
                    element = self.pay_info_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.pay_info_list[i] = element.to_alipay_dict()
            if hasattr(self.pay_info_list, 'to_alipay_dict'):
                params['pay_info_list'] = self.pay_info_list.to_alipay_dict()
            else:
                params['pay_info_list'] = self.pay_info_list
        if self.product_info_list:
            if isinstance(self.product_info_list, list):
                for i in range(0, len(self.product_info_list)):
                    element = self.product_info_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.product_info_list[i] = element.to_alipay_dict()
            if hasattr(self.product_info_list, 'to_alipay_dict'):
                params['product_info_list'] = self.product_info_list.to_alipay_dict()
            else:
                params['product_info_list'] = self.product_info_list
        if self.refund_info_list:
            if isinstance(self.refund_info_list, list):
                for i in range(0, len(self.refund_info_list)):
                    element = self.refund_info_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.refund_info_list[i] = element.to_alipay_dict()
            if hasattr(self.refund_info_list, 'to_alipay_dict'):
                params['refund_info_list'] = self.refund_info_list.to_alipay_dict()
            else:
                params['refund_info_list'] = self.refund_info_list
        if self.supplier_order_id:
            if hasattr(self.supplier_order_id, 'to_alipay_dict'):
                params['supplier_order_id'] = self.supplier_order_id.to_alipay_dict()
            else:
                params['supplier_order_id'] = self.supplier_order_id
        if self.total_amount:
            if hasattr(self.total_amount, 'to_alipay_dict'):
                params['total_amount'] = self.total_amount.to_alipay_dict()
            else:
                params['total_amount'] = self.total_amount
        if self.uid:
            if hasattr(self.uid, 'to_alipay_dict'):
                params['uid'] = self.uid.to_alipay_dict()
            else:
                params['uid'] = self.uid
        if self.uid_open_id:
            if hasattr(self.uid_open_id, 'to_alipay_dict'):
                params['uid_open_id'] = self.uid_open_id.to_alipay_dict()
            else:
                params['uid_open_id'] = self.uid_open_id
        if self.user_name:
            if hasattr(self.user_name, 'to_alipay_dict'):
                params['user_name'] = self.user_name.to_alipay_dict()
            else:
                params['user_name'] = self.user_name
        if self.user_phone:
            if hasattr(self.user_phone, 'to_alipay_dict'):
                params['user_phone'] = self.user_phone.to_alipay_dict()
            else:
                params['user_phone'] = self.user_phone
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceMedicalHmEquityorderCreateModel()
        if 'appoint_info_list' in d:
            o.appoint_info_list = d['appoint_info_list']
        if 'benefit_code' in d:
            o.benefit_code = d['benefit_code']
        if 'biz_serial_no' in d:
            o.biz_serial_no = d['biz_serial_no']
        if 'biz_type' in d:
            o.biz_type = d['biz_type']
        if 'certificate_no' in d:
            o.certificate_no = d['certificate_no']
        if 'certificate_type' in d:
            o.certificate_type = d['certificate_type']
        if 'equity_package_code' in d:
            o.equity_package_code = d['equity_package_code']
        if 'hm_uid' in d:
            o.hm_uid = d['hm_uid']
        if 'order_source' in d:
            o.order_source = d['order_source']
        if 'order_time' in d:
            o.order_time = d['order_time']
        if 'order_type' in d:
            o.order_type = d['order_type']
        if 'out_uid' in d:
            o.out_uid = d['out_uid']
        if 'pay_info_list' in d:
            o.pay_info_list = d['pay_info_list']
        if 'product_info_list' in d:
            o.product_info_list = d['product_info_list']
        if 'refund_info_list' in d:
            o.refund_info_list = d['refund_info_list']
        if 'supplier_order_id' in d:
            o.supplier_order_id = d['supplier_order_id']
        if 'total_amount' in d:
            o.total_amount = d['total_amount']
        if 'uid' in d:
            o.uid = d['uid']
        if 'uid_open_id' in d:
            o.uid_open_id = d['uid_open_id']
        if 'user_name' in d:
            o.user_name = d['user_name']
        if 'user_phone' in d:
            o.user_phone = d['user_phone']
        return o


