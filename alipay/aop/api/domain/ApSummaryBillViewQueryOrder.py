#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ApSummaryBillViewQueryOrder(object):

    def __init__(self):
        self._arrangement_no = None
        self._bill_end_month = None
        self._bill_nos = None
        self._bill_start_month = None
        self._bill_status_list = None
        self._biz_pd_code_list = None
        self._business_dimension_1 = None
        self._business_dimension_2 = None
        self._business_dimension_3 = None
        self._business_dimension_4 = None
        self._business_dimension_5 = None
        self._business_dimension_6 = None
        self._business_dimension_7 = None
        self._ccy = None
        self._inst_id_list = None
        self._negative = None
        self._sales_product_code_list = None
        self._settle_ip_role_id = None
        self._settle_merchant_id = None
        self._settle_status_list = None
        self._settle_time_type_list = None

    @property
    def arrangement_no(self):
        return self._arrangement_no

    @arrangement_no.setter
    def arrangement_no(self, value):
        self._arrangement_no = value
    @property
    def bill_end_month(self):
        return self._bill_end_month

    @bill_end_month.setter
    def bill_end_month(self, value):
        self._bill_end_month = value
    @property
    def bill_nos(self):
        return self._bill_nos

    @bill_nos.setter
    def bill_nos(self, value):
        if isinstance(value, list):
            self._bill_nos = list()
            for i in value:
                self._bill_nos.append(i)
    @property
    def bill_start_month(self):
        return self._bill_start_month

    @bill_start_month.setter
    def bill_start_month(self, value):
        self._bill_start_month = value
    @property
    def bill_status_list(self):
        return self._bill_status_list

    @bill_status_list.setter
    def bill_status_list(self, value):
        if isinstance(value, list):
            self._bill_status_list = list()
            for i in value:
                self._bill_status_list.append(i)
    @property
    def biz_pd_code_list(self):
        return self._biz_pd_code_list

    @biz_pd_code_list.setter
    def biz_pd_code_list(self, value):
        if isinstance(value, list):
            self._biz_pd_code_list = list()
            for i in value:
                self._biz_pd_code_list.append(i)
    @property
    def business_dimension_1(self):
        return self._business_dimension_1

    @business_dimension_1.setter
    def business_dimension_1(self, value):
        self._business_dimension_1 = value
    @property
    def business_dimension_2(self):
        return self._business_dimension_2

    @business_dimension_2.setter
    def business_dimension_2(self, value):
        self._business_dimension_2 = value
    @property
    def business_dimension_3(self):
        return self._business_dimension_3

    @business_dimension_3.setter
    def business_dimension_3(self, value):
        self._business_dimension_3 = value
    @property
    def business_dimension_4(self):
        return self._business_dimension_4

    @business_dimension_4.setter
    def business_dimension_4(self, value):
        self._business_dimension_4 = value
    @property
    def business_dimension_5(self):
        return self._business_dimension_5

    @business_dimension_5.setter
    def business_dimension_5(self, value):
        self._business_dimension_5 = value
    @property
    def business_dimension_6(self):
        return self._business_dimension_6

    @business_dimension_6.setter
    def business_dimension_6(self, value):
        self._business_dimension_6 = value
    @property
    def business_dimension_7(self):
        return self._business_dimension_7

    @business_dimension_7.setter
    def business_dimension_7(self, value):
        self._business_dimension_7 = value
    @property
    def ccy(self):
        return self._ccy

    @ccy.setter
    def ccy(self, value):
        self._ccy = value
    @property
    def inst_id_list(self):
        return self._inst_id_list

    @inst_id_list.setter
    def inst_id_list(self, value):
        if isinstance(value, list):
            self._inst_id_list = list()
            for i in value:
                self._inst_id_list.append(i)
    @property
    def negative(self):
        return self._negative

    @negative.setter
    def negative(self, value):
        self._negative = value
    @property
    def sales_product_code_list(self):
        return self._sales_product_code_list

    @sales_product_code_list.setter
    def sales_product_code_list(self, value):
        if isinstance(value, list):
            self._sales_product_code_list = list()
            for i in value:
                self._sales_product_code_list.append(i)
    @property
    def settle_ip_role_id(self):
        return self._settle_ip_role_id

    @settle_ip_role_id.setter
    def settle_ip_role_id(self, value):
        self._settle_ip_role_id = value
    @property
    def settle_merchant_id(self):
        return self._settle_merchant_id

    @settle_merchant_id.setter
    def settle_merchant_id(self, value):
        self._settle_merchant_id = value
    @property
    def settle_status_list(self):
        return self._settle_status_list

    @settle_status_list.setter
    def settle_status_list(self, value):
        if isinstance(value, list):
            self._settle_status_list = list()
            for i in value:
                self._settle_status_list.append(i)
    @property
    def settle_time_type_list(self):
        return self._settle_time_type_list

    @settle_time_type_list.setter
    def settle_time_type_list(self, value):
        if isinstance(value, list):
            self._settle_time_type_list = list()
            for i in value:
                self._settle_time_type_list.append(i)


    def to_alipay_dict(self):
        params = dict()
        if self.arrangement_no:
            if hasattr(self.arrangement_no, 'to_alipay_dict'):
                params['arrangement_no'] = self.arrangement_no.to_alipay_dict()
            else:
                params['arrangement_no'] = self.arrangement_no
        if self.bill_end_month:
            if hasattr(self.bill_end_month, 'to_alipay_dict'):
                params['bill_end_month'] = self.bill_end_month.to_alipay_dict()
            else:
                params['bill_end_month'] = self.bill_end_month
        if self.bill_nos:
            if isinstance(self.bill_nos, list):
                for i in range(0, len(self.bill_nos)):
                    element = self.bill_nos[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.bill_nos[i] = element.to_alipay_dict()
            if hasattr(self.bill_nos, 'to_alipay_dict'):
                params['bill_nos'] = self.bill_nos.to_alipay_dict()
            else:
                params['bill_nos'] = self.bill_nos
        if self.bill_start_month:
            if hasattr(self.bill_start_month, 'to_alipay_dict'):
                params['bill_start_month'] = self.bill_start_month.to_alipay_dict()
            else:
                params['bill_start_month'] = self.bill_start_month
        if self.bill_status_list:
            if isinstance(self.bill_status_list, list):
                for i in range(0, len(self.bill_status_list)):
                    element = self.bill_status_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.bill_status_list[i] = element.to_alipay_dict()
            if hasattr(self.bill_status_list, 'to_alipay_dict'):
                params['bill_status_list'] = self.bill_status_list.to_alipay_dict()
            else:
                params['bill_status_list'] = self.bill_status_list
        if self.biz_pd_code_list:
            if isinstance(self.biz_pd_code_list, list):
                for i in range(0, len(self.biz_pd_code_list)):
                    element = self.biz_pd_code_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.biz_pd_code_list[i] = element.to_alipay_dict()
            if hasattr(self.biz_pd_code_list, 'to_alipay_dict'):
                params['biz_pd_code_list'] = self.biz_pd_code_list.to_alipay_dict()
            else:
                params['biz_pd_code_list'] = self.biz_pd_code_list
        if self.business_dimension_1:
            if hasattr(self.business_dimension_1, 'to_alipay_dict'):
                params['business_dimension_1'] = self.business_dimension_1.to_alipay_dict()
            else:
                params['business_dimension_1'] = self.business_dimension_1
        if self.business_dimension_2:
            if hasattr(self.business_dimension_2, 'to_alipay_dict'):
                params['business_dimension_2'] = self.business_dimension_2.to_alipay_dict()
            else:
                params['business_dimension_2'] = self.business_dimension_2
        if self.business_dimension_3:
            if hasattr(self.business_dimension_3, 'to_alipay_dict'):
                params['business_dimension_3'] = self.business_dimension_3.to_alipay_dict()
            else:
                params['business_dimension_3'] = self.business_dimension_3
        if self.business_dimension_4:
            if hasattr(self.business_dimension_4, 'to_alipay_dict'):
                params['business_dimension_4'] = self.business_dimension_4.to_alipay_dict()
            else:
                params['business_dimension_4'] = self.business_dimension_4
        if self.business_dimension_5:
            if hasattr(self.business_dimension_5, 'to_alipay_dict'):
                params['business_dimension_5'] = self.business_dimension_5.to_alipay_dict()
            else:
                params['business_dimension_5'] = self.business_dimension_5
        if self.business_dimension_6:
            if hasattr(self.business_dimension_6, 'to_alipay_dict'):
                params['business_dimension_6'] = self.business_dimension_6.to_alipay_dict()
            else:
                params['business_dimension_6'] = self.business_dimension_6
        if self.business_dimension_7:
            if hasattr(self.business_dimension_7, 'to_alipay_dict'):
                params['business_dimension_7'] = self.business_dimension_7.to_alipay_dict()
            else:
                params['business_dimension_7'] = self.business_dimension_7
        if self.ccy:
            if hasattr(self.ccy, 'to_alipay_dict'):
                params['ccy'] = self.ccy.to_alipay_dict()
            else:
                params['ccy'] = self.ccy
        if self.inst_id_list:
            if isinstance(self.inst_id_list, list):
                for i in range(0, len(self.inst_id_list)):
                    element = self.inst_id_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.inst_id_list[i] = element.to_alipay_dict()
            if hasattr(self.inst_id_list, 'to_alipay_dict'):
                params['inst_id_list'] = self.inst_id_list.to_alipay_dict()
            else:
                params['inst_id_list'] = self.inst_id_list
        if self.negative:
            if hasattr(self.negative, 'to_alipay_dict'):
                params['negative'] = self.negative.to_alipay_dict()
            else:
                params['negative'] = self.negative
        if self.sales_product_code_list:
            if isinstance(self.sales_product_code_list, list):
                for i in range(0, len(self.sales_product_code_list)):
                    element = self.sales_product_code_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.sales_product_code_list[i] = element.to_alipay_dict()
            if hasattr(self.sales_product_code_list, 'to_alipay_dict'):
                params['sales_product_code_list'] = self.sales_product_code_list.to_alipay_dict()
            else:
                params['sales_product_code_list'] = self.sales_product_code_list
        if self.settle_ip_role_id:
            if hasattr(self.settle_ip_role_id, 'to_alipay_dict'):
                params['settle_ip_role_id'] = self.settle_ip_role_id.to_alipay_dict()
            else:
                params['settle_ip_role_id'] = self.settle_ip_role_id
        if self.settle_merchant_id:
            if hasattr(self.settle_merchant_id, 'to_alipay_dict'):
                params['settle_merchant_id'] = self.settle_merchant_id.to_alipay_dict()
            else:
                params['settle_merchant_id'] = self.settle_merchant_id
        if self.settle_status_list:
            if isinstance(self.settle_status_list, list):
                for i in range(0, len(self.settle_status_list)):
                    element = self.settle_status_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.settle_status_list[i] = element.to_alipay_dict()
            if hasattr(self.settle_status_list, 'to_alipay_dict'):
                params['settle_status_list'] = self.settle_status_list.to_alipay_dict()
            else:
                params['settle_status_list'] = self.settle_status_list
        if self.settle_time_type_list:
            if isinstance(self.settle_time_type_list, list):
                for i in range(0, len(self.settle_time_type_list)):
                    element = self.settle_time_type_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.settle_time_type_list[i] = element.to_alipay_dict()
            if hasattr(self.settle_time_type_list, 'to_alipay_dict'):
                params['settle_time_type_list'] = self.settle_time_type_list.to_alipay_dict()
            else:
                params['settle_time_type_list'] = self.settle_time_type_list
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ApSummaryBillViewQueryOrder()
        if 'arrangement_no' in d:
            o.arrangement_no = d['arrangement_no']
        if 'bill_end_month' in d:
            o.bill_end_month = d['bill_end_month']
        if 'bill_nos' in d:
            o.bill_nos = d['bill_nos']
        if 'bill_start_month' in d:
            o.bill_start_month = d['bill_start_month']
        if 'bill_status_list' in d:
            o.bill_status_list = d['bill_status_list']
        if 'biz_pd_code_list' in d:
            o.biz_pd_code_list = d['biz_pd_code_list']
        if 'business_dimension_1' in d:
            o.business_dimension_1 = d['business_dimension_1']
        if 'business_dimension_2' in d:
            o.business_dimension_2 = d['business_dimension_2']
        if 'business_dimension_3' in d:
            o.business_dimension_3 = d['business_dimension_3']
        if 'business_dimension_4' in d:
            o.business_dimension_4 = d['business_dimension_4']
        if 'business_dimension_5' in d:
            o.business_dimension_5 = d['business_dimension_5']
        if 'business_dimension_6' in d:
            o.business_dimension_6 = d['business_dimension_6']
        if 'business_dimension_7' in d:
            o.business_dimension_7 = d['business_dimension_7']
        if 'ccy' in d:
            o.ccy = d['ccy']
        if 'inst_id_list' in d:
            o.inst_id_list = d['inst_id_list']
        if 'negative' in d:
            o.negative = d['negative']
        if 'sales_product_code_list' in d:
            o.sales_product_code_list = d['sales_product_code_list']
        if 'settle_ip_role_id' in d:
            o.settle_ip_role_id = d['settle_ip_role_id']
        if 'settle_merchant_id' in d:
            o.settle_merchant_id = d['settle_merchant_id']
        if 'settle_status_list' in d:
            o.settle_status_list = d['settle_status_list']
        if 'settle_time_type_list' in d:
            o.settle_time_type_list = d['settle_time_type_list']
        return o


