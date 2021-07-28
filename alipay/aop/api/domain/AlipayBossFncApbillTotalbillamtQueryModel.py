#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayBossFncApbillTotalbillamtQueryModel(object):

    def __init__(self):
        self._ar_no = None
        self._bill_invoice_link_statuses = None
        self._bill_no = None
        self._bill_types = None
        self._biz_type = None
        self._end_month = None
        self._inst_id = None
        self._invoice_type = None
        self._ip_role_id = None
        self._ip_role_ids = None
        self._mid = None
        self._mids = None
        self._pay_statuses = None
        self._pd_codes = None
        self._price_id = None
        self._price_policy_id = None
        self._start_month = None

    @property
    def ar_no(self):
        return self._ar_no

    @ar_no.setter
    def ar_no(self, value):
        self._ar_no = value
    @property
    def bill_invoice_link_statuses(self):
        return self._bill_invoice_link_statuses

    @bill_invoice_link_statuses.setter
    def bill_invoice_link_statuses(self, value):
        if isinstance(value, list):
            self._bill_invoice_link_statuses = list()
            for i in value:
                self._bill_invoice_link_statuses.append(i)
    @property
    def bill_no(self):
        return self._bill_no

    @bill_no.setter
    def bill_no(self, value):
        self._bill_no = value
    @property
    def bill_types(self):
        return self._bill_types

    @bill_types.setter
    def bill_types(self, value):
        if isinstance(value, list):
            self._bill_types = list()
            for i in value:
                self._bill_types.append(i)
    @property
    def biz_type(self):
        return self._biz_type

    @biz_type.setter
    def biz_type(self, value):
        self._biz_type = value
    @property
    def end_month(self):
        return self._end_month

    @end_month.setter
    def end_month(self, value):
        self._end_month = value
    @property
    def inst_id(self):
        return self._inst_id

    @inst_id.setter
    def inst_id(self, value):
        self._inst_id = value
    @property
    def invoice_type(self):
        return self._invoice_type

    @invoice_type.setter
    def invoice_type(self, value):
        self._invoice_type = value
    @property
    def ip_role_id(self):
        return self._ip_role_id

    @ip_role_id.setter
    def ip_role_id(self, value):
        self._ip_role_id = value
    @property
    def ip_role_ids(self):
        return self._ip_role_ids

    @ip_role_ids.setter
    def ip_role_ids(self, value):
        if isinstance(value, list):
            self._ip_role_ids = list()
            for i in value:
                self._ip_role_ids.append(i)
    @property
    def mid(self):
        return self._mid

    @mid.setter
    def mid(self, value):
        self._mid = value
    @property
    def mids(self):
        return self._mids

    @mids.setter
    def mids(self, value):
        if isinstance(value, list):
            self._mids = list()
            for i in value:
                self._mids.append(i)
    @property
    def pay_statuses(self):
        return self._pay_statuses

    @pay_statuses.setter
    def pay_statuses(self, value):
        if isinstance(value, list):
            self._pay_statuses = list()
            for i in value:
                self._pay_statuses.append(i)
    @property
    def pd_codes(self):
        return self._pd_codes

    @pd_codes.setter
    def pd_codes(self, value):
        if isinstance(value, list):
            self._pd_codes = list()
            for i in value:
                self._pd_codes.append(i)
    @property
    def price_id(self):
        return self._price_id

    @price_id.setter
    def price_id(self, value):
        self._price_id = value
    @property
    def price_policy_id(self):
        return self._price_policy_id

    @price_policy_id.setter
    def price_policy_id(self, value):
        self._price_policy_id = value
    @property
    def start_month(self):
        return self._start_month

    @start_month.setter
    def start_month(self, value):
        self._start_month = value


    def to_alipay_dict(self):
        params = dict()
        if self.ar_no:
            if hasattr(self.ar_no, 'to_alipay_dict'):
                params['ar_no'] = self.ar_no.to_alipay_dict()
            else:
                params['ar_no'] = self.ar_no
        if self.bill_invoice_link_statuses:
            if isinstance(self.bill_invoice_link_statuses, list):
                for i in range(0, len(self.bill_invoice_link_statuses)):
                    element = self.bill_invoice_link_statuses[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.bill_invoice_link_statuses[i] = element.to_alipay_dict()
            if hasattr(self.bill_invoice_link_statuses, 'to_alipay_dict'):
                params['bill_invoice_link_statuses'] = self.bill_invoice_link_statuses.to_alipay_dict()
            else:
                params['bill_invoice_link_statuses'] = self.bill_invoice_link_statuses
        if self.bill_no:
            if hasattr(self.bill_no, 'to_alipay_dict'):
                params['bill_no'] = self.bill_no.to_alipay_dict()
            else:
                params['bill_no'] = self.bill_no
        if self.bill_types:
            if isinstance(self.bill_types, list):
                for i in range(0, len(self.bill_types)):
                    element = self.bill_types[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.bill_types[i] = element.to_alipay_dict()
            if hasattr(self.bill_types, 'to_alipay_dict'):
                params['bill_types'] = self.bill_types.to_alipay_dict()
            else:
                params['bill_types'] = self.bill_types
        if self.biz_type:
            if hasattr(self.biz_type, 'to_alipay_dict'):
                params['biz_type'] = self.biz_type.to_alipay_dict()
            else:
                params['biz_type'] = self.biz_type
        if self.end_month:
            if hasattr(self.end_month, 'to_alipay_dict'):
                params['end_month'] = self.end_month.to_alipay_dict()
            else:
                params['end_month'] = self.end_month
        if self.inst_id:
            if hasattr(self.inst_id, 'to_alipay_dict'):
                params['inst_id'] = self.inst_id.to_alipay_dict()
            else:
                params['inst_id'] = self.inst_id
        if self.invoice_type:
            if hasattr(self.invoice_type, 'to_alipay_dict'):
                params['invoice_type'] = self.invoice_type.to_alipay_dict()
            else:
                params['invoice_type'] = self.invoice_type
        if self.ip_role_id:
            if hasattr(self.ip_role_id, 'to_alipay_dict'):
                params['ip_role_id'] = self.ip_role_id.to_alipay_dict()
            else:
                params['ip_role_id'] = self.ip_role_id
        if self.ip_role_ids:
            if isinstance(self.ip_role_ids, list):
                for i in range(0, len(self.ip_role_ids)):
                    element = self.ip_role_ids[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.ip_role_ids[i] = element.to_alipay_dict()
            if hasattr(self.ip_role_ids, 'to_alipay_dict'):
                params['ip_role_ids'] = self.ip_role_ids.to_alipay_dict()
            else:
                params['ip_role_ids'] = self.ip_role_ids
        if self.mid:
            if hasattr(self.mid, 'to_alipay_dict'):
                params['mid'] = self.mid.to_alipay_dict()
            else:
                params['mid'] = self.mid
        if self.mids:
            if isinstance(self.mids, list):
                for i in range(0, len(self.mids)):
                    element = self.mids[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.mids[i] = element.to_alipay_dict()
            if hasattr(self.mids, 'to_alipay_dict'):
                params['mids'] = self.mids.to_alipay_dict()
            else:
                params['mids'] = self.mids
        if self.pay_statuses:
            if isinstance(self.pay_statuses, list):
                for i in range(0, len(self.pay_statuses)):
                    element = self.pay_statuses[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.pay_statuses[i] = element.to_alipay_dict()
            if hasattr(self.pay_statuses, 'to_alipay_dict'):
                params['pay_statuses'] = self.pay_statuses.to_alipay_dict()
            else:
                params['pay_statuses'] = self.pay_statuses
        if self.pd_codes:
            if isinstance(self.pd_codes, list):
                for i in range(0, len(self.pd_codes)):
                    element = self.pd_codes[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.pd_codes[i] = element.to_alipay_dict()
            if hasattr(self.pd_codes, 'to_alipay_dict'):
                params['pd_codes'] = self.pd_codes.to_alipay_dict()
            else:
                params['pd_codes'] = self.pd_codes
        if self.price_id:
            if hasattr(self.price_id, 'to_alipay_dict'):
                params['price_id'] = self.price_id.to_alipay_dict()
            else:
                params['price_id'] = self.price_id
        if self.price_policy_id:
            if hasattr(self.price_policy_id, 'to_alipay_dict'):
                params['price_policy_id'] = self.price_policy_id.to_alipay_dict()
            else:
                params['price_policy_id'] = self.price_policy_id
        if self.start_month:
            if hasattr(self.start_month, 'to_alipay_dict'):
                params['start_month'] = self.start_month.to_alipay_dict()
            else:
                params['start_month'] = self.start_month
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayBossFncApbillTotalbillamtQueryModel()
        if 'ar_no' in d:
            o.ar_no = d['ar_no']
        if 'bill_invoice_link_statuses' in d:
            o.bill_invoice_link_statuses = d['bill_invoice_link_statuses']
        if 'bill_no' in d:
            o.bill_no = d['bill_no']
        if 'bill_types' in d:
            o.bill_types = d['bill_types']
        if 'biz_type' in d:
            o.biz_type = d['biz_type']
        if 'end_month' in d:
            o.end_month = d['end_month']
        if 'inst_id' in d:
            o.inst_id = d['inst_id']
        if 'invoice_type' in d:
            o.invoice_type = d['invoice_type']
        if 'ip_role_id' in d:
            o.ip_role_id = d['ip_role_id']
        if 'ip_role_ids' in d:
            o.ip_role_ids = d['ip_role_ids']
        if 'mid' in d:
            o.mid = d['mid']
        if 'mids' in d:
            o.mids = d['mids']
        if 'pay_statuses' in d:
            o.pay_statuses = d['pay_statuses']
        if 'pd_codes' in d:
            o.pd_codes = d['pd_codes']
        if 'price_id' in d:
            o.price_id = d['price_id']
        if 'price_policy_id' in d:
            o.price_policy_id = d['price_policy_id']
        if 'start_month' in d:
            o.start_month = d['start_month']
        return o


