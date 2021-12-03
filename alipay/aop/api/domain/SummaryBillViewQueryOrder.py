#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class SummaryBillViewQueryOrder(object):

    def __init__(self):
        self._arrangement_no = None
        self._bill_end_month = None
        self._bill_start_month = None
        self._bill_status_list = None
        self._inst_id_list = None
        self._page_num = None
        self._page_size = None
        self._payer_ip_role_id = None
        self._settle_ip_role_id_list = None
        self._settle_status_list = None
        self._settle_time_type_list = None
        self._summary_dmsn_1 = None

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
        self._bill_status_list = value
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
    def page_num(self):
        return self._page_num

    @page_num.setter
    def page_num(self, value):
        self._page_num = value
    @property
    def page_size(self):
        return self._page_size

    @page_size.setter
    def page_size(self, value):
        self._page_size = value
    @property
    def payer_ip_role_id(self):
        return self._payer_ip_role_id

    @payer_ip_role_id.setter
    def payer_ip_role_id(self, value):
        self._payer_ip_role_id = value
    @property
    def settle_ip_role_id_list(self):
        return self._settle_ip_role_id_list

    @settle_ip_role_id_list.setter
    def settle_ip_role_id_list(self, value):
        if isinstance(value, list):
            self._settle_ip_role_id_list = list()
            for i in value:
                self._settle_ip_role_id_list.append(i)
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
    @property
    def summary_dmsn_1(self):
        return self._summary_dmsn_1

    @summary_dmsn_1.setter
    def summary_dmsn_1(self, value):
        self._summary_dmsn_1 = value


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
        if self.bill_start_month:
            if hasattr(self.bill_start_month, 'to_alipay_dict'):
                params['bill_start_month'] = self.bill_start_month.to_alipay_dict()
            else:
                params['bill_start_month'] = self.bill_start_month
        if self.bill_status_list:
            if hasattr(self.bill_status_list, 'to_alipay_dict'):
                params['bill_status_list'] = self.bill_status_list.to_alipay_dict()
            else:
                params['bill_status_list'] = self.bill_status_list
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
        if self.page_num:
            if hasattr(self.page_num, 'to_alipay_dict'):
                params['page_num'] = self.page_num.to_alipay_dict()
            else:
                params['page_num'] = self.page_num
        if self.page_size:
            if hasattr(self.page_size, 'to_alipay_dict'):
                params['page_size'] = self.page_size.to_alipay_dict()
            else:
                params['page_size'] = self.page_size
        if self.payer_ip_role_id:
            if hasattr(self.payer_ip_role_id, 'to_alipay_dict'):
                params['payer_ip_role_id'] = self.payer_ip_role_id.to_alipay_dict()
            else:
                params['payer_ip_role_id'] = self.payer_ip_role_id
        if self.settle_ip_role_id_list:
            if isinstance(self.settle_ip_role_id_list, list):
                for i in range(0, len(self.settle_ip_role_id_list)):
                    element = self.settle_ip_role_id_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.settle_ip_role_id_list[i] = element.to_alipay_dict()
            if hasattr(self.settle_ip_role_id_list, 'to_alipay_dict'):
                params['settle_ip_role_id_list'] = self.settle_ip_role_id_list.to_alipay_dict()
            else:
                params['settle_ip_role_id_list'] = self.settle_ip_role_id_list
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
        if self.summary_dmsn_1:
            if hasattr(self.summary_dmsn_1, 'to_alipay_dict'):
                params['summary_dmsn_1'] = self.summary_dmsn_1.to_alipay_dict()
            else:
                params['summary_dmsn_1'] = self.summary_dmsn_1
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = SummaryBillViewQueryOrder()
        if 'arrangement_no' in d:
            o.arrangement_no = d['arrangement_no']
        if 'bill_end_month' in d:
            o.bill_end_month = d['bill_end_month']
        if 'bill_start_month' in d:
            o.bill_start_month = d['bill_start_month']
        if 'bill_status_list' in d:
            o.bill_status_list = d['bill_status_list']
        if 'inst_id_list' in d:
            o.inst_id_list = d['inst_id_list']
        if 'page_num' in d:
            o.page_num = d['page_num']
        if 'page_size' in d:
            o.page_size = d['page_size']
        if 'payer_ip_role_id' in d:
            o.payer_ip_role_id = d['payer_ip_role_id']
        if 'settle_ip_role_id_list' in d:
            o.settle_ip_role_id_list = d['settle_ip_role_id_list']
        if 'settle_status_list' in d:
            o.settle_status_list = d['settle_status_list']
        if 'settle_time_type_list' in d:
            o.settle_time_type_list = d['settle_time_type_list']
        if 'summary_dmsn_1' in d:
            o.summary_dmsn_1 = d['summary_dmsn_1']
        return o


