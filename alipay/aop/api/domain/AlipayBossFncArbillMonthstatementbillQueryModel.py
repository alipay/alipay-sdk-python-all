#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.Pair import Pair


class AlipayBossFncArbillMonthstatementbillQueryModel(object):

    def __init__(self):
        self._anl_dmsn_1_list = None
        self._anl_dmsn_2_list = None
        self._anl_dmsn_3_list = None
        self._anl_dmsn_4_list = None
        self._arrangement_no = None
        self._bill_month_begin = None
        self._bill_month_end = None
        self._charge_itme_code = None
        self._check_state = None
        self._dmsn_query_list = None
        self._env_source = None
        self._inst_id = None
        self._invoice_status = None
        self._ip_id = None
        self._ip_role_id = None
        self._page_no = None
        self._page_size = None
        self._pay_status_list = None
        self._pay_way_list = None
        self._prod_code = None
        self._settle_period = None
        self._settle_type = None
        self._type_list = None

    @property
    def anl_dmsn_1_list(self):
        return self._anl_dmsn_1_list

    @anl_dmsn_1_list.setter
    def anl_dmsn_1_list(self, value):
        if isinstance(value, list):
            self._anl_dmsn_1_list = list()
            for i in value:
                self._anl_dmsn_1_list.append(i)
    @property
    def anl_dmsn_2_list(self):
        return self._anl_dmsn_2_list

    @anl_dmsn_2_list.setter
    def anl_dmsn_2_list(self, value):
        if isinstance(value, list):
            self._anl_dmsn_2_list = list()
            for i in value:
                self._anl_dmsn_2_list.append(i)
    @property
    def anl_dmsn_3_list(self):
        return self._anl_dmsn_3_list

    @anl_dmsn_3_list.setter
    def anl_dmsn_3_list(self, value):
        if isinstance(value, list):
            self._anl_dmsn_3_list = list()
            for i in value:
                self._anl_dmsn_3_list.append(i)
    @property
    def anl_dmsn_4_list(self):
        return self._anl_dmsn_4_list

    @anl_dmsn_4_list.setter
    def anl_dmsn_4_list(self, value):
        if isinstance(value, list):
            self._anl_dmsn_4_list = list()
            for i in value:
                self._anl_dmsn_4_list.append(i)
    @property
    def arrangement_no(self):
        return self._arrangement_no

    @arrangement_no.setter
    def arrangement_no(self, value):
        self._arrangement_no = value
    @property
    def bill_month_begin(self):
        return self._bill_month_begin

    @bill_month_begin.setter
    def bill_month_begin(self, value):
        self._bill_month_begin = value
    @property
    def bill_month_end(self):
        return self._bill_month_end

    @bill_month_end.setter
    def bill_month_end(self, value):
        self._bill_month_end = value
    @property
    def charge_itme_code(self):
        return self._charge_itme_code

    @charge_itme_code.setter
    def charge_itme_code(self, value):
        self._charge_itme_code = value
    @property
    def check_state(self):
        return self._check_state

    @check_state.setter
    def check_state(self, value):
        if isinstance(value, list):
            self._check_state = list()
            for i in value:
                self._check_state.append(i)
    @property
    def dmsn_query_list(self):
        return self._dmsn_query_list

    @dmsn_query_list.setter
    def dmsn_query_list(self, value):
        if isinstance(value, list):
            self._dmsn_query_list = list()
            for i in value:
                if isinstance(i, Pair):
                    self._dmsn_query_list.append(i)
                else:
                    self._dmsn_query_list.append(Pair.from_alipay_dict(i))
    @property
    def env_source(self):
        return self._env_source

    @env_source.setter
    def env_source(self, value):
        self._env_source = value
    @property
    def inst_id(self):
        return self._inst_id

    @inst_id.setter
    def inst_id(self, value):
        self._inst_id = value
    @property
    def invoice_status(self):
        return self._invoice_status

    @invoice_status.setter
    def invoice_status(self, value):
        if isinstance(value, list):
            self._invoice_status = list()
            for i in value:
                self._invoice_status.append(i)
    @property
    def ip_id(self):
        return self._ip_id

    @ip_id.setter
    def ip_id(self, value):
        self._ip_id = value
    @property
    def ip_role_id(self):
        return self._ip_role_id

    @ip_role_id.setter
    def ip_role_id(self, value):
        self._ip_role_id = value
    @property
    def page_no(self):
        return self._page_no

    @page_no.setter
    def page_no(self, value):
        self._page_no = value
    @property
    def page_size(self):
        return self._page_size

    @page_size.setter
    def page_size(self, value):
        self._page_size = value
    @property
    def pay_status_list(self):
        return self._pay_status_list

    @pay_status_list.setter
    def pay_status_list(self, value):
        if isinstance(value, list):
            self._pay_status_list = list()
            for i in value:
                self._pay_status_list.append(i)
    @property
    def pay_way_list(self):
        return self._pay_way_list

    @pay_way_list.setter
    def pay_way_list(self, value):
        if isinstance(value, list):
            self._pay_way_list = list()
            for i in value:
                self._pay_way_list.append(i)
    @property
    def prod_code(self):
        return self._prod_code

    @prod_code.setter
    def prod_code(self, value):
        self._prod_code = value
    @property
    def settle_period(self):
        return self._settle_period

    @settle_period.setter
    def settle_period(self, value):
        if isinstance(value, list):
            self._settle_period = list()
            for i in value:
                self._settle_period.append(i)
    @property
    def settle_type(self):
        return self._settle_type

    @settle_type.setter
    def settle_type(self, value):
        self._settle_type = value
    @property
    def type_list(self):
        return self._type_list

    @type_list.setter
    def type_list(self, value):
        if isinstance(value, list):
            self._type_list = list()
            for i in value:
                self._type_list.append(i)


    def to_alipay_dict(self):
        params = dict()
        if self.anl_dmsn_1_list:
            if isinstance(self.anl_dmsn_1_list, list):
                for i in range(0, len(self.anl_dmsn_1_list)):
                    element = self.anl_dmsn_1_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.anl_dmsn_1_list[i] = element.to_alipay_dict()
            if hasattr(self.anl_dmsn_1_list, 'to_alipay_dict'):
                params['anl_dmsn_1_list'] = self.anl_dmsn_1_list.to_alipay_dict()
            else:
                params['anl_dmsn_1_list'] = self.anl_dmsn_1_list
        if self.anl_dmsn_2_list:
            if isinstance(self.anl_dmsn_2_list, list):
                for i in range(0, len(self.anl_dmsn_2_list)):
                    element = self.anl_dmsn_2_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.anl_dmsn_2_list[i] = element.to_alipay_dict()
            if hasattr(self.anl_dmsn_2_list, 'to_alipay_dict'):
                params['anl_dmsn_2_list'] = self.anl_dmsn_2_list.to_alipay_dict()
            else:
                params['anl_dmsn_2_list'] = self.anl_dmsn_2_list
        if self.anl_dmsn_3_list:
            if isinstance(self.anl_dmsn_3_list, list):
                for i in range(0, len(self.anl_dmsn_3_list)):
                    element = self.anl_dmsn_3_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.anl_dmsn_3_list[i] = element.to_alipay_dict()
            if hasattr(self.anl_dmsn_3_list, 'to_alipay_dict'):
                params['anl_dmsn_3_list'] = self.anl_dmsn_3_list.to_alipay_dict()
            else:
                params['anl_dmsn_3_list'] = self.anl_dmsn_3_list
        if self.anl_dmsn_4_list:
            if isinstance(self.anl_dmsn_4_list, list):
                for i in range(0, len(self.anl_dmsn_4_list)):
                    element = self.anl_dmsn_4_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.anl_dmsn_4_list[i] = element.to_alipay_dict()
            if hasattr(self.anl_dmsn_4_list, 'to_alipay_dict'):
                params['anl_dmsn_4_list'] = self.anl_dmsn_4_list.to_alipay_dict()
            else:
                params['anl_dmsn_4_list'] = self.anl_dmsn_4_list
        if self.arrangement_no:
            if hasattr(self.arrangement_no, 'to_alipay_dict'):
                params['arrangement_no'] = self.arrangement_no.to_alipay_dict()
            else:
                params['arrangement_no'] = self.arrangement_no
        if self.bill_month_begin:
            if hasattr(self.bill_month_begin, 'to_alipay_dict'):
                params['bill_month_begin'] = self.bill_month_begin.to_alipay_dict()
            else:
                params['bill_month_begin'] = self.bill_month_begin
        if self.bill_month_end:
            if hasattr(self.bill_month_end, 'to_alipay_dict'):
                params['bill_month_end'] = self.bill_month_end.to_alipay_dict()
            else:
                params['bill_month_end'] = self.bill_month_end
        if self.charge_itme_code:
            if hasattr(self.charge_itme_code, 'to_alipay_dict'):
                params['charge_itme_code'] = self.charge_itme_code.to_alipay_dict()
            else:
                params['charge_itme_code'] = self.charge_itme_code
        if self.check_state:
            if isinstance(self.check_state, list):
                for i in range(0, len(self.check_state)):
                    element = self.check_state[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.check_state[i] = element.to_alipay_dict()
            if hasattr(self.check_state, 'to_alipay_dict'):
                params['check_state'] = self.check_state.to_alipay_dict()
            else:
                params['check_state'] = self.check_state
        if self.dmsn_query_list:
            if isinstance(self.dmsn_query_list, list):
                for i in range(0, len(self.dmsn_query_list)):
                    element = self.dmsn_query_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.dmsn_query_list[i] = element.to_alipay_dict()
            if hasattr(self.dmsn_query_list, 'to_alipay_dict'):
                params['dmsn_query_list'] = self.dmsn_query_list.to_alipay_dict()
            else:
                params['dmsn_query_list'] = self.dmsn_query_list
        if self.env_source:
            if hasattr(self.env_source, 'to_alipay_dict'):
                params['env_source'] = self.env_source.to_alipay_dict()
            else:
                params['env_source'] = self.env_source
        if self.inst_id:
            if hasattr(self.inst_id, 'to_alipay_dict'):
                params['inst_id'] = self.inst_id.to_alipay_dict()
            else:
                params['inst_id'] = self.inst_id
        if self.invoice_status:
            if isinstance(self.invoice_status, list):
                for i in range(0, len(self.invoice_status)):
                    element = self.invoice_status[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.invoice_status[i] = element.to_alipay_dict()
            if hasattr(self.invoice_status, 'to_alipay_dict'):
                params['invoice_status'] = self.invoice_status.to_alipay_dict()
            else:
                params['invoice_status'] = self.invoice_status
        if self.ip_id:
            if hasattr(self.ip_id, 'to_alipay_dict'):
                params['ip_id'] = self.ip_id.to_alipay_dict()
            else:
                params['ip_id'] = self.ip_id
        if self.ip_role_id:
            if hasattr(self.ip_role_id, 'to_alipay_dict'):
                params['ip_role_id'] = self.ip_role_id.to_alipay_dict()
            else:
                params['ip_role_id'] = self.ip_role_id
        if self.page_no:
            if hasattr(self.page_no, 'to_alipay_dict'):
                params['page_no'] = self.page_no.to_alipay_dict()
            else:
                params['page_no'] = self.page_no
        if self.page_size:
            if hasattr(self.page_size, 'to_alipay_dict'):
                params['page_size'] = self.page_size.to_alipay_dict()
            else:
                params['page_size'] = self.page_size
        if self.pay_status_list:
            if isinstance(self.pay_status_list, list):
                for i in range(0, len(self.pay_status_list)):
                    element = self.pay_status_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.pay_status_list[i] = element.to_alipay_dict()
            if hasattr(self.pay_status_list, 'to_alipay_dict'):
                params['pay_status_list'] = self.pay_status_list.to_alipay_dict()
            else:
                params['pay_status_list'] = self.pay_status_list
        if self.pay_way_list:
            if isinstance(self.pay_way_list, list):
                for i in range(0, len(self.pay_way_list)):
                    element = self.pay_way_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.pay_way_list[i] = element.to_alipay_dict()
            if hasattr(self.pay_way_list, 'to_alipay_dict'):
                params['pay_way_list'] = self.pay_way_list.to_alipay_dict()
            else:
                params['pay_way_list'] = self.pay_way_list
        if self.prod_code:
            if hasattr(self.prod_code, 'to_alipay_dict'):
                params['prod_code'] = self.prod_code.to_alipay_dict()
            else:
                params['prod_code'] = self.prod_code
        if self.settle_period:
            if isinstance(self.settle_period, list):
                for i in range(0, len(self.settle_period)):
                    element = self.settle_period[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.settle_period[i] = element.to_alipay_dict()
            if hasattr(self.settle_period, 'to_alipay_dict'):
                params['settle_period'] = self.settle_period.to_alipay_dict()
            else:
                params['settle_period'] = self.settle_period
        if self.settle_type:
            if hasattr(self.settle_type, 'to_alipay_dict'):
                params['settle_type'] = self.settle_type.to_alipay_dict()
            else:
                params['settle_type'] = self.settle_type
        if self.type_list:
            if isinstance(self.type_list, list):
                for i in range(0, len(self.type_list)):
                    element = self.type_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.type_list[i] = element.to_alipay_dict()
            if hasattr(self.type_list, 'to_alipay_dict'):
                params['type_list'] = self.type_list.to_alipay_dict()
            else:
                params['type_list'] = self.type_list
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayBossFncArbillMonthstatementbillQueryModel()
        if 'anl_dmsn_1_list' in d:
            o.anl_dmsn_1_list = d['anl_dmsn_1_list']
        if 'anl_dmsn_2_list' in d:
            o.anl_dmsn_2_list = d['anl_dmsn_2_list']
        if 'anl_dmsn_3_list' in d:
            o.anl_dmsn_3_list = d['anl_dmsn_3_list']
        if 'anl_dmsn_4_list' in d:
            o.anl_dmsn_4_list = d['anl_dmsn_4_list']
        if 'arrangement_no' in d:
            o.arrangement_no = d['arrangement_no']
        if 'bill_month_begin' in d:
            o.bill_month_begin = d['bill_month_begin']
        if 'bill_month_end' in d:
            o.bill_month_end = d['bill_month_end']
        if 'charge_itme_code' in d:
            o.charge_itme_code = d['charge_itme_code']
        if 'check_state' in d:
            o.check_state = d['check_state']
        if 'dmsn_query_list' in d:
            o.dmsn_query_list = d['dmsn_query_list']
        if 'env_source' in d:
            o.env_source = d['env_source']
        if 'inst_id' in d:
            o.inst_id = d['inst_id']
        if 'invoice_status' in d:
            o.invoice_status = d['invoice_status']
        if 'ip_id' in d:
            o.ip_id = d['ip_id']
        if 'ip_role_id' in d:
            o.ip_role_id = d['ip_role_id']
        if 'page_no' in d:
            o.page_no = d['page_no']
        if 'page_size' in d:
            o.page_size = d['page_size']
        if 'pay_status_list' in d:
            o.pay_status_list = d['pay_status_list']
        if 'pay_way_list' in d:
            o.pay_way_list = d['pay_way_list']
        if 'prod_code' in d:
            o.prod_code = d['prod_code']
        if 'settle_period' in d:
            o.settle_period = d['settle_period']
        if 'settle_type' in d:
            o.settle_type = d['settle_type']
        if 'type_list' in d:
            o.type_list = d['type_list']
        return o


