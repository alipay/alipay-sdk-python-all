#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class RefundInfoBean(object):

    def __init__(self):
        self._actual_ref_amt = None
        self._mer_name = None
        self._ord_amt = None
        self._org_req_seq_id = None
        self._req_seq_id = None
        self._thirdpay_mer_id = None
        self._thirdpay_org = None
        self._trans_finish_time = None
        self._trans_time = None

    @property
    def actual_ref_amt(self):
        return self._actual_ref_amt

    @actual_ref_amt.setter
    def actual_ref_amt(self, value):
        self._actual_ref_amt = value
    @property
    def mer_name(self):
        return self._mer_name

    @mer_name.setter
    def mer_name(self, value):
        self._mer_name = value
    @property
    def ord_amt(self):
        return self._ord_amt

    @ord_amt.setter
    def ord_amt(self, value):
        self._ord_amt = value
    @property
    def org_req_seq_id(self):
        return self._org_req_seq_id

    @org_req_seq_id.setter
    def org_req_seq_id(self, value):
        self._org_req_seq_id = value
    @property
    def req_seq_id(self):
        return self._req_seq_id

    @req_seq_id.setter
    def req_seq_id(self, value):
        self._req_seq_id = value
    @property
    def thirdpay_mer_id(self):
        return self._thirdpay_mer_id

    @thirdpay_mer_id.setter
    def thirdpay_mer_id(self, value):
        self._thirdpay_mer_id = value
    @property
    def thirdpay_org(self):
        return self._thirdpay_org

    @thirdpay_org.setter
    def thirdpay_org(self, value):
        self._thirdpay_org = value
    @property
    def trans_finish_time(self):
        return self._trans_finish_time

    @trans_finish_time.setter
    def trans_finish_time(self, value):
        self._trans_finish_time = value
    @property
    def trans_time(self):
        return self._trans_time

    @trans_time.setter
    def trans_time(self, value):
        self._trans_time = value


    def to_alipay_dict(self):
        params = dict()
        if self.actual_ref_amt:
            if hasattr(self.actual_ref_amt, 'to_alipay_dict'):
                params['actual_ref_amt'] = self.actual_ref_amt.to_alipay_dict()
            else:
                params['actual_ref_amt'] = self.actual_ref_amt
        if self.mer_name:
            if hasattr(self.mer_name, 'to_alipay_dict'):
                params['mer_name'] = self.mer_name.to_alipay_dict()
            else:
                params['mer_name'] = self.mer_name
        if self.ord_amt:
            if hasattr(self.ord_amt, 'to_alipay_dict'):
                params['ord_amt'] = self.ord_amt.to_alipay_dict()
            else:
                params['ord_amt'] = self.ord_amt
        if self.org_req_seq_id:
            if hasattr(self.org_req_seq_id, 'to_alipay_dict'):
                params['org_req_seq_id'] = self.org_req_seq_id.to_alipay_dict()
            else:
                params['org_req_seq_id'] = self.org_req_seq_id
        if self.req_seq_id:
            if hasattr(self.req_seq_id, 'to_alipay_dict'):
                params['req_seq_id'] = self.req_seq_id.to_alipay_dict()
            else:
                params['req_seq_id'] = self.req_seq_id
        if self.thirdpay_mer_id:
            if hasattr(self.thirdpay_mer_id, 'to_alipay_dict'):
                params['thirdpay_mer_id'] = self.thirdpay_mer_id.to_alipay_dict()
            else:
                params['thirdpay_mer_id'] = self.thirdpay_mer_id
        if self.thirdpay_org:
            if hasattr(self.thirdpay_org, 'to_alipay_dict'):
                params['thirdpay_org'] = self.thirdpay_org.to_alipay_dict()
            else:
                params['thirdpay_org'] = self.thirdpay_org
        if self.trans_finish_time:
            if hasattr(self.trans_finish_time, 'to_alipay_dict'):
                params['trans_finish_time'] = self.trans_finish_time.to_alipay_dict()
            else:
                params['trans_finish_time'] = self.trans_finish_time
        if self.trans_time:
            if hasattr(self.trans_time, 'to_alipay_dict'):
                params['trans_time'] = self.trans_time.to_alipay_dict()
            else:
                params['trans_time'] = self.trans_time
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = RefundInfoBean()
        if 'actual_ref_amt' in d:
            o.actual_ref_amt = d['actual_ref_amt']
        if 'mer_name' in d:
            o.mer_name = d['mer_name']
        if 'ord_amt' in d:
            o.ord_amt = d['ord_amt']
        if 'org_req_seq_id' in d:
            o.org_req_seq_id = d['org_req_seq_id']
        if 'req_seq_id' in d:
            o.req_seq_id = d['req_seq_id']
        if 'thirdpay_mer_id' in d:
            o.thirdpay_mer_id = d['thirdpay_mer_id']
        if 'thirdpay_org' in d:
            o.thirdpay_org = d['thirdpay_org']
        if 'trans_finish_time' in d:
            o.trans_finish_time = d['trans_finish_time']
        if 'trans_time' in d:
            o.trans_time = d['trans_time']
        return o


