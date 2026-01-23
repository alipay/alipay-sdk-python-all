#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class CustomerLeadsRelationResponse(object):

    def __init__(self):
        self._bd_nick_name = None
        self._bd_work_no = None
        self._bid = None
        self._cid = None
        self._customer_name = None
        self._customer_short_name = None
        self._dept_name = None
        self._dept_no = None
        self._id = None
        self._leads_code = None
        self._passport_id = None
        self._passport_id_list = None
        self._platform_uid = None

    @property
    def bd_nick_name(self):
        return self._bd_nick_name

    @bd_nick_name.setter
    def bd_nick_name(self, value):
        self._bd_nick_name = value
    @property
    def bd_work_no(self):
        return self._bd_work_no

    @bd_work_no.setter
    def bd_work_no(self, value):
        self._bd_work_no = value
    @property
    def bid(self):
        return self._bid

    @bid.setter
    def bid(self, value):
        self._bid = value
    @property
    def cid(self):
        return self._cid

    @cid.setter
    def cid(self, value):
        self._cid = value
    @property
    def customer_name(self):
        return self._customer_name

    @customer_name.setter
    def customer_name(self, value):
        self._customer_name = value
    @property
    def customer_short_name(self):
        return self._customer_short_name

    @customer_short_name.setter
    def customer_short_name(self, value):
        self._customer_short_name = value
    @property
    def dept_name(self):
        return self._dept_name

    @dept_name.setter
    def dept_name(self, value):
        self._dept_name = value
    @property
    def dept_no(self):
        return self._dept_no

    @dept_no.setter
    def dept_no(self, value):
        self._dept_no = value
    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        self._id = value
    @property
    def leads_code(self):
        return self._leads_code

    @leads_code.setter
    def leads_code(self, value):
        self._leads_code = value
    @property
    def passport_id(self):
        return self._passport_id

    @passport_id.setter
    def passport_id(self, value):
        self._passport_id = value
    @property
    def passport_id_list(self):
        return self._passport_id_list

    @passport_id_list.setter
    def passport_id_list(self, value):
        if isinstance(value, list):
            self._passport_id_list = list()
            for i in value:
                self._passport_id_list.append(i)
    @property
    def platform_uid(self):
        return self._platform_uid

    @platform_uid.setter
    def platform_uid(self, value):
        self._platform_uid = value


    def to_alipay_dict(self):
        params = dict()
        if self.bd_nick_name:
            if hasattr(self.bd_nick_name, 'to_alipay_dict'):
                params['bd_nick_name'] = self.bd_nick_name.to_alipay_dict()
            else:
                params['bd_nick_name'] = self.bd_nick_name
        if self.bd_work_no:
            if hasattr(self.bd_work_no, 'to_alipay_dict'):
                params['bd_work_no'] = self.bd_work_no.to_alipay_dict()
            else:
                params['bd_work_no'] = self.bd_work_no
        if self.bid:
            if hasattr(self.bid, 'to_alipay_dict'):
                params['bid'] = self.bid.to_alipay_dict()
            else:
                params['bid'] = self.bid
        if self.cid:
            if hasattr(self.cid, 'to_alipay_dict'):
                params['cid'] = self.cid.to_alipay_dict()
            else:
                params['cid'] = self.cid
        if self.customer_name:
            if hasattr(self.customer_name, 'to_alipay_dict'):
                params['customer_name'] = self.customer_name.to_alipay_dict()
            else:
                params['customer_name'] = self.customer_name
        if self.customer_short_name:
            if hasattr(self.customer_short_name, 'to_alipay_dict'):
                params['customer_short_name'] = self.customer_short_name.to_alipay_dict()
            else:
                params['customer_short_name'] = self.customer_short_name
        if self.dept_name:
            if hasattr(self.dept_name, 'to_alipay_dict'):
                params['dept_name'] = self.dept_name.to_alipay_dict()
            else:
                params['dept_name'] = self.dept_name
        if self.dept_no:
            if hasattr(self.dept_no, 'to_alipay_dict'):
                params['dept_no'] = self.dept_no.to_alipay_dict()
            else:
                params['dept_no'] = self.dept_no
        if self.id:
            if hasattr(self.id, 'to_alipay_dict'):
                params['id'] = self.id.to_alipay_dict()
            else:
                params['id'] = self.id
        if self.leads_code:
            if hasattr(self.leads_code, 'to_alipay_dict'):
                params['leads_code'] = self.leads_code.to_alipay_dict()
            else:
                params['leads_code'] = self.leads_code
        if self.passport_id:
            if hasattr(self.passport_id, 'to_alipay_dict'):
                params['passport_id'] = self.passport_id.to_alipay_dict()
            else:
                params['passport_id'] = self.passport_id
        if self.passport_id_list:
            if isinstance(self.passport_id_list, list):
                for i in range(0, len(self.passport_id_list)):
                    element = self.passport_id_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.passport_id_list[i] = element.to_alipay_dict()
            if hasattr(self.passport_id_list, 'to_alipay_dict'):
                params['passport_id_list'] = self.passport_id_list.to_alipay_dict()
            else:
                params['passport_id_list'] = self.passport_id_list
        if self.platform_uid:
            if hasattr(self.platform_uid, 'to_alipay_dict'):
                params['platform_uid'] = self.platform_uid.to_alipay_dict()
            else:
                params['platform_uid'] = self.platform_uid
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = CustomerLeadsRelationResponse()
        if 'bd_nick_name' in d:
            o.bd_nick_name = d['bd_nick_name']
        if 'bd_work_no' in d:
            o.bd_work_no = d['bd_work_no']
        if 'bid' in d:
            o.bid = d['bid']
        if 'cid' in d:
            o.cid = d['cid']
        if 'customer_name' in d:
            o.customer_name = d['customer_name']
        if 'customer_short_name' in d:
            o.customer_short_name = d['customer_short_name']
        if 'dept_name' in d:
            o.dept_name = d['dept_name']
        if 'dept_no' in d:
            o.dept_no = d['dept_no']
        if 'id' in d:
            o.id = d['id']
        if 'leads_code' in d:
            o.leads_code = d['leads_code']
        if 'passport_id' in d:
            o.passport_id = d['passport_id']
        if 'passport_id_list' in d:
            o.passport_id_list = d['passport_id_list']
        if 'platform_uid' in d:
            o.platform_uid = d['platform_uid']
        return o


