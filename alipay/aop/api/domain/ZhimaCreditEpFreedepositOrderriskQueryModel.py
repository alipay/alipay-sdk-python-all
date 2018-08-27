#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.MachineInfo import MachineInfo


class ZhimaCreditEpFreedepositOrderriskQueryModel(object):

    def __init__(self):
        self._current_use_limit = None
        self._ep_cert_no = None
        self._ep_cert_type = None
        self._ep_name = None
        self._first_rent_amount = None
        self._lease_periods = None
        self._machine_info_list = None
        self._merchant_lease_order_no = None
        self._need_pay_deposit_amount = None
        self._order_no = None
        self._pay_date = None
        self._period_lease_amount = None
        self._product_code = None
        self._rec_address = None
        self._rec_mobile = None
        self._rec_name = None
        self._remain_limit = None
        self._total_amount = None

    @property
    def current_use_limit(self):
        return self._current_use_limit

    @current_use_limit.setter
    def current_use_limit(self, value):
        self._current_use_limit = value
    @property
    def ep_cert_no(self):
        return self._ep_cert_no

    @ep_cert_no.setter
    def ep_cert_no(self, value):
        self._ep_cert_no = value
    @property
    def ep_cert_type(self):
        return self._ep_cert_type

    @ep_cert_type.setter
    def ep_cert_type(self, value):
        self._ep_cert_type = value
    @property
    def ep_name(self):
        return self._ep_name

    @ep_name.setter
    def ep_name(self, value):
        self._ep_name = value
    @property
    def first_rent_amount(self):
        return self._first_rent_amount

    @first_rent_amount.setter
    def first_rent_amount(self, value):
        self._first_rent_amount = value
    @property
    def lease_periods(self):
        return self._lease_periods

    @lease_periods.setter
    def lease_periods(self, value):
        self._lease_periods = value
    @property
    def machine_info_list(self):
        return self._machine_info_list

    @machine_info_list.setter
    def machine_info_list(self, value):
        if isinstance(value, list):
            self._machine_info_list = list()
            for i in value:
                if isinstance(i, MachineInfo):
                    self._machine_info_list.append(i)
                else:
                    self._machine_info_list.append(MachineInfo.from_alipay_dict(i))
    @property
    def merchant_lease_order_no(self):
        return self._merchant_lease_order_no

    @merchant_lease_order_no.setter
    def merchant_lease_order_no(self, value):
        self._merchant_lease_order_no = value
    @property
    def need_pay_deposit_amount(self):
        return self._need_pay_deposit_amount

    @need_pay_deposit_amount.setter
    def need_pay_deposit_amount(self, value):
        self._need_pay_deposit_amount = value
    @property
    def order_no(self):
        return self._order_no

    @order_no.setter
    def order_no(self, value):
        self._order_no = value
    @property
    def pay_date(self):
        return self._pay_date

    @pay_date.setter
    def pay_date(self, value):
        self._pay_date = value
    @property
    def period_lease_amount(self):
        return self._period_lease_amount

    @period_lease_amount.setter
    def period_lease_amount(self, value):
        self._period_lease_amount = value
    @property
    def product_code(self):
        return self._product_code

    @product_code.setter
    def product_code(self, value):
        self._product_code = value
    @property
    def rec_address(self):
        return self._rec_address

    @rec_address.setter
    def rec_address(self, value):
        self._rec_address = value
    @property
    def rec_mobile(self):
        return self._rec_mobile

    @rec_mobile.setter
    def rec_mobile(self, value):
        self._rec_mobile = value
    @property
    def rec_name(self):
        return self._rec_name

    @rec_name.setter
    def rec_name(self, value):
        self._rec_name = value
    @property
    def remain_limit(self):
        return self._remain_limit

    @remain_limit.setter
    def remain_limit(self, value):
        self._remain_limit = value
    @property
    def total_amount(self):
        return self._total_amount

    @total_amount.setter
    def total_amount(self, value):
        self._total_amount = value


    def to_alipay_dict(self):
        params = dict()
        if self.current_use_limit:
            if hasattr(self.current_use_limit, 'to_alipay_dict'):
                params['current_use_limit'] = self.current_use_limit.to_alipay_dict()
            else:
                params['current_use_limit'] = self.current_use_limit
        if self.ep_cert_no:
            if hasattr(self.ep_cert_no, 'to_alipay_dict'):
                params['ep_cert_no'] = self.ep_cert_no.to_alipay_dict()
            else:
                params['ep_cert_no'] = self.ep_cert_no
        if self.ep_cert_type:
            if hasattr(self.ep_cert_type, 'to_alipay_dict'):
                params['ep_cert_type'] = self.ep_cert_type.to_alipay_dict()
            else:
                params['ep_cert_type'] = self.ep_cert_type
        if self.ep_name:
            if hasattr(self.ep_name, 'to_alipay_dict'):
                params['ep_name'] = self.ep_name.to_alipay_dict()
            else:
                params['ep_name'] = self.ep_name
        if self.first_rent_amount:
            if hasattr(self.first_rent_amount, 'to_alipay_dict'):
                params['first_rent_amount'] = self.first_rent_amount.to_alipay_dict()
            else:
                params['first_rent_amount'] = self.first_rent_amount
        if self.lease_periods:
            if hasattr(self.lease_periods, 'to_alipay_dict'):
                params['lease_periods'] = self.lease_periods.to_alipay_dict()
            else:
                params['lease_periods'] = self.lease_periods
        if self.machine_info_list:
            if isinstance(self.machine_info_list, list):
                for i in range(0, len(self.machine_info_list)):
                    element = self.machine_info_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.machine_info_list[i] = element.to_alipay_dict()
            if hasattr(self.machine_info_list, 'to_alipay_dict'):
                params['machine_info_list'] = self.machine_info_list.to_alipay_dict()
            else:
                params['machine_info_list'] = self.machine_info_list
        if self.merchant_lease_order_no:
            if hasattr(self.merchant_lease_order_no, 'to_alipay_dict'):
                params['merchant_lease_order_no'] = self.merchant_lease_order_no.to_alipay_dict()
            else:
                params['merchant_lease_order_no'] = self.merchant_lease_order_no
        if self.need_pay_deposit_amount:
            if hasattr(self.need_pay_deposit_amount, 'to_alipay_dict'):
                params['need_pay_deposit_amount'] = self.need_pay_deposit_amount.to_alipay_dict()
            else:
                params['need_pay_deposit_amount'] = self.need_pay_deposit_amount
        if self.order_no:
            if hasattr(self.order_no, 'to_alipay_dict'):
                params['order_no'] = self.order_no.to_alipay_dict()
            else:
                params['order_no'] = self.order_no
        if self.pay_date:
            if hasattr(self.pay_date, 'to_alipay_dict'):
                params['pay_date'] = self.pay_date.to_alipay_dict()
            else:
                params['pay_date'] = self.pay_date
        if self.period_lease_amount:
            if hasattr(self.period_lease_amount, 'to_alipay_dict'):
                params['period_lease_amount'] = self.period_lease_amount.to_alipay_dict()
            else:
                params['period_lease_amount'] = self.period_lease_amount
        if self.product_code:
            if hasattr(self.product_code, 'to_alipay_dict'):
                params['product_code'] = self.product_code.to_alipay_dict()
            else:
                params['product_code'] = self.product_code
        if self.rec_address:
            if hasattr(self.rec_address, 'to_alipay_dict'):
                params['rec_address'] = self.rec_address.to_alipay_dict()
            else:
                params['rec_address'] = self.rec_address
        if self.rec_mobile:
            if hasattr(self.rec_mobile, 'to_alipay_dict'):
                params['rec_mobile'] = self.rec_mobile.to_alipay_dict()
            else:
                params['rec_mobile'] = self.rec_mobile
        if self.rec_name:
            if hasattr(self.rec_name, 'to_alipay_dict'):
                params['rec_name'] = self.rec_name.to_alipay_dict()
            else:
                params['rec_name'] = self.rec_name
        if self.remain_limit:
            if hasattr(self.remain_limit, 'to_alipay_dict'):
                params['remain_limit'] = self.remain_limit.to_alipay_dict()
            else:
                params['remain_limit'] = self.remain_limit
        if self.total_amount:
            if hasattr(self.total_amount, 'to_alipay_dict'):
                params['total_amount'] = self.total_amount.to_alipay_dict()
            else:
                params['total_amount'] = self.total_amount
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ZhimaCreditEpFreedepositOrderriskQueryModel()
        if 'current_use_limit' in d:
            o.current_use_limit = d['current_use_limit']
        if 'ep_cert_no' in d:
            o.ep_cert_no = d['ep_cert_no']
        if 'ep_cert_type' in d:
            o.ep_cert_type = d['ep_cert_type']
        if 'ep_name' in d:
            o.ep_name = d['ep_name']
        if 'first_rent_amount' in d:
            o.first_rent_amount = d['first_rent_amount']
        if 'lease_periods' in d:
            o.lease_periods = d['lease_periods']
        if 'machine_info_list' in d:
            o.machine_info_list = d['machine_info_list']
        if 'merchant_lease_order_no' in d:
            o.merchant_lease_order_no = d['merchant_lease_order_no']
        if 'need_pay_deposit_amount' in d:
            o.need_pay_deposit_amount = d['need_pay_deposit_amount']
        if 'order_no' in d:
            o.order_no = d['order_no']
        if 'pay_date' in d:
            o.pay_date = d['pay_date']
        if 'period_lease_amount' in d:
            o.period_lease_amount = d['period_lease_amount']
        if 'product_code' in d:
            o.product_code = d['product_code']
        if 'rec_address' in d:
            o.rec_address = d['rec_address']
        if 'rec_mobile' in d:
            o.rec_mobile = d['rec_mobile']
        if 'rec_name' in d:
            o.rec_name = d['rec_name']
        if 'remain_limit' in d:
            o.remain_limit = d['remain_limit']
        if 'total_amount' in d:
            o.total_amount = d['total_amount']
        return o


